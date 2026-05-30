# 🛠️ Setup — 4 steps

This is a **GitHub profile README**. To make it appear on your profile:

### 1. Create the magic repo
Make a repo named **exactly** your username: `just-brainwaves/just-brainwaves`
(GitHub renders this repo's README on your profile page.)

### 2. Drop in the files
```
just-brainwaves/
├── README.md
├── assets/
│   ├── header.svg
│   ├── terminal.svg
│   └── divider.svg
└── .github/
    └── workflows/
        └── snake.yml
```
Relative paths (`./assets/header.svg`) work once everything is in the repo.

### 3. Turn on the snake 🐍
- Push the repo, then go to the **Actions** tab → enable workflows.
- Open **"Generate Contribution Snake"** → **Run workflow**.
- It creates an `output` branch with the snake SVGs the README points to.
- After that it auto-refreshes twice a day.

### 4. Personalize
- Every stat/card already uses `just-brainwaves` — change it if you fork.
- In the **Projects** section, duplicate the pin-card block and set `&repo=YOUR_REPO`.
- Want a different vibe? Recolor the SVGs (search the hex codes) — the palette is:
  `#00f0ff` cyan · `#a855f7` violet · `#ff2e97` magenta · `#39ff14` lime · `#0a0e1a` void.

> Heads up: the animated SVGs (`header`, `terminal`, `divider`) animate in GitHub's
> browser view because SMIL + in-SVG CSS survive GitHub's image proxy. Static
> previews (and some markdown renderers) show them frozen — that's expected.
