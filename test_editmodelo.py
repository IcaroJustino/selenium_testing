import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestEditmodelo():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_editmodelo(self):
    self.driver.get("http://localhost:8080/RevendaVeiculosSpringMVC/modelos")
    self.driver.set_window_size(888, 696)
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(1) .glyphicon-edit").click()
    self.driver.find_element(By.CSS_SELECTOR, "body").click()
    self.driver.find_element(By.ID, "descricao").send_keys("Corsa_modelo_diferente")
    self.driver.find_element(By.ID, "fabricante.id").click()
    dropdown = self.driver.find_element(By.ID, "fabricante.id")
    dropdown.find_element(By.XPATH, "//option[. = 'FORD']").click()
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.CSS_SELECTOR, ".close > span").click()
  
