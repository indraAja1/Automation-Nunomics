import unittest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def run_test():
    # Tambahkan logika pengujian di sini atau panggil test class jika menggunakan unittest
    unittest.TextTestRunner().run(unittest.TestLoader().loadTestsFromTestCase(TestComfirmBank))

class TestComfirmBank(unittest.TestCase):
    def setUp(self):
        # Inisialisasi instance dari OpenNunomics
        from open_app_kyc import AksesLogin # type: ignore
        self.login_test = AksesLogin()
        self.login_test.test_login_succes()  # Lakukan login sebelum melanjutkan
        self.driver = self.login_test.driver

    def test_code_referral_symbol(self):
        try:
            kyc = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ID, 'com.nunomics.app.debug:id/btnInfo'))
            )
            kyc.click()
            print("Step 6: Klik tombol 'Lakukan Registrasi KYC'")
            
            input_code = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((AppiumBy.ID, 'com.nunomics.app.debug:id/etReferral'))
            )
            input_code.send_keys('0TP ZDY7')
            print("Step 7: Masukkan Kode Promotor dengan spasi '0TP ZDY7 ke field Kode Promotor'")
            
            mulai = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ID, 'com.nunomics.app.debug:id/btnStart'))
            )
            print("Step 8: Klik tombol 'Mulai'")

            message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.nunomics.app.debug:id/tvBottom"]'))
            )
            if message:
                toast_text = message.text
                print(f"Negative Test Case sukses: Pesan error muncul dengan benar - '{toast_text}'")
            else:
                print("Negative Test Case gagal: Pesan error tidak muncul.")
            mulai.click()
        except Exception as e:
            print(f"Terjadi kesalahan saat mengakses halaman Kode Promo: {e}")

    def tearDown(self):
        self.login_test.tearDown()
