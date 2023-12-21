# Generated by Selenium IDE
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

class TestIniciarvenda():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_iniciarvenda(self):
    self.driver.get("http://localhost:8080/RevendaVeiculosSpringMVC/veiculos")
    self.driver.set_window_size(888, 696)
    self.driver.find_element(By.LINK_TEXT, "TRANSAÇÕES").click()
    self.driver.find_element(By.LINK_TEXT, "Iniciar venda").click()
    self.driver.find_element(By.ID, "placa").click()
    self.driver.find_element(By.ID, "placa").send_keys("MNT1020")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
    self.driver.find_element(By.ID, "txtData").click()
    self.driver.find_element(By.CSS_SELECTOR, "tr:nth-child(4) > .day:nth-child(6)").click()
    self.driver.find_element(By.ID, "txtDesconto").click()
    self.driver.find_element(By.ID, "txtDesconto").send_keys("50")
    self.driver.find_element(By.ID, "txtObs").click()
    self.driver.find_element(By.ID, "txtObs").send_keys("desconto de black friday")
    self.driver.find_element(By.ID, "formaPgt").click()
    self.driver.find_element(By.ID, "formaPgt").click()
    self.driver.find_element(By.ID, "quantia").click()
    self.driver.find_element(By.ID, "quantia").send_keys("60000")
    self.driver.find_element(By.ID, "btnAddPgt").click()
    element = self.driver.find_element(By.ID, "btnAddPgt")
    actions = ActionChains(self.driver)
    actions.move_to_element(element).perform()
    self.driver.find_element(By.CSS_SELECTOR, ".text-right > .btn").click()
    self.driver.find_element(By.ID, "placa").click()
    self.driver.find_element(By.LINK_TEXT, "Continuar").click()
    self.driver.find_element(By.LINK_TEXT, "Salvar venda").click()
    self.driver.find_element(By.CSS_SELECTOR, ".close > span").click()
  