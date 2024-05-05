from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

url = "https://www.coursyz.com"
username = "username"
password = "password"

driver = webdriver.Chrome()
driver.get(url + '/wp-login.php')
username_field = driver.find_element(By.ID, 'user_login')
password_field = driver.find_element(By.ID, 'user_pass')
username_field.send_keys(username)
password_field.send_keys(password)
password_field.send_keys(Keys.RETURN)
time.sleep(5)

if 'wp-admin' in driver.current_url:
    product_url = "https://www.coursyz.com/wp-admin/edit.php?post_type=product"
    driver.get(product_url)
    time.sleep(5)

    page_source = driver.page_source

    # print(page_source)

    product_titles = []
    start_index = page_source.find('<td data-colname="Title">')
    while start_index != -1:
        start_index = page_source.find('">', start_index) + 2
        end_index = page_source.find('</a>', start_index)
        product_title = page_source[start_index:end_index]
        product_titles.append(product_title)
        start_index = page_source.find('<td data-colname="Title">', end_index)

    for title in product_titles:
        print(title)

    input("Press Enter to close the browser...")
    driver.quit()
else:
    print('Login failed.')
