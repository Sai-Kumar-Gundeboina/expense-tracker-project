from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base


# DATABASE_URL = "sqlite:////../database-test/expenses.db"
DATABASE_URL = "sqlite:///../database/expenses.db"
# engine connect python <==> database
engine = create_engine(
    DATABASE_URL,
    connect_args = {"check_same_thread": False}
)

SessionLocal = sessionmaker(
    autocommit = False,
    autoflush = False,
    bind = engine
)

Base = declarative_base()