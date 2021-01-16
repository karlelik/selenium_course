#!/usr/bin/env python
# coding: utf-8

# In[4]:


from selenium import webdriver
import time
import math

link = "http://suninjuly.github.io/alert_accept.html"
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome('\Games\chromedriver.exe')
    browser.get(link)

    button1 = browser.find_element_by_css_selector("button.btn")
    button1.click()
    
    alert = browser.switch_to.alert
    alert.accept()
    
    x_element = browser.find_element_by_id('input_value')
    x = x_element.text
    y = calc(x)

 
    input1 = browser.find_element_by_css_selector("div.form-group #answer")
    input1.send_keys(y)
    
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

finally:
    time.sleep(5)
    browser.quit()


# In[ ]:




