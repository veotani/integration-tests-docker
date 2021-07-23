import psycopg2


def get_conn(user, password, host, port, dbname):
    return psycopg2.connect(dsn=f"user={user} password={password} dbname={dbname} host={host} port={port}")


def get_cur(conn):
    return conn.cursor()


def prepare_db(cur):
    cur.execute("CREATE TABLE IF NOT EXISTS test (some_number integer)")


def insert_test_data(cur):
    cur.execute("INSERT INTO test (some_number) VALUES (1)")


def get_last_number(cur):
    cur.execute("SELECT some_number FROM test")
    res = cur.fetchone()
    if len(res) > 0:
        return res[-1]
    else:
        raise Exception('there are no values in the db')

def test_db_integration():
    user, password = "postgres", "example"
    host, port = "python-integration-test_postgresql_1", "5432"
    dbname = user
    with get_conn(user, password, host, port, dbname) as conn:
        with get_cur(conn) as cur:
            prepare_db(cur)
            insert_test_data(cur) 
            assert get_last_number(cur) == 1
