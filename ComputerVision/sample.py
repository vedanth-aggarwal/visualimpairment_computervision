from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def create_google_form(questions):
    # Open Chrome browser
    driver = webdriver.Chrome()
    driver.maximize_window()

    # Go to Google Forms
    driver.get("https://docs.google.com/forms")

    # Click on the blank form button
    time.sleep(3)  # Wait for the page to load
    blank_form_button = driver.find_element_by_xpath("//div[contains(text(),'Blank')]")
    blank_form_button.click()

    # Loop through each question in the dictionary and add it to the form
    for question_number, question_data in questions.items():
        # Click on the add question button
        time.sleep(2)  # Wait for the button to be clickable
        add_question_button = driver.find_element_by_xpath("//div[contains(text(),'Add question')]")
        add_question_button.click()

        # Enter question text
        question_input = driver.find_element_by_xpath("//textarea[@aria-label='Question']")
        question_input.send_keys(f"{question_number}. {question_data['question']}")
        question_input.send_keys(Keys.ENTER)  # Move to next line

        # Enter options
        for option in question_data['options']:
            option_input = driver.switch_to.active_element
            option_input.send_keys(option)
            option_input.send_keys(Keys.ENTER)  # Move to next line

        # Choose correct option
        correct_option_input = driver.switch_to.active_element
        correct_option_input.send_keys(Keys.TAB)
        correct_option_input.send_keys(Keys.ENTER)

    # Save the form
    time.sleep(2)  # Wait for the save button to be clickable
    save_button = driver.find_element_by_xpath("//div[contains(text(),'Save')]")
    save_button.click()

    # Close the browser
    time.sleep(2)
    driver.quit()

# Example dictionary of MCQs
mcqs = {
    1: {
        'question': 'What is the capital of France?',
        'options': ['Paris', 'London', 'Berlin', 'Rome'],
        'correct_option': 'Paris'
    },
    2: {
        'question': 'Which planet is known as the Red Planet?',
        'options': ['Mars', 'Venus', 'Jupiter', 'Saturn'],
        'correct_option': 'Mars'
    }
}

# Create Google Form
create_google_form(mcqs)
