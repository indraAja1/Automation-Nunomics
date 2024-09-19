import unittest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

# Case : Nomor handphone salah, tetapi password benar.

# import open app
sys.path.insert(0, r'D:\\ngetesappium\\Open App')
from open_app_login_pin import open_app_pin, options
# Variable ID/XPATH
# Variable diambil dari Appium Inspector
field_nohp = 'com.nunomics.app.debug:id/etUsernameEmail'
field_pass = 'com.nunomics.app.debug:id/etPassword'
btn_login_id = 'com.nunomics.app.debug:id/btnApply'
toast_error = "//android.widget.Toast[@text='User not registered yet!']"

# Variabel input
input_nohp = "088585923488" #Nomor telepon salah, tetapi password benar
input_pass = "Testing1" #Nomor telepon salah, tetapi password benar

class TestLoginIncorrectPhone(unittest.TestCase):
    def setUp(self) -> None:
        # Buka aplikasi dan inisialisasi driver menggunakan open_app
        self.driver = open_app_pin()  # Pastikan open_app() mengembalikan driver
        if not self.driver:
            raise Exception("Driver tidak berhasil diinisialisasi dari open_app()")
        
    def test_login_with_wrong_phone_and_correct_password(self):
        try:
            # Tunggu beberapa detik untuk memastikan halaman login dimuat
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_nohp))
            )

            # Input email/username/no.hp
            input_field = WebDriverWait(self.driver, 9).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_nohp))
            )
            input_field.clear() # hapus email yang sudah keinput
            input_field.send_keys(input_nohp)
            print(f"Step 3: Masukkan no handphone '{input_nohp}' ke dalam field Username/ Email/ No Hp")            

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
            self.driver.terminate_app(options.app_package)
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
