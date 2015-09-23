import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

class SeguroTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("http://www.segurosimple.com/")


    def test_modal_te_llamamos(self):
        id_modal = "llamame"
        #codigo javascript a ejecutarse en la web app para encontrar un elemento
        js_get_modal_displayed= "return document.getElementById('%s').style.display == 'block'" % id_modal
        element = self.driver.find_element_by_id("Tellamamos")
        element.click()
        modal_es_mostrado = False
        try:
            modal_es_mostrado = WebDriverWait(self.driver, 5).until(lambda driver:
                            self.driver.execute_script(js_get_modal_displayed))
        except TimeoutException:
            print "TimeoutException"
        self.assertTrue (modal_es_mostrado, "Modal <%s> no fue mostrado" % id_modal)
        # Mala practica fines visuales
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
