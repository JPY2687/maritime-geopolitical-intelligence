from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config.settings import get_settings


database_url = get_settings().database_url
engine = create_engine(
    database_url,
    connect_args={"check_same_thread": False} if database_url.startswith("sqlite") else {},
)
SessionLocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
