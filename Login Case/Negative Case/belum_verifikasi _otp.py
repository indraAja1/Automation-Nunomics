import unittest
import sys
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.insert(0, r'D:\\ngetesappium\\Daftar Case\\Open App') 
from open_app_login import open_app

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
nama_lengkap = "Hayosiapa"
input_username = "Testing9"
input_email = "ngetesappiu2m@gmail.com"
input_nohp = "082137006443"
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
            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_nama))
            ).send_keys(nama_lengkap)
            
            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_username))
            ).send_keys(input_username)
            
            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_email))
            ).send_keys(input_email)
            
            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_nohp))
            ).send_keys(input_nohp)
            
            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_pass))
            ).send_keys(input_password)
            
            WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_konfirmasi))
            ).send_keys(input_konfirmasi_password)
            
            cb_kebijakan = WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable((AppiumBy.ID, checkbox))
            )
            cb_kebijakan.click()
            
            btn_daf = WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable((AppiumBy.ID, btn_daftar))
            )
            btn_daf.click()
            #Back
            max_retries = 2
            for _ in range(max_retries):
                back = WebDriverWait(self.driver, 14).until(
                    EC.element_to_be_clickable((AppiumBy.XPATH, XPATH_back))
                )
                back.click()
            try:
                error_message_back = WebDriverWait(self.driver, 4).until(
                    EC.presence_of_element_located((AppiumBy.XPATH, toast_message_back))
                )
                if error_message_back:
                    print("Pesan peringatan Keluar dengan benar : (Anda tidak akan bisa kembali ke halaman OTP lagi jika keluar, tekan tombol kembali sekali lagi untuk keluar) ")
                else:
                    print("Pesan peringatan Keluar gagal: Pesan error tidak muncul.")
                    
            except Exception as e:
                    print("Pesan error tidak terdeteksi atau tidak muncul dalam waktu yang ditentukan.")
                    print(f"Terjadi kesalahan: {e}")

            # Login Case Negative 
            login_btn = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ID, btn_login))
            )
            print("Kembali ke halaman Welcome -> Login")   
            login_btn.click()
            
            username_login = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_user_login))
            )
            username_login.clear()
            username_login.send_keys(input_username)
            
            password_login = WebDriverWait(self.driver, 2).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_pass))
            )
            password_login.clear()
            password_login.send_keys(input_password)
            
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ID, btn_login_id))
            ).click()
            
        # Verifikasi pesan error
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
