import unittest
from src.skate import *
from src.swen344_db_utils import connect

class TestChat(unittest.TestCase):

    def test_rebuild_tables(self):
        rebuildTables()
        result = exec_get_all('SELECT * FROM example_table')
        self.assertEqual([], result, "no rows in example_table")

    def test_rebuild_tables_is_idempotent(self):
        rebuildTables()
        rebuildTables()
        result = exec_get_all('SELECT * FROM example_table')
        self.assertEqual([], result, "no rows in example_table")