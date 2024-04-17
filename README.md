<div align="center">

# xDriver

![PyPI - Version](https://img.shields.io/pypi/v/xdriver?color=green&link=https%3A%2F%2Fpypi.org%2Fproject%2Fxdriver%2F)
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/xdriver?link=https%3A%2F%2Fpypi.org%2Fproject%2Fxdriver%2F)

Expanded Selenium WebDriver.
</div>

## Setup & Examples of Usage
 - Install the package using the `pip install xdriver` command.
 - Create a pytest function scope fixture that will start/close the webdriver before/after each test `conftest.py`
 - Create a test that will use the driver provided by the before-mentioned fixture `test_example.py`

Example _tests_ directory structure:
```
tests/
│
├── conftest.py
└── test_example.py
```
_conftest.py_ file content:
```python
@pytest.fixture(scope='function')
def driver() -> Driver:
    """
    Starts the Driver before test and closes it afterward
    """
    driver = Driver(webdriver_type="chromedriver")
    yield driver
    driver.quit()
```
_test_example.py_ file content:
```python
from selenium.webdriver.common.by import By


def test_example(driver):
    """
    Tests if the example page has the h1 WebElement
    """
    driver.get("https://example.com/")
    assert driver.check_if_element_exists((By.CSS_SELECTOR, "h1")), "h1 element was not found!"
```

### Additional Information
All available methods can be found in the `webdriver.py` file. Some examples:
```
get_element()
get_clickable_element()
check_if_element_exists()
check_if_clickable_element_exists()
hover_over_element()
...
```
If you ever need to use the default selenium webdriver use `driver.driver`:
```python
from selenium.webdriver.common.by import By


def test_example_default_webdriver(driver):
    """
    Example of default Selenium WebDriver usage 
    Tests if h1 element is displayed
    """
    driver.get("https://example.com/")
    h1 = driver.driver.find_element(By.CSS_SELECTOR, "h1")
    assert h1.is_displayed(), "h1 element was not displayed!"
```