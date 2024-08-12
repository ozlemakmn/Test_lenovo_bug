from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from constants.globalConstants import *
from time import sleep


class Test_Register():
     
  def setup_method(self):
   self.driver = webdriver.Chrome()
   self.driver.maximize_window()
   self.driver.get(BASE_URL)
   self.vars = {} 
   
  def teardown_method(self):
   self.driver.quit()
   
  def waitForElementVisible(self,locator,timeout=10):
    return WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located(locator))

  def test_services(self):
    services_button = self.waitForElementVisible((By.XPATH,Services_Button_xpath))
    services_button.click()
    
    self.driver.execute_script(ScrollTo)
    sleep(2)
    
    Cyber_Resiliency_Button=self.waitForElementVisible((By.XPATH,Cyber_Resiliency_Button_xpath))
    Cyber_Resiliency_Button.click()
    sleep(10)
    
  def test_404_error(self):
    self.driver.get("https://news.lenovo.com/pressroom/press-releases/ai-powered-solution-microsoft-simplifies-security/") #url'si verilen sayfa üzerinden title tespit etme.
    title = self.driver.title 
    print(f"Sayfa basliği: {title}")
    assert "Page not found - Lenovo StoryHub Lenovo's official site for press materials and original stories about the vision and passion behind the technology." not in title, f"Hatas tespit edildi! Başlık: {title}"
  
      

