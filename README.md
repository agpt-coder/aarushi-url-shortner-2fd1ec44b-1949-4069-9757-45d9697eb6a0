---
date: 2024-04-16T09:57:25.526039
author: AutoGPT <info@agpt.co>
---

# aarushi-url-shortner-2

To implement a URL shortening service using the specified tech stack (Python, FastAPI, PostgreSQL, and Prisma ORM), the user needs to address several critical components. The service must accept a long URL as an input, generate a uniquely short alias for this URL, store the mapping between the alias and the original URL in a PostgreSQL database using Prisma ORM, and finally, return the shortened URL to the user. When this short URL is accessed, it should redirect the user to the original, long URL. Key considerations from the interview and research include ensuring the uniqueness of the short URL alias by utilizing a mixture of uppercase and lowercase letters, numbers, and possibly employing hash functions, while also avoiding ambiguous characters to prevent confusion. Additionally, the FastAPI framework will handle the redirection through the 'RedirectResponse' class, allowing for a seamless transition to the original URL when the short URL is accessed. Storing the URL mappings requires setting up a model in Prisma that includes at least the original URL and the generated short code, with enhanced functionality such as tracking capabilities as per the user's requirements. This project involves not just the development of a URL shortening functionality but also considerations for security, efficiency, and user experience.

## What you'll need to run this
* An unzipper (usually shipped with your OS)
* A text editor
* A terminal
* Docker
  > Docker is only needed to run a Postgres database. If you want to connect to your own
  > Postgres instance, you may not have to follow the steps below to the letter.


## How to run 'aarushi-url-shortner-2'

1. Unpack the ZIP file containing this package

2. Adjust the values in `.env` as you see fit.

3. Open a terminal in the folder containing this README and run the following commands:

    1. `poetry install` - install dependencies for the app

    2. `docker-compose up -d` - start the postgres database

    3. `prisma generate` - generate the database client for the app

    4. `prisma db push` - set up the database schema, creating the necessary tables etc.

4. Run `uvicorn project.server:app --reload` to start the app

## How to deploy on your own GCP account
1. Set up a GCP account
2. Create secrets: GCP_EMAIL (service account email), GCP_CREDENTIALS (service account key), GCP_PROJECT, GCP_APPLICATION (app name)
3. Ensure service account has following permissions: 
    Cloud Build Editor
    Cloud Build Service Account
    Cloud Run Developer
    Service Account User
    Service Usage Consumer
    Storage Object Viewer
4. Remove on: workflow, uncomment on: push (lines 2-6)
5. Push to master branch to trigger workflow
