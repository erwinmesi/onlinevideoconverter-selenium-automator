from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from chrome_downloads import ChromeDownloads

class OnlineVideoConverterDownloader:
    converter_url = 'https://www.onlinevideoconverter.com/youtube-converter'

    def __init__(self):
        options = Options()
        options.add_argument("--disable-notifications")
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=options)
        self.browser.maximize_window()

    def download(self, link):
        self.browser.get(self.converter_url)

        self.browser.find_element(By.ID, 'texturl').send_keys(link)

        self.browser.find_element(By.CLASS_NAME, 'start-button').click()

        try:
            WebDriverWait(self.browser, 60).until(EC.presence_of_element_located((By.ID, 'downloadq')))
        finally:
            ChromeDownloads().wait_for_all_to_finish()
            self.browser.find_element(By.ID, 'downloadq').click()
            
            self.browser.implicitly_wait(3)
            self.close_ad_page()
        
    def close_ad_page(self):
        current_window = self.browser.current_window_handle
        try:
            new_window = [window for window in self.browser.window_handles if window != current_window][0]
            self.browser.switch_to.window(new_window) # Switch to new window/tab
            self.browser.close() # Close new window/tab
            self.browser.switch_to.window(current_window) # Switch to initial window/tab
        except IndexError:
            pass

    def quit(self):
        self.browser.quit()