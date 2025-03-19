# Flight Price Prediction using Flask/Render - A Machine Learning Project

## Overview

This repository focuses on deploying a basic machine learning model of Flight Price Prediction using Flask. It includes interpreting learning curves, evaluating and selecting models, creating a web application with Flask, and deploying the app using Render.

# Project Flow Details :
1. **Model Training:**
    - **Gather and Split data**
    - **Data pre-processing**
    - **Model selection (Learning Curves)**
    - **Model training**
    - **Model persistence**

---

2. **Create Input form**

---

3. **Create the Web Application**
    - **Flask**: We built a web application using the Flask framework.
    - **WTForms**: We integrated WTForms for handling web forms and input validation.
    - **HTML Templates**: We utilized HTML templates with Jinja2 for dynamic content rendering.
    - **Template Inheritance**: We applied template inheritance to create reusable and maintainable templates.

---

4. **Create HTML templates**

---

5. **Testing on Local Server**

---

6. **GitHub set-up and pushing changes to Remote Repository**
    ### 📄 Basic Git Commands to Push Files to GitHub
- **Initialize a Git repository (if not already initialized) (first time only):**
   ```bash
   git init
   ```
- **Check the status of files (see changes, untracked files, etc.):**
   ```bash
   git status
   ```
- **Add files to the staging area (to prepare them for commit):**
   - To add a specific file:
     ```bash
     git add filename
     ```
   - To add all files (Stage all files):
     ```bash
     git add .
     ```
- **Commit the staged files with a meaningful message:**
   ```bash
   git commit -m "Your commit message here"
   ```
- **Connect/Add the remote repository URL (only once per project):**
   ```bash
   git remote add origin https://github.com/username/repo-name.git
   ```
- **Push files to GitHub:**
   - First push (set upstream branch) to GitHub:
     ```bash
     git push -u origin main
     ```
     *(or `master`, depending on your default branch name)*
   - Subsequent pushes:
     ```bash
     git push
     ```
- **Check current remote URL(s):**
   ```bash
   git remote -v
   ```
- **Pull latest changes from GitHub (important if working with others):**
   ```bash
   git pull origin main
   ```
- **See commit history:**
   ```bash
   git log
   ```
- **Change branch name (if needed, e.g., from master to main) (optional):**
    ```bash
    git branch -M main
    ```

--- 

7. **🚀 API Serving and Deploy Application using Render (💰 Free Plan)**
    This guide walks you through creating a Render account using GitHub, selecting the Free Plan, and deploying your AI/ML model website hosted on GitHub. **Model Serving**: The trained machine learning model was served as an API using Flask.
    ### 🌐 Create a Render Account via GitHub
    - Go to [Render's Website](https://render.com/).
    - Select **Sign up with GitHub**.
    - Authorize **Render** to access your GitHub account and complete any additional steps (like confirming email if required).
    - Choose Free Plan: that Free Static Site Hosting, Web Services (750 hours/month) and PostgreSQL database (up to 1 GB).
    - Prepare Your GitHub Repository has all necessary files (HTML, Python/Flask/Django, model files, etc.) and a `requirements.txt` file listing dependencieslike (flask, scikit-learn, numpy, pandas, etc.)
    ### 🚀 Deploy GitHub AI/ML Website on Render
    - On Render Dashboard, click **New + → Web Service**.
    - Under **Connect a repository**, select **GitHub**.
    - Authorize Render to access your GitHub repositories (if not already authorized).
    - Select the repository containing your AI/ML model website.
    ### 🛠️ Configure Deployment:
    - **Name**: Set a name for your service.
    - **Branch**: Choose `master` or your desired branch.
    - **Runtime**: Select **Python 3**.
    - **Start Command**:
        ```bash
        gunicorn app:app
        ```
        _(Modify if needed, e.g., `main:app` for `main.py` files)_
        _Environment file `.env` (if needed)_
    - Under **Instance Type**, select **Free Instance**.
    - Go to **Environment** section and add any variables (like API keys, model paths, etc.) (if required).
    - Click on **Create Web Service**. Render will build and deploy your app. Once complete, you’ll receive a [**public URL**](https://flight-price-prediction-oo4w.onrender.com) to access your website!
    ### 🔄 Auto-Deploy on GitHub Changes
    Render automatically redeploys when you push new commits to the connected branch and update any files (model, code, HTML, CSS).

---

# ✅ Done! Your AI/ML model website is now live. 🎉