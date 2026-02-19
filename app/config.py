from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    """Application settings with feature toggles.
    
    These settings mirror the demos-demo-library configuration.
    When the library is updated, these toggles should be updated to match.
    """
    
    # Server settings
    host: str = "0.0.0.0"
    port: int = 8000
    
    # Feature toggles - mirror demos-demo-library config
    math_addition_enabled: bool = True
    math_subtraction_enabled: bool = False
    math_division_enabled: bool = False
    
    # Library version tracking
    library_version: str = "1.3.0"
    
    class Config:
        env_file = ".env"
        env_prefix = "MATH_SERVICE_"


settings = Settings()
