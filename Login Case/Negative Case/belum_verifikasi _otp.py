import unittest
import sys
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Case : Login dengan akun yang belum memasukkan OTP.

# import open app daftar
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
XPATH_back = '//android.widget.LinearLayout[@resource-id="com.nunomics.app.debug:id/ivBack"]'
btn_login = 'com.nunomics.app.debug:id/btnLogin'
field_user_login = 'com.nunomics.app.debug:id/etUsernameEmail'
btn_login_id = 'com.nunomics.app.debug:id/btnApply'
toast_message_back = '//android.widget.Toast[@text="Anda tidak akan bisa kembali ke halaman OTP lagi jika keluar, tekan tombol kembali sekali lagi untuk keluar"]'
toast_error = '//android.widget.Toast[@text="User not registered yet!"]'


# Variable input
input_nama = "Hayosiapa"
input_username = "Testing988"
input_email = "ngetesappiu2m@gmail.com"
input_nohp = "08123456789"
input_password = "Testing1"
input_konfirmasi_password = "Testing1"

class TestLoginUnverifiedOTP(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = open_app()  # Pastikan open_app() mengembalikan driver
        if not self.driver:
            raise Exception("Driver tidak berhasil diinisialisasi dari open_app()")
        
    def test_login_with_unverified_otp(self):
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

            cb_kebijakan = WebDriverWait(self.driver, 9).until(
                EC.element_to_be_clickable((AppiumBy.ID, checkbox))
            )
            cb_kebijakan.click()
            print("Step 9: Klik checkbox 'Kebijakan Privasi'")
            
            btn_daf = WebDriverWait(self.driver, 9).until(
                EC.element_to_be_clickable((AppiumBy.ID, btn_daftar))
            )
            btn_daf.click()
            print("Step 10: Klik tombol 'Daftar'")
            # Back
            max_retries = 2
            for attempt in range(max_retries):
                back = WebDriverWait(self.driver, 14).until(
                    EC.element_to_be_clickable((AppiumBy.XPATH, XPATH_back))
                )
                print(f"Step 11: Klik < (Kembali) dan tidak melakukan input OTP ke-{attempt + 1}")
                back.click()
                
            error_message_back = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, toast_message_back))
            )
            if error_message_back:
                toast_text_back = error_message_back.text  # Mendapatkan teks dari elemen toast
                print(f"Negative Test Case sukses: Pesan error muncul dengan benar - '{toast_text_back}'")
            else:
                print("Negative Test Case gagal: Pesan error tidak muncul.")

            # Login Case Negative 
            login_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ID, btn_login))
            )
            login_btn.click()
            print("Step 12: Klik tombol 'Maasuk'")

            
            username_login = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_user_login))
            )
            username_login.clear()
            username_login.send_keys(input_username)
            print(f"Step 13: Masukkan Username '{input_username}' ke dalam field Username/ Email/ No Hp")

            password_login = WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_pass))
            )
            password_login.clear()
            password_login.send_keys(input_password)
            print(f"Step 14: Masukkan Password '{input_password}' ke dalam field Password")
            
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ID, btn_login_id))
            ).click()
            print("Step 15: Klik tombol 'Masuk Sekarang'")

        # Verifikasi pesan error
            error_message = WebDriverWait(self.driver, 10).until(
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
