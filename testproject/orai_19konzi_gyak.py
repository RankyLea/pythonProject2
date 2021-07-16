import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

opt = Options()

opt.headless = False
driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=opt)

driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/hackernews/index.html")
try:
    links = WebDriverWait(driver, 30).until(
        EC.visibility_of_all_elements_located((By.XPATH, '//div[@class="story"]/div/a')))
except TimeoutException:
    print('Időtúllépés')

link_file = open('linkek.txt', 'w')
for link in links:
    link_file.write(f'{link.text}\n')
link_file.close()

driver.close()

# Gyűjtsük ki a 15 leggyakrabban előforduló szót a linkek címéből
# Ld. Shakespeare szonettek leggyakoribb szavainak kigyüjtése videó/pyfile