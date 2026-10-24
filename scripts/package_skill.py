"""Construit un package runtime déterministe du skill dsi-fpt."""

from __future__ import annotations

import argparse
import re
import sys
import zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = "dsi-fpt"
FIXED_TIMESTAMP = (2026, 1, 1, 0, 0, 0)

# Artefact de maintenance : jamais distribué dans le package runtime.
EXCLUDED_FILES = {ROOT / "references" / "cache-valeurs.md"}

VERSION_TITLE_PATTERN = re.compile(
    r"#\s*Skill\s*:\s*" + re.escape(SKILL_NAME) + r"\s*\(v(\d+\.\d+\.\d+)\)"
)


def read_version() -> str:
    """Lit la version du skill depuis le titre de SKILL.md."""
    skill_path = ROOT / "SKILL.md"
    text = skill_path.read_text(encoding="utf-8")
    match = VERSION_TITLE_PATTERN.search(text)
    if not match:
        raise ValueError("SKILL.md : version introuvable dans le titre (# Skill : ... (vX.Y.Z))")
    return match.group(1)


def runtime_files() -> list[Path]:
    """Liste les seuls fichiers nécessaires à l'exécution du skill."""
    files = [ROOT / "SKILL.md", ROOT / "agents" / "openai.yaml"]
    files.extend(sorted((ROOT / "references").rglob("*")))
    files.extend(sorted((ROOT / "objets").rglob("*")))
    selected = [
        path
        for path in files
        if path.is_file() and path not in EXCLUDED_FILES
    ]
    if any(path.is_symlink() or not path.resolve().is_relative_to(ROOT) for path in selected):
        raise ValueError("Lien symbolique ou fichier hors dépôt dans le runtime")
    if not (ROOT / "agents" / "openai.yaml").is_file():
        raise ValueError("agents/openai.yaml absent")
    return selected


def checked_output(raw_output: str | None, version: str) -> Path:
    """Résout la destination et refuse toute écriture hors du dépôt."""
    default_output = ROOT / "dist" / f"{SKILL_NAME}-{version}.zip"
    output = Path(raw_output).expanduser() if raw_output else default_output
    if not output.is_absolute():
        output = ROOT / output
    output = output.resolve()
    try:
        output.relative_to(ROOT)
    except ValueError as error:
        raise ValueError("La destination du package doit rester dans le dépôt") from error
    if output.suffix != ".zip" or output in runtime_files() or output == ROOT / "LICENSE":
        raise ValueError("La destination doit être une archive .zip distincte des sources")
    return output


def write_package(output: Path) -> None:
    """Écrit une archive triée avec horodatages fixes (résultat déterministe)."""
    output.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for path in runtime_files():
            relative = path.relative_to(ROOT).as_posix()
            info = zipfile.ZipInfo(relative, FIXED_TIMESTAMP)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, path.read_bytes())


def parse_args() -> argparse.Namespace:
    """Construit l'interface en ligne de commande."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output",
        help="archive cible dans le dépôt (défaut : dist/dsi-fpt-<VERSION>.zip)",
    )
    return parser.parse_args()


def main() -> int:
    """Construit l'archive et affiche son chemin et son contenu."""
    args = parse_args()
    try:
        version = read_version()
        output = checked_output(args.output, version)
        write_package(output)
    except (OSError, ValueError) as error:
        print(f"[ÉCHEC] {error}")
        return 1
    print(f"[OK] Package créé : {output}")
    print(f"[OK] {len(runtime_files())} fichiers runtime")
    return 0


if __name__ == "__main__":
    sys.exit(main())
