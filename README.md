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

### The cycle

1. Open the folder: in GitHub Desktop, **Repository -> Show in Explorer**, or
   Ctrl+Shift+F.
2. Edit a file in any plain-text editor. Notepad works; VS Code or Notepad++ is
   easier because it shows the structure.
3. Back in GitHub Desktop, the left panel lists what changed. Click a file to
   see the exact lines.
4. Type a short summary in the box at the bottom left, click **Commit to main**,
   then click **Push origin** at the top.
5. Wait about two minutes. Check the **Actions** tab on GitHub: a green check
   means the site is updated, a red X means the build failed and the log names
   the file at fault. The old site stays up until a build succeeds.

Never edit files while GitHub Desktop is mid-commit, and do not rename the
`_pages`, `_news`, `_data`, or `_bibliography` folders.

### The two rules that break a build

**Front matter.** Every page begins with a block fenced by `---` lines. Keep
the `key: value` shape, keep the indentation, and do not delete the fences. If a
value contains a colon followed by a space, wrap the whole value in double
quotes.

**Blank lines.** Markdown needs a blank line before a list and before a heading.
Two lines of text with no blank line between them render as one paragraph.

### What to edit, and where

| Goal | File |
|---|---|
| Biography on the home page | `_pages/about.md`, below the closing `---` |
| Office address under the photo | `profile.more_info` in `_pages/about.md` |
| Photo | replace `assets/img/prof_pic.jpg`, keep the filename |
| Research interests, projects, directions | `_pages/research.md` |
| Publication list | `_bibliography/papers.bib` |
| Courses, curriculum, mentoring | `_pages/teaching.md` |
| CV summary page | `_pages/cv.md` |
| CV PDF behind the download icon | `assets/pdf/Amanat_Ur_Rahman_CV.pdf`, keep the filename |
| News items | `_news/`, one file per item |
| Email, Scholar, LinkedIn, GitHub | `_data/socials.yml` |
| Venue badge colors | `_data/venues.yml` |
| Site title, URL, description, keywords | `_config.yml` |
| Navigation order, hiding a page | `nav` and `nav_order` in each page's front matter |

### Adding a news item

Create a file in `_news/` named `YYYY-MM-DD-short-slug.md`:

```markdown
---
layout: post
date: 2027-01-15
inline: true
related_posts: false
---

Paper accepted at Operations Research.
```

The date in the filename and the `date:` field should match. The home page shows
the five most recent; change `announcements.limit` in `_pages/about.md` to show
more. Delete the file to remove the item.

### Adding a publication

Append an entry to `_bibliography/papers.bib`. Order does not matter; the page
sorts by year.

```bibtex
@article{rahman2027example,
  abbr={INFORMS},
  title={Title of the Paper},
  author={Rahman, Amanat Ur and Giovannelli, Tommaso},
  journal={Operations Research},
  volume={75},
  number={2},
  pages={100--120},
  year={2027},
  doi={10.1287/opre.2027.0001},
  html={https://doi.org/10.1287/opre.2027.0001},
  selected={true},
  abstract={One paragraph.}
}
```

- The key on the first line (`rahman2027example`) must be unique
- `author=` must use `Last, First` form, so `Rahman, Amanat Ur`, or the name
  will not render in bold
- `abbr=` is the badge on the left; add its color to `_data/venues.yml`
- `selected={true}` also promotes the entry to the home page
- `html=` adds a link button, `pdf=filename.pdf` links a file in `assets/pdf/`
- Every field ends with a comma except the last one

When a manuscript moves from review to acceptance, edit its entry in place:
change `abbr` from `Under Review` to the journal, and fill in `journal`,
`volume`, `pages`, and `doi`.

### Adding a course

Copy an existing block in `_pages/teaching.md` and change the text. The pattern:

```markdown
- **ISE 4012: Probabilistic Systems Models.** Instructor, Fall 2027.
  Topics: Markov chains, queueing models, reliability, simulation basics.
```

The second line must be indented by two spaces so it stays inside the bullet.
To add an institution, add a `## Institution Name` heading.

### Adding a research project

Copy an existing block in `_pages/research.md`. The pattern is a bold title, an
italic line of coauthors and status, then bullets:

```markdown
**Title of the project**
*with A. Coauthor. Under review, 2027.*

- First point
- Second point
```

### Hiding or reordering pages

In a page's front matter, `nav: false` removes it from the navigation bar
without deleting the page, and `nav_order` sets left-to-right position. Current
order: research 1, publications 2, teaching 3, cv 4.

### If something goes wrong

GitHub Desktop's **History** tab lists every commit. Right-click one and choose
**Revert changes in commit** to undo it, then push. The site returns to its
previous state on the next build.

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
