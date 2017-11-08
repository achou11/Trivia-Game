import unittest
import game


class FunctionsTest(unittest.TestCase):
    def test_riddle_list_is_list(self):
        self.assertIs(type(game.create_riddle_list()), list, msg="riddle_list_create does not return list object")


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(FunctionsTest)
    unittest.TextTestRunner(verbosity=2).run(suite)