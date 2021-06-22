from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


class ChromeAuto:
    def __init__(self):
        self.driver_path = 'D:\/Projects\/flasks\/api_era\/app\/resources\/chromedriver.exe'
        self.options = webdriver.ChromeOptions()
        # self.options.add_argument()
        self.chrome = webdriver.Chrome(
            self.driver_path,
            options=self.options
        )
    
    def site_url(self, site):
        self.chrome.get(site)

    def default(self):
        x_1 = self.chrome.find_element_by_css_selector("button[data-reactid='63']")
        x_1.click()
        sleep(5)
        find_stock = self.chrome.find_element_by_css_selector('button[data-reactid="133"]')
        find_stock.click()
        sleep(7)
        result_table = self.chrome.find_element_by_css_selector('table[class="W(100%)"]')
        rows = result_table.find_elements(By.TAG_NAME, 'tr')
        result = {}
        for row in rows:
            cont = 0
            cols = row.find_elements(By.TAG_NAME, "td")
            keys = ['symbol', 'name', 'price']
            values = []
            for col in cols:
                cont += 1
                values.append(col.text)
                if cont > 3:
                    break
            res = dict(zip(keys, values))
            if len(values) > 1:
                key = values[0]
                result.update({key: res})
        sleep(5)
        return result

    def search(self, region):
        remove = self.chrome.find_element_by_css_selector("button[data-reactid='33']")
        remove.click()
        self.chrome.find_element_by_css_selector('li[data-reactid="37"]').click()
        self.chrome.find_element_by_css_selector('input[placeholder="Find filters"]').send_keys(region)
        xs = self.chrome.find_elements_by_css_selector('li[style="width: 50%;"]')
        sleep(4)
        for x in xs:
            try:
                x.find_element(By.TAG_NAME, 'label').click()
            except:
                pass
        sleep(5)
        self.chrome.find_element_by_css_selector('button[data-reactid="133"]').click()
        sleep(5)
        result_table = self.chrome.find_element_by_css_selector('table[class="W(100%)"]')
        rows = result_table.find_elements(By.TAG_NAME, 'tr')
        result = {}
        for row in rows:
            cont = 0
            cols = row.find_elements(By.TAG_NAME, "td")
            keys = ['symbol', 'name', 'price']
            values = []
            for col in cols:
                cont += 1
                values.append(col.text)
                if cont > 3:
                    break
            res = dict(zip(keys, values))
            if len(values) > 1:
                key = values[0]
                result.update({key: res})
        sleep(5)
        return result

    def quit(self):
        self.chrome.quit()

    