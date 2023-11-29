from typing import Optional

from sqlalchemy import create_engine
from sqlalchemy.engine import Engine, URL

from config import DBConfig


def create_db_engine(db_name: Optional[str] = None) -> Engine:
    """
    Factory method for the database engine. Creates an SQLAlchemy Engine from the
    database configuration

    Parameters
    ----------
    db_name : Optional[str], optional (default=None)

    Returns
    -------
    Engine
        The database engine
    """

    if not db_name:
        raise Exception("You must specify the 'db_name' param")

    connection_url = URL.create(
        drivername=DBConfig.driver_name,
        host=DBConfig.host,
        port=DBConfig.port,
        username=DBConfig.username,
        password=DBConfig.password,
        database=db_name,
    )

    return create_engine(connection_url, pool_pre_ping=True)
