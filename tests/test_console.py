#!/usr/bin/python3
"""Console unittest module"""


import unittest
import MySQLdb
from models.user import User
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class TestConsole(unittest.TestCase):
    """Test cases for the console"""

    def setUp(self):
        """Setup for the tests"""
        self.db = MySQLdb.connect(host="localhost", user="root", passwd="root",
                                  db="your_test_db")
        self.cur = self.db.cursor()
        self.cur.execute("SELECT COUNT(*) FROM users")
        self.initial_count = self.cur.fetchone()[0]

    def tearDown(self):
        """Teardown for the tests"""
        self.cur.close()
        self.db.close()

    def test_create_user(self):
        """Test creating a user through the console"""
        console = HBNBCommand()
        with patch('sys.stdout', new=StringIO()) as f:
            console.onecmd(
                'create User email="test@test.com" password="test" \
                first_name="Test" last_name="User"'
                )
        self.cur.execute("SELECT COUNT(*) FROM users")
        new_count = self.cur.fetchone()[0]
        self.assertEqual(new_count, self.initial_count + 1)


if __name__ == '__main__':
    unittest.main()
