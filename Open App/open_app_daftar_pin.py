from appium import webdriver
from selenium.common.exceptions import TimeoutException
from appium.options.android import UiAutomator2Options
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Case : Open Aplikasi NUnomics ke halaman Masuk

import sys
sys.path.insert(0, r'D:\\ngetesappium\\touch')
from touch import perform_swipe, click_at_coordinates


options = UiAutomator2Options()
options.platform_name = 'Android'
options.automation_name = 'uiautomator2'
options.udid = 'IFLZFAJJHASOEE95'
options.device_name = 'POCO X6 Pro 5G'
options.app_package = 'com.nunomics.app.debug'
options.app_activity = 'com.nunomics.app.ui.SplashActivity'
options.no_reset = True

appium_server_url = 'http://127.0.0.1:4723/wd/hub'

# Variable ID/checkbox/btn/XPATH
btn_daftar = 'com.nunomics.app.debug:id/btnDaftar'
input_pin = 'com.nunomics.app.debug:id/firstPinView'
profil = 'com.nunomics.app.debug:id/profile'
keluar = 'com.nunomics.app.debug:id/llLogout'
keluar_true = 'com.nunomics.app.debug:id/positiveBtn'

def open_app_pin():
    try:
        driver = webdriver.Remote(appium_server_url, options=options)

        # Close App
        driver.terminate_app(options.app_package)
        
        # Open App
        driver.activate_app(options.app_package)

        # Step A Ketika aplikasi tidak ada akun yang tersangkut
        WebDriverWait(driver, 8).until(
            EC.element_to_be_clickable((AppiumBy.ID, btn_daftar))
        ).click()
        print("Step 1: Open App Nunomics")
        print("Step 2: Klik tombol 'Masuk'")
        return driver
    except TimeoutException:
        # Jika tombol 'Next' tidak ditemukan, maka input PIN
        # Step B
        print("Step 1: Open App Nunomics")

        pin_element = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.ID, input_pin))
        )
        pin_element.send_keys("111111")  # Ganti dengan PIN yang diinginkan
        
        # # Klik utuk notif dialog
        # time.sleep(5)
        # click_at_coordinates(driver, 1100, 688)
            

        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.ID, profil))
        ).click()
        
        perform_swipe(driver, 468, 1311, 487, 548) # Scroll

        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.ID, keluar))
        ).click()
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.ID, keluar_true))
        ).click()
        
        WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.ID, btn_daftar))
        ).click()
        print("Step 2: Klik tombol 'Masuk'")
        
        return driver  # Kembalikan driver

    except Exception as e:
        print(f"Terjadi kesalahan saat inisialisasi: {e}")
        return None
    
if __name__ == "__main__":
    open_app_pin()
