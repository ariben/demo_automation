'''
Ejemplo clasico: abrir browser, buscar elemento, ingresar cadena de texto
'''

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait


driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.segurosimple.com/")
element = driver.find_element_by_id("Marca")
element.send_keys("Alfa-Romeo")
element = driver.find_element_by_id("EmailCotizacion")
element.send_keys("emaildeprueba@test.com")
element = driver.find_element_by_id("Modelo")
# Mala practica fines visuales
time.sleep(10)
driver.quit()
