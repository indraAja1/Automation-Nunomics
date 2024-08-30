import unittest
import sys
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Import open app
sys.path.insert(0, r'D:\\ngetesappium\\Open App')
from open_app_daftar import open_app

# Variable ID
field_nama = 'com.nunomics.app.debug:id/etFullName'
field_username = 'com.nunomics.app.debug:id/etUsername'
field_email = 'com.nunomics.app.debug:id/etEmail'
field_nohp = 'com.nunomics.app.debug:id/etNomorTelepon'
field_pass = 'com.nunomics.app.debug:id/etPassword'
field_konfirmasi = 'com.nunomics.app.debug:id/etConfirmPassword'
checkbox = 'com.nunomics.app.debug:id/cbAgreement2'
btn_daftar = 'com.nunomics.app.debug:id/btnApply'
toast_error = '//android.widget.TextView[@resource-id="com.nunomics.app.debug:id/message"]'

# Variable input
nama_lengkap = "SiapaHayotesting"
input_username = "Testing79"
input_email = "ngetesappium@gmail.com"
input_nohp = "08950502708834473532"
input_password = "Testing1"
input_konfirmasi_password = "Testing1"

class TestSignupLongPhoneNumber(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = open_app()
        if not self.driver:
            raise Exception("Driver tidak berhasil diinisialisasi dari open_app()")
        
    def test_signup_with_long_phone_number(self):
        try:
            # Isi formulir pendaftaran
            WebDriverWait(self.driver, 7).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_nama))
            ).send_keys(nama_lengkap)
            
            WebDriverWait(self.driver, 7).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_username))
            ).send_keys(input_username)
            
            WebDriverWait(self.driver, 7).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_email))
            ).send_keys(input_email)
            
            WebDriverWait(self.driver, 7).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_nohp))
            ).send_keys(input_nohp)
            
            WebDriverWait(self.driver, 7).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_pass))
            ).send_keys(input_password)
            
            WebDriverWait(self.driver, 7).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_konfirmasi))
            ).send_keys(input_konfirmasi_password)
            
            # Klik pada checkbox kebijakan
            cb_kebijakan = WebDriverWait(self.driver, 8).until(
                EC.element_to_be_clickable((AppiumBy.ID, checkbox))
            )
            cb_kebijakan.click()
            
            # Klik tombol daftar
            daftar = WebDriverWait(self.driver, 8).until(
                EC.element_to_be_clickable((AppiumBy.ID, btn_daftar))
            )
            daftar.click()
            
            # Tunggu dan periksa jika ada pesan error
            error_message = WebDriverWait(self.driver, 7).until(
                EC.presence_of_element_located((AppiumBy.XPATH, toast_error))
            )
            if error_message:
                toast_text = error_message.text  # Mendapatkan teks dari elemen toast
                print(f"Negative Test Case sukses: Pesan error muncul dengan benar - '{toast_text}'")
            else:
                print("Negative Test Case gagal: Pesan error tidak muncul.")
        
        except Exception as e:
            print("Pesan error tidak terdeteksi atau tidak muncul dalam waktu yang ditentukan.")
            print(f"Test gagal: {e}")

    def tearDown(self) -> None:
        if hasattr(self, 'driver') and self.driver:
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
