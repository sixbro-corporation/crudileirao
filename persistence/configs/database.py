import os
import asyncpg

DATABASE_URL = os.getenv("DATABASE_URL")

pool: asyncpg.Pool = None

async def get_pool() -> asyncpg.Pool:
    return pool

async def init_db():
    global pool
    pool = await asyncpg.create_pool(DATABASE_URL)

async def close_pool():
    global pool
    if pool:
        await pool.close()
