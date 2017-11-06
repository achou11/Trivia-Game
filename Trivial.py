# Trivia Game
# Names:

import unittest


def correctAnswer(input, answer):
    return input == answer

def wrongAnswer(input, answer):
    return input == answer


class MyUnitTest(unittest.TestCase):
    def test_correct(self):
        answer = "Taco"
        input = "Taco"
        self.assertEqual(correctAnswer(input, answer), True)

    def test_wrong(self):
        answer = "Taco"
        input = "burrito"
        self.assertEqual(wrongAnswer(input, answer), False)



def main():
       # Begin unit testing
       suite = unittest.TestLoader().loadTestsFromTestCase(MyUnitTest)
       unittest.TextTestRunner(verbosity=2).run(suite)

       score = 0
       inFile = open("questionSet.txt", "r")
       ready = eval(input("I want to play a game... \nAre you ready(1/0): "))
       while ready != 1:
              ready = eval(input("Dude, are you ready(1/0): "))
       for line in inFile:
              line = str(line.rstrip())
              print(line)
              answer = inFile.readline()
              answer = str(answer.rstrip())
              userIn = str(input(""))
              
              if userIn == answer:
                     score = score + 1
                     print("You are damn right")
                     print("score: ", score, "\n")
                     
              else:
                     score = score - 1
                     print("WRONG!")
                     print("score: ", score, "\n")
              
       print("You just finished game... \nFinal score: ", score)

main()
