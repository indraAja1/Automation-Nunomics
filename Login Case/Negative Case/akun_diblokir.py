import unittest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

# Import open app
sys.path.insert(0, r'D:\\ngetesappium\\Open App')
from open_app_login import open_app

# Variable ID/XPATH
field_username = 'com.nunomics.app.debug:id/etUsernameEmail'
field_pass = 'com.nunomics.app.debug:id/etPassword'
btn_login_id = 'com.nunomics.app.debug:id/btnApply'
toast_error = "//android.widget.Toast[@text='Your account has been blocked, please check your email!']"

# Variable Input
input_username = "Testing3"
input_pass = "Testing12"

class TestLoginBlockAccount(unittest.TestCase):
    def setUp(self) -> None:
        # Buka aplikasi dan inisialisasi driver menggunakan open_app
        self.driver = open_app()  # Pastikan open_app() mengembalikan driver
        if not self.driver:
            raise Exception("Driver tidak berhasil diinisialisasi dari open_app()")

    def test_login_with_blocked_account(self):
        try:
            
            input_field = WebDriverWait(self.driver, 9).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_username))
            )
            input_field.clear() # hapus email yang sudah keinput
            input_field.send_keys(input_username)
            print(f"Step 3: Masukkan Username '{input_username}' ke dalam field Username/ Email/ No Hp")            

            input_field_password = WebDriverWait(self.driver, 9).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_pass))
            )
            input_field_password.clear()  # hapus password yang sudah keinput
            input_field_password.send_keys(input_pass)
            print(f"Step 4: Masukkan Password '{input_pass}' ke dalam field Password")

            # Klik tombol login hingga error muncul atau mencapai batas klik
            max_retries = 10
            error_detected = False
            print("Step 5: Klik tombol 'Masuk Sekarang'")
            for attempt in range(max_retries):
                btn_login = WebDriverWait(self.driver, 10).until(
                    EC.element_to_be_clickable((AppiumBy.ID, btn_login_id))
                )
                print(f"Tap (Masuk Sekarang) ke-{attempt + 1}")
                btn_login.click()

                # Verifikasi pesan error
                try:
                    error_message = WebDriverWait(self.driver, 7).until(
                        EC.presence_of_element_located((AppiumBy.XPATH, toast_error))
                    )
                    if error_message:
                        toast_text = error_message.text  
                        print(f"Negative Test Case sukses: Pesan error muncul dengan benar - '{toast_text}'")
                        error_detected = True
                        break
                except Exception:
                    print(f"Pesan error tidak terdeteksi pada attempt ke-{attempt + 1}.")
            
            # Cek apakah pesan error berhasil dideteksi
            if not error_detected:
                print("Test gagal: Pesan error tidak muncul setelah semua percobaan login.")
        
        except Exception as e:
            print(f"Test gagal: {e}")

    def tearDown(self) -> None:
        if hasattr(self, 'driver') and self.driver:
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
