from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
    )

    QDRANT_URL: str
    QDRANT_API_KEY: str
    GROQ_API_KEY: str
    JINA_API_KEY: str
    COLLECTION_NAME: str = "company_docs"
    CORS_ORIGIN: str
    GROQ_MODEL: str = "llama-3.3-70b-versatile"


settings = Settings()

ROLE_HIERARCHY: dict[str, list[str]] = {
    "ceo":      ["ceo"],
    "hr":       ["ceo", "hr"],
    "manager":  ["ceo", "hr", "manager"],
    "employee": ["ceo", "hr", "manager", "employee"],
}
ROLES: list[str] = list(ROLE_HIERARCHY.keys())

# Used by access_agent.py to determine "higher" role
ROLE_RANK: dict[str, int] = {"employee": 0, "manager": 1, "hr": 2, "ceo": 3}
