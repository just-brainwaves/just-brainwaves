# 🛠️ Setup — 4 steps

This is a **GitHub profile README** with an *Architectural Dark* theme
(ink-black background · slate type · a single emerald accent) that blends into
GitHub's dark UI. To make it appear on your profile:

### 1. Create the magic repo
Make a repo named **exactly** your username: `just-brainwaves/just-brainwaves`
(GitHub renders this repo's README on your profile page.)

### 2. Drop in the files
```
just-brainwaves/
├── README.md
├── assets/
│   ├── header.svg      ← hero banner (self-drawing lines)
│   ├── pipeline.svg    ← RAG pipeline signature visual
│   ├── divider.svg     ← reused section divider
│   └── footer.svg      ← animated wave footer
└── .github/
    └── workflows/
        └── snake.yml
```
Relative paths (`./assets/header.svg`) resolve once everything is in the repo.

### 3. Turn on the snake 🐍
- Push the repo, then open the **Actions** tab → enable workflows.
- Open **"Generate Contribution Snake"** → **Run workflow**.
- It builds an `output` branch holding the two snake SVGs the README points to.
- After that it auto-refreshes twice a day.

> **Why the snake looked black before:** the old palette painted the *empty*
> grid cells near-black (`0a0e1a`) and recolored the dots cyan, so on a profile
> with sparse history it read as "all black, no green." The workflow now uses a
> **light palette** — empty cells are light grey (`ebedf0`) and contributions
> fade up through emerald, with an ink-colored snake that stays visible on white.
> The README also defaults to the **light** SVG.

### 4. Host your own stats instance 📊
The **stats**, **top-langs**, and **project pin** cards use
[`github-readme-stats`](https://github.com/anuraghazra/github-readme-stats). The
shared public instance (`github-readme-stats.vercel.app`) is chronically
rate-limited and frequently returns `503 DEPLOYMENT_PAUSED`, which is why those
cards show as broken images. The fix is a free 2-minute self-host:

1. Deploy your own copy (one click):
   <https://vercel.com/new/clone?repository-url=https://github.com/anuraghazra/github-readme-stats>
2. When Vercel asks for a **project name**, use `github-readme-stats-just-brainwaves`
   so the deployed URL becomes `https://github-readme-stats-just-brainwaves.vercel.app`
   (the exact host this README already points to — no edits needed).
3. *(Optional)* For private-commit counts, add a `PAT_1` env var in Vercel with a
   GitHub token (`repo` + `read:user` scopes), then redeploy.

> Forking to a different name? Swap the host everywhere in one shot:
> ```bash
> sed -i 's#github-readme-stats-just-brainwaves\.vercel\.app#YOUR-INSTANCE.vercel.app#g' README.md
> ```

### 5. Personalize
- Every stat/card already uses `just-brainwaves` — change it if you fork.
- In **Projects**, duplicate the pin-card block and set `&repo=YOUR_REPO`.
- Recolor everything by swapping the palette (search the hex codes):

  | token     | hex        | used for                              |
  |-----------|------------|---------------------------------------|
  | bg        | `#0d1117`  | card / banner background (GitHub dark) |
  | bg-deep   | `#010409`  | gradient floor                        |
  | surface   | `#161b22`  | elevated panels / badge labels        |
  | line      | `#30363d`  | hairlines / borders                   |
  | text      | `#e6edf3`  | headings / wordmark                   |
  | body      | `#adbac7`  | card body text                        |
  | muted     | `#8b949e`  | captions                              |
  | emerald   | `#10b981`  | the single accent                     |
  | emerald+  | `#34d399`  | bright accent / hover glow            |
  | glow      | `#5ee9a8`  | traveling-node highlight              |

> Heads up: the animated SVGs (`header`, `pipeline`, `divider`, `footer`)
> animate in GitHub's browser view because SMIL + in-SVG CSS survive
> GitHub's image proxy. Static previews (and some markdown renderers) show them
> frozen — that's expected. No external GIFs or emoji-PNGs are used, so there
> are no broken-image links to chase.
