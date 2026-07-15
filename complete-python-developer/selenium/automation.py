from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# service = Service(executable_path=r'C:\Users\echavez\Desktop\Github\selenium\chromedriver.exe') # path to chromedriver executable
options = Options()
options.add_experimental_option("detach", True) # keeps chrome open
options.add_argument("--start-maximized")
options.add_argument("--ignore-ssl-errors=yes")
options.add_argument("--ignore-certificate-errors")

# Method 1: Using the Service Base class
#service = Service(executable_path=r'C:\Users\echavez\Desktop\Github\selenium\chromedriver.exe')
#chrome_browser = webdriver.Chrome(service=service, options=options) # keeps chrome open

# Method 2: Using the subclass (ChromeService) of Service class
service = webdriver.ChromeService(executable_path=r'C:\Users\echavez\Desktop\Github\selenium\chromedriver.exe') # path to chromedriver executable
chrome_browser = webdriver.Chrome(service=service, options=options) # keeps chrome open
chrome_browser.get('https://qaplayground.com/practice/input-fields')

assert 'Input Field Automation Practice | QA Playground | QA Playground' in chrome_browser.title

chrome_browser.implicitly_wait(2)
movie_name_input = chrome_browser.find_element(By.ID, 'movieNameInput')
movie_name_input.clear()
assert 'Enter a movie name…' in movie_name_input.get_attribute('placeholder')
assert 'Enter a movie name…' in chrome_browser.page_source
movie_name_input.send_keys('The Matrix')

submit_movie_btn = chrome_browser.find_element(By.ID, 'submitMovieBtn')
assert 'Submit' in chrome_browser.page_source
assert 'Submit' in submit_movie_btn.text
submit_movie_btn.click()

result_message = chrome_browser.find_element(By.ID, 'result-s01')
assert 'The Matrix' in result_message.text

chrome_browser.quit()
# time.sleep(2)
# show_message_button = chrome_browser.find_element(By.CLASS_NAME, 'btn-default')
# show_message_button.click()

# output_message = chrome_browser.find_element(By.ID, 'display')
# assert 'I AM EXTRA COOOOOL' in output_message.text