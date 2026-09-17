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
| Name, title, tagline, bio, links, research interests, the four "at a glance" numbers | `_data/profile.yml` |
| Degrees, theses, advisors, coursework | `_data/education.yml` |
| Research and industry positions with bullets | `_data/experience.yml` |
| Publications, grouped by category | `_data/publications.yml` |
| Talks, posters, seminars | `_data/talks.yml` |
| Courses taught, prepared-to-teach list, curriculum work, mentoring | `_data/teaching.yml` |
| Research page: intro, projects, directions | `_data/research.yml` |
| Awards | `_data/awards.yml` |
| Skills | `_data/skills.yml` |
| Reviewing, service, memberships | `_data/service.yml` |
| News items on the home page | `_data/news.yml` |
| Photo | replace `assets/img/pic_medium_AR.jpg`, keep the filename |
| CV PDF behind the download buttons | replace `assets/pdf/Amanat_Ur_Rahman_CV.pdf`, keep the filename |
| Navigation bar order, site title, description | `_config.yml` |
| Colors, fonts, spacing | `assets/css/style.css` (tokens are at the top) |

Pages: `index.html` (home), `research.html`, `publications.html`, `talks.html`,
`teaching.html`, `cv.html`, `404.html`. Shared pieces are in `_includes/`; the
page frame is `_layouts/default.html`.

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

**Add a publication** (inside the right category in `_data/publications.yml`;
write your name as `A. U. Rahman`, which is bolded automatically):

```yaml
    - id: rahman2027example
      title: Title of the paper
      authors: A. U. Rahman and T. Giovannelli
      venue: Operations Research 75(2), 100 to 120
      year: "2027"
      doi: 10.1287/opre.2027.0001
      selected: true
```

`selected: true` also lists it on the home page. When a manuscript is
accepted, edit its existing entry: move it to the journal category, remove
`status`, and fill in `venue` and `doi`.

**Add a talk** (top of `_data/talks.yml`; entries are grouped by `year`):

```yaml
- kind: Conference presentation
  venue: 2027 INFORMS Annual Meeting
  location: Atlanta, GA, USA
  date: October 2027
  year: "2027"
  title: Title of the talk
  authors: A. U. Rahman and T. Giovannelli
  presenter: A. U. Rahman
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
