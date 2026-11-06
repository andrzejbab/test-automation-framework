from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

Base = declarative_base()

class DatabaseManager:
    def __init__(self, db_url: str):
        self.db_url = db_url
        self.engine = None
        self.SessionLocal = None

        """Initializes the database engine and session factory."""
        # pool_pre_ping=True automatically handles stale/dropped connections
        self.engine = create_engine(self.db_url, pool_pre_ping=True)
        self.SessionLocal = sessionmaker(
                autocommit=False, 
                autoflush=False, 
                bind=self.engine
        )
        print("Database connected successfully.")
            

    def close(self):
        """Disposes of the engine completely. Call ONLY when shutting down the app."""
        if self.engine is not None:
            self.engine.dispose()
            print("Database engine disposed.")


    def execute_query(self, command: str):
        """
        Executes a command safely by creating a fresh, temporary session,
        running the query, and ensuring it closes properly.
        """
        # Using a context manager ensures the session ALWAYS closes, 
        # even if an exception occurs.
        with self.SessionLocal() as session:
            try:
                result = session.execute(text(command)).scalar()
                session.commit() # Commit changes if it's an insert/update/delete
                return result
            except Exception as e:
                session.rollback() # Rollback if anything fails
                print(f"An error occurred during execution: {e}")
                raise



