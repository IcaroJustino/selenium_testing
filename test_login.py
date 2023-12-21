
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

class TestLogin():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_login(self):
    self.driver.get("http://localhost:8080/RevendaVeiculosSpringMVC/login")
    self.driver.set_window_size(888, 696)
    self.driver.find_element(By.CSS_SELECTOR, ".close").click()
    self.driver.find_element(By.ID, "login").click()
    self.driver.find_element(By.ID, "login").send_keys("gerente")
    self.driver.find_element(By.ID, "senha").click()
    self.driver.find_element(By.ID, "senha").send_keys("senha")
    self.driver.find_element(By.CSS_SELECTOR, ".btn").click()
  
