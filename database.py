import sqlite3

bd = sqlite3.connect("2048.sqlite")

cur = bd.cursor()


cur.close()