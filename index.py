from time import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyautogui
import time


options = Options()
options.add_argument(
    "user-data-dir=C:\\Users\\matheus\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2")
driver = webdriver.Chrome(options=options)

contador = 1
paginacao = 70

driver.get(f"https://www.whatstube.com.br/categoria/videos/page/{paginacao}/")
time.sleep(1)

while contador < 10:
    try:
        driver.find_element_by_xpath(
            f'//*[@id="sb-site"]/div/div[2]/div[1]/div[2]/div[{contador}]/article/div[2]/h3/a').click()
        time.sleep(2)
        driver.find_element_by_xpath(
            '//*[@id="sb-site"]/div/div[2]/div[1]/article/table/tbody/tr/td[3]/span/a').click()
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="baixar-link"]').click()
        time.sleep(4)
        pyautogui.click(x=695, y=534)
        time.sleep(1)
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("tab")
        pyautogui.press("enter")
        pyautogui.press("up")
        pyautogui.press("up")
        pyautogui.press("enter")
        time.sleep(1)
        pyautogui.click(x=626, y=43)

        driver.get(
            f"https://www.whatstube.com.br/categoria/videos/page/{paginacao}")
        time.sleep(2)

        if contador == 9:
            paginacao = paginacao+1
            contador = 2
        contador = contador+1

        print(f"PAGINA {paginacao} VIDEO {contador}")

    except:
        print(f"VIDEO {contador} NÃO ENCONTRADO NA PAGINA {paginacao}")

        if contador == 9:
            paginacao = paginacao+1
            contador = 2
        contador = contador+1
print("Saiu!")
