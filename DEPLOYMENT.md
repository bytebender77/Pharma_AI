# Deployment Guide

## 1. GitHub (Source Code)
1.  Initialize a git repository if you haven't already:
    ```bash
    git init
    git add .
    git commit -m "Initial commit"
    ```
2.  Create a new repository on GitHub.
3.  Push your code:
    ```bash
    git remote add origin <your-github-repo-url>
    git branch -M main
    git push -u origin main
    ```

## 2. Render (Backend)
1.  Go to [Render Dashboard](https://dashboard.render.com/).
2.  Click **New +** -> **Web Service**.
3.  Connect your GitHub repository.
4.  Configure the service:
    *   **Name:** `medcore-backend` (or similar)
    *   **Runtime:** Python 3
    *   **Build Command:** `pip install -r requirements.txt`
    *   **Start Command:** `uvicorn app.main:app --host 0.0.0.0 --port 10000`
5.  **Environment Variables:**
    *   Add `OPENAI_API_KEY` with your actual key.
6.  Click **Create Web Service**.
7.  Copy the **Service URL** (e.g., `https://medcore-backend.onrender.com`). You will need this for the frontend.

## 3. Vercel (Frontend)
1.  Go to [Vercel Dashboard](https://vercel.com/dashboard).
2.  Click **Add New...** -> **Project**.
3.  Import your GitHub repository.
4.  Configure the project:
    *   **Framework Preset:** Vite
    *   **Root Directory:** `frontend` (Important! Click "Edit" next to Root Directory and select the `frontend` folder).
5.  **Environment Variables:**
    *   Key: `VITE_API_URL`
    *   Value: The Render Backend URL you copied earlier (e.g., `https://medcore-backend.onrender.com`). **Do not add a trailing slash.**
6.  Click **Deploy**.

## Verification
Once deployed, open your Vercel URL. The app should load, and when you run a query, it should connect to your Render backend (which connects to OpenAI) and display the results.
