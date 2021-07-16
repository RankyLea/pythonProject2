from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())

driver.get(https: // www.met.hu /)

field = driver.find_elements_by_id("no_such_element")
print("Such element can not be found")

driver.close()
