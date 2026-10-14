# My First DevOps Project

This project is a beginner-friendly Flask application created to learn the basics of DevOps workflows such as:

- building a simple Python web app
- writing tests
- containerizing with Docker
- documenting how to run and verify the project

## Project goal

The application exposes two endpoints:

- `GET /` returns: `Hello from my first DevOps project!`
- `GET /health` returns a JSON payload with the status `healthy`

## Files in this project

- `app.py` - the Flask web application with the routes.
- `requirements.txt` - Python package dependencies.
- `tests/test_app.py` - pytest tests for both endpoints.
- `Dockerfile` - instructions to run the app in a container.
- `.gitignore` - ignores Python and editor-generated files.
- `README.md` - explains the project and setup steps.

## Local setup

1. Create a virtual environment:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the application:
   ```bash
   python app.py
   ```
4. Open the app in a browser at:
   ```text
   http://localhost:5000/
   ```

## Endpoint examples

- `GET http://localhost:5000/` should return:
  ```text
  Hello from my first DevOps project!
  ```
- `GET http://localhost:5000/health` should return:
  ```json
  {"status": "healthy"}
  ```

## Run tests

Use pytest to validate the application behavior:

```bash
pytest
```

## Build a Docker image

From the project folder, build the image with:

```bash
docker build -t my-first-devops-project .
```

Then run the container:

```bash
docker run -p 5000:5000 my-first-devops-project
```

## Basic security notes

- The Docker image runs as a non-root user.
- Environment variables are kept simple and not exposed in source code.
- The app does not include secrets or credentials.

## Learning next steps

As you continue learning DevOps, the next topics to explore are:

- Git and GitHub workflow
- CI/CD pipelines
- environment variables and configuration management
- monitoring and health checks
- deployment to a hosting platform

This project is intentionally simple so it is easier to understand how a basic web app moves from code to container to deployment.
