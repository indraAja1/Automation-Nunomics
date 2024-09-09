import unittest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

# Case : Login dengan format email salah

# import open app
sys.path.insert(0, r'D:\\ngetesappium\\Open App')
from open_app_login import open_app

# Variable ID/XPATH
# Variable diambil dari Appium Inspector
field_email = 'com.nunomics.app.debug:id/etUsernameEmail'
field_pass = 'com.nunomics.app.debug:id/etPassword'
btn_login_id = 'com.nunomics.app.debug:id/btnApply'
toast_error = "//android.widget.Toast[@text='Terjadi kesalahan']" 

# Variabel input
input_email = "usertesting1satu@" #Login dengan format email salah
input_pass = "Testing1"

class TestLoginEmailValidation(unittest.TestCase):
    def setUp(self) -> None:
        # Buka aplikasi dan inisialisasi driver menggunakan open_app
        self.driver = open_app()  # Pastikan open_app() mengembalikan driver
        if not self.driver:
            raise Exception("Driver tidak berhasil diinisialisasi dari open_app()")
        
    def test_error_message_for_invalid_email(self):
        try:

            # Input email/username/no.hp
            input_field = WebDriverWait(self.driver, 9).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_email))
            )
            input_field.clear() # hapus email yang sudah keinput
            input_field.send_keys(input_email)
            print(f"Step 3: Masukkan Email '{input_email}' ke dalam field Username/ Email/ No Hp")            


            # Input password
            input_field_password = WebDriverWait(self.driver, 9).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_pass))
            )
            input_field_password.clear()  # hapus password yang sudah keinput
            input_field_password.send_keys(input_pass)
            print(f"Step 4: Masukkan Password '{input_pass}' ke dalam field Password")

            # Klik tombol login
            btn_login = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ID, btn_login_id))
            )
            btn_login.click()
            print("Step 5: Klik tombol 'Masuk Sekarang'")
            
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
