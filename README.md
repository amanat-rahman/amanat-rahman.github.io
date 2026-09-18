# amanat-rahman.github.io

Personal website of Amanat Ur Rahman. A hand-built Jekyll site, deployed by
GitHub Pages directly from the `main` branch. No theme dependency, no build
workflow: push, wait about a minute, done.

## How the site is organized

All content lives in plain YAML files under `_data/`. The pages in the root
folder are templates that read those files. To change what the site says, edit
`_data/`; to change how it looks, edit `assets/css/style.css`.

| To change | Edit |
|---|---|
| Name, title, tagline, bio, links, research interests, contact block | `_data/profile.yml` |
| Degrees, theses, advisors, coursework | `_data/education.yml` |
| Research and industry positions with bullets | `_data/experience.yml` |
| Publications | `_data/publications.yml` |
| Talks, posters, seminars | `_data/talks.yml` |
| Courses taught, prepared-to-teach list, curriculum work, mentoring | `_data/teaching.yml` |
| Research page: intro, research, directions, projects | `_data/research.yml` |
| Awards and honors | `_data/awards.yml` |
| Skills | `_data/skills.yml` |
| Reviewing, service, memberships | `_data/service.yml` |
| Work address and email (stored reversed) | `contact:` in `_data/profile.yml` |
| News items on the home page | `_data/news.yml` |
| Photo | replace `assets/img/pic_medium_AR.jpg`, keep the filename |
| CV PDF behind the download buttons | replace `assets/pdf/Amanat_Ur_Rahman_CV.pdf`, keep the filename |
| Navigation bar order, site title, description | `_config.yml` |
| Colors, fonts, spacing | `assets/css/style.css` (tokens are at the top) |

The home page is, in order: intro and photo, contact, research interests, news.

Pages: `index.html` (home), `research.html`, `publications.html`,
`teaching.html`, `awards.html`, `cv.html`, `404.html`. Shared pieces are in
`_includes/`; the page frame is `_layouts/default.html`.

**Research page wording.** Each research entry uses Question, Approach, Outcome.
Keep the Outcome line about what a decision maker gets from the work, not about
how hard the instance was to solve. Projects use short bullets, never
paragraphs.

**Publications and talks share one page.** `_data/publications.yml` and
`_data/talks.yml` are merged, sorted by the `sort` field (`YYYYMM`), and grouped
by year. Each entry carries a `type` that becomes its tag: `journal`,
`proceedings`, `working`, `talk`, `poster`, or `seminar`.

**The email address is obfuscated.** `_data/profile.yml` stores it reversed and
split, `_includes/email.html` renders it as readable text, and
`assets/js/site.js` reassembles it into a `mailto:` link in the browser. The
plain address never appears in the HTML source. To change it, reverse the new
address by hand: the local part goes in `user_reversed`, the domain in
`domain_reversed`, both written backwards.

## Editing cycle

1. Edit a file in this folder.
2. In GitHub Desktop: write a summary, **Commit to main**, **Push origin**.
3. GitHub rebuilds the site in about a minute. The Actions tab shows a
   `pages build and deployment` run; green means live.

If a build fails, the previous version stays online. The run log names the file
and line at fault, and the cause is nearly always YAML indentation.

## YAML rules that matter

- Indentation is two spaces per level. Never tabs.
- A value containing a colon followed by a space, or starting with a quote or
  bracket, must be wrapped in double quotes: `title: "Design: a study"`.
- A multi-line paragraph starts with `>-` on the key line, with the text
  indented beneath it.
- Lists are lines starting with `- `.

## Common edits

**Add a news item** (top of `_data/news.yml`; the home page shows the five
most recent by date):

```yaml
- date: 2027-01-15
  text: Paper accepted at Operations Research.
```

**Add a publication** (`_data/publications.yml`; write your name as
`A. U. Rahman`, which is bolded automatically):

```yaml
- id: rahman2027example
  type: journal          # journal | proceedings | working
  title: Title of the paper
  authors: A. U. Rahman and T. Giovannelli
  venue: Operations Research 75(2), 100 to 120
  year: "2027"
  sort: "202703"         # YYYYMM, orders entries within the year
  doi: 10.1287/opre.2027.0001
```

When a manuscript is accepted, edit its existing entry: change `type` from
`working` to `journal`, delete the `status` line, and fill in the real `venue`
and `doi`.

**Add a talk** (`_data/talks.yml`):

```yaml
- type: talk             # talk | poster | seminar
  title: Title of the talk
  authors: A. U. Rahman and T. Giovannelli
  venue: 2027 INFORMS Annual Meeting, Atlanta, GA, USA
  date: October 2027
  year: "2027"
  sort: "202710"
  presenter: A. U. Rahman
  award: Best paper award      # optional
```

**Add a course** under the right institution and group in `_data/teaching.yml`:

```yaml
          - code: ISE 4012
            title: Probabilistic Systems Models
            term: Fall 2027
            topics: Markov chains, queueing models, reliability
```

## Local preview (optional)

Requires Ruby and Bundler.

```bash
bundle install
bundle exec jekyll serve
```

Then open `http://localhost:4000`.
