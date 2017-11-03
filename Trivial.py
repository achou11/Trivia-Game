
def main():
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
