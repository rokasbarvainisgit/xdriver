from selenium.webdriver.common.by import By


TEST_WEBSITE = "https://pypi.org"


def test_get_element(driver):
    driver.get(TEST_WEBSITE)
    driver.get_element((By.ID, "search"))


def test_get_clickable_element(driver):
    driver.get(TEST_WEBSITE)
    driver.get_clickable_element((By.ID, "search")).click()


def test_driver_check_if_element_exists(driver):
    driver.get(TEST_WEBSITE)
    assert driver.check_if_element_exists((By.ID, "content")) is True, "WebElement was not found!"


def test_check_if_clickable_element_exists(driver):
    driver.get(TEST_WEBSITE)
    assert driver.check_if_clickable_element_exists((By.ID, "search")) is True, "Elem was not found!"


def test_hover_over_element(driver):
    driver.get(TEST_WEBSITE)
    driver.hover_over_element((By.ID, "search"))


def test_get_elements(driver):
    driver.get(TEST_WEBSITE)
    assert len(driver.get_elements((By.CSS_SELECTOR, "div"))) > 0, "No div WebElements were found!"
