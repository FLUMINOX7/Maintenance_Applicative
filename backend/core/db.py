

class DbWrapper():
    pass
from contextlib import contextmanager

import psycopg_pool
import psycopg


class DbWrapper():
    def __init__(self):
        self.pool = psycopg_pool.ConnectionPool(
            f"host=localhost port=5432 dbname=todolistdb user=todolist"
        )
        
    def _execute_one(self, query: str, args: tuple = ()):
        with self.pool.connection() as conn:
            conn.row_factory = psycopg.rows.dict_row
            with conn.cursor() as cur:
                cur.execute(query, args)
                
                return cur.fetchone()
            
    def _execute_many(self, query: str, args: tuple = ()):
        with self.pool.connection() as conn:
            conn.row_factory = psycopg.rows.dict_row
            with conn.cursor() as cur:
                cur.execute(query, args)
                
                return cur.fetchall()

    @contextmanager
    def _transaction(self):
        with self.pool.connection() as conn:
            conn.row_factory = psycopg.rows.dict_ro
            with conn.cursor() as cur:
                yield cur
    
    
wrapper: DbWrapper | None = None


def init_db():
    global wrapper
    
    try:
        wrapper = DbWrapper()
    except Exception as e:
        exit(1) # TODO logging

import psycopg


class DbWrapper():
    def __init__(self):
        self.pool = psycopg_pool.ConnectionPool(
            f"host=localhost port=5432 dbname=todolistdb user=todolist"
        )
        
    def _execute_one(self, query: str, args: tuple = ()):
        with self.pool.connection() as conn:
            conn.row_factory = psycopg.rows.dict_row
            with conn.cursor() as cur:
                cur.execute(query, args)
                
                return cur.fetchone()
            
    def _execute_many(self, query: str, args: tuple = ()):
        with self.pool.connection() as conn:
            conn.row_factory = psycopg.rows.dict_row
            with conn.cursor() as cur:
                cur.execute(query, args)
                
                return cur.fetchall()

    @contextmanager
    def _transaction(self):
        with self.pool.connection() as conn:
            conn.row_factory = psycopg.rows.dict_ro
            with conn.cursor() as cur:
                yield cur
    
    
wrapper: DbWrapper | None = None


def init_db():
    global wrapper
    
    try:
        wrapper = DbWrapper()
    except Exception as e:
        exit(1) # TODO logging
