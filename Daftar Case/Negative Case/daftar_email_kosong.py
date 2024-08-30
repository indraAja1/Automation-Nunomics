import unittest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

# Impor open_app dari path yang ditentukan
sys.path.insert(0, r'D:\\ngetesappium\\Open App')
from open_app_daftar import open_app

# Variable ID/XPATH
# Variable diambil dari Appium Inspector
field_nama = 'com.nunomics.app.debug:id/etFullName'
field_username = 'com.nunomics.app.debug:id/etUsername'
field_email = 'com.nunomics.app.debug:id/etEmail'
field_nohp = 'com.nunomics.app.debug:id/etNomorTelepon'
field_pass = 'com.nunomics.app.debug:id/etPassword'
field_konfirmasi = 'com.nunomics.app.debug:id/etConfirmPassword'
checkbox = 'com.nunomics.app.debug:id/cbAgreement2'
btn_login_id = 'com.nunomics.app.debug:id/btnApply'

# Variabel input
nama_lengkap = "Testes"
input_username = "Testing"
input_email = ""
input_nohp = "081234567890"
input_password = "Testing1"
input_konfirmasi_password = "Testing1"

class TestSignupEmptyEmail(unittest.TestCase):
    def setUp(self) -> None:
        # Buka aplikasi dan inisialisasi driver menggunakan open_app
        self.driver = open_app()  # Pastikan open_app() mengembalikan driver
        if not self.driver:
            raise Exception("Driver tidak berhasil diinisialisasi dari open_app()")
        
    def test_signup_with_empty_email(self):
        try:
            WebDriverWait(self.driver, 7).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_nama))
            ).send_keys(nama_lengkap)
            
            WebDriverWait(self.driver, 7).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_username))
            ).send_keys(input_username)
            
            WebDriverWait(self.driver, 7).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_nohp))
            ).send_keys(input_nohp)
            
            WebDriverWait(self.driver, 7).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_pass))
            ).send_keys(input_password)
            
            WebDriverWait(self.driver, 7).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_konfirmasi))
            ).send_keys(input_konfirmasi_password)
            
            WebDriverWait(self.driver, 8).until(
                EC.element_to_be_clickable((AppiumBy.ID, checkbox))
            ).click()
            # Temukan tombol login
            button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ID, btn_login_id))
            )
            # Cek apakah button aktif (enabled)
            if button.is_enabled():
                print("Button aktif")
                button.click()  # Klik tombol login jika aktif
            else:
                print("Button tidak aktif Karena :",)
            if not input_email:
                    print("- Field Email Kosong.")
                    
        except Exception as e:
            print(f"Terjadi kesalahan saat login: {e}")

    def tearDown(self) -> None:
        if hasattr(self, 'driver') and self.driver:
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
    
