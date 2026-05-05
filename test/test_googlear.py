

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions  as EC

#driver.implicitly_wait(10) # => ejecxutá a encontrar todo lo  que esta abajo si lo encontrás antes segui tu camino. 

def test_busqueda_talento_tech( chrome_driver ):
    wait = WebDriverWait(chrome_driver,4)

    chrome_driver.get("https://duckduckgo.com/") 

    try:
        input_google = wait.until(
        EC.presence_of_element_located((By.NAME , "qs"))
        )

        input_google.send_keys("talento tech")
        input_google.send_keys(Keys.RETURN)
    except Exception as e:
        print(f"ERROR: No se econtró selector. {e}")