import unittest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
# import open app
sys.path.insert(0, r'D:\\ngetesappium\\Login Case')
from open_app import open_app

# Variable ID/XPATH
# Variable diambil dari Appium Inspector
field_username = 'com.nunomics.app.debug:id/etUsernameEmail'
field_pass = 'com.nunomics.app.debug:id/etPassword'
btn_login_id = 'com.nunomics.app.debug:id/btnApply'
toast_message_xpath = "//android.widget.Toast[@text='Make sure the account and password are correct!']" #Liat XPATH

# Variabel input
input_username = "dimasnur" #Username benar, tetapi password salah.
input_pass = "Pass Fail" #Username benar, tetapi password salah.

class OpenNunomics(unittest.TestCase):
    def setUp(self) -> None:
        # Buka aplikasi dan inisialisasi driver menggunakan open_app
        self.driver = open_app()  # Pastikan open_app() mengembalikan driver
        if not self.driver:
            raise Exception("Driver tidak berhasil diinisialisasi dari open_app()")
        
    def test_loginerror(self):
        try:
            # Tunggu beberapa detik untuk memastikan halaman login dimuat
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_username))
            )

            # Input email/username/no.hp
            input_field = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_username))
            )
            input_field.clear() # hapus email yang sudah keinput
            input_field.send_keys(input_username)

            # Input password
            input_field_password = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_pass))
            )
            input_field_password.clear()  # hapus password yang sudah keinput
            input_field_password.send_keys(input_pass)

            # Klik tombol login
            btn_login = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ID, btn_login_id))
            )
            btn_login.click()
            print("Username benar, tetapi password salah.")
            # Verifikasi pesan error
            try:
                error_message = WebDriverWait(self.driver, 4).until(
                    EC.presence_of_element_located((AppiumBy.XPATH, toast_message_xpath))
                )
                if error_message:
                    print("Negative Test Case sukses: Pesan error muncul dengan benar (Make sure the account and password are correct!)",)
                else:
                    print("Negative Test Case gagal: Pesan error tidak muncul.")
            except Exception as e:
                print("Pesan error tidak terdeteksi atau tidak muncul dalam waktu yang ditentukan.")
                print(f"Terjadi kesalahan: {e}")

        except Exception as e:
            print(f"Terjadi kesalahan saat login: {e}")

if __name__ == "__main__":
    unittest.main()
