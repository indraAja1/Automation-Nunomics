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
input_nama = ""
input_username = ""
input_email = ""
input_nohp = ""
input_password = ""
input_konfirmasi_password = ""

class TestSignupEmpty(unittest.TestCase):
    def setUp(self) -> None:
        # Buka aplikasi dan inisialisasi driver menggunakan open_app
        self.driver = open_app()  # Pastikan open_app() mengembalikan driver
        if not self.driver:
            raise Exception("Driver tidak berhasil diinisialisasi dari open_app()")
        
    def test_signup_with_empty(self):
        try:
            # Abaikan input Nama Lengkap
            print(f"Step 3: Tidak ada Nama Lengkap yang dimasukan '{input_nama}' ke dalam field Nama Lengkap")            

            # Abaikan input Username
            print(f"Step 4: Tidak ada Username yang dimasukan '{input_username}' ke dalam field Username")            
            
            # Abaikan input Email
            print(f"Step 5: Tidak ada Email yang dimasukan '{input_email}' ke dalam field Email")            
            
            # Abaikan input No Handphone
            print(f"Step 6: Tidak ada No Handphone yang dimasukan '{input_nohp}' ke dalam field No Handphone")            

            # Abaikan input Password
            print(f"Step 7: Tidak ada Password yang dimasukan '{input_password}' ke dalam field Password")            

            # Abaikan input Konfirmasi Password
            print(f"Step 8: Tidak ada Konfirmasi Password yang dimasukan'{input_konfirmasi_password}' ke dalam field Konfirmasi Password")            

            cb_kebijakan = WebDriverWait(self.driver, 8).until(
                EC.element_to_be_clickable((AppiumBy.ID, checkbox))
            )
            cb_kebijakan.click()
            print("Step 9: Klik checkbox 'Kebijakan Privasi'")
            
            button = WebDriverWait(self.driver, 8).until(
                EC.presence_of_element_located((AppiumBy.ID, btn_daftar))
            )

            # Cek apakah semua field kosong dan cetak pesan sesuai
            if not any([input_nama, input_username, input_email, input_nohp, input_password, input_konfirmasi_password]):
                print("Step 10: Semua field kosong, tombol 'Daftar' tidak akan aktif.")
            else:
                print("Step 10: Klik tombol 'Daftar'")            
            # Cek apakah tombol aktif (enabled)
            if button.is_enabled():
                print("Button aktif")
                button.click()  # Klik tombol daftar jika aktif
            else:
                print("Button tidak aktif. Periksa field yang kosong.")
            
            # Periksa dan cetak pesan jika field kosong
            if not input_nama:
                print("- Field Nama Lengkap kosong.")
            if not input_username:
                print("- Field Username kosong.")
            if not input_email:
                print("- Field Email kosong.")
            if not input_nohp:
                print("- Field Nomor Telepon kosong.")
            if not input_password:
                print("- Field Password kosong.")
            if not input_konfirmasi_password:
                print("- Field Konfirmasi Password kosong.")
                
        except Exception as e:
            print(f"Terjadi kesalahan saat pendaftaran: {e}")

    def tearDown(self) -> None:
        if hasattr(self, 'driver') and self.driver:
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
