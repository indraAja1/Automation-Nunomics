import unittest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

# Case : Salah satu field di isi (Username/email/nohp di isi dan password kosong) 

# Impor open_app dari path yang ditentukan
sys.path.insert(0, r'D:\\ngetesappium\\Open App')
from open_app_login_pin import open_app_pin, options
# Variable ID/XPATH
# Variable diambil dari Appium Inspector
field_nohp = 'com.nunomics.app.debug:id/etUsernameEmail'
field_pass = 'com.nunomics.app.debug:id/etPassword'
btn_login_id = 'com.nunomics.app.debug:id/btnApply'

# Variabel input
input_nohp = "089505027088"
input_pass = ""

class TestLoginFieldPasswordEmpty(unittest.TestCase):
    def setUp(self) -> None:
        # Buka aplikasi dan inisialisasi driver menggunakan open_app
        self.driver = open_app_pin()  # Pastikan open_app() mengembalikan driver
        if not self.driver:
            raise Exception("Driver tidak berhasil diinisialisasi dari open_app()")
        
    def test_login_with_empty_password(self):
        try:
            # Input email/username/no.hp
            input_field = WebDriverWait(self.driver, 9).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_nohp))
            )
            input_field.clear()  # Hapus No Handphone yang sudah diinput
            input_field.send_keys(input_nohp)
            print(f"Step 3: Masukkan No Handphone '{input_nohp}' ke dalam field Username/ Email/ No Hp")

            input_password = WebDriverWait(self.driver, 9).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_pass))
            )
            # Abaikan input Password
            input_password.clear()  # Hapus Password yang sudah diinput
            print(f"Step 4: Tidak ada Password yang dimasukkan '{input_pass}' ke dalam field Password")

            # Temukan tombol login
            button = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ID, btn_login_id))
            )
            if not input_pass:
                print("Step 5: Field Password kosong, tombol 'Daftar' tidak akan aktif.")
            else:
                print("Step 5: Klik tombol 'Daftar'")

            # Cek apakah button aktif (enabled)
            if button.is_enabled():
                print("Button aktif")
                button.click()  # Klik tombol login jika aktif
            else:
                print("Button tidak aktif Karena :",)
            if not input_pass:
                    print("- Field password kosong.")
                    
        except Exception as e:
            print(f"Terjadi kesalahan saat login: {e}")

    def tearDown(self) -> None:
        if hasattr(self, 'driver') and self.driver:
            self.driver.terminate_app(options.app_package)
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
    