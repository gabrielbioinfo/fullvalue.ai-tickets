# Project Context: API (Backend)

## Project Overview

---

## Project Rules and Guidelines

### General Rules

1. **Language**: All code, comments, and documentation must be written in **English**.
2. **Code Quality**: Follow Python best practices, including PEP 8 standards. Must follow the ruff config rules inside the pyproject.toml
3. **Async first**: All the application should use async by default everytime we have some i/o.
4. **Inversion of controll**: Should use the Fastapi DI container to allow inversion of controll
5. **User case oriented**: The application should apply a clean arch approach having usecases as the application layer rules and the models should hold the business rules.
6. **Early returns**: Prefer early returns avoiding forking the app flow using else.
7. **Fastapi - Annotated**: Prefer to use Annotated to add metadata to our parameters.
8. **Testing**: Ensure all models are unit tested and usecases integrated tests. The covered should by done by tests using **pytest**.
9. **Version Control**: Commit changes with clear and descriptive messages.
10. **Dependencies**: Use **uv** for dependency management.

### Development Guidelines

1. **Frameworks**:
   - Use **FastAPI** for building APIs.
   - Use **LangChain** and **OpenAI** for text summarization.
2. **Linting and Formatting**:
   - Use **Ruff** for linting and formatting.
   - Ensure all code passes lint checks before committing.
3. **Environment**:
   - Secrets and API keys must be stored in `.env` files or a secrets manager.
4. **Container**:
   - Ensure the application is containerized and can be run using Docker.

### API Design

1. **Endpoints**:
   - Healthcheck: `GET /healthz`
2. **Response Standards**:
   - Use JSON for all responses.
   - For streaming, use `text/event-stream`.
3. **Error Handling**:
   - Return appropriate HTTP status codes.
   - Include meaningful error messages in responses.

### Security

1. **Authentication**:
   - Support JWT-based authentication.
2. **Authentication Middleware**:
   - Should evaluate the authentication with Fastapi.
3. **Cors Middleware**:
   - Only allows the frontend application to call the API.
4. **Secrets Management**:
   - Use `.env` files or AWS Secrets Manager for sensitive data.
5. **Data Privacy**:
   - Ensure no sensitive data is logged.

### Scalability

1. **Containerization**:
   - Use Docker for consistent deployments.
2. **Auto-scaling**:
   - Design the backend to scale based on CPU/memory/requests.
3. **Monitoring**:
   - Implement observability tools (e.g., OpenTelemetry).

---