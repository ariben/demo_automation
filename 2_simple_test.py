import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.segurosimple.com/")
element = driver.find_element_by_id("Marca")
modelo = "Daewoo"
#modelo = "Alfa-Romeo"
element.send_keys(modelo)
element = driver.find_element_by_id("EmailCotizacion")
element.send_keys("mimail@test.com")
element = driver.find_element_by_id("Modelo")
assert len(element.text) > len(":: Seleccione ::") , "Los modelos de la marca %s no fueron cargados" % modelo
# Mala practica fines visuales
time.sleep(3)
driver.quit()
