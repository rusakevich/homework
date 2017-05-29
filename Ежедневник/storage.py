import sqlite3

def connect(db_name=None):
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)

    return conn


def initialize(conn):
    with conn:
        script_file_path = Path.join(Path.dirname(__file__), 'schema.sql')

        with open(script_file_path) as f:
            conn.executescript(f.read())

