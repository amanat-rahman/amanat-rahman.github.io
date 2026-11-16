#!/usr/bin/env python3
"""
Rebuild the CV PDF that the website serves.

Source: Amanat's general academic CV (cv_AR_cowork/academic_cv/Amanat_Ur_Rahman_CV_general.tex),
the version not tied to any job posting. The website copy differs from it in:
  * no phone number
  * email obfuscated, with no mailto link, so the PDF text layer holds no
    machine-readable address
  * no GPA or CGPA
  * no References section (referees' names and contact details stay private)
  * "Ph.D. Student" in the header until CANDIDATE below is set to True
  * the 2026 INFORMS talk listed under the paper's current title

cv_AR_cowork is read-only. Patches are applied to a temporary copy, compiled
there, and only the resulting PDF is copied into this repository.

Run after any change to the CV:

    python3 tools/build-web-cv.py

Requires pdflatex. Override the source folder with --src if it moves.
"""
import argparse
import pathlib
import re
import shutil
import subprocess
import sys
import tempfile

# Set to True once Amanat passes his Ph.D. proposal defense (November 20, 2026).
CANDIDATE = False

DEFAULT_SRC = pathlib.Path.home() / "OneDrive" / "cv_AR_cowork" / "academic_cv"
SRC_NAME = "Amanat_Ur_Rahman_CV_general.tex"
STY_NAME = "cv_academic_style_AR.sty"
OUT = pathlib.Path(__file__).resolve().parent.parent / "assets" / "pdf" / "Amanat_Ur_Rahman_CV.pdf"

EMAIL_SAFE = "rahmanah\\,[at]\\,mail\\,[dot]\\,uc\\,[dot]\\,edu"


def patch(text):
    """Apply every web-copy change, failing loudly if the source has moved on."""
    missing = []

    def sub(pattern, repl, label, count=1, flags=0):
        nonlocal text
        new, n = re.subn(pattern, repl, text, count=count, flags=flags)
        if n == 0:
            missing.append(label)
        text = new

    if "\\def\\CVTRACK{research}" not in text:
        sub(r"\\def\\CVTRACK\{\w+\}", r"\\def\\CVTRACK{research}", "CVTRACK switch")

    # Contact line: drop the phone, replace the mailto link with the obfuscated address.
    sub(r"\+1 \(502\) 340-6559\\cvsep\s*", "", "phone in contact line")
    sub(r"\\href\{mailto:rahmanah@mail\.uc\.edu\}\{rahmanah@mail\.uc\.edu\}",
        lambda m: EMAIL_SAFE, "email in contact line")

    # Every GPA or CGPA, wherever it sits on the line.
    sub(r"\s*\\hfill\s*C?GPA:\s*[0-9.]+/4\.00", "", "GPA lines", count=0)

    # References section: the command is defined empty, so every \secReferences prints nothing.
    sub(r"\\newcommand\{\\secReferences\}\{%",
        lambda m: "\\newcommand{\\secReferences}{}\n\\newcommand{\\secReferencesPrivate}{%",
        "References section")

    if not CANDIDATE:
        sub(r"Ph\.D\.\\ Candidate", lambda m: "Ph.D.\\ Student", "header title (Candidate)")

    # The 2026 INFORMS talk was given under the paper's current title (Amanat, 16 Nov 2026).
    # MOPTA and IISE 2026 keep the earlier title, under which T. Giovannelli presented.
    old_title = ("Using stochastic programming to mitigate patient no-shows and short-notice "
                 "cancellations in outpatient clinics through overbooking and walk-ins.")
    new_title = ("Two-stage stochastic optimization of outpatient scheduling with overbooking and "
                 "walk-in patients under no-shows and short-notice cancellations.")
    pattern = r"\s+".join(map(re.escape, old_title.split())) + r"(\s+2026 INFORMS Annual Meeting)"
    sub(pattern, lambda m: new_title + m.group(1), "INFORMS 2026 talk title")

    if missing:
        sys.exit("The CV source changed; these patches no longer match:\n  - "
                 + "\n  - ".join(missing)
                 + "\nUpdate tools/build-web-cv.py before publishing.")
    return text


def verify(pdf):
    """Refuse to publish a PDF that still carries private details."""
    raw = pdf.read_bytes()
    for probe in (b"mailto", b"340-6559", b"rahmanah@"):
        if probe in raw:
            sys.exit(f"Refusing to publish: {probe.decode()!r} is still in the PDF.")
    try:
        txt = subprocess.run(["pdftotext", str(pdf), "-"], capture_output=True,
                             text=True, check=True).stdout
    except (FileNotFoundError, subprocess.CalledProcessError):
        sys.exit("pdftotext unavailable; cannot verify the PDF, so it was not published.")
    probes = ["GPA", "502", "@", "Phone", "References", "Neptune", "AWS"]
    if not CANDIDATE:
        probes.append("Candidate")
    for probe in probes:
        if probe in txt:
            sys.exit(f"Refusing to publish: {probe!r} is still in the PDF text.")


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--src", type=pathlib.Path, default=DEFAULT_SRC,
                    help=f"folder holding {SRC_NAME} (default: {DEFAULT_SRC})")
    args = ap.parse_args()

    tex = args.src / SRC_NAME
    sty = args.src / STY_NAME
    for f in (tex, sty):
        if not f.exists():
            sys.exit(f"Not found: {f}")

    with tempfile.TemporaryDirectory() as tmp:
        work = pathlib.Path(tmp)
        shutil.copy(sty, work / sty.name)
        (work / "cv.tex").write_text(patch(tex.read_text(encoding="utf-8")), encoding="utf-8")
        for _ in range(2):            # twice, so page totals and refs settle
            r = subprocess.run(["pdflatex", "-interaction=nonstopmode", "-halt-on-error", "cv.tex"],
                               cwd=work, capture_output=True, text=True)
        if r.returncode != 0:
            sys.exit("pdflatex failed:\n" + r.stdout[-2000:])
        built = work / "cv.pdf"
        verify(built)
        OUT.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(built, OUT)

    print(f"Wrote {OUT} ({OUT.stat().st_size:,} bytes). Commit and push to publish.")


if __name__ == "__main__":
    main()
