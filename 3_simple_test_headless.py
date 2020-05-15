from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import os


chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.binary_location = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome'

driver = webdriver.Chrome(executable_path='/usr/local/bin/chromedriver', \
options=chrome_options)

driver.get("http://www.segurosimple.com/")
element = driver.find_element_by_id("Marca")
#modelo = "Daewoo"
modelo = "Alfa-Romeo"
element.send_keys(modelo)

annio_fabricacion = "2008"
element = driver.find_element_by_id("Año")
element.send_keys(annio_fabricacion)


element = driver.find_element_by_id("Modelo")
assert len(element.text) > len(":: Seleccione ::"), \
        "Los modelos de la marca %s no fueron cargados" % modelo
modelo = "147 1.6 TI"
element.send_keys(modelo)

driver.find_element_by_id("TelefonoCotizacion").send_keys("997261789")

element = driver.find_element_by_id("EmailCotizacion")
element.send_keys("mimail@yahoo.com")

element = driver.find_element_by_id("edadUsuario")
element.send_keys("30")

print(os.getcwd())
filepath = os.getcwd()+'/Screenshots/headless.png'
driver.save_screenshot(filepath)


driver.find_element_by_id("btnComparar").click()



# Mala practica fines visuales
time.sleep(3)
driver.quit()
