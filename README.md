# Physics-Plots Web App — Quick Guide

## Setup (first time)

```bash
npm install
```

---

## Run locally (development)

```bash
npm run dev
```

Open in browser:

```
http://localhost:4321/
```

The page updates automatically when you save changes.

---

## Add plots

1. Place files in:

```
public/plots/
```

2. Update:

```
src/data/plots.json
```

Make sure JSON syntax is valid (double quotes, no trailing commas).

---

## Add a new page (optional)

Copy an existing page:

```
src/pages/VVsemilep → src/pages/myplots
```

Edit:

```
index.astro
```

New page will be available at:

```
/myplots
```

---

## Build static site

```bash
npm run build
```

Output:

```
dist/
```

---

## Deploy to internet

```bash
npx vercel link
npx vercel --prod
```

This publishes the site to a stable URL:

```
https://your-project.vercel.app
```

---

## Update website

After making changes:

```bash
npm run build
npx vercel --prod
```

The same domain will be updated.

---

## Notes

* Do not open `dist/index.html` directly; use a server or deploy.
* Routes correspond to files in `src/pages/`.
* Data files (JSON) do not create pages by themselves.
* Labels for plots can be derived from filenames or added in rendering code.

---

## Workflow

```bash
npm run dev        # develop
npm run build      # build
npx vercel --prod  # deploy
```
