import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class SeguroTest(unittest.TestCase):
    def setUp(self):
        capabilities = { 'platform': 'Windows', 'browserName': 'internet explorer', 'version': '9' }
        self.driver = webdriver.Remote(
    		    command_executor='http://83aedbee7ef3b23052c76b91d0396f4f:02c030fee633d01bd7f5b983116cb8b1@hub.testingbot.com/wd/hub',
    			desired_capabilities=capabilities)
        self.driver.maximize_window()
        self.driver.get("http://www.segurosimple.com/")


    def test_modelo_por_marca(self):
        element = self.driver.find_element_by_id("Marca")
        #modelo = "Daewoo"
        modelo = "Alfa-Romeo"
        element.send_keys(modelo)
        element = self.driver.find_element_by_id("EmailCotizacion")
        element.send_keys("mimail@test.com")
        element = self.driver.find_element_by_id("Modelo")
        assert len(element.text) > len(":: Seleccione ::") , "Los modelos de la marca %s no fueron cargados" % modelo
        # Mala practica fines visuales
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


browsers = [
              { 'platform': 'Windows', 'browserName': 'firefox', 'version': '35' },
              { 'platform': 'Windows', 'browserName': 'internet explorer', 'version': '9' },
              {'platform': 'Windows', 'browserName': 'chrome', 'version': ''}

           ]



if __name__ == "__main__":
    unittest.main()
