import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import Select
import time
import utils

CONTINUE_SHOPPING_BUTTON_ID = "continue-shopping"
CHECKOUT_BUTTON_ID = "checkout"
FIRST_NAME_FIELD_ID = "first-name"
LAST_NAME_FIELD_ID = "last-name"
POSTAL_CODE_FIELD_ID = "postal-code"
CONTINUE_BUTTON_ID = "continue"
CANCEL_BUTTON_ID = "cancel"
FINISH_BUTTON_ID = "finish"

CART_LIST_CLASS = "cart_list"
CART_TIEM_CLASS = "cart_item"
CART_QUANTITY_CLASS = "cart_quantity"
INVENTORY_ITEM_NAME_CLASS = "inventory_item_name"
INVENTORY_ITEM_PRICE_CLASS = "inventory_item_price"

TOTAL_CLASS = "summary_subtotal_label"
TAX_CLASS = "summary_tax_label"
TOTAL_SUMMARY_CLASS = "summary_total_label"

COMPLETE_HEADER_CLASS = "complete-header"



@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    utils.login(driver, "standard_user", "secret_sauce")
    time.sleep(1)
    yield driver
    driver.quit()

def is_complete_page_is_displayed(driver):
    try:
        label = driver.find_element(By.CLASS_NAME, COMPLETE_HEADER_CLASS)
        return label.text == "Thank you for your order!"
    except NoSuchElementException:
        return False

def get_item_total(driver):
     label = driver.find_element(By.CLASS_NAME, TOTAL_CLASS)
     return float(label.text[13:])

def get_tax(driver):
     label = driver.find_element(By.CLASS_NAME, TAX_CLASS)
     return float(label.text[6:])

def get_total(driver):
     label = driver.find_element(By.CLASS_NAME, TOTAL_SUMMARY_CLASS)
     return float(label.text[8:])

def continue_shopping(driver):
    continue_button = driver.find_element(By.ID, CHECKOUT_BUTTON_ID)
    continue_button.click()
    time.sleep(2)

def finsih_shopping(driver):
    finish_button = driver.find_element(By.ID, FINISH_BUTTON_ID)
    finish_button.click()
    time.sleep(2)

def continue_shopping2(driver):
    continue_button = driver.find_element(By.ID, CONTINUE_BUTTON_ID)
    continue_button.click()
    time.sleep(2)

def cancel_shopping(driver):
    cancel_button = driver.find_element(By.ID, CANCEL_BUTTON_ID)
    cancel_button.click()
    time.sleep(2)

def fill_forms(driver, first_name, last_name, postal_code):
    first_name_field = driver.find_element(By.ID, FIRST_NAME_FIELD_ID)
    last_name_field = driver.find_element(By.ID, LAST_NAME_FIELD_ID)
    postal_code_field = driver.find_element(By.ID, POSTAL_CODE_FIELD_ID)
    first_name_field.clear()
    last_name_field.clear()
    postal_code_field.clear()

    time.sleep(5)
    print(first_name)
    first_name_field.send_keys(first_name)   
    print(last_name)
    last_name_field.send_keys(last_name)
    print(postal_code)
    postal_code_field.send_keys(postal_code)

def get_product_information(driver):
    product_list = []
    inventory_items = driver.find_elements(By.CLASS_NAME, CART_TIEM_CLASS)
    print("inventory_items len: ", len(inventory_items))
    for item in inventory_items:    
        name_item = item.find_element(By.CLASS_NAME, INVENTORY_ITEM_NAME_CLASS)
        price_item = item.find_element(By.CLASS_NAME, INVENTORY_ITEM_PRICE_CLASS)
        
        product_list.append((name_item.text, float(price_item.text[1:])))
    return product_list

def test_purchase_one_item_successfully(driver):
    utils.add_product_to_shopping_cart(driver, "Sauce Labs Backpack")
    utils.open_shopping_cart(driver)
    continue_shopping(driver)
    fill_forms(driver, "Anna", "Tester", "58-100")
    continue_shopping2(driver)
    
    product_list = get_product_information(driver)
    print(product_list)
    assert ('Sauce Labs Backpack', 29.99) in product_list

    total_item = get_item_total(driver)
    tax = get_tax(driver)
    total = get_total(driver)

    assert total_item == 29.99
    assert tax == 2.40
    assert total == 32.39

    finsih_shopping(driver)
    time.sleep(1)
    assert is_complete_page_is_displayed(driver) == True


def test_cancel_purchase_one_item_successfully(driver):
    utils.add_product_to_shopping_cart(driver, "Sauce Labs Backpack")
    utils.open_shopping_cart(driver)
    continue_shopping(driver)
    fill_forms(driver, "Anna", "Tester", "58-100")
    continue_shopping2(driver)
    
    product_list = get_product_information(driver)
    print(product_list)
    assert ('Sauce Labs Backpack', 29.99) in product_list

    total_item = get_item_total(driver)
    tax = get_tax(driver)
    total = get_total(driver)

    assert total_item == 29.99
    assert tax == 2.40
    assert total == 32.39

    cancel_shopping(driver)
    time.sleep(1)
    assert is_complete_page_is_displayed(driver) == False

def test_purchase_two_item_successfully(driver):
    utils.add_product_to_shopping_cart(driver, "Sauce Labs Backpack")
    utils.add_product_to_shopping_cart(driver, "Sauce Labs Bike Light")
    utils.open_shopping_cart(driver)
    continue_shopping(driver)
    time.sleep(10)
    fill_forms(driver, "Anna", "Tester", "58-100")
    time.sleep(10)
    continue_shopping2(driver)
    time.sleep(10)
    
    product_list = get_product_information(driver)
    print(product_list)

    time.sleep(10)

    assert ('Sauce Labs Backpack', 29.99) in product_list
    assert ('Sauce Labs Bike Light', 9.99) in product_list

    total_item = get_item_total(driver)
    tax = get_tax(driver)
    total = get_total(driver)

    assert total_item == 39.98
    assert tax == 3.2
    assert total == 43.18

    finsih_shopping(driver)
    time.sleep(1)
    assert is_complete_page_is_displayed(driver) == True

def test_cancel_purchase_two_items_successfully(driver):
    utils.add_product_to_shopping_cart(driver, "Sauce Labs Backpack")
    utils.add_product_to_shopping_cart(driver, "Sauce Labs Bike Light")
    utils.open_shopping_cart(driver)
    continue_shopping(driver)
    time.sleep(10)
    fill_forms(driver, "Anna", "Tester", "58-100")
    time.sleep(10)
    continue_shopping2(driver)
    time.sleep(10)
    
    product_list = get_product_information(driver)
    print(product_list)

    time.sleep(10)

    assert ('Sauce Labs Backpack', 29.99) in product_list
    assert ('Sauce Labs Bike Light', 9.99) in product_list

    total_item = get_item_total(driver)
    tax = get_tax(driver)
    total = get_total(driver)

    assert total_item == 39.98
    assert tax == 3.2
    assert total == 43.18

    cancel_shopping(driver)
    time.sleep(1)
    assert is_complete_page_is_displayed(driver) == False
    time.sleep(20)

def test_try_purchase_item_without_fill_form_successfully(driver):
    utils.add_product_to_shopping_cart(driver, "Sauce Labs Backpack")
    utils.open_shopping_cart(driver)
    continue_shopping(driver)
    continue_shopping2(driver)
    first_name_input = driver.find_element(By.ID, "first-name")
    last_name_input = driver.find_element(By.ID, "last-name")
    postal_name_input = driver.find_element(By.ID, "postal-code")

    class_name = first_name_input.get_attribute("class")
    assert "input_error" in class_name.split()

    class_name = last_name_input.get_attribute("class")
    assert "input_error" in class_name.split()

    class_name = postal_name_input.get_attribute("class")
    assert "input_error" in class_name.split()
    
    time.sleep(20)

def test_try_purchase_item_without_fill_all_field_in_form_successfully(driver):
    utils.add_product_to_shopping_cart(driver, "Sauce Labs Backpack")
    utils.open_shopping_cart(driver)
    continue_shopping(driver)
    
    fill_forms(driver, "", "Tester", "58-100")
    continue_shopping2(driver)
    first_name_input = driver.find_element(By.ID, "first-name")
    last_name_input = driver.find_element(By.ID, "last-name")
    postal_name_input = driver.find_element(By.ID, "postal-code")

    class_name = first_name_input.get_attribute("class")
    assert "input_error" in class_name.split()
    
    time.sleep(20)
