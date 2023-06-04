import pytest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import time
import utils


URL = "https://www.saucedemo.com/"
SHOP_NAME = "Swag Labs" 

TEST_USER_NAME = "standard_user"
PASSWORD = "secret_sauce"

LOGIN_PAGE_ELEMENTS = [
    ("user-name", "Username"),
    ("password", "Password"),
    ("login-button", "Login")
]


PRODUCT_PAGE_ELEMENTS = [
    ("react-burger-menu-btn", "Menu przycisk"),
    ("shopping_cart_container", "Koszyk przycisk"),
    ("inventory_container", "Lista produktów"),
]

@pytest.fixture(scope="module")
def driver():
    driver = webdriver.Chrome()
    
    yield driver
    driver.quit()

def is_login_page_correct(driver):
    result = True
    
    #Sprawdź czy wyświetlona są następujące pola: Swag Labs, UserName, Password, Login
    assert SHOP_NAME in driver.title

    for value in LOGIN_PAGE_ELEMENTS:
        try:
            element = driver.find_element(By.ID,value[0])
            assert element is not None, "Element istnieje: {}".format(value[1])
        except NoSuchElementException:
            result = False
            assert element is None, "Element nie istnieje: {}".format(value[1])
    return result

def is_product_page_correct(driver):
    result = True

    assert "Swag Labs" in driver.title

    for value in PRODUCT_PAGE_ELEMENTS:
        try:
            element = driver.find_element(By.ID,value[0])
            assert element is not None, "Element istnieje: {}".format(value[1])
        except NoSuchElementException:
            result = False
            assert element is None, "Element nie istnieje: {}".format(value[1])

    return result


def test_should_login_successfully(driver):
    driver.get(URL)

    #Sprawdź czy wyświetlona są następujące pola: Swag Labs, UserName, Password, Login
    if is_login_page_correct(driver) == False:
        pytest.fail("Test zakończony z powodu, że nie istnieje jeden z elementów na stronie logowania")
 
    #Logowanie
    utils.login(driver, TEST_USER_NAME, PASSWORD)

    #Sprawdzenie czy istnieją odpowiednie elementy na stronie sklepu
    assert is_product_page_correct(driver), "Strona z produktami została wyświetlona w nieprawidłowy sposób"            
    utils.logout(driver)


def test_should_login_unsucessfully_when_username_is_incorrect(driver):
    driver.get(URL)
    time.sleep(2)
    
    #Sprawdź czy wyświetlona są następujące pola: Swag Labs, UserName, Password, Login
    if is_login_page_correct(driver) == False:
        pytest.fail("Test zakończony z powodu, że nie istnieje jeden z elementów na stronie logowania")

    INCORECT_USER_NAME = "standard_username"
    #Logowanie
    utils.login(driver, INCORECT_USER_NAME, PASSWORD)
    time.sleep(2)

    try:
        element = driver.find_element(By.CLASS_NAME, "error-message-container")
    except NoSuchElementException:
         assert element is not None, "Informacj o nierpawdiłowym użytkowniu lub haśle nie została wyświetlona"
    
    assert element.is_displayed() == True, "Informacj o nierpawdiłowym użytkowniu lub haśle nie została wyświetlona"
    time.sleep(2)

def test_should_login_unsucessfully_when_password_is_incorrect(driver):
    driver.get(URL)
    time.sleep(2)
    
    #Sprawdź czy wyświetlona są następujące pola: Swag Labs, UserName, Password, Login
    if is_login_page_correct(driver) == False:
        pytest.fail("Test zakończony z powodu, że nie istnieje jeden z elementów na stronie logowania")

    INCORECT_PASSWORD = "secret_secret"
    #Logowanie
    utils.login(driver, TEST_USER_NAME, INCORECT_PASSWORD)
    time.sleep(2)

    try:
        element = driver.find_element(By.CLASS_NAME, "error-message-container")
    except NoSuchElementException:
         assert element is not None, "Informacj o nierpawdiłowym użytkowniu lub haśle nie została wyświetlona"
    
    assert element.is_displayed() == True, "Informacj o nierpawdiłowym użytkowniu lub haśle nie została wyświetlona"
    time.sleep(2)
