import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

database_url = os.environ.get("postgresql://vitepostgresql_user:gKS2S5YyLABhftvQGmpeCMUBg7fPdCfW@dpg-cvvrdaa4d50c739lu7fg-a/vitepostgresql")

if not database_url:
    raise ValueError("DATABASE_URL environment variable not set")

engine = create_engine(database_url, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
