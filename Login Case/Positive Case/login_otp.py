import unittest
import sys
import random
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Case : Login berhasil setelah verifikasi OTP dari SMS

# Open app daftasr
sys.path.insert(0, r'D:\\ngetesappium\\Open App')
from open_app_daftar_pin import open_app_pin, options


# Variable ID
field_nama = 'com.nunomics.app.debug:id/etFullName'
field_username = 'com.nunomics.app.debug:id/etUsername'
field_username_login = 'com.nunomics.app.debug:id/etUsernameEmail'
field_email = 'com.nunomics.app.debug:id/etEmail'
field_nohp = 'com.nunomics.app.debug:id/etNomorTelepon'
field_pass = 'com.nunomics.app.debug:id/etPassword'
field_konfirmasi = 'com.nunomics.app.debug:id/etConfirmPassword'
checkbox = 'com.nunomics.app.debug:id/cbAgreement2'
btn_daftar = 'com.nunomics.app.debug:id/btnApply'
otp = 'com.nunomics.app.debug:id/firstPinView'
btn_ok = 'com.nunomics.app.debug:id/btnOk'
btn_login_id = 'com.nunomics.app.debug:id/btnApply'
btn_notif_id = 'com.android.permissioncontroller:id/permission_allow_button'


# Variable input
input_nama = "apaHayotesting"
input_username = "Testing8"
input_email = "testing.0@yahoo.com"
input_password = "Testing1"
input_konfirmasi_password = "Testing1"
input_otp = "111111"

class TestSignupToLoginWithOTP(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = open_app_pin()  # Pastikan open_app() mengembalikan driver
        if not self.driver:
            raise Exception("Driver tidak berhasil diinisialisasi dari open_app()")
    def test_login_with_otp(self):
        try:

            nama_lengkap = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_nama))
            )
            nama_lengkap.send_keys(input_nama)
            print(f"Step 3: Masukkan Nama Lengkap '{input_nama}' ke dalam field Nama Lengkap")            

            username = WebDriverWait(self.driver, 9).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_username))
            )
            username.send_keys(input_username)
            print(f"Step 4: Masukkan Username '{input_username}' ke dalam field Username")            
            
            email = WebDriverWait(self.driver, 9).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_email))
            )
            email.send_keys(input_email)
            print(f"Step 5: Masukkan Email '{input_email}' ke dalam field Email")            
            
            # Membuat nomor handphone random
            start = '08'
            rest_of_number = ''.join([str(random.randint(0, 9)) for _ in range(11)])
            random_phone = start + rest_of_number

            # Masukkan nomor handphone random ke dalam field No Handphone
            WebDriverWait(self.driver, 9).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_nohp))
            ).send_keys(random_phone)
            print(f"Step 6: Masukkan No Handphone '{random_phone}' ke dalam field No Handphone")             
            
            password = WebDriverWait(self.driver, 9).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_pass))
            )
            password.send_keys(input_password)
            print(f"Step 7: Masukkan Password '{input_password}' ke dalam field Password")            
            
            konfirmasi_password =WebDriverWait(self.driver, 9).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_konfirmasi))
            )
            konfirmasi_password.send_keys(input_konfirmasi_password)
            print(f"Step 8: Masukkan Konfirmasi Password '{input_konfirmasi_password}' ke dalam field Konfirmasi Password")            
            
            cb_kebijakan = WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable((AppiumBy.ID, checkbox))
            )
            cb_kebijakan.click()
            print("Step 9: Klik checkbox 'Kebijakan Privasi'")
            
            btn_daf = WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable((AppiumBy.ID, btn_daftar))
            )
            btn_daf.click()
            print("Step 10: Klik tombol 'Daftar'")

            WebDriverWait(self.driver, 9).until(
                EC.visibility_of_element_located((AppiumBy.ID, otp))
            ).send_keys(input_otp)
            print(f"Step 11: Masukan OTP '{input_otp}' ke field OTP")
        
            oke = WebDriverWait(self.driver, 9).until(
                EC.visibility_of_element_located((AppiumBy.ID, btn_ok))
            )
            oke.click()
            print("Step 12: Klik tombol 'OK'")     
            
            # Redirect to Login Page            
            input_field = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_username_login))
            )
            input_field.clear()
            input_field.send_keys(input_username)
            print(f"Step 13: Masukkan Username '{input_username}' ke dalam field Username/ Email/ No Hp")

            input_field_password = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_pass))
            )
            input_field_password.clear()
            input_field_password.send_keys(input_password)
            print(f"Step 14: Masukkan Password '{input_password}' ke dalam field Password")

            btn_login = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ID, btn_login_id))
            )
            btn_login.click()
            print("Step 15: Klik tombol 'Masuk Sekarang'")
            
            # Perizinan Notifikasi sistem android            
            WebDriverWait(self.driver, 11).until(
                EC.visibility_of_element_located((AppiumBy.ID, btn_notif_id))
            )
            btn_notif = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ID, btn_notif_id))
            )
            btn_notif.click()
            
        except Exception as e:
            print(f"Test gagal: {e}")
            

    def tearDown(self) -> None:
        if hasattr(self, 'driver') and self.driver:
            self.driver.terminate_app(options.app_package)
            self.driver.quit()


if __name__ == "__main__":
    unittest.main()
