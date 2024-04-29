from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    PROJ_DIR: Path = Path(__file__).parent
    DATA_DIR: Path = PROJ_DIR / "data"
    SRC_DIR: Path = PROJ_DIR / "src"
    NB_DIR: Path = PROJ_DIR / "nb"
    ASSET_DIR: Path = PROJ_DIR / "asset"
    IMG_DIR: Path = ASSET_DIR / "img"


settings = Settings()
