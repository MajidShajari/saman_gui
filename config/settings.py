# Third Library
from pydantic import BaseModel
from pydantic_settings import BaseSettings, SettingsConfigDict


class GuiSettings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")
    LDAP_SERVER = "192.168.20.11"
    DOMAIN = "RAFA-GROUP.com"


settings = GuiSettings()
