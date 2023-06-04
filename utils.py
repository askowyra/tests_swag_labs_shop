from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

PRODUCT_LIST = {
    "Sauce Labs Backpack": ("add-to-cart-sauce-labs-backpack", "$29.99", "remove-sauce-labs-backpack"),
    "Sauce Labs Bike Light": ("add-to-cart-sauce-labs-bike-light", "$9.99", "remove-sauce-labs-bike-light"),
    "Sauce Labs Bolt T-Shirt": ("add-to-cart-sauce-labs-bolt-t-shirt", "$15.99", "remove-sauce-labs-bolt-t-shirt"),
    "Sauce Labs Fleece Jacket": ("add-to-cart-sauce-labs-fleece-jacket", "$49.99", "remove-sauce-labs-fleece-jacket"),
    "Sauce Labs Onesie": ("add-to-cart-sauce-labs-onesie", "$7.99", "remove-sauce-labs-onesie"),
    "Test.allTheThings() T-Shirt (Red)": ("add-to-cart-test.allthethings()-t-shirt-(red)", "$15.99", "remove-test.allthethings()-t-shirt-(red)")
}

BASKET_BUTTON_CLASS_NAME = "shopping_cart_link"

def login(driver, username, password):
    user_name_input = driver.find_element(By.ID, "user-name")
    user_name_input.send_keys(username)

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys(password)
    password_input.send_keys(Keys.RETURN)
    time.sleep(1)

def logout(driver):
    time.sleep(1)
    button = driver.find_element(By.ID, "react-burger-menu-btn")
    button.click()
    time.sleep(1)
    logout = driver.find_element(By.ID, "logout_sidebar_link")
    logout.click()

def add_product_to_shopping_cart(driver, product_name):
    product_id = PRODUCT_LIST[product_name][0]
    add_to_cart = driver.find_element(By.ID, product_id)
    add_to_cart.click()
    time.sleep(2)

def open_shopping_cart(driver):
    time.sleep(5)
    print("open_shopping_cart")
    shopping_cart_link = driver.find_element(By.CLASS_NAME, BASKET_BUTTON_CLASS_NAME)
    shopping_cart_link.click()
    time.sleep(5)