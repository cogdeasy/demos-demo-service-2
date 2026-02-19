# Demos Math Service (Python)

A Python/FastAPI REST service that provides mathematical operations, mirroring the functionality of [demos-demo-service](https://github.com/cogdeasy/demos-demo-service) (Java).

## Overview

This service demonstrates a **multi-language microservices architecture** where both Java and Python services share the same feature toggles and configuration patterns. When the shared [demos-demo-library](https://github.com/cogdeasy/demos-demo-library) is updated, both services receive automated PRs from [Devin AI](https://devin.ai).

## API Endpoints

| Method | Endpoint | Description | Parameters |
|--------|----------|-------------|------------|
| GET | `/health` | Health check with feature status | - |
| POST | `/api/math/add` | Add two numbers | `a`, `b` (query params) |
| POST | `/api/math/subtract` | Subtract two numbers | `a`, `b` (query params) |

### Example Requests

```bash
# Health check
curl http://localhost:8000/health

# Addition
curl -X POST "http://localhost:8000/api/math/add?a=5&b=3"
# Returns: {"result": 8}

# Subtraction (if enabled)
curl -X POST "http://localhost:8000/api/math/subtract?a=10&b=4"
# Returns: {"result": 6}
```

## Quick Start

### Prerequisites

- Python 3.10+
- pip

### Installation

```bash
# Clone the repository
git clone https://github.com/cogdeasy/demos-demo-service-2.git
cd demos-demo-service-2

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment config
cp .env.example .env

# Run the service
python -m app.main
```

The service will start on `http://localhost:8000`.

### API Documentation

Once running, visit:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## Configuration

Configure via environment variables or `.env` file:

```bash
# Server settings
MATH_SERVICE_HOST=0.0.0.0
MATH_SERVICE_PORT=8000

# Feature toggles - mirror demos-demo-library config
MATH_SERVICE_MATH_ADDITION_ENABLED=true
MATH_SERVICE_MATH_SUBTRACTION_ENABLED=false

# Library version tracking
MATH_SERVICE_LIBRARY_VERSION=1.0.0
```

### Feature Toggles

| Variable | Default | Description |
|----------|---------|-------------|
| `MATH_SERVICE_MATH_ADDITION_ENABLED` | `true` | Enable/disable addition |
| `MATH_SERVICE_MATH_SUBTRACTION_ENABLED` | `false` | Enable/disable subtraction |

## Project Structure

```
demos-demo-service-2/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI application
│   ├── config.py            # Settings & feature toggles
│   └── math_operations.py   # Math logic
├── tests/
│   └── test_math.py         # Unit tests
├── requirements.txt
├── .env.example
└── README.md
```

## Automated Library Updates

This service is part of an automated update workflow:

```
┌─────────────────────┐
│ demos-demo-library  │  (Java library)
│ PR merged to main   │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│   GitHub Action     │
│   triggers Devin    │
└──────────┬──────────┘
           │
     ┌─────┴─────┐
     ▼           ▼
┌─────────┐ ┌─────────┐
│ Java    │ │ Python  │
│ Service │ │ Service │  ← You are here
│ PR      │ │ PR      │
└─────────┘ └─────────┘
```

When the library is updated:
1. [Devin AI](https://devin.ai) automatically creates a PR
2. The PR updates feature toggles in `app/config.py`
3. The PR updates `LIBRARY_VERSION` tracking
4. Review and merge to apply changes

### What Gets Updated

| Library Change | Python Service Update |
|----------------|----------------------|
| New version | `library_version` in config |
| New feature toggle | New setting in `Settings` class |
| New operation | New method in `math_operations.py` |

## Development

### Running Tests

```bash
pytest tests/ -v
```

### Code Style

```bash
# Install dev dependencies
pip install black flake8

# Format code
black app/ tests/

# Lint
flake8 app/ tests/
```

### Adding New Operations

1. Add the method to `app/math_operations.py`:
```python
@staticmethod
def multiply(a: int, b: int) -> int:
    if not settings.math_multiplication_enabled:
        raise RuntimeError("Multiplication is disabled")
    return a * b
```

2. Add the toggle to `app/config.py`:
```python
math_multiplication_enabled: bool = False
```

3. Add the endpoint to `app/main.py`:
```python
@app.post("/api/math/multiply")
def multiply(a: int = Query(...), b: int = Query(...)):
    result = math.multiply(a, b)
    return {"result": result}
```

## Related Repositories

| Repository | Language | Description |
|------------|----------|-------------|
| [demos-demo-library](https://github.com/cogdeasy/demos-demo-library) | Java | Shared math library |
| [demos-demo-service](https://github.com/cogdeasy/demos-demo-service) | Java | Java REST service |
| [demos-demo-service-2](https://github.com/cogdeasy/demos-demo-service-2) | Python | Python REST service (this repo) |

## License

MIT
