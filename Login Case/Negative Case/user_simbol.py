import unittest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
# import open app
sys.path.insert(0, r'D:\\ngetesappium\\Login Case')
from open_app import open_app

# Variable ID
# Di ambil dari APPIUM INSPECTOR
field_username = 'com.nunomics.app.debug:id/etUsernameEmail'
field_pass = 'com.nunomics.app.debug:id/etPassword'
btn_login_id = 'com.nunomics.app.debug:id/btnApply'
toast_message_xpath = "//android.widget.Toast[@text='Terjadi kesalahan']" 

# Variable Input
input_username = "dimasnur*$#&"
input_pass = "Testing1"

class OpenNunomics(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = open_app()  # Pastikan open_app() mengembalikan driver
        if not self.driver:
            raise Exception("Driver tidak berhasil diinisialisasi dari open_app()")
        
    def test_loginsucces(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_username))
            )
            input_field = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_username))
            )
            input_field.clear()
            input_field.send_keys(input_username)

            input_field_password = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_pass))
            )
            input_field_password.clear()
            input_field_password.send_keys(input_pass)

            btn_login = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ID, btn_login_id))
            )
            btn_login.click()
            print("Login dengan username yang mengandung karakter spesial (contoh: @, #,$)")
            try:
                error_message = WebDriverWait(self.driver, 4).until(
                    EC.presence_of_element_located((AppiumBy.XPATH, toast_message_xpath))
                )
                if error_message:
                    print("Negative Test Case sukses: Pesan error muncul dengan benar (Terjadi kesalahan)",)
                else:
                    print("Negative Test Case gagal: Pesan error tidak muncul.")
            except Exception as e:
                print("Pesan error tidak terdeteksi atau tidak muncul dalam waktu yang ditentukan.")
                print(f"Terjadi kesalahan: {e}")

        except Exception as e:
            print(f"Terjadi kesalahan saat login: {e}")

if __name__ == "__main__":
    unittest.main()
