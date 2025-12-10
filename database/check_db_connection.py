from database.session import engine

async def check_db_connection():
    try:
        async with engine.connect() as conn:
            from sqlalchemy import text
            await conn.execute(statement=text("SELECT 1"))
        print("database connection is success")
    except Exception as e:
        print("database connection is failed")
        raise e