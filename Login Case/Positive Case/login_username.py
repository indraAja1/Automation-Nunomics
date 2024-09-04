import unittest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
# import open app
sys.path.insert(0, r'D:\\ngetesappium\\Open App')
from open_app_login import open_app

# Variable ID
field_username = 'com.nunomics.app.debug:id/etUsernameEmail'
field_pass = 'com.nunomics.app.debug:id/etPassword'
btn_login_id = 'com.nunomics.app.debug:id/btnApply'
btn_notif_id = 'com.android.permissioncontroller:id/permission_allow_button'

# Variable Input
input_username = "dimasnur"
input_pass = "Testing1"

class TestLoginValidUsername(unittest.TestCase):
    def setUp(self):
        self.driver = open_app()  # Pastikan open_app() mengembalikan driver
        if not self.driver:
            raise Exception("Driver tidak berhasil diinisialisasi dari open_app()")

    def test_login_with_valid_username(self):
        try:

            print(f"Step 3: Masukkan username '{input_username}' ke dalam field Username/ Email/ No Hp")
            input_field = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_username))
            )
            input_field.clear()
            input_field.send_keys(input_username)

            print(f"Step 4: Masukkan password '{input_pass}' ke dalam field Password")
            input_field_password = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_pass))
            )
            input_field_password.clear()
            input_field_password.send_keys(input_pass)

            print("Step 5: Klik tombol 'Masuk Sekarang'")
            btn_login = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((AppiumBy.ID, btn_login_id))
            )
            btn_login.click()

            # Tunggu dan klik tombol perizinan
            WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((AppiumBy.ID, btn_notif_id))
            )
            btn_notif = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((AppiumBy.ID, btn_notif_id))
            )
            btn_notif.click()
            
        except Exception as e:
            print(f"Terjadi kesalahan saat login: {e}")

    def tearDown(self) -> None:
        if hasattr(self, 'driver') and self.driver:
            self.driver.quit()
            
if __name__ == "__main__":
    unittest.main()
