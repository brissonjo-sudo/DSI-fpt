"""Validation statique reproductible du dépôt dsi-fpt.

Ce script ne dépend que de la bibliothèque standard (aucun ``pip install``).
Il retourne 0 si tous les contrôles passent, 1 sinon, et affiche un
récapitulatif lisible en français.

Option ``--partiel`` : pendant la rédaction, les fichiers attendus mais pas
encore écrits (branches, objets, gabarits, fichiers de suivi) deviennent des
avertissements. Tous les autres contrôles restent bloquants. La CI tourne
sans cette option.
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "dsi-fpt"

# Invariants de garde-fou : chaînes devant apparaître verbatim dans SKILL.md.
# Ce sont les deux "hard stops" (§5.2 incident, §5.3 surveillance) et la
# frontière dpo-ct (§5.5) : l'invariant central de sûreté de ce skill.
REQUIRED_GUARDRAIL_SNIPPETS = (
    "STOP — Incident de sécurité en cours ou récent.",
    "Aucune contre-mesure offensive, aucun accès à un système tiers.",
    "Ne pas décider seul de ce qui revient à l'exécutif",
    "STOP — Cette demande vise à accéder aux contenus ou aux traces d'une personne,",
    "BASCULE dpo-ct (base légale, information, AIPD)",
    "BASCULE dpo-ct — Cette question porte sur le droit des données personnelles.",
    "Une frontière ne s'illustre pas",
)

# Branches de references/ : chacune suit le gabarit à 12 sections.
BRANCH_FILES = {
    "gouvernance-strategie.md",
    "securite-si.md",
    "crise-cyber-continuite.md",
    "infrastructures-reseaux.md",
    "cloud-hebergement.md",
    "applications-interoperabilite.md",
    "dematerialisation-teleservices.md",
    "accessibilite-numerique.md",
    "ia-donnees.md",
    "contrats-prestataires.md",
    "ecrits-numerique.md",
    "retex.md",
}
SUPPORT_FILES = {
    "analyse-situation.md",
    "_gabarit-branche.md",
    "socle-sources-verification.md",
    "references-verifiees.md",
    "cache-valeurs.md",
}
EXPECTED_REFERENCE_FILES = BRANCH_FILES | SUPPORT_FILES
EXPECTED_OBJETS = {
    "_gabarit-objet.md",
    "projet-si.md",
    "incident-securite.md",
    "teleservice.md",
    "solution-saas.md",
    "site-reseau.md",
    "compte-poste-agent.md",
}
EXPECTED_TEMPLATES = {
    "fiche-projet-si.md",
    "rapport-incident.md",
    "cahier-des-charges-technique.md",
    "charte-usage-si.md",
    "note-homologation.md",
}
BRANCH_SECTIONS = 12
OBJET_SECTIONS = 6
MIN_TEST_CASES = 28
MIN_ATTENDUS = 4

# Identifiants officiels en dur interdits hors registre vérifié : invariant
# anti-hallucination central (AGENTS.md, contrainte 2). CELEX inclus.
OFFICIAL_ID_PATTERN = re.compile(
    r"\b(?:(?:LEGIARTI|JORFTEXT|CETATEXT|LEGITEXT)\d+|(?:0|3)\d{4}[LRDF]\d{4}(?:-\d{8})?)\b"
)
REGISTRY = Path("references/references-verifiees.md")

# Fichiers de maintenance où les valeurs datées sont permises : le registre,
# le cache (exclu du paquet runtime) et les gabarits de conception.
VALUE_EXEMPT = {
    REGISTRY,
    Path("references/cache-valeurs.md"),
    Path("references/_gabarit-branche.md"),
    Path("objets/_gabarit-objet.md"),
}
MONTHS = (
    "janvier|février|mars|avril|mai|juin|juillet|août|septembre|octobre|"
    "novembre|décembre"
)
# Valeurs de mémoire interdites dans le runtime (AGENTS.md, contrainte 1) :
# montants, délais chiffrés, dates d'application, versions de référentiel.
VALUE_PATTERNS = {
    "montant": re.compile(r"\d[\d  .,]*\s?(?:€|euros?\b|k€|M€)", re.IGNORECASE),
    "délai chiffré": re.compile(
        r"\b\d+\s?(?:h\b|heures?|jours?|semaines?|mois|ans?\b|années?)", re.IGNORECASE
    ),
    "date": re.compile(rf"\b\d{{1,2}}(?:er)?\s+(?:{MONTHS})\s+\d{{4}}\b", re.IGNORECASE),
    "version de référentiel": re.compile(
        r"\b(?:RGAA|RGS|RGI|SecNumCloud|EBIOS(?: RM)?)\s*v?\d", re.IGNORECASE
    ),
    "seuil de population": re.compile(r"\b\d[\d  .]*\s?habitants\b", re.IGNORECASE),
}

# Dépôts voisins : un chemin qui commence par l'un d'eux n'existe que dans un
# clonage multi-dépôts à plat. On nomme le skill, jamais le fichier.
SIBLING_REPO_NAMES = frozenset(
    {
        "dpm-fpt",
        "drh-fpt",
        "dpo-ct",
        "dirfi-fpt",
        "dsi-fpt",
        "droit-francais-skill",
        "collectivite-territoriale",
    }
)

# Anti-PII : IBAN français, NIR, adresse e-mail, adresse IPv4 (un plan
# d'adressage réel est un détail d'architecture exploitable).
IBAN_FR_PATTERN = re.compile(r"\bFR\d{2}(?:[ -]?[0-9A-Z]){23}\b", re.IGNORECASE)
NIR_PATTERN = re.compile(
    r"(?<!\d)[12][ -]?\d{2}[ -]?(?:0[1-9]|1[0-2])[ -]?(?:2[AB]|\d{2})"
    r"[ -]?\d{3}[ -]?\d{3}[ -]?\d{2}(?!\d)",
    re.IGNORECASE,
)
EMAIL_PATTERN = re.compile(r"\b[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}\b", re.IGNORECASE)
EMAIL_ALLOWED_EXACT = {"noreply@anthropic.com"}
EMAIL_ALLOWED_DOMAIN_SUFFIX = ".gouv.fr"
IPV4_PATTERN = re.compile(r"\b(?:\d{1,3}\.){3}\d{1,3}\b")

VERSION_TITLE_PATTERN = re.compile(
    r"#\s*Skill\s*:\s*" + re.escape(SKILL_NAME) + r"\s*\(v(\d+\.\d+\.\d+)\)"
)
SECTION_PATTERN = re.compile(r"^## (\d+)\.", re.MULTILINE)


class Validation:
    """Collecte les erreurs et avertissements sans interrompre les contrôles."""

    def __init__(self, partiel: bool = False) -> None:
        self.errors: list[str] = []
        self.warnings: list[str] = []
        self.checks = 0
        self.partiel = partiel

    def require(self, condition: bool, message: str) -> None:
        """Enregistre une exigence bloquante et son éventuel échec."""
        self.checks += 1
        if not condition:
            self.errors.append(message)

    def warn(self, condition: bool, message: str) -> None:
        """Enregistre un avertissement non bloquant."""
        self.checks += 1
        if not condition:
            self.warnings.append(message)

    def expect_file(self, condition: bool, message: str) -> None:
        """Fichier attendu : bloquant, sauf en mode partiel."""
        if self.partiel:
            self.warn(condition, message)
        else:
            self.require(condition, message)


def read_text(path: Path) -> str:
    """Lit un fichier UTF-8."""
    return path.read_text(encoding="utf-8")


def parse_frontmatter(text: str) -> dict[str, str]:
    """Parse le frontmatter simple de SKILL.md sans dépendance externe."""
    if not text.startswith("---\n"):
        return {}
    end = text.find("\n---\n", 4)
    if end < 0:
        return {}
    raw = text[4:end]
    fields: dict[str, str] = {}
    current: str | None = None
    for line in raw.splitlines():
        match = re.match(r"^([a-z_]+):(?:\s*(.*))?$", line)
        if match:
            current = match.group(1)
            value = match.group(2) or ""
            fields[current] = "" if value in {">-", "|-"} else value
        elif current and line.startswith("  "):
            fields[current] = f"{fields[current]} {line.strip()}".strip()
    return fields


def runtime_markdown_files() -> list[Path]:
    """Retourne les fichiers Markdown réellement chargés par le skill."""
    files: list[Path] = []
    skill = ROOT / "SKILL.md"
    if skill.is_file():
        files.append(skill)
    for directory in ("references", "objets"):
        base = ROOT / directory
        if base.is_dir():
            files.extend(sorted(base.rglob("*.md")))
    return files


def validate_frontmatter(validation: Validation) -> None:
    """Valide le contrat minimal du frontmatter du skill."""
    skill_path = ROOT / "SKILL.md"
    if not skill_path.is_file():
        validation.require(False, "SKILL.md : fichier absent")
        return
    fields = parse_frontmatter(read_text(skill_path))
    validation.require(
        set(fields) == {"name", "description"},
        "SKILL.md : le frontmatter doit contenir exactement name et description "
        f"(trouvé : {sorted(fields) or 'aucun'})",
    )
    validation.require(
        fields.get("name") == SKILL_NAME,
        f"SKILL.md : name invalide (attendu {SKILL_NAME!r}, trouvé {fields.get('name')!r})",
    )
    description = fields.get("description", "")
    validation.require(
        1 <= len(description) <= 1024,
        f"SKILL.md : description hors limite (longueur {len(description)})",
    )
    # Risque de routage n°1 : la description doit nommer ce qu'elle exclut.
    for sibling in ("dpo-ct", "drh-fpt", "dpm-fpt", "dirfi-fpt"):
        validation.require(
            sibling in description,
            f"SKILL.md : la description doit nommer la frontière {sibling!r}",
        )


def validate_guardrail_invariants(validation: Validation) -> None:
    """Vérifie que les garde-fous non négociables restent verbatim dans SKILL.md."""
    skill_path = ROOT / "SKILL.md"
    if not skill_path.is_file():
        return
    skill = read_text(skill_path)
    for snippet in REQUIRED_GUARDRAIL_SNIPPETS:
        validation.require(
            snippet in skill,
            f"SKILL.md : invariant de garde-fou absent (verbatim requis) : {snippet!r}",
        )


def extract_skill_version() -> str | None:
    """Extrait la version depuis le titre de SKILL.md (# Skill : dsi-fpt (vX.Y.Z))."""
    skill_path = ROOT / "SKILL.md"
    if not skill_path.is_file():
        return None
    match = VERSION_TITLE_PATTERN.search(read_text(skill_path))
    return match.group(1) if match else None


def validate_versions(validation: Validation) -> None:
    """Vérifie l'alignement de la version courante entre les fichiers du dépôt.

    La version de référence est lue depuis le titre de SKILL.md : le titre est
    aussi ce que lit ``sync_skills.py`` dans le plugin agrégateur.
    """
    version = extract_skill_version()
    validation.require(
        version is not None,
        f"SKILL.md : titre de version introuvable (attendu : # Skill : {SKILL_NAME} (vX.Y.Z))",
    )
    if version is None:
        return
    validation.require(
        f"version : **{version}**" in read_text(ROOT / "SKILL.md"),
        f"SKILL.md : motif 'version : **{version}**' absent des métadonnées",
    )
    expected = {
        ROOT / "README.md": f"v{version}",
        ROOT / "CHANGELOG.md": f"[{version}]",
        ROOT / "vault" / f"index-{SKILL_NAME}.md": f"version: {version}",
    }
    for path, marker in expected.items():
        relative = path.relative_to(ROOT)
        if not path.is_file():
            validation.expect_file(False, f"{relative} : fichier absent")
            continue
        validation.require(
            marker in read_text(path),
            f"{relative} : marqueur de version {marker!r} absent",
        )


def check_inventory(
    validation: Validation, directory: Path, expected: set[str], label: str
) -> set[str]:
    """Compare le contenu d'un dossier à l'inventaire attendu ; renvoie les présents."""
    if not directory.is_dir():
        validation.expect_file(False, f"{label} : dossier absent")
        return set()
    present = {path.name for path in directory.glob("*.md")}
    for name in sorted(expected - present):
        validation.expect_file(False, f"{label}{name} : fichier manquant")
    for name in sorted(present - expected):
        validation.require(False, f"{label}{name} : fichier inattendu")
    validation.checks += 1
    return present & expected


def count_sections(path: Path) -> list[int]:
    """Renvoie les numéros des sections de niveau 2 numérotées (## N.)."""
    return [int(number) for number in SECTION_PATTERN.findall(read_text(path))]


def validate_structure(validation: Validation) -> None:
    """Inventaire exact et structure imposée des branches et des objets."""
    references = ROOT / "references"
    present = check_inventory(validation, references, EXPECTED_REFERENCE_FILES, "references/")
    for name in sorted(present & BRANCH_FILES):
        path = references / name
        sections = count_sections(path)
        validation.require(
            sections == list(range(1, BRANCH_SECTIONS + 1)),
            f"references/{name} : sections numérotées {sections}, attendu 1 à "
            f"{BRANCH_SECTIONS} dans l'ordre (gabarit de branche)",
        )
        validation.require(
            read_text(path).startswith("# Branche — "),
            f"references/{name} : titre attendu '# Branche — <nom>'",
        )

    objets = ROOT / "objets"
    present = check_inventory(validation, objets, EXPECTED_OBJETS, "objets/")
    for name in sorted(present - {"_gabarit-objet.md"}):
        path = objets / name
        sections = count_sections(path)
        validation.require(
            sections == list(range(1, OBJET_SECTIONS + 1)),
            f"objets/{name} : sections numérotées {sections}, attendu 1 à "
            f"{OBJET_SECTIONS} dans l'ordre (gabarit d'objet)",
        )
        validation.require(
            read_text(path).startswith("# Objet métier — "),
            f"objets/{name} : titre attendu '# Objet métier — <nom> (vX.Y.Z)'",
        )

    check_inventory(
        validation, references / "templates", EXPECTED_TEMPLATES, "references/templates/"
    )
    validation.require(not (ROOT / "assets").exists(), "assets/ : ce dossier ne doit pas exister")


def validate_cases(validation: Validation) -> None:
    """Valide le schéma et la couverture des cas de test structurés."""
    path = ROOT / "tests" / "cas-de-test.json"
    if not path.is_file():
        validation.expect_file(False, "tests/cas-de-test.json : fichier absent")
        return
    try:
        cases = json.loads(read_text(path))
    except json.JSONDecodeError as error:
        validation.require(False, f"tests/cas-de-test.json : JSON invalide ({error})")
        return
    validation.require(isinstance(cases, list), "tests/cas-de-test.json : racine non-liste")
    if not isinstance(cases, list):
        return
    validation.require(
        len(cases) == MIN_TEST_CASES,
        f"tests/cas-de-test.json : {len(cases)} cas au lieu de {MIN_TEST_CASES}",
    )
    identifiers: list[str] = []
    expected_keys = {"id", "branche", "type", "prompt", "attendus"}
    for index, case in enumerate(cases, start=1):
        validation.require(
            isinstance(case, dict) and set(case) == expected_keys,
            f"cas {index} : schéma invalide (attendu {sorted(expected_keys)})",
        )
        if not isinstance(case, dict):
            continue
        if isinstance(case.get("id"), str):
            identifiers.append(case["id"])
        for key in ("branche", "type", "prompt"):
            validation.require(bool(case.get(key)), f"cas {index} : {key} vide")
        attendus = case.get("attendus")
        validation.require(
            isinstance(attendus, list) and len(attendus) >= MIN_ATTENDUS,
            f"cas {index} : attendus insuffisants (au moins {MIN_ATTENDUS} requis)",
        )
        validation.require(
            isinstance(attendus, list) and all(isinstance(a, str) and a.strip() for a in attendus),
            f"cas {index} : attendu vide ou non textuel",
        )
        validation.require(
            case.get("type") == ("critique" if index >= 21 else "standard"),
            f"cas {index} : classification différente du cadrage",
        )
    validation.require(
        len(identifiers) == len(set(identifiers)),
        "tests/cas-de-test.json : identifiants dupliqués",
    )
    validation.require(identifiers == [f"cas-{n:02d}" for n in range(1, 29)],
                       "tests/cas-de-test.json : ordre ou identifiants non conformes")
    expected_targets = BRANCH_FILES | {f"objets/{n}" for n in EXPECTED_OBJETS - {"_gabarit-objet.md"}}
    actual_targets = {str(c.get("branche", "")) + ".md" for c in cases if isinstance(c, dict)}
    validation.require(expected_targets <= actual_targets,
                       "tests/cas-de-test.json : branche ou objet non couvert")


def extract_markdown_targets(text: str) -> set[str]:
    """Extrait les chemins Markdown locaux cités en backticks ou en lien."""
    targets = set(re.findall(r"`([^`\n]+\.md(?:#[^`\n]+)?)`", text))
    targets.update(re.findall(r"\[[^\]]+\]\(([^)\n]+\.md(?:#[^)\n]+)?)\)", text))
    return targets


def target_exists(source: Path, target: str) -> bool:
    """Résout un lien local : relatif au fichier, racine, references/, templates/, objets/."""
    clean = target.split("#", 1)[0].replace("\\", "/")
    if not clean or "*" in clean or "<" in clean:
        return True
    if clean.startswith(("http://", "https://")):
        return True
    candidates = (
        source.parent / clean,
        ROOT / clean,
        ROOT / "references" / clean,
        ROOT / "references" / "templates" / clean,
        ROOT / "objets" / clean,
    )
    return any(candidate.resolve().is_file() for candidate in candidates)


def sibling_repo_pointer(target: str) -> str | None:
    """Renvoie le dépôt voisin visé par un chemin, ou None."""
    clean = target.split("#", 1)[0].replace("\\", "/")
    if "/" not in clean:
        return None
    head = clean.split("/", 1)[0]
    return head if head.lower() in SIBLING_REPO_NAMES else None


def validate_runtime_links(validation: Validation) -> None:
    """Vérifie les pointeurs Markdown du runtime.

    Un lien vers un fichier attendu mais pas encore écrit n'est qu'un
    avertissement en mode partiel ; un lien vers un fichier hors inventaire
    reste une erreur.
    """
    planned = (
        {f"references/{name}" for name in EXPECTED_REFERENCE_FILES}
        | {f"objets/{name}" for name in EXPECTED_OBJETS}
        | {f"references/templates/{name}" for name in EXPECTED_TEMPLATES}
    )
    planned_names = {path.rsplit("/", 1)[-1] for path in planned}
    for path in runtime_markdown_files():
        relative = path.relative_to(ROOT)
        for target in extract_markdown_targets(read_text(path)):
            sibling = sibling_repo_pointer(target)
            validation.require(
                sibling is None,
                f"{relative} : pointeur inter-dépôts interdit ({target}) — nommer "
                f"le skill `{sibling}`, jamais le chemin d'un de ses fichiers",
            )
            if sibling is not None or target_exists(path, target):
                continue
            name = target.split("#", 1)[0].replace("\\", "/").rsplit("/", 1)[-1]
            if name in planned_names:
                validation.expect_file(False, f"{relative} : lien vers un fichier pas encore écrit ({target})")
            else:
                validation.require(False, f"{relative} : lien local introuvable ({target})")


def validate_forbidden_content(validation: Validation) -> None:
    """Identifiants officiels hors registre, et valeurs de mémoire dans le runtime."""
    for path in runtime_markdown_files():
        relative = path.relative_to(ROOT)
        text = read_text(path)
        if relative != REGISTRY:
            matches = OFFICIAL_ID_PATTERN.findall(text)
            validation.require(
                not matches,
                f"{relative} : identifiant officiel en dur interdit hors registre "
                f"vérifié ({', '.join(sorted(set(matches)))})",
            )
        if relative in VALUE_EXEMPT or relative == Path("SKILL.md"):
            continue
        for label, pattern in VALUE_PATTERNS.items():
            found = sorted({match.group(0).strip() for match in pattern.finditer(text)})
            validation.require(
                not found,
                f"{relative} : {label} de mémoire interdit dans le runtime "
                f"({', '.join(found[:5])}) — nommer la valeur, renvoyer au registre",
            )
    for path in sorted((ROOT / "docs").rglob("*.md")):
        validation.require(not OFFICIAL_ID_PATTERN.search(read_text(path)),
                           f"{path.relative_to(ROOT)} : identifiant officiel hors registre")


def is_allowed_email(email: str) -> bool:
    """Détermine si une adresse e-mail détectée est explicitement tolérée."""
    if email.lower() in EMAIL_ALLOWED_EXACT:
        return True
    return email.lower().endswith(EMAIL_ALLOWED_DOMAIN_SUFFIX)


def validate_anti_pii(validation: Validation) -> None:
    """Recherche IBAN, NIR, e-mails et adresses IP dans tous les fichiers .md."""
    for path in sorted(ROOT.rglob("*.md")):
        if ".git" in path.parts:
            continue
        text = read_text(path)
        relative = path.relative_to(ROOT)
        validation.require(not IBAN_FR_PATTERN.findall(text), f"{relative} : IBAN français détecté")
        validation.require(
            not NIR_PATTERN.findall(text), f"{relative} : numéro de sécurité sociale détecté"
        )
        emails = [m for m in EMAIL_PATTERN.findall(text) if not is_allowed_email(m)]
        validation.require(
            not emails, f"{relative} : adresse e-mail détectée ({', '.join(sorted(set(emails)))})"
        )
        ips = IPV4_PATTERN.findall(text)
        validation.require(
            not ips, f"{relative} : adresse IP détectée ({', '.join(sorted(set(ips)))})"
        )


def main(argv: list[str]) -> int:
    """Exécute tous les contrôles et retourne un code compatible CI."""
    validation = Validation(partiel="--partiel" in argv)
    validate_frontmatter(validation)
    validate_guardrail_invariants(validation)
    validate_versions(validation)
    validate_structure(validation)
    validate_cases(validation)
    validate_runtime_links(validation)
    validate_forbidden_content(validation)
    validate_anti_pii(validation)
    for name in ("scripts/eval_suite.py", "scripts/package_skill.py", "agents/openai.yaml",
                 "tests/bareme-cas-de-test.md", ".github/workflows/validation.yml"):
        validation.expect_file((ROOT / name).is_file(), f"{name} : fichier absent")

    for warning in validation.warnings:
        print(f"[AVERTISSEMENT] {warning}")
    if validation.errors:
        for error in validation.errors:
            print(f"[ÉCHEC] {error}")
        print(
            f"[ÉCHEC] {len(validation.errors)} erreur(s), "
            f"{len(validation.warnings)} avertissement(s), {validation.checks} contrôles"
        )
        return 1
    print(
        f"[OK] {validation.checks} contrôles statiques réussis "
        f"({len(validation.warnings)} avertissement(s) non bloquant(s))"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
