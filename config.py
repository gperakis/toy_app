from pydantic import BaseSettings, Field


class DBSettings(BaseSettings):
    driver_name: str = Field(default="mysql+pymysql", env="DB_DRIVER")
    host: str = Field(env="MYSQL_HOST")
    port: int = Field(default=3306, env="MYSQL_PORT")
    username: str = Field(env="MYSQL_USER")
    password: str = Field(env="MYSQL_PASSWORD")

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


DBConfig = DBSettings()
