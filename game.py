import os
import random


# function to create list of riddles from riddles.txt
def create_riddle_list():
    riddle_list = []
    with open('./riddles.txt', 'r') as f:
        for id, line in enumerate(f):
            pair = line.split('&')
            question, answer = pair[0], pair[-1].replace('\n', '')
            riddle_list.append({
                'id': id,
                'question': question,
                'answer': answer,
                })
    return riddle_list


# function to choose which random answers to display with the actual answer
def choose_random_answers_to_display(riddle_list, riddle_displayed):
    index_list = [random.randint(0, len(riddle_list)-1) for _ in range(3)]
    answer_list = [riddle_list[i]['answer'] for i in index_list]
    answer_list.append(riddle_displayed['answer'])
    random.shuffle(answer_list)
    return answer_list


# function to randomly choose which riddle to use for each iteration
def choose_random_riddle_to_display(riddle_list):
    return riddle_list[random.randint(0, len(riddle_list)-1)]


# function to clear screen
def clear_screen(os_name):
    if os_name == 'posix':
        os.system('clear')
    else:
        os.system('cls')


def main():
    OS_NAME = os.name
    riddle_list = create_riddle_list()
    play = True

    # begin playing loop
    while play:
        clear_screen(OS_NAME)

        # initialize score
        score = 0
        print('\nWelcome to The Incoherent Trivia Game!\n\nYou\'ll be presented with a riddle and four answers to the riddle. Only one of the answers is correct.\nThe screen will clear when presenting the next question (there are 10 total), but you can view past questions just by scrolling up.\nIf at any point you want to quit, just type \'quit\'\n')

        # ask if user wants to play
        ask_to_play = input('Ready to play? (y/n) ==> ').lower()
        while ask_to_play not in ['y', 'n']:
            print('Please enter y or n\n')
            ask_to_play = input('Ready to play? (y/n) ==> ').lower()

        if ask_to_play == 'n':
            print('Ok nevermind. Bye.\n')
            break

        clear_screen(OS_NAME)

        # start game
        for i in range(1, 11):

            riddle_pair = choose_random_riddle_to_display(riddle_list)
            question = riddle_pair['question']
            actual_answer = riddle_pair['answer']
            answer_choices = choose_random_answers_to_display(riddle_list, riddle_pair)

            print(f'\nQuestions left: {11 - i}\n')
            print(f'Current score: {score}\n\n')
            print(f'Question {i}:\n\n{question}\n')
            print('Here are the choices:\n')

            number_answer_dict = {}
            for i, choice in enumerate(answer_choices, 1):
                number_answer_dict[i] = choice
                print(f'{i}: {choice}\n')

            user_guess = input('What\'s your guess? (1, 2, 3, or 4) ==> ')

            if user_guess == 'quit':
                play = False
                break

            else:
                while user_guess not in ('1', '2', '3', '4'):
                    print('Please enter 1, 2, 3, or 4\n')
                    user_guess = input('What\'s your guess? (1, 2, 3, or 4) ==> ')

                if number_answer_dict[int(user_guess)] != actual_answer:
                    print(f'\nWrong answer!\nThe correct answer is: {actual_answer}\n')
                else:
                    score += 1
                    print('\nNice job! +1 for your score\n')

            input('\nPress any key to continue...')

            clear_screen(OS_NAME)

        if play == False:
            print('Quitting...')
            continue
        else:
            print(f'Congrats on making it to the end! Your final score was {score}\n')
            play_again = input('Play again? (y/n) ==> ').lower()
            while play_again not in ['y', 'n']:
                play_again = input('Play again? (y/n) ==> ').lower()

        if play_again == 'y':
            continue
        else:
            play = False
            print('Ok thanks for playing!')
            break

main()
