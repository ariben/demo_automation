import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

class SeguroTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://www.segurosimple.com/")


    def test_modelo_por_marca(self):
        element = self.driver.find_element_by_id("Marca")
        modelo = "Daewoo"
        #modelo = "Alfa-Romeo"
        element.send_keys(modelo)
        element = self.driver.find_element_by_id("EmailCotizacion")
        element.send_keys("mimail@test.com")
        element = self.driver.find_element_by_id("Modelo")
        assert len(element.text) > len(":: Seleccione ::") , "Los modelos de la marca %s no fueron cargados" % modelo
        # Mala practica fines visuales
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
