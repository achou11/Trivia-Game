import unittest
import game


class FunctionsTest(unittest.TestCase):

    # create_riddle_list
    def test_riddle_list_not_empty(self):
        self.assertFalse(not game.create_riddle_list(), msg='riddle_list_create() returns empty list')

    def test_riddle_list_is_list(self):
        self.assertIs(type(game.create_riddle_list()), list, msg='riddle_list_create() does not return list object')


    # choose_random_answers_to_display
    def test_random_answers_list_is_list(self):
        riddle_list = game.create_riddle_list()
        riddle_displayed = {
            'id': 0,
            'question': 'What is the question?',
            'answer': 'This is the answer.'
        }

        self.assertIs(type(game.choose_random_answers_to_display(riddle_list, riddle_displayed)), list, msg='choose_random_answers_to_display does not return a list')


    # choose_random_riddle_to_display
    def test_random_riddle_to_display(self):
        riddle_list = game.create_riddle_list()

        self.assertIs(type(game.choose_random_riddle_to_display(riddle_list)), dict, msg='Random riddle chosen is not of type dict')


if __name__ == "__main__":
    suite = unittest.TestLoader().loadTestsFromTestCase(FunctionsTest)
    unittest.TextTestRunner(verbosity=2).run(suite)