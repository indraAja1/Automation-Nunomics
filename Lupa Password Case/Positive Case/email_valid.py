import unittest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

# Impor open_app dari path yang ditentukan
sys.path.insert(0, r'D:\\ngetesappium\\Open App')
from open_app_login import open_app

# Variable ID/XPATH
# Variable diambil dari Appium Inspector
lupa_password = 'com.nunomics.app.debug:id/btnForgotPassword'
field_email = 'com.nunomics.app.debug:id/etUsernameEmail'
btn_kirim = 'com.nunomics.app.debug:id/btnApply'
pesan_sukses = '//android.widget.TextView[@text="Silakan cek email kamu untuk langkah berikutnya"]'
btn_ok = 'com.nunomics.app.debug:id/btnOk'

# Variabel input
input_email = "indradimas234@gmail.com"

class TestForgotPasswordValidEmail(unittest.TestCase):
    def setUp(self) -> None:
        # Buka aplikasi dan inisialisasi driver menggunakan open_app
        self.driver = open_app()  # Pastikan open_app() mengembalikan driver
        if not self.driver:
            raise Exception("Driver tidak berhasil diinisialisasi dari open_app()")
        
    def test_valid_email(self):
        try:
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ID, lupa_password))
            ).click()

            # Input email
            input_field = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_email))
            )
            input_field.send_keys(input_email)

            # klik button kirim
            WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.ID, btn_kirim))
            ).click()
            
            message_succes = WebDriverWait(self.driver, 7).until(
                EC.presence_of_element_located((AppiumBy.XPATH, pesan_sukses))
            )
            if message_succes:
                toast_text_succes = message_succes.text  # Mendapatkan teks dari elemen toast
                print(f"Negative Test Case sukses: Pesan error muncul dengan benar - '{toast_text_succes}'")
            else:
                print("Negative Test Case gagal: Pesan error tidak muncul.")       
                
            ok = WebDriverWait(self.driver, 7).until(
                EC.element_to_be_clickable((AppiumBy.ID, btn_ok))
            )
            ok.click()
        except Exception as e:
            print(f"Terjadi kesalahan saat login: {e}")

    def tearDown(self) -> None:
        if hasattr(self, 'driver') and self.driver:
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
    
