import unittest
import sys
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from appium.webdriver.common.touch_action import TouchAction

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
setuju_argement1 = 'com.nunomics.app.debug:id/btnAgree'

# Variable Input
input_promotor = '0TPUZDY7'

class TestComfirmBank(unittest.TestCase):
    def setUp(self):
        # Inisialisasi instance dari OpenNunomics
        self.login_test = AksesLogin()
        self.login_test.test_login_succes()  # Lakukan login sebelum melanjutkan
        # Ambil driver dari login_test
        self.driver = self.login_test.driver

    def test_code_referral_invalid(self):
        try:
            kyc = WebDriverWait(self.driver, 7).until(
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
            mulai.click()

            # Periksa pesan toast
            try:
                message = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((AppiumBy.XPATH, toast_message))
                )
                toast_text = message.text  # Mendapatkan teks dari elemen toast
                print(f"Negative Test Case sukses: Pesan error muncul dengan benar - '{toast_text}'")
            except Exception as e:
                print("Negative Test Case gagal: Pesan error tidak muncul.")
            
            # Klik button mulai jika perlu
            WebDriverWait(self.driver, 8).until(
                EC.element_to_be_clickable((AppiumBy.ID, agi))
            ).click()
            
            WebDriverWait(self.driver, 8).until(
                EC.element_to_be_clickable((AppiumBy.ID, agreement1))
            ).click()
        except Exception as e:
            print(f"Terjadi kesalahan saat mengakses halaman utama: {e}")
            
    def scroll_to_coordinates(self, x, y):
        action = TouchAction(self.driver)
        action.press(x=x, y=y).move_to(x=x, y=y-200).release().perform()

    def tearDown(self) -> None:
        self.login_test.tearDown()

if __name__ == "__main__":
    unittest.main()
