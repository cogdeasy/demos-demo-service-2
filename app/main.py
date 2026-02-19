"""Demos Math Service - Python/FastAPI implementation.

This service mirrors the functionality of demos-demo-service (Java)
and uses the same feature toggles as demos-demo-library.
"""

from fastapi import FastAPI, HTTPException, Query
from app.config import settings
from app.math_operations import MathOperations

app = FastAPI(
    title="Demos Math Service",
    description="Python REST service for mathematical operations",
    version="1.0.0",
)

math = MathOperations()


@app.get("/health")
def health_check():
    """Health check endpoint."""
    return {
        "status": "healthy",
        "library_version": settings.library_version,
        "features": {
            "addition": settings.math_addition_enabled,
            "subtraction": settings.math_subtraction_enabled,
            "division": settings.math_division_enabled,
        }
    }


@app.post("/api/math/add")
def add(a: int = Query(...), b: int = Query(...)):
    """Add two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Sum of a and b
    """
    try:
        result = math.add(a, b)
        return {"result": result}
    except RuntimeError as e:
        raise HTTPException(status_code=403, detail=str(e))


@app.post("/api/math/subtract")
def subtract(a: int = Query(...), b: int = Query(...)):
    """Subtract two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Difference of a and b
    """
    try:
        result = math.subtract(a, b)
        return {"result": result}
    except RuntimeError as e:
        raise HTTPException(status_code=403, detail=str(e))


@app.post("/api/math/divide")
def divide(a: int = Query(...), b: int = Query(...)):
    """Divide two numbers.
    
    Args:
        a: First number
        b: Second number
        
    Returns:
        Quotient of a and b as a float
    """
    try:
        result = math.divide(a, b)
        return {"result": result}
    except RuntimeError as e:
        raise HTTPException(status_code=403, detail=str(e))
    except ArithmeticError:
        raise HTTPException(status_code=400, detail="Division by zero")


if __name__== "__main__":
    import uvicorn
    uvicorn.run(app, host=settings.host, port=settings.port)
