import time
import unittest
from openapp import open_app
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import sys
sys.path.insert(0, r'D:\\ngetesappium\\Get otp')
from otp_handler import get_otp_with_timeout

# Variable ID
field_nama = 'com.nunomics.app.debug:id/etFullName'
field_username = 'com.nunomics.app.debug:id/etUsername'
field_email = 'com.nunomics.app.debug:id/etEmail'
field_nohp = 'com.nunomics.app.debug:id/etNomorTelepon'
field_pass = 'com.nunomics.app.debug:id/etPassword'
field_konfirmasi = 'com.nunomics.app.debug:id/etConfirmPassword'
checkbox = 'com.nunomics.app.debug:id/cbAgreement2'
btn_daftar = 'com.nunomics.app.debug:id/btnApply'
input_otp = 'com.nunomics.app.debug:id/firstPinView'
btn_ok = 'com.nunomics.app.debug:id/btnOk'

# Variable input
nama_lengkap = "SiapaHayotesting"
input_username = "Testing79"
input_email = "ngetesappium@gmail.com"
input_nohp = "082137006458"
input_password = "Testing1"
input_konfirmasi_password = "Testing1"

class Daftar(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = open_app()  # Pastikan open_app() mengembalikan driver
        if not self.driver:
            raise Exception("Driver tidak berhasil diinisialisasi dari open_app()")
        
    def test_daftar(self):
        try:
            # Isi formulir pendaftaran
            WebDriverWait(self.driver, 1).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_nama))
            ).send_keys(nama_lengkap)
            
            WebDriverWait(self.driver, 1).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_username))
            ).send_keys(input_username)
            
            WebDriverWait(self.driver, 1).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_email))
            ).send_keys(input_email)
            
            WebDriverWait(self.driver, 1).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_nohp))
            ).send_keys(input_nohp)
            
            WebDriverWait(self.driver, 1).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_pass))
            ).send_keys(input_password)
            
            WebDriverWait(self.driver, 1).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_konfirmasi))
            ).send_keys(input_konfirmasi_password)
            
            cb_kebijakan = WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable((AppiumBy.ID, checkbox))
            )
            cb_kebijakan.click()
            
            daftar = WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable((AppiumBy.ID, btn_daftar))
            )
            daftar.click()

            # Tunggu OTP dengan batas waktu yang ditentukan
            print("Menunggu OTP...")
            otp_code = get_otp_with_timeout(timeout=120, poll_interval=10)
            if otp_code:
                otp_field = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((AppiumBy.ID, input_otp))
                )
                otp_field.send_keys(otp_code)
                print(f"OTP '{otp_code}' berhasil dimasukkan")
            else:
                print("Gagal mendapatkan OTP dari SMS dalam batas waktu yang ditentukan")
                
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((AppiumBy.ID, btn_ok))
            ).click()

        except Exception as e:
            print(f"Test gagal: {e}")
          
if __name__ == "__main__":
    unittest.main()
