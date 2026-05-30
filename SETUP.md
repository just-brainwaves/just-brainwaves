# 🛠️ Setup — 4 steps

This is a **GitHub profile README** with an *Architectural Light* theme
(bone-white background · ink type · a single emerald accent). To make it appear
on your profile:

### 1. Create the magic repo
Make a repo named **exactly** your username: `just-brainwaves/just-brainwaves`
(GitHub renders this repo's README on your profile page.)

### 2. Drop in the files
```
just-brainwaves/
├── README.md
├── assets/
│   ├── header.svg      ← hero banner (self-drawing lines)
│   ├── terminal.svg    ← light "whoami" console
│   ├── matrix.svg      ← the signature data-rain piece
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

### 4. Personalize
- Every stat/card already uses `just-brainwaves` — change it if you fork.
- In **Projects**, duplicate the pin-card block and set `&repo=YOUR_REPO`.
- Recolor everything by swapping the palette (search the hex codes):

  | token   | hex        | used for                         |
  |---------|------------|----------------------------------|
  | paper   | `#ffffff`  | card backgrounds                 |
  | bone    | `#fbfbfa`  | banner / footer background       |
  | ink     | `#111114`  | headings / wordmark              |
  | graphite| `#3f3f46`  | body text                        |
  | slate   | `#9aa0a6`  | muted captions                   |
  | line    | `#e9eae7`  | hairlines / borders              |
  | emerald | `#0e9f6e`  | the single accent (everything)   |

> Heads up: the animated SVGs (`header`, `terminal`, `matrix`, `divider`,
> `footer`) animate in GitHub's browser view because SMIL + in-SVG CSS survive
> GitHub's image proxy. Static previews (and some markdown renderers) show them
> frozen — that's expected. No external GIFs or emoji-PNGs are used, so there
> are no broken-image links to chase.
