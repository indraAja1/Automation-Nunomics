import unittest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

# Case : Daftar dengam otp resend (PROD)

# import otp / import open app
sys.path.insert(0, r'D:\\ngetesappium\\Get otp (PROD)')
from otp_hadler import get_otp_with_timeout  # type: ignore

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
resend_otp = 'com.nunomics.app.debug:id/tvResend'
input_otp = 'com.nunomics.app.debug:id/firstPinView'
otp_ok = 'com.nunomics.app.debug:id/positiveBtn'
btn_ok = 'com.nunomics.app.debug:id/btnOk'

# Variable input
input_nama = "NgetesPassword"
input_username = "Testing"
input_email = "testing.0@yahoo.com"
input_nohp = "082137006458"
input_password = "Tes3#ting$aja&"
input_konfirmasi_password = "Tes3#ting$aja&"

class TestSignupResendOTP(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = open_app_pin()  # Pastikan open_app() mengembalikan driver
        if not self.driver:
            raise Exception("Driver tidak berhasil diinisialisasi dari open_app()")
        
    def test_resend_otp_during_signup(self):
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
            print(f"Step 5: Masukkan Email '{input_email}' ke dalam field Email")            

            WebDriverWait(self.driver, 9).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_nohp))
            ).send_keys(input_nohp)
            print(f"Step 6: Masukkan No Handphone '{input_nohp}' ke dalam field No Handphone")            

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
            
            resend = WebDriverWait(self.driver, 35).until(
                EC.element_to_be_clickable((AppiumBy.ID, resend_otp))
            )
            print("Step 11: Menunggu button 'Resend OTP' dalam 30 detik")            
            resend.click()
            
            oke_otp = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ID, otp_ok))
            )
            oke_otp.click()
            print("Step 12: Klik button 'OK' pada pesan pop up")            
            
            # Tunggu OTP dengan batas waktu yang ditentukan
            otp_code = get_otp_with_timeout(timeout=170, poll_interval=18)
            if otp_code:
                otp_field = WebDriverWait(self.driver, 10).until(
                    EC.presence_of_element_located((AppiumBy.ID, input_otp))
                )
                otp_field.send_keys(otp_code)
                print(f"Step 13: Masukan OTP '{otp_code}' ke field OTP")
            else:
                print("Gagal mendapatkan OTP dari SMS dalam batas waktu yang ditentukan")
                 
            oke = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((AppiumBy.ID, btn_ok))
            )
            oke.click()
            print("Step 14: Klik tombol 'OK'")

        except Exception as e:
            print(f"Test gagal: {e}")

    def tearDown(self) -> None:
        if hasattr(self, 'driver') and self.driver:
            self.driver.terminate_app(options.app_package)
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
