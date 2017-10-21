import unittest
from pyswip.prolog import Prolog
from testDjikstraProlog import loadDatabase


class Error(Exception):
    pass


class ConsultError(Error):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return self.value


class TestLoadDatabase(unittest.TestCase):
    def setUp(self):
        print("# set up test load Database")

    def test_load_database(self):
        try:
            prolog = Prolog()
            loadDatabase(prolog)

        except:
            print("ERROR: cannot load database")

        finally:
            # do something after show msg
            pass

if __name__ == '__main__':
    unittest.main()
