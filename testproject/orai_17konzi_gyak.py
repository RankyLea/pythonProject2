from selenium import  webdriver
from selenium.webdriver.chrome.options import options
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager)().install()

options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
driver.get("https://witty-hill-0acfceb03.azurestaticapps.net/twitter.html")

testdata = 'This is the first tweet'
post = driver.find_element_by_xpath()
post.send_keys(testdata)

button = driver.find_element_by_xpath()
assert (testdata == driver.find_element_by_class("text-grey-700")>[0])

heart_button = driver.find_element_by_xpath(/html/body/div[1]/div[2]/div/div[1]/ul/div[1]/li/div/div[2]/div[4]/div[3]/div[1]/svg[1])

# TC0 bejelentkezett állapot ellenőrzése (saját felhasználó avatár megjelenik)
# TC1 bejegyzéshez kép csatolása az ikonnal
# TC2 karakterszámláló tesztelése: 0 kar, 1 kar, 140 kar, 141 karakter
# TC3 Tweet gomb engedélyezettsége 0 kar -> 1 kar, 1 kar -> 0 kar
# TC4 új Tweet megjelenése Tweet gomb megnyomása után
# TC5 válasz (re-tweet) funkció vizsgálata (jelenleg nem működik)
# TC6 chat gomb (jelenleg nem működik)
# TC7 jelenleg követett felhasználók ellenörzése
# TC8 follow/unfollow gomb felirata követett és nem követett felhasználóknál
# TC9 új felhasználó követése Follow gomb
# TC10 követett felhasználó követésének megszüntetése unfollow
# TC11 felhsználónév korrekt megjelenítése (tweetek, követett és nem követett felhasználók listája)
# TC12 idegen felhasználó tweetjeinek megtekintése (jelenleg nem működik)
# TC13 saját profil szerkesztes
# TC14 saját account settings
# TC15 kijelentkezes