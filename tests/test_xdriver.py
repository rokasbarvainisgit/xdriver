from selenium.webdriver.common.by import By


TEST_WEBSITE = "https://pypi.org"


def test_get_elem_by_locator(driver):
    driver.get(TEST_WEBSITE)
    driver.get_elem_by_locator((By.ID, "search"))


def test_get_clickable_elem_by_locator(driver):
    driver.get(TEST_WEBSITE)
    driver.get_clickable_elem_by_locator((By.ID, "search")).click()


def test_driver_check_if_elem_exists_by_locator(driver):
    driver.get(TEST_WEBSITE)
    assert driver.check_if_elem_exists_by_locator((By.ID, "content")) is True, "Elem was not found!"


def test_check_if_clickable_elem_exists_by_locator(driver):
    driver.get(TEST_WEBSITE)
    assert driver.check_if_clickable_elem_exists_by_locator((By.ID, "search")) is True, "Elem was not found!"
