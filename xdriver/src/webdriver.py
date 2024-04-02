from selenium.common import StaleElementReferenceException, NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from typing import List, Optional
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class Driver(object):
    """
    Expanded Selenium WebDriver class that has methods with explicit waits.

    We recommend creating a 'function' scope pytest fixture that will initiate this Driver before each test
     and quit it after each test.
    """
    def __init__(self,
                 webdriver_type: str = "chromedriver",
                 options: Optional[List] = None,
                 default_timeout: int = None):
        """
        Initiates a custom webdriver.

        :param webdriver_type: webdriver type (chromedriver, geckodriver, etc. currently supports: chromedriver)
        :param options: list of Webdriver options to be added
        :param default_timeout: default timeout for getting WebElements
        """
        if "chromedriver" in str(webdriver_type).lower():
            chromedriver_options = ChromeOptions()
            if options:
                for arg in options:
                    chromedriver_options.add_argument(arg)
            self.driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()),
                                           options=chromedriver_options)
        else:
            raise Exception(f"Provided Webdriver type was not recognised! {webdriver_type}")
        self.driver.set_page_load_timeout(120)
        if default_timeout is None:
            self._default_timeout = 30
        else:
            self._default_timeout = default_timeout

    def driver(self) -> WebDriver:
        """
        Returns the default selenium webdriver obj

        :return: WebDriver
        """
        return self.driver

    def quit(self) -> None:
        """
        Quit the webdriver
        """
        self.driver.quit()

    def get(self, url: str) -> None:
        """
        Opens the webpage provided in the 'url' parameter

        :param url: url
        """
        self.driver.get(url)

    def get_clickable_elem_by_locator(self, locator: tuple[str, str], timeout: int = None) -> WebElement:
        """
        Waits for element to become clickable and returns that element

        :param locator: tuple of (selector, value)
        :param timeout: max time to wait for the WebElement before failing in seconds (Optional), default = 30

        :return: WebElement
        """
        if timeout is None:
            timeout = self._default_timeout
        try:
            return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
        except (StaleElementReferenceException, NoSuchElementException, TimeoutException) as e:
            raise TimeoutException(f"Web element was not found! locator={locator}, Exception={e}")

    def get_elem_by_locator(self, locator: tuple[str, str], timeout: int = None) -> WebElement:
        """
        Waits for element and returns that element

        :param locator: tuple of (selector, value)
        :param timeout: max time to wait for the WebElement before failing in seconds (Optional), default = 30

        :return: WebElement
        """
        if timeout is None:
            timeout = self._default_timeout
        try:
            return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator))
        except (StaleElementReferenceException, NoSuchElementException, TimeoutException) as e:
            raise TimeoutException(f"Web element was not found! locator={locator}, Exception={e}")

    def check_if_elem_exists_by_locator(self, locator: tuple[str, str], timeout: int = None) -> bool:
        """
        Checks if element exists by locator and returns a bool

        :param locator: tuple of (selector, value)
        :param timeout:  max time to wait for the WebElement before failing in seconds (Optional), default = 30

        :return: bool if element exists by locator
        """
        if timeout is None:
            timeout = self._default_timeout
        try:
            self.get_elem_by_locator(locator=locator, timeout=timeout)
        except TimeoutException:
            return False
        return True

    def check_if_clickable_elem_exists_by_locator(self, locator: tuple[str, str], timeout: int = None) -> bool:
        """
        Checks if clickable element exists by locator and returns a bool

        :param locator: tuple of (selector, value)
        :param timeout: max time to wait for the WebElement before failing in seconds (Optional), default = 30

        :return: bool if element exists and is clickable by locator
        """
        if timeout is None:
            timeout = self._default_timeout
        try:
            self.get_elem_by_locator(locator=locator, timeout=timeout)
        except TimeoutException:
            return False
        return True
