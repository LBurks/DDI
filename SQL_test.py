import unittest
import sqlite3
import SQL

conn = sqlite3.connect('test.db')

class SQL_test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        c = conn.cursor()
        c.executescript("""
                create table websites (
                    WEBSITE_ID int,
                    Name text,
                    URL text
                );
                create table pages (
                    PAGE_ID int,
                    WEBSITE_ID int,
                    path text
                );
                create table vulnerabilities (
                    VULN_ID int,
                    PAGE_ID int,
                    data text
                );
            
            INSERT INTO websites VALUES 
            (1, 'foo', 'http://foo.com'), 
            (2, 'bar', 'http://foo.com');

            INSERT INTO pages VALUES 
            (1, 1, '/login.html'), 
            (2, 1, '/logout.html'), 
            (3, 1, '/admin.html'), 
            (4, 2, '/login.html'), 
            (5, 2, '/logout.html'), 
            (6, 2, '/admin.html');

            INSERT INTO vulnerabilities VALUES
            (1, 1, 'SQL injection response blah'),
            (2, 1, 'XXE response'),
            (3, 1, 'Stored XSS response'),
            (4, 2, 'Session hijack'),
            (5, 4, 'XXE response'),
            (6, 6, 'Default credentials resposne');
    """)
        
    def test(self):
        c = conn.cursor()
        output = [(1, 1, 'SQL injection response blah'), (2, 1, 'XXE response'), (3, 1, 'Stored XSS response')]
        self.assertEqual(SQL.run_sql(c), output)

    @classmethod
    def tearDownClass(cls):
        c = conn.cursor()
        c.executescript("""
                DROP TABLE websites;
                DROP TABLE pages;
                DROP TABLE vulnerabilities;
                """)

def main():
    unittest.main()

if __name__ == "__main__":
    main()

