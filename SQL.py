import sqlite3

# c - a SQLite connection to a database.
def run_sql(c):
    c.execute("SELECT * FROM vulnerabilities WHERE PAGE_ID = (SELECT PAGE_ID FROM pages WHERE WEBSITE_ID = (SELECT WEBSITE_ID FROM websites WHERE URL = 'http://foo.com') AND path='/login.html');")
    return c.fetchall()

