def establish_connection():
    from psycopg2 import connect, DatabaseError

    try:
        connection = connect("postgres://alex:postgres@127.0.0.1/recipes")
        connection.autocommit = True
        return connection

    except DatabaseError:
        raise RuntimeError("Could not connect to databse")


def query(statement, vars=None):
    from psycopg2.extras import RealDictCursor as cursor_type

    with establish_connection() as conn:
        with conn.cursor(cursor_factory=cursor_type) as cursor:
            cursor.execute(statement, vars)
            print(cursor.query.decode("utf-8"))

            return cursor.fetchall()
