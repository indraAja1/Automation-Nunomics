import unittest
import sys
import random
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Case : Daftar dengan OTP tidak valid

# import open app
sys.path.insert(0, r'D:\\ngetesappium\\Open App')
from open_app_daftar_pin import open_app_pin, options

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
toast_error = '//android.widget.TextView[@resource-id="com.nunomics.app.debug:id/message"]'

# Variable input
input_nama = "Hayosiapa"
input_username = "Testinf9"
input_email = "ngetesappiu2m@gmail.com"
input_password = "Testing1"
input_konfirmasi_password = "Testing1"
otp_code = '381034'

class TestSignupInvalidOTP(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = open_app_pin()  # Pastikan open_app() mengembalikan driver
        if not self.driver:
            raise Exception("Driver tidak berhasil diinisialisasi dari open_app()")
        
    def test_signup_with_invalid_otp(self):
        try:
            # Isi formulir pendaftaran
            WebDriverWait(self.driver, 9).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_nama))
            ).send_keys(input_nama)
            print(f"Step 3: Masukkan Nama Lengkap '{input_nama}' ke dalam field Nama Lengkap")            
 
            WebDriverWait(self.driver, 9).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_username))
            ).send_keys(input_username)
            print(f"Step 4: Masukkan Username '{input_username}' ke dalam field Username")            

            
            WebDriverWait(self.driver, 9).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_email))
            ).send_keys(input_email)
            print(f"Step 5: Masukkan Email  '{input_email}' ke dalam field Email")            

            # Membuat nomor handphone random
            start = '08'
            rest_of_number = ''.join([str(random.randint(0, 9)) for _ in range(11)])
            random_phone = start + rest_of_number

            # Masukkan nomor handphone random ke dalam field No Handphone
            WebDriverWait(self.driver, 9).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_nohp))
            ).send_keys(random_phone)
            print(f"Step 6: Masukkan No Handphone '{random_phone}' ke dalam field No Handphone")  
            
            WebDriverWait(self.driver, 9).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_pass))
            ).send_keys(input_password)
            print(f"Step 7: Masukkan Password '{input_password}' ke dalam field Password")            

            WebDriverWait(self.driver, 9).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_konfirmasi))
            ).send_keys(input_konfirmasi_password)
            print(f"Step 8: Masukkan Konfirmasi Password '{input_konfirmasi_password}' ke dalam field Konfirmasi Password")            

            cb_kebijakan = WebDriverWait(self.driver, 8).until(
                EC.element_to_be_clickable((AppiumBy.ID, checkbox))
            )
            cb_kebijakan.click()
            print("Step 9: Klik checkbox 'Kebijakan Privasi'")
            
            btn_daf = WebDriverWait(self.driver, 8).until(
                EC.element_to_be_clickable((AppiumBy.ID, btn_daftar))
            )
            btn_daf.click()
            print("Step 10: Klik tombol 'Daftar'")
            
            otp_field = WebDriverWait(self.driver, 8).until(
                EC.visibility_of_element_located((AppiumBy.ID, input_otp))
            )
            otp_field.send_keys(otp_code)
            print(f"Step 11: Masukan OTP tidak valid '{otp_code}' ke field OTP")
            
            # Verifikasi pesan error
            error_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.XPATH, toast_error))
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
            self.driver.terminate_app(options.app_package)
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()
