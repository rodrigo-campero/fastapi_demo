# My FastAPI Project

This is a FastAPI project for building a web API with a structured folder organization.

## Project Structure

- `app/`: Main application package.

  - `main.py`: FastAPI application instance and main routes.
  - `api/`: API route definitions.
    - `endpoints/`: Specific API endpoints.
      - `file.py`: Example API endpoint for file upload.
    - `models/`: Pydantic models for request and response objects.
      - `file.py`: Pydantic model for file upload.
  - `core/`: Core functionalities and configurations.
    - `config.py`: Configuration settings.
    - `security.py`: Security-related functions.

- `tests/`: Test directory.

  - `test_main.py`: Tests for the main FastAPI application.
  - `test_api/`: Tests for API endpoints.
    - `test_file.py`: Tests for file upload endpoint.

- `requirements.txt`: Project dependencies.
- `main.py`: Entry point for running the FastAPI application.
- `.env`: Environment variables (optional).
- `README.md`: Project documentation.

## Running the Application

1. Install project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

2. Run the FastAPI application:

   ```bash
   uvicorn main:app --reload
   ```

3. Access the Swagger documentation at [http://127.0.0.1:8080/docs](http://127.0.0.1:8080/docs) or ReDoc at [http://127.0.0.1:8080/redoc](http://127.0.0.1:8080/redoc) to interact with the API.

## Testing

Run tests using:

```bash
pytest
```

## Libs

```bash
fastapi
"uvicorn[standard]"
sqlalchemy
pydantic-settings
passlib
```
