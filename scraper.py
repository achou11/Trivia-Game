from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, WebDriverException


def write_into_file(question, answer, file):
    q = question.replace('\n', ' ')
    a = answer.replace('\n', ' ')
    f.write(f'{q}&{a}\n')


driver = webdriver.Chrome()
url = 'https://www.riddles.com/archives'
driver.get(url)

page = 1
last_page = 100

with open('riddles.txt', 'w') as f:

    for i in range(page, last_page+1):

        print(f'***Page: {i}***\n')
        # Get list of riddle blocks for each page
        riddle_blocks = driver.find_elements_by_css_selector('div.panel-body.lead')


        for r_block in riddle_blocks:

            riddle_text = r_block.find_element_by_css_selector('blockquote.orange_dk_blockquote')

            show_answer_button = r_block.find_element_by_class_name('btn-riddle')

            driver.execute_script('return arguments[0].scrollIntoView();', show_answer_button)

            WebDriverWait(driver, 2).until(EC.presence_of_element_located((By.CLASS_NAME, 'dark_purple_blockquote')))

            show_answer_button.click()

            answer = r_block.find_element_by_class_name('dark_purple_blockquote')

            print("Question: ", riddle_text.text)
            print("\tAnswer: ", answer.text)
            print('\n\n')

            write_into_file(riddle_text.text, answer.text, f)


        if i != last_page:
            try:
                page_bar = driver.find_element_by_class_name('pagination')
                next_page = page_bar.find_elements_by_tag_name('li')[-1].find_element_by_tag_name('a')
                next_page.click()

            except (NoSuchElementException, WebDriverException):
                next_page_url = f'https://www.riddles.com/archives?page={i}'
                driver.get(next_page_url)

    driver.quit()
    print('Driver finished.')

print('riddles.txt closed.')

