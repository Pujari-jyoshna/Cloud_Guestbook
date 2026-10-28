# Cloud Guestbook

A beginner Python project: a Flask website runs on Render's cloud web service and saves guestbook messages in PostgreSQL. Locally, it uses SQLite. Render reads `render.yaml` to create the web service and database together.

## Files to upload to GitHub

Upload these five files from the project folder: `app.py`, `requirements.txt`, `render.yaml`, `.gitignore`, and `README.md`. Do not upload `.venv`, `.env`, or `guestbook.db`.

## Run it on your Windows laptop

1. Open this folder in VS Code (**File → Open Folder...**).
2. Open **Terminal → New Terminal**.
3. Create a virtual environment:

   ```powershell
   py -m venv .venv
   ```

4. Install the packages into it (activation is not required):

   ```powershell
   .\.venv\Scripts\python.exe -m pip install -r requirements.txt
   ```

5. Start the website:

   ```powershell
   .\.venv\Scripts\python.exe -m flask --app app run
   ```

6. In Chrome, open `http://127.0.0.1:5000`.

## Put it on GitHub

1. Sign in to GitHub in Chrome and create a repository named `cloud-guestbook`.
2. On the new repository page, choose **Add file → Upload files**.
3. Select the five files listed above from this folder. Commit with the message `Add cloud guestbook project`.

## Deploy it to Render

1. Create or sign in to a Render account and connect GitHub when Render asks.
2. In Render, choose **New → Blueprint**.
3. Select the `cloud-guestbook` GitHub repository and its `main` branch.
4. Render reads `render.yaml`. Review the resources: one web service and one PostgreSQL database. Choose **Apply** or **Deploy Blueprint** to create them.
5. Wait for both resources and the web service deployment to finish. Open the web service's `onrender.com` URL.
6. Post a guestbook message, refresh the page, and confirm it appears in the list.

## Important free-plan limits

Render's free web service can go idle and take about a minute to start again on the next visit. Render's free PostgreSQL database expires 30 days after creation; it is for learning and testing, and its data is not backed up. Do not store important or private information in this demo. Check the current Render dashboard and pricing before deploying; service availability or terms can change.

## What the cloud parts mean

- **Cloud compute:** Render runs `app.py` on a server reachable over the internet.
- **Cloud database:** Render PostgreSQL stores messages independently of the web server's temporary files.
- **Environment variable:** Render provides `DATABASE_URL` so the program can connect without putting database credentials in code.
- **GitHub deployment:** Render connects to the repository and can deploy future commits automatically.
