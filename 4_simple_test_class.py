'''
Convirtiendo script en clases de prueba

Setup: será lo primero que se ejecute, usualmente contiene la inicializacion
del browser + url de la webapp

tearDown: lo que siempre se ejecutara para terminar el script(cerrar el browser)
'''

import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class SeguroTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://www.segurosimple.com/")


    def test_modelo_por_marca(self):
        #modelo = "Daewoo"
        test_data = {"marca": "Alfa-Romeo", "modelo": "147 1.6 TI",
                    "mail":"mimial@yahoo.com", "annio_fabricacion":"2008",
                    "fono":"997261789", "edad_usuario": "36"}

        element = self.driver.find_element_by_id("Marca")
        element.send_keys(test_data["marca"])

        element = self.driver.find_element_by_id("Año")
        element.send_keys(test_data["annio_fabricacion"])

        element = self.driver.find_element_by_id("Modelo")
        assert len(element.text) > len(":: Seleccione ::"),\
         "Los modelos de la marca %s no fueron cargados" % test_data["marca"]
        element.send_keys(test_data["modelo"])

        self.driver.find_element_by_id("edadUsuario").send_keys(test_data["edad_usuario"])
        self.driver.find_element_by_id("TelefonoCotizacion").send_keys(test_data["fono"])
        self.driver.find_element_by_id("EmailCotizacion").send_keys(test_data["mail"])
        self.driver.find_element_by_id("btnComparar").click()
        try:
            btn_descarga = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "btDescargar")))
        except TimeoutException:
            print ("TimeoutException")
        self.assertTrue (btn_descarga, "La pagina de descarga no fue mostrada")


    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
