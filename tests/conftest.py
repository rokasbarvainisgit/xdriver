from xdriver.src.webdriver import Driver
import pytest


@pytest.fixture(scope='function')
def driver() -> Driver:
    """
    Starts the Driver before test and closes it afterward
    """
    driver = Driver(webdriver_type="chromedriver",
                    options=['--headless',
                             '--window-size=1920,1080',
                             '--no-sandbox',
                             '--disable-dev-shm-usage'],
                    default_timeout=30)
    yield driver
    driver.quit()
