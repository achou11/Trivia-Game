import unittest
import game


class FunctionsTest(unittest.TestCase):

    # tests for create_riddle_list function
    def test_riddle_list_not_empty(self):
        self.assertFalse(not game.create_riddle_list(), msg='riddle_list_create() returns empty list')

    def test_riddle_list_is_list(self):
        self.assertIs(type(game.create_riddle_list()), list, msg='riddle_list_create() does not return list object')


    # tests for choose_random_answers_to_display function
    def test_random_answers_list_is_list(self):
        riddle_list = game.create_riddle_list()
        riddle_displayed = {
            'id': 0,
            'question': 'What is the question?',
            'answer': 'This is the answer.'
        }

        self.assertIs(type(game.choose_random_answers_to_display(riddle_list, riddle_displayed)), list, msg='choose_random_answers_to_display does not return a list')

    def test_random_answer_length(self):
        riddle_list = game.create_riddle_list()
        riddle_displayed = {
                'id': 0,
                'question': 'What is the question?',
                'answer': 'This is the answer.'
        }

        self.assertEquals(len(game.choose_random_answers_to_display(riddle_list, riddle_displayed)), 4, msg='choose_random_answers_to_display not returning list of length 4')

    def test_actual_answer_in_random_answers_list(self):
        riddle_list = game.create_riddle_list()
        riddle_displayed = {
                'id': 0,
                'question': 'What is the question?',
                'answer': 'This is the answer.'
        }
        random_answers = game.choose_random_answers_to_display(riddle_list, riddle_displayed)

        self.assertIn(riddle_displayed['answer'], random_answers, msg='Actual answer not in random answers to be displayed')


    # tests for choose_random_riddle_to_display function
    def test_random_riddle_to_display(self):
        riddle_list = game.create_riddle_list()

        self.assertIs(type(game.choose_random_riddle_to_display(riddle_list)), dict, msg='Random riddle chosen is not of type dict')

    def test_random_riddle_displayed_has_required_keys(self):
        riddle_list = game.create_riddle_list()
        riddle_displayed = game.choose_random_riddle_to_display(riddle_list)
        required_keys = ['id', 'question', 'answer']

        self.assertEquals(required_keys, list(riddle_displayed.keys()), msg='Riddle selected to display does not contain all required keys')


if __name__ == "__main__":
    testSuite = unittest.TestLoader().loadTestsFromTestCase(FunctionsTest)
    unittest.TextTestRunner(verbosity=2).run(testSuite)
