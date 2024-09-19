import unittest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

# Case : Lupa password dengan email valid yang terdaftar

# Impor open_app dari path yang ditentukan
sys.path.insert(0, r'D:\\ngetesappium\\Open App')
from open_app_login_pin import open_app_pin, options

# Variable ID/XPATH
# Variable diambil dari Appium Inspector
lupa_password = 'com.nunomics.app.debug:id/btnForgotPassword'
field_email = 'com.nunomics.app.debug:id/etUsernameEmail'
btn_kirim = 'com.nunomics.app.debug:id/btnApply'
pesan_sukses = '//android.widget.TextView[@text="Silakan cek email kamu untuk langkah berikutnya"]'
btn_ok = 'com.nunomics.app.debug:id/btnOk'

# Variabel input
input_email = "usertesting1satu@gmail.com"

class TestForgotPasswordValidEmail(unittest.TestCase):
    def setUp(self) -> None:
        # Buka aplikasi dan inisialisasi driver menggunakan open_app
        self.driver = open_app_pin()  # Pastikan open_app() mengembalikan driver
        if not self.driver:
            raise Exception("Driver tidak berhasil diinisialisasi dari open_app()")
        
    def test_valid_email(self):
        try:
            
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ID, lupa_password))
            ).click()
            print("Step 3: Klik teks 'Lupa Password'")            

            input_field = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_email))
            )
            input_field.send_keys(input_email)
            print(f"Step 4: Masukkan Email '{input_email}' ke dalam field email")

            WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((AppiumBy.ID, btn_kirim))
            ).click()
            print("Step 5: Klik tombol 'Kirim'")
            
            succes_message = WebDriverWait(self.driver, 7).until(
                EC.presence_of_element_located((AppiumBy.XPATH, pesan_sukses))
            )
            if succes_message:
                toast_text_succes = succes_message.text  # Mendapatkan teks dari elemen toast
                print(f"Positive Test Case sukses: Pesan berhasil muncul dengan benar - '{toast_text_succes}'")
            else:
                print("Positive Test Case gagal: Pesan berhasil tidak muncul.")       
                
                
            ok = WebDriverWait(self.driver, 7).until(
                EC.element_to_be_clickable((AppiumBy.ID, btn_ok))
            )
            ok.click()
            print("Step 6: Klik tombol 'OK'")
        except Exception as e:
            print(f"Terjadi kesalahan saat login: {e}")
            

    def tearDown(self) -> None:
        if hasattr(self, 'driver') and self.driver:
            self.driver.terminate_app(options.app_package)
            self.driver.quit()
            
if __name__ == "__main__":
    unittest.main()
    
