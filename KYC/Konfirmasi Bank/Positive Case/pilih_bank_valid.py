import unittest
import sys
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
  
# Import touch actions untuk swipe
sys.path.insert(0, r'D:\\ngetesappium\\KYC\\Konfirmasi Bank\\S&K')
from touch import perform_swipe

# Tambahkan jalur ke sys.path
sys.path.insert(0, r'D:\\ngetesappium\\Open App')
from open_app_kyc import AksesLogin

# Variable ID/XPATH
btn_kyc = 'com.nunomics.app.debug:id/btnInfo'
field_promotor = 'com.nunomics.app.debug:id/etReferral'
btn_mulai = 'com.nunomics.app.debug:id/btnStart'
toast_message = '//android.widget.TextView[@resource-id="com.nunomics.app.debug:id/tvBottom"]'
agi = 'com.nunomics.app.debug:id/rbAgi'
agreement1 = 'com.nunomics.app.debug:id/cbAgreement1'
agreement2 = 'com.nunomics.app.debug:id/cbAgreement2'
agreement3 = 'com.nunomics.app.debug:id/cbAgreement3'
setuju = 'com.nunomics.app.debug:id/btnAgree'
lanjut = 'com.nunomics.app.debug:id/btnNext'

# Variable Input
input_promotor = '0TPUZDY7'

class TestComfirmBank(unittest.TestCase):
    def setUp(self):
        # Inisialisasi instance dari OpenNunomics
        self.login_test = AksesLogin()
        self.login_test.test_login_succes()  # Lakukan login sebelum melanjutkan
        # Ambil driver dari login_test
        self.driver = self.login_test.driver
            
    def test_corfirm_bank(self):
        try:
            kyc = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((AppiumBy.ID, btn_kyc))
            )
            kyc.click()
            
            input_code = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_promotor))
            )
            input_code.send_keys(input_promotor)
            
            mulai = WebDriverWait(self.driver, 8).until(
                EC.element_to_be_clickable((AppiumBy.ID, btn_mulai))
            )
            
            # Cek dan ambil pesan toast
            message = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, toast_message))
            )
            if message:
                toast_text = message.text  # Mendapatkan teks dari elemen toast
                print(f"Pesan valid muncul dengan benar - '{toast_text}'")
            else:
                print("Pesan valid tidak muncul.")

            # Klik button mulai
            mulai.click()
            
            WebDriverWait(self.driver, 8).until(
                EC.element_to_be_clickable((AppiumBy.ID, agi))   
            ).click()
            
            # Centang agreement 1
            WebDriverWait(self.driver, 8).until(
                EC.element_to_be_clickable((AppiumBy.ID, agreement1))   
            ).click()
            
            # Scroll ke bawah
            perform_swipe(self.driver, 581, 2599, 623, 403)
            
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ID, setuju))   
            ).click()
            
            # Centang agreement 2
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ID, agreement2))   
            ).click()
                        
            # Scroll ke bawah lagi
            perform_swipe(self.driver, 581, 2599, 623, 403) # Scroll pertama
            perform_swipe(self.driver, 581, 2599, 1023, 703) # Scroll kedua
            
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ID, setuju))   
            ).click()
            
            # Centang agreement 3
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ID, agreement3))   
            ).click()
            
        except Exception as e:
            print(f"Terjadi kesalahan saat mengakses halaman Pilih Bank: {e}")

    def tearDown(self) -> None:
        self.login_test.tearDown()

if __name__ == "__main__":
    unittest.main()
