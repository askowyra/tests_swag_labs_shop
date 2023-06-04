import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time
import utils

SELECT_CLASS = "product_sort_container"
INVENTORY_ITEM_ID = "inventory_item"
NAME_CLASS = "inventory_item_name"
PRICE_CLASS = "inventory_item_price"

def get_product_list(driver):
    product_list = []
    inventory_items = driver.find_elements(By.CLASS_NAME, INVENTORY_ITEM_ID)
    for item in inventory_items:
        name_item = item.find_element(By.CLASS_NAME, NAME_CLASS)
        price_item = item.find_element(By.CLASS_NAME, PRICE_CLASS)
        product_list.append((name_item.text, float(price_item.text[1:])))
    return product_list

def is_sorted_asc_by_name(product_list):
    sorted_list = product_list.copy()
    sorted(sorted_list, key= lambda p: p[0])
    return sorted_list == product_list

def is_sorted_desc_by_name(product_list):
    sorted_list = product_list.copy()
    sorted(sorted_list, key= lambda p: p[0], reverse=True)
    return sorted_list == product_list

def is_sorted_asc_by_price(product_list):
    sorted_list = product_list.copy()
    sorted(sorted_list, key= lambda p: p[1])
    return sorted_list == product_list

def is_sorted_desc_by_price(product_list):
    sorted_list = product_list.copy()
    sorted(sorted_list, key= lambda p: p[1], reverse=True)
    return sorted_list == product_list

def set_select_value(driver, value):
    select_element = driver.find_element(By.CLASS_NAME, SELECT_CLASS)
    select = Select(select_element)
    select.select_by_value(value)


def sort_by_name_asc(driver):
    set_select_value(driver, "az")

def sort_by_name_desc(driver):
    set_select_value(driver, "za")

def sort_by_price_asc(driver):
    set_select_value(driver, "lohi")

def sort_by_price_desc(driver):
    set_select_value(driver, "hilo")

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    utils.login(driver, "standard_user", "secret_sauce")
    time.sleep(1)
    yield driver
    driver.quit()


def test_product_list_should_be_sorted(driver):
    sort_by_name_asc(driver)
    product_list = get_product_list(driver)
    time.sleep(2)

    assert is_sorted_asc_by_name(product_list) == True

    sort_by_name_desc(driver)
    product_list = get_product_list(driver)
    
    time.sleep(2)
    assert is_sorted_desc_by_name(product_list) == True

    sort_by_price_asc(driver)
    product_list = get_product_list(driver)
    
    time.sleep(2)
    assert is_sorted_asc_by_price(product_list) == True

    sort_by_price_desc(driver)
    product_list = get_product_list(driver)
    
    time.sleep(2)
    assert is_sorted_desc_by_price(product_list) == True