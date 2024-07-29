from xdriver.src.webdriver import Driver
import pytest


@pytest.fixture(scope='function')
def chromedriver() -> Driver:
    """
    Starts the chromedriver before test and closes it afterward
    """
    driver = Driver(webdriver_type="chromedriver",
                    options=['--headless',
                             '--window-size=1920,1080',
                             '--no-sandbox',
                             '--disable-dev-shm-usage'],
                    default_timeout=30)
    yield driver
    driver.quit()


@pytest.fixture(scope='function')
def geckodriver() -> Driver:
    """
    Starts the Driver before test and closes it afterward
    """
    driver = Driver(webdriver_type="geckodriver",
                    options=['--headless',
                             '--width=1920',
                             '--height=1080'],
                    default_timeout=30)
    yield driver
    driver.quit()
