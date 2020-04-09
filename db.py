import os
import sqlite3

BEAR_DB_PATH = os.path.expanduser(
    "~/Library/Group Containers/9K33E3U3T4.net.shinyfrog.bear/Application Data/database.sqlite"
)


def db_connect(db_path=BEAR_DB_PATH):
    con = sqlite3.connect(db_path)
    return con
