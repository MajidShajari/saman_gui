# Third Library
from pydantic_settings import BaseSettings, SettingsConfigDict


class GuiSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    LDAP_SERVER: str = ""
    DOMAIN: str = ""


settings = GuiSettings()
