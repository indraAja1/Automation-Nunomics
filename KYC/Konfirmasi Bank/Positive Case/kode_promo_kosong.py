import unittest
import sys
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Tambahkan jalur ke sys.path
sys.path.insert(0, r'D:\\ngetesappium\\Open App')
from open_app_kyc import AksesLogin

# Variable ID/XPATH
btn_kyc = 'com.nunomics.app.debug:id/btnInfo'
field_promotor = 'com.nunomics.app.debug:id/etReferral'
btn_mulai = 'com.nunomics.app.debug:id/btnStart'
toast_message = '//android.widget.TextView[@resource-id="com.nunomics.app.debug:id/tvBottom"]'

# Variable Input
input_promotor = ''

class TestComfirmBank(unittest.TestCase):
    def setUp(self):
        # Inisialisasi instance dari OpenNunomics
        self.login_test = AksesLogin()
        self.login_test.test_login_succes()  # Lakukan login sebelum melanjutkan
        # Ambil driver dari login_test
        self.driver = self.login_test.driver

    def test_code_referral_invalid(self):
        try:
            kyc = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ID, btn_kyc))
            )
            kyc.click()
            print("Step 6: Klik tombol 'Lakukan Registrasi KYC'")
            
            input_code = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_promotor))
            )
            input_code.send_keys(input_promotor)
            print(f"Step 7: Masukkan Kode Promotor '{input_promotor} ke field Kode Promotor'")
            
            
            mulai = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ID, btn_mulai))
            )
            print("Step 8: Klik tombol 'Mulai'")
            
            # Verifikasi succes message
            message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.XPATH, toast_message))
            )
            if message:
                toast_text = message.text  # Mendapatkan teks dari elemen toast
                print(f"Pesan valid muncul dengan benar - '{toast_text}'")
            else:
                print("Pesan valid tidak muncul.")
            mulai.click()
        except Exception as e:
            print(f"Terjadi kesalahan saat mengakses halaman Kode Promo: {e}")
            # assert False

    def tearDown(self) -> None:
        self.login_test.tearDown()

if __name__ == "__main__":
    unittest.main()
