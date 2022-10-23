import sqlite3 as sq

settings = {'currency': None}


def sql_request_settings(key):
    with sq.connect('settings.db') as con:
        cur = con.cursor()
        cur.execute(f"SELECT v FROM sett WHERE k == '{key}'")
        res = cur.fetchall()[0]
        return res
