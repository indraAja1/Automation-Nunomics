import unittest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

# Impor open_app dari path yang ditentukan
sys.path.insert(0, r'D:\\ngetesappium\\Open App')
from open_app_daftar import open_app

# Variable ID/XPATH
# Variable diambil dari Appium Inspector
field_nama = 'com.nunomics.app.debug:id/etFullName'
field_username = 'com.nunomics.app.debug:id/etUsername'
field_email = 'com.nunomics.app.debug:id/etEmail'
field_nohp = 'com.nunomics.app.debug:id/etNomorTelepon'
field_pass = 'com.nunomics.app.debug:id/etPassword'
field_konfirmasi = 'com.nunomics.app.debug:id/etConfirmPassword'
checkbox = 'com.nunomics.app.debug:id/cbAgreement2'
btn_daftar = 'com.nunomics.app.debug:id/btnApply'

# Variabel input
input_nama = "Testes"
input_username = "ngetes1212"
input_email = "Ngetesappium@gmail.com"
input_nohp = "081234567891"
input_password = "Testing1"
input_konfirmasi_password = "Testing1"

class TestSignupEmptyCheckbox(unittest.TestCase):
    def setUp(self) -> None:
        # Buka aplikasi dan inisialisasi driver menggunakan open_app
        self.driver = open_app()  # Pastikan open_app() mengembalikan driver
        if not self.driver:
            raise Exception("Driver tidak berhasil diinisialisasi dari open_app()")
        
    def test_signup_with_unchecked_checkbox(self):
        try:
            WebDriverWait(self.driver, 9).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_nama))
            ).send_keys(input_nama)
            print(f"Step 3: Masukkan Nama Lengkap '{input_nama}' ke dalam field Nama Lengkap")            
 
            WebDriverWait(self.driver, 9).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_username))
            ).send_keys(input_username)
            print(f"Step 4: Masukkan Username '{input_username}' ke dalam field Username")            

            WebDriverWait(self.driver, 9).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_email))
            ).send_keys(input_email)
            print(f"Step 5: Masukkan Email '{input_email}' ke dalam field Email")            

            WebDriverWait(self.driver, 9).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_nohp))
            ).send_keys(input_nohp)
            print(f"Step 6: Masukkan No Handphone '{input_nohp}' ke dalam field No Handphone")            

            WebDriverWait(self.driver, 9).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_pass))
            ).send_keys(input_password)
            print(f"Step 7: Masukkan Password '{input_password}' ke dalam field Password")            

            WebDriverWait(self.driver, 9).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_konfirmasi))
            ).send_keys(input_konfirmasi_password)
            print(f"Step 8: Masukkan Konfirmasi Password '{input_konfirmasi_password}' ke dalam field Konfirmasi Password")            

            # Abaikan pengecekan checkbox
            print("Step 9: Tidak mencentang checkbox 'Kebijakan Privasi'")
            
            button = WebDriverWait(self.driver, 8).until(
                EC.presence_of_element_located((AppiumBy.ID, btn_daftar))
            )

                        
            # Cek apakah tombol aktif (enabled)
            if button.is_enabled():
                print("Step 10: Tombol Klik 'Daftar'")
                print("Button aktif")
                button.click()  # Klik tombol daftar jika aktif
            else:
                print("Step 10: Tombol 'Daftar' tidak akan aktif jika checkbox 'Kebijakan Privasi' tidak dicentang.")
                print("Button tidak aktif karena checkbox 'Kebijakan Privasi' tidak dicentang.")
                
        except Exception as e:
            print(f"Terjadi kesalahan saat pendaftaran: {e}")

    def tearDown(self) -> None:
        if hasattr(self, 'driver') and self.driver:
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
