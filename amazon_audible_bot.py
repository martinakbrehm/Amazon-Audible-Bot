from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

web = "https://www.audible.com/search"
path = "/home/marti/Downloads/chromedriver/chromedriver"
driver = webdriver.Chrome()
driver.get(web)
driver.maximize_window()

#pagination
pagination = driver.find_element(By.XPATH,'//ul[contains(@class, "pagingElements")]')
pages = pagination.find_elements(By.TAG_NAME,'li')
last_page = int(pages[-2].text)
next_page = driver.find_element(By.XPATH, '//span[contains(@class, "nextButton")]')
next_page.click()

current_page = 1
book_title = []
book_author = []
book_length = []

while current_page <= last_page:

    container = driver.find_element(By.CLASS_NAME, 'adbl-impression-container')
    container1 = container.find_element(By.XPATH, './/ul')
    products = container1.find_elements(By.XPATH, './li')

    for product in products:
        book_title.append(product.find_element(By.XPATH,'.//h3[contains(@class, "bc-heading")]').text)
        book_author.append(product.find_element(By.XPATH,'.//li[contains(@class, "authorLabel")]').text)
        book_length.append(product.find_element(By.XPATH,'.//li[contains(@class, "runtimeLabel")]').text)
    current_page = current_page + 1
    try:
        next_page = driver.find_element(By.XPATH, '//span[contains(@class, "nextButton")]')
        next_page.click()
    except:
        pass
driver.quit()

df_books = pd.DataFrame({'title': book_title, 'author': book_author, 'lenght': book_length})
df_books.to_csv('books.csv', index=False)