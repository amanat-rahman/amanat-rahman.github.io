#!/usr/bin/env python3
"""
Rebuild the CV PDF that the website serves.

The website copy differs from the CV Amanat submits with applications:
  * research-track section order
  * no phone number
  * email obfuscated, with no mailto link, so the PDF text layer holds no
    machine-readable address
  * no GPA or CGPA

The master source in cv_AR_cowork is never modified. Patches are applied to a
temporary copy, compiled there, and only the resulting PDF is copied in.

Run after any change to the CV:

    python3 tools/build-web-cv.py

Requires pdflatex. Override the source folder with --src if it moves.
"""
import argparse
import pathlib
import shutil
import subprocess
import sys
import tempfile

DEFAULT_SRC = pathlib.Path.home() / "OneDrive" / "cv_AR_cowork" / "academic_cv"
OUT = pathlib.Path(__file__).resolve().parent.parent / "assets" / "pdf" / "Amanat_Ur_Rahman_CV.pdf"

OLD_CONTACT = """\t{+1 (502) 340-6559\\cvsep
\t\t\\href{mailto:rahmanah@mail.uc.edu}{rahmanah@mail.uc.edu}\\cvsep
\t\t\\href{https://scholar.google.com/citations?user=2l4fFy4AAAAJ}{Google Scholar}\\cvsep
\t\t\\href{https://amanat-rahman.github.io/}{amanat-rahman.github.io}}"""

NEW_CONTACT = """\t{rahmanah\\,[at]\\,mail\\,[dot]\\,uc\\,[dot]\\,edu\\cvsep
\t\t\\href{https://scholar.google.com/citations?user=2l4fFy4AAAAJ}{Google Scholar}\\cvsep
\t\t\\href{https://amanat-rahman.github.io/}{amanat-rahman.github.io}}"""

GPA_LINES = [
    ("University of Cincinnati \\hfill GPA: 3.952/4.00\\\\", "University of Cincinnati\\\\"),
    ("University of Louisville \\hfill GPA: 3.875/4.00\\\\", "University of Louisville\\\\"),
    ("Ahsanullah University of Science and Technology (AUST) \\hfill CGPA: 3.795/4.00\\\\",
     "Ahsanullah University of Science and Technology (AUST)\\\\"),
]


def patch(text):
    """Apply every web-copy change, failing loudly if the source has moved on."""
    missing = []

    if "\\def\\CVTRACK{teaching}" in text:
        text = text.replace("\\def\\CVTRACK{teaching}", "\\def\\CVTRACK{research}", 1)
    elif "\\def\\CVTRACK{research}" not in text:
        missing.append("CVTRACK switch")

    if OLD_CONTACT in text:
        text = text.replace(OLD_CONTACT, NEW_CONTACT, 1)
    elif NEW_CONTACT not in text:
        missing.append("contact block (phone + email)")

    for old, new in GPA_LINES:
        if old in text:
            text = text.replace(old, new, 1)
        elif new not in text:
            missing.append(f"GPA line: {old[:40]}...")

    if missing:
        sys.exit("The CV source changed; these patches no longer match:\n  - "
                 + "\n  - ".join(missing)
                 + "\nUpdate tools/build-web-cv.py before publishing.")
    return text


def verify(pdf):
    """Refuse to publish a PDF that still carries personal details."""
    raw = pdf.read_bytes()
    for probe in (b"mailto", b"340-6559", b"rahmanah@"):
        if probe in raw:
            sys.exit(f"Refusing to publish: {probe.decode()!r} is still in the PDF.")
    try:
        txt = subprocess.run(["pdftotext", str(pdf), "-"], capture_output=True,
                             text=True, check=True).stdout
    except (FileNotFoundError, subprocess.CalledProcessError):
        print("pdftotext unavailable; skipped the text-layer check.")
        return
    for probe in ("GPA", "502"):
        if probe in txt:
            sys.exit(f"Refusing to publish: {probe!r} is still in the PDF text.")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--src", type=pathlib.Path, default=DEFAULT_SRC,
                    help=f"folder holding cv_academic_AR.tex (default: {DEFAULT_SRC})")
    args = ap.parse_args()

    tex = args.src / "cv_academic_AR.tex"
    sty = args.src / "cv_academic_style_AR.sty"
    for f in (tex, sty):
        if not f.exists():
            sys.exit(f"Not found: {f}")

    with tempfile.TemporaryDirectory() as tmp:
        work = pathlib.Path(tmp)
        shutil.copy(sty, work / sty.name)
        (work / tex.name).write_text(patch(tex.read_text(encoding="utf-8")), encoding="utf-8")
        for _ in range(2):            # twice, so page totals and refs settle
            r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", tex.name],
                               cwd=work, capture_output=True, text=True)
        if r.returncode != 0:
            sys.exit("pdflatex failed:\n" + r.stdout[-2000:])
        built = work / "cv_academic_AR.pdf"
        verify(built)
        OUT.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(built, OUT)

    print(f"Wrote {OUT} ({OUT.stat().st_size:,} bytes). Commit and push to publish.")


if __name__ == "__main__":
    main()
