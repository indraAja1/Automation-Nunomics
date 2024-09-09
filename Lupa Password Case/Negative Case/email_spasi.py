import unittest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

# Case : Lupa password dengan email mengandung spasi

# Impor open_app dari path yang ditentukan
sys.path.insert(0, r'D:\\ngetesappium\\Open App')
from open_app_login import open_app

# Variable ID/XPATH
# Variable diambil dari Appium Inspector
lupa_password = 'com.nunomics.app.debug:id/btnForgotPassword'
field_email = 'com.nunomics.app.debug:id/etUsernameEmail'
btn_kirim = 'com.nunomics.app.debug:id/btnApply'
toast_error = 'com.nunomics.app.debug:id/message'


# Variabel input
input_email = "indrad ima s234@gmail.com"

class TestForgotPasswordEmailSpaces(unittest.TestCase):
    def setUp(self) -> None:
        # Buka aplikasi dan inisialisasi driver menggunakan open_app
        self.driver = open_app()  # Pastikan open_app() mengembalikan driver
        if not self.driver:
            raise Exception("Driver tidak berhasil diinisialisasi dari open_app()")
        
    def test_valid_email_with_spaces(self):
        try:

            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ID, lupa_password))
            ).click()
            print("Step 3: Klik teks 'Lupa Password'")            

            input_field = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_email))
            )
            input_field.send_keys(input_email)
            print(f"Step 4: Masukkan Email dengan spasi '{input_email}' ke dalam field email")

            WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.ID, btn_kirim))
            ).click()
            print("Step 5: Klik tombol 'Kirim'")
            
            error_message = WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.ID, toast_error))
            )
            if error_message:
                toast_text = error_message.text  # Mendapatkan teks dari elemen toast
                print(f"Negative Test Case sukses: Pesan error muncul dengan benar - '{toast_text}'")
            else:
                print("Negative Test Case gagal: Pesan error tidak muncul.")
        except Exception as e:
            print(f"Terjadi kesalahan saat login: {e}")

    def tearDown(self) -> None:
        if hasattr(self, 'driver') and self.driver:
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
    
