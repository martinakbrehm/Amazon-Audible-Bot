from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

web = "https://www.audible.com/search"
path = "/home/marti/Downloads/chromedriver/chromedriver"
driver = webdriver.Chrome()
driver.get(web)
driver.maximize_window()

container = driver.find_element(By.CLASS_NAME, 'adbl-impression-container')
container1 = container.find_element(By.XPATH, './/ul')
products = container1.find_elements(By.XPATH, './li')

book_title = []
book_author = []
book_length = []

for product in products:
    book_title.append(product.find_element(By.XPATH,'.//h3[contains(@class, "bc-heading")]').text)
    book_author.append(product.find_element(By.XPATH,'.//li[contains(@class, "authorLabel")]').text)
    book_length.append(product.find_element(By.XPATH,'.//li[contains(@class, "runtimeLabel")]').text)

driver.quit()

df_books = pd.DataFrame({'title': book_title, 'author': book_author, 'lenght': book_length})
df_books.to_csv('books.csv', index=False)