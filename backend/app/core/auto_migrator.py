from sqlalchemy import inspect, text
from app.core.database import engine, Base
from fastapi import FastAPI

def run_auto_migrations():
    with engine.begin() as conn:
        inspector = inspect(conn)
        for table_name, table in Base.metadata.tables.items():
            if not inspector.has_table(table_name):
                table.create(bind=conn)
                continue

            existing_columns = {col["name"] for col in inspector.get_columns(table_name)}
            model_columns = {col.name: col for col in table.columns}

            for col_name, col in model_columns.items():
                if col_name not in existing_columns:
                    col_type = col.type.compile(engine.dialect)
                    nullable = "NULL" if col.nullable else "NOT NULL"
                    default = ""
                    if col.default is not None and getattr(col.default, "arg", None) is not None:
                        default = f" DEFAULT '{col.default.arg}'"
                    sql = f'ALTER TABLE "{table_name}" ADD COLUMN "{col_name}" {col_type} {nullable}{default};'
                    conn.execute(text(sql))
                    existing_columns.add(col_name)

def init_auto_migrator(app: FastAPI):
    @app.on_event("startup")
    def startup_event():
        run_auto_migrations()
