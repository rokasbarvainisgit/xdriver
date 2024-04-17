from selenium.webdriver.common.by import By


TEST_WEBSITE = "https://pypi.org"


def test_get_elem_by_locator(driver):
    driver.get(TEST_WEBSITE)
    driver.get_element((By.ID, "search"))


def test_get_clickable_elem_by_locator(driver):
    driver.get(TEST_WEBSITE)
    driver.get_clickable_element((By.ID, "search")).click()


def test_driver_check_if_elem_exists_by_locator(driver):
    driver.get(TEST_WEBSITE)
    assert driver.check_if_element_exists((By.ID, "content")) is True, "Elem was not found!"


def test_check_if_clickable_elem_exists_by_locator(driver):
    driver.get(TEST_WEBSITE)
    assert driver.check_if_clickable_element_exists((By.ID, "search")) is True, "Elem was not found!"


def test_hover_over_elem_by_locator(driver):
    driver.get(TEST_WEBSITE)
    driver.hover_over_element((By.ID, "search"))
