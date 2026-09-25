# Deploying to Render.com

This is a small Flask app, so use Render's **Web Service** type (not Static Site).

## 1. Push to GitHub
Add these files to your `CS_1_CaesarCipher_byte` repo (or wherever your Task 1 repo lives):
```
app.py
requirements.txt
Procfile
templates/index.html
static/style.css
static/app.js
```
Then:
```bash
git add .
git commit -m "feat: added Flask web app for Caesar Cipher"
git push origin main
```

## 2. Create the service on Render
1. Go to [render.com](https://render.com) → **New +** → **Web Service**.
2. Connect your GitHub account and select this repository.
3. Fill in:
   - **Name:** `caesar-cipher-byte` (or anything)
   - **Runtime:** Python 3
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app`
4. Click **Create Web Service**.

Render reads the `Procfile` automatically, so the Start Command above is a backup — either works.

## 3. Done
In about a minute you'll get a live URL like:
`https://caesar-cipher-byte.onrender.com`

That's the link to put in your README and your LinkedIn post per the AVIP SOPs.

## Notes
- Free-tier Render services spin down after inactivity, so the first request after
  a while may take ~30–50 seconds to wake up. That's normal, not a bug.
- `/healthz` returns `ok` — useful if you ever add uptime monitoring.
