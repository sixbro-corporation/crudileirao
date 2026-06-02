import os
import asyncpg

DATABASE_URL = os.getenv("DATABASE_URL")
pool: asyncpg.Pool = None

async def init_db():
    global pool
    pool = await asyncpg.create_pool(DATABASE_URL)

async def close_pool():
    global pool
    if pool:
        await pool.close()
        pool = None


async def get_db_connection():
    if pool is None:
        raise RuntimeError("O pool de conexões não foi inicializado. Execute `init_db()` primeiro.")

    conn = await pool.acquire()
    try:
        yield conn
    finally:
        await pool.release(conn)