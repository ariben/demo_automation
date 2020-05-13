import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

'''
El siguiente script requiere tener una cuenta en testingbot.com
Una vez creada copiar tu id de : http://testingbot.com/support/getting-started/python.html
'''


class SeguroTest(unittest.TestCase):
    def setUp(self):
        capabilities = { 'platform': 'Windows', 'browserName': 'internet explorer', 'version': '9' }
        self.driver = webdriver.Remote(
    		    command_executor='http://id:secret@hub.testingbot.com/wd/hub',
    			desired_capabilities=capabilities)
        self.driver.maximize_window()
        self.driver.get("http://www.segurosimple.com/")


    def test_modelo_por_marca(self):
        #modelo = "Daewoo"
        test_data = {"marca": "Alfa-Romeo", "modelo": "147 1.6 TI",
                    "mail":"mimial@yahoo.com", "annio_fabricacion":"2008",
                    "fono":"997261789", "edad_usuario": "36"}

        element = self.driver.find_element_by_id("Marca")
        element.send_keys(test_data["marca"])

        element = self.driver.find_element_by_id("annio_fabricacion")
        element.send_keys(test_data["annio_fabricacion"])

        element = self.driver.find_element_by_id("Modelo")
        assert len(element.text) > len(":: Seleccione ::"),\
         "Los modelos de la marca %s no fueron cargados" % test_data["marca"]
        element.send_keys(test_data["modelo"])

        self.driver.find_element_by_id("edadUsuario").send_keys(test_data["edad_usuario"])
        self.driver.find_element_by_id("TelefonoCotizacion").send_keys(test_data["fono"])
        self.driver.find_element_by_id("EmailCotizacion").send_keys(test_data["mail"])
        self.driver.find_element_by_id("btnComparar").click()
        # Mala practica fines visuales
        time.sleep(5)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
