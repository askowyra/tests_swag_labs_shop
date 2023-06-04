import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import utils


PRODUCT_LIST = {
    "Sauce Labs Backpack": ("add-to-cart-sauce-labs-backpack", "$29.99", "remove-sauce-labs-backpack"),
    "Sauce Labs Bike Light": ("add-to-cart-sauce-labs-bike-light", "$9.99", "remove-sauce-labs-bike-light"),
    "Sauce Labs Bolt T-Shirt": ("add-to-cart-sauce-labs-bolt-t-shirt", "$15.99", "remove-sauce-labs-bolt-t-shirt"),
    "Sauce Labs Fleece Jacket": ("add-to-cart-sauce-labs-fleece-jacket", "$49.99", "remove-sauce-labs-fleece-jacket"),
    "Sauce Labs Onesie": ("add-to-cart-sauce-labs-onesie", "$7.99", "remove-sauce-labs-onesie"),
    "Test.allTheThings() T-Shirt (Red)": ("add-to-cart-test.allthethings()-t-shirt-(red)", "$15.99", "remove-test.allthethings()-t-shirt-(red)")
}

BASKET_BUTTON_CLASS_NAME = "shopping_cart_link"
SHOPPING_CART_BADGE_CLASS = "shopping_cart_badge"

PRODUCT_SORT_CONTAINER_CLASS_NAME = "product_sort_container"
MENU_BUTTON_ID = "react-burger-menu-btn"
CONTINUE_SHOPPING_ID = "continue-shopping"
CHECKOUT_SHOPPING_ID = "checkout"
CART_ITEM_CLASS = "cart_item"


@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    utils.login(driver, "standard_user", "secret_sauce")
    time.sleep(1)
    yield driver
    driver.quit()

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

def remove_product_from_shopping_cart(driver, product):
    product_id = PRODUCT_LIST[product][2]
    element = driver.find_element(By.ID, product_id)
    element.click()

def get_number_of_product_in_shopping_cart_product_page(driver):
    element = driver.find_element(By.CLASS_NAME, SHOPPING_CART_BADGE_CLASS)
    print("get_number_of_product_in_shopping_cart {}".format(element.text))
    return int(element.text)

def get_number_of_product_in_shopping_cart(driver):
    elements = driver.find_elements(By.CLASS_NAME, CART_ITEM_CLASS)
    return len(elements)


def is_shopping_cart_contain_product(driver, product):
    product_id = PRODUCT_LIST[product][2]
    elements = driver.find_elements(By.ID, product_id)
    return len(elements) == 1

def test_should_add_one_product_to_shopping_cart(driver):
    product_name = "Sauce Labs Backpack"
    add_product_to_shopping_cart(driver, product_name) 
    open_shopping_cart(driver)

    assert get_number_of_product_in_shopping_cart_product_page(driver) == 1
    assert is_shopping_cart_contain_product(driver, "Sauce Labs Backpack") == True
    

def test_should_remove_one_product_from_shopping_cart(driver):
    product_name = "Sauce Labs Backpack"
    add_product_to_shopping_cart(driver, product_name)
    open_shopping_cart(driver)

    remove_product_from_shopping_cart(driver, product_name)
    assert get_number_of_product_in_shopping_cart(driver) == 0


def test_should_add_three_products_to_shopping_cart(driver):
    add_product_to_shopping_cart(driver, "Sauce Labs Backpack")

    assert get_number_of_product_in_shopping_cart_product_page(driver) == 1

    add_product_to_shopping_cart(driver, "Sauce Labs Bike Light")

    assert get_number_of_product_in_shopping_cart_product_page(driver) == 2

    add_product_to_shopping_cart(driver, "Sauce Labs Bolt T-Shirt")

    assert get_number_of_product_in_shopping_cart_product_page(driver) == 3

    open_shopping_cart(driver)
    assert is_shopping_cart_contain_product(driver, "Sauce Labs Backpack") == True
    assert is_shopping_cart_contain_product(driver, "Sauce Labs Bike Light") == True
    assert is_shopping_cart_contain_product(driver, "Sauce Labs Bolt T-Shirt") == True


def test_should_remove_three_products_from_shopping_cart(driver):
    add_product_to_shopping_cart(driver, "Sauce Labs Backpack")
    add_product_to_shopping_cart(driver, "Sauce Labs Bike Light")
    add_product_to_shopping_cart(driver, "Sauce Labs Bolt T-Shirt")

    open_shopping_cart(driver)
    remove_product_from_shopping_cart(driver, "Sauce Labs Backpack")

    assert get_number_of_product_in_shopping_cart(driver) == 2

    remove_product_from_shopping_cart(driver, "Sauce Labs Bike Light")

    assert get_number_of_product_in_shopping_cart(driver) == 1

    remove_product_from_shopping_cart(driver, "Sauce Labs Bolt T-Shirt")
   
    assert get_number_of_product_in_shopping_cart(driver) == 0

def test_should_add_six_products_to_shopping_cart(driver):
    add_product_to_shopping_cart(driver, "Sauce Labs Backpack")

    assert get_number_of_product_in_shopping_cart_product_page(driver) == 1

    add_product_to_shopping_cart(driver, "Sauce Labs Bike Light")

    assert get_number_of_product_in_shopping_cart_product_page(driver) == 2

    add_product_to_shopping_cart(driver, "Sauce Labs Bolt T-Shirt")

    assert get_number_of_product_in_shopping_cart_product_page(driver) == 3

    add_product_to_shopping_cart(driver, "Sauce Labs Fleece Jacket")

    assert get_number_of_product_in_shopping_cart_product_page(driver) == 4

    add_product_to_shopping_cart(driver, "Sauce Labs Onesie")

    assert get_number_of_product_in_shopping_cart_product_page(driver) == 5

    add_product_to_shopping_cart(driver, "Test.allTheThings() T-Shirt (Red)")

    assert get_number_of_product_in_shopping_cart_product_page(driver) == 6

    open_shopping_cart(driver)

    assert is_shopping_cart_contain_product(driver, "Sauce Labs Backpack") == True
    assert is_shopping_cart_contain_product(driver, "Sauce Labs Bike Light") == True
    assert is_shopping_cart_contain_product(driver, "Sauce Labs Bolt T-Shirt") == True
    assert is_shopping_cart_contain_product(driver, "Sauce Labs Fleece Jacket") == True
    assert is_shopping_cart_contain_product(driver, "Sauce Labs Onesie") == True
    assert is_shopping_cart_contain_product(driver, "Test.allTheThings() T-Shirt (Red)") == True


def test_should_remove_six_products_from_shopping_cart(driver):
    add_product_to_shopping_cart(driver, "Sauce Labs Backpack")
    add_product_to_shopping_cart(driver, "Sauce Labs Bike Light")
    add_product_to_shopping_cart(driver, "Sauce Labs Bolt T-Shirt")
    add_product_to_shopping_cart(driver, "Sauce Labs Fleece Jacket")
    add_product_to_shopping_cart(driver, "Sauce Labs Onesie")
    add_product_to_shopping_cart(driver, "Test.allTheThings() T-Shirt (Red)")

    open_shopping_cart(driver)
    remove_product_from_shopping_cart(driver, "Sauce Labs Backpack")

    assert get_number_of_product_in_shopping_cart(driver) == 5

    remove_product_from_shopping_cart(driver, "Sauce Labs Bike Light")

    assert get_number_of_product_in_shopping_cart(driver) == 4

    remove_product_from_shopping_cart(driver, "Sauce Labs Bolt T-Shirt")

    assert get_number_of_product_in_shopping_cart(driver) == 3

    remove_product_from_shopping_cart(driver, "Sauce Labs Fleece Jacket")

    assert get_number_of_product_in_shopping_cart(driver) == 2

    remove_product_from_shopping_cart(driver, "Sauce Labs Onesie")

    assert get_number_of_product_in_shopping_cart(driver) == 1

    remove_product_from_shopping_cart(driver, "Test.allTheThings() T-Shirt (Red)")

    assert get_number_of_product_in_shopping_cart(driver) == 0

def test_should_display_correct_shopping_cart_after_multiple_operation(driver):
    add_product_to_shopping_cart(driver, "Sauce Labs Backpack")

    assert get_number_of_product_in_shopping_cart_product_page(driver) == 1

    add_product_to_shopping_cart(driver, "Sauce Labs Bike Light")

    assert get_number_of_product_in_shopping_cart_product_page(driver) == 2

    remove_product_from_shopping_cart(driver, "Sauce Labs Backpack")

    assert get_number_of_product_in_shopping_cart_product_page(driver) == 1

    add_product_to_shopping_cart(driver, "Sauce Labs Backpack")

    assert get_number_of_product_in_shopping_cart_product_page(driver) == 2

    open_shopping_cart(driver)

    assert is_shopping_cart_contain_product(driver, "Sauce Labs Backpack") == True
    assert is_shopping_cart_contain_product(driver, "Sauce Labs Bike Light") == True
