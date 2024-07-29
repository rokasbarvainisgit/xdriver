from selenium.webdriver.common.by import By


TEST_WEBSITE = "https://pypi.org"


def test_get_element(chromedriver):
    chromedriver.get(TEST_WEBSITE)
    chromedriver.get_element((By.ID, "search"))


def test_get_clickable_element(chromedriver):
    chromedriver.get(TEST_WEBSITE)
    chromedriver.get_clickable_element((By.ID, "search")).click()


def test_driver_check_if_element_exists(chromedriver):
    chromedriver.get(TEST_WEBSITE)
    assert chromedriver.check_if_element_exists((By.ID, "content")) is True, "WebElement was not found!"


def test_check_if_clickable_element_exists(chromedriver):
    chromedriver.get(TEST_WEBSITE)
    assert chromedriver.check_if_clickable_element_exists((By.ID, "search")) is True, "Elem was not found!"


def test_hover_over_element(chromedriver):
    chromedriver.get(TEST_WEBSITE)
    chromedriver.hover_over_element((By.ID, "search"))


def test_get_elements(chromedriver):
    chromedriver.get(TEST_WEBSITE)
    assert len(chromedriver.get_elements((By.CSS_SELECTOR, "div"))) > 0, "No div WebElements were found!"


def test_get_element_with_geckodriver(geckodriver):
    geckodriver.get(TEST_WEBSITE)
    geckodriver.get_element((By.ID, "search"))
