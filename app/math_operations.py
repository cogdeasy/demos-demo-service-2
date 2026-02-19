"""Math operations module.

This module mirrors the functionality of demos-demo-library.
Operations are gated by feature toggles defined in config.
"""

from app.config import settings


class MathOperations:
    """Math operations with feature toggle support."""
    
    @staticmethod
    def add(a: int, b: int) -> int:
        """Add two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Sum of a and b
            
        Raises:
            RuntimeError: If addition is disabled
        """
        if not settings.math_addition_enabled:
            raise RuntimeError("Addition is disabled")
        return a + b
    
    @staticmethod
    def subtract(a: int, b: int) -> int:
        """Subtract two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Difference of a and b
            
        Raises:
            RuntimeError: If subtraction is disabled
        """
        if not settings.math_subtraction_enabled:
            raise RuntimeError("Subtraction is disabled")
        return a - b

    @staticmethod
    def divide(a: int, b: int) -> float:
        """Divide two numbers.
        
        Args:
            a: First number
            b: Second number
            
        Returns:
            Quotient of a and b as a float
            
        Raises:
            RuntimeError: If division is disabled
            ArithmeticError: If dividing by zero
        """
        if not settings.math_division_enabled:
            raise RuntimeError("Division is disabled")
        if b == 0:
            raise ArithmeticError("Division by zero")
        return a / b
