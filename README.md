# amanat-rahman.github.io

Personal academic website of Amanat Ur Rahman, built on the
[al-folio](https://github.com/alshedivat/al-folio) Jekyll theme and deployed to
GitHub Pages through GitHub Actions.

---

## 1. One-time deployment setup

The site is already configured for the URL `https://amanat-rahman.github.io`.
Three steps remain, all on GitHub.

### Step 1 — create the repository

On GitHub, create a **new public repository named exactly**:

```
amanat-rahman.github.io
```

Do not add a README, .gitignore, or license during creation. The repository name
must match the username exactly, otherwise the site will be served from a
subpath and every internal link will break.

### Step 2 — push this folder

From this folder, in Git Bash or PowerShell:

```bash
git init
git branch -M main
git add .
git commit -m "Initial site"
git remote add origin https://github.com/amanat-rahman/amanat-rahman.github.io.git
git push -u origin main
```

If Git asks for credentials, use a GitHub personal access token as the password
(Settings -> Developer settings -> Personal access tokens -> Fine-grained tokens,
with Contents: Read and write on this repository).

### Step 3 — enable Pages and Actions

1. Repository -> **Settings** -> **Actions** -> **General** -> under "Workflow
   permissions" select **Read and write permissions**, then Save.
2. Push once (Step 2 does this). The workflow `.github/workflows/deploy.yml`
   runs, builds the site, and pushes the compiled output to a branch named
   `gh-pages`.
3. Repository -> **Settings** -> **Pages** -> under "Build and deployment",
   set Source = **Deploy from a branch**, Branch = **gh-pages**, folder = **/ (root)**.
   Save.

The site appears at `https://amanat-rahman.github.io` within a few minutes.
Check **Actions** tab for build status. A red run means the build failed; the log
names the file at fault.

---

## 2. Day-to-day editing

Every change follows the same cycle: edit a file here, then

```bash
git add .
git commit -m "describe the change"
git push
```

The Action rebuilds and redeploys automatically. There is no need to build
locally.

### What to edit, and where

| Goal | File |
|---|---|
| Biography text on the home page | `_pages/about.md` (below the `---` block) |
| Photo | replace `assets/img/prof_pic.jpg` (currently a placeholder) |
| Office address block under the photo | `profile.more_info` in `_pages/about.md` |
| Email, Scholar, LinkedIn, GitHub, CV link | `_data/socials.yml` |
| Publications | `_bibliography/papers.bib` |
| News items on the home page | `_news/` (one file per item) |
| CV PDF served by the download icon | `assets/pdf/Amanat_Ur_Rahman_CV.pdf` |
| Venue badge colors in the bibliography | `_data/venues.yml` |
| Site title, URL, description, keywords | `_config.yml` |

### Adding a news item

Create a file in `_news/` named `YYYY-MM-DD-short-slug.md`:

```markdown
---
layout: post
date: 2027-01-15
inline: true
related_posts: false
---

Paper accepted at ...
```

The home page shows the five most recent items. Change `announcements.limit` in
`_pages/about.md` to show more.

### Adding a publication

Append a BibTeX entry to `_bibliography/papers.bib`. Useful non-standard fields:

- `abbr={INFORMS}` renders a small badge on the left
- `selected={true}` promotes the entry to the home page
- `html={https://doi.org/...}` adds a link button
- `pdf={filename.pdf}` links a file placed in `assets/pdf/`
- `abstract={...}` adds an expandable abstract

Author names must be written `Rahman, Amanat Ur` so that jekyll-scholar bolds
them (the matching rule lives under `scholar:` in `_config.yml`).

---

## 3. Page set

| Page | File | In nav |
|---|---|---|
| Home / About | `_pages/about.md` | yes, permalink `/` |
| Research | `_pages/research.md` | yes, order 1 |
| Publications | `_pages/publications.md` | yes, order 2 |
| Teaching | `_pages/teaching.md` | yes, order 3 |
| CV | `_pages/cv.md` | yes, order 4 |
| News archive | `_pages/news.md` | hidden, reachable at `/news/` |
| 404 | `_pages/404.md` | n/a |

`nav_order` in a page's front matter controls left-to-right position. Set
`nav: false` to hide a page without deleting it.

Style note: these pages are deliberately itemized rather than narrative. Course
entries carry a code, title, role, term, and topic list. Research entries carry
a title, coauthors, status, and bullets. No teaching philosophy or statement
prose appears on the site; those belong in the application package.

To add a projects, blog, or group page later, copy the corresponding file from
<https://github.com/alshedivat/al-folio/tree/main/_pages> into `_pages/`, add
the collection it depends on under `collections:` in `_config.yml`, and set
`nav: true`.

---

## 4. Local preview (optional)

Not required, since the Action builds on every push. If a local preview is
wanted, the theme needs Ruby 3.3.5 and Bundler:

```bash
bundle install
bundle exec jekyll serve
```

Docker is the simpler path on Windows:

```bash
docker compose up
```

Both serve the site at `http://localhost:8080`.

---

## 5. Open items

- `assets/img/prof_pic.jpg` is a generated placeholder. Replace it with a
  professional headshot, square crop, at least 800x800 px.
- The CV PDF in `assets/pdf/` is a copy of the research-track build dated
  2026-08. Re-copy it whenever the CV is recompiled.
- Google Scholar, LinkedIn, and GitHub handles in `_data/socials.yml` are set;
  add `orcid_id` once an ORCID record exists.
- The publications page is the natural next addition; the bibliography that
  feeds it is already complete. Flip `nav: false` to `nav: true` in
  `_pages/publications.md` when the working papers are ready to be listed
  publicly.
- Two entries in `papers.bib` are marked `Under Review` and `In Prep.`. Update
  those `abbr` and `journal` fields as the manuscripts progress.
