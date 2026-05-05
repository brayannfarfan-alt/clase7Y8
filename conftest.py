import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager 
from selenium.webdriver.chrome.service import Service 

# fixtures
@pytest.fixture
def chrome_driver():
    service = Service(ChromeDriverManager().install()) # v.151
    driver = webdriver.Chrome(service=service)

    yield driver

    driver.quit()

