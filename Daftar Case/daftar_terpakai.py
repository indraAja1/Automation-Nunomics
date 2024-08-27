import unittest
from open_app import open_app
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Variable ID
field_nama = 'com.nunomics.app.debug:id/etFullName'
field_username = 'com.nunomics.app.debug:id/etUsername'
field_email = 'com.nunomics.app.debug:id/etEmail'
field_nohp = 'com.nunomics.app.debug:id/etNomorTelepon'
field_pass = 'com.nunomics.app.debug:id/etPassword'
field_konfirmasi = 'com.nunomics.app.debug:id/etConfirmPassword'
checkbox = 'com.nunomics.app.debug:id/cbAgreement2'
btn_daftar = 'com.nunomics.app.debug:id/btnApply'
toast_error = '//android.widget.Toast[@text="Data user has been added!"]'  # Misalnya, pesan error jika user sudah ada

# Variable input
nama_lengkap = "SiapaHayotesting"
input_username = "Testing79"
input_email = "ngetesappium@gmail.com"
input_nohp = "082137006458"
input_password = "Testing1"
input_konfirmasi_password = "Testing1"

class TestDaftarNegative(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = open_app()
        if not self.driver:
            raise Exception("Driver tidak berhasil diinisialisasi dari open_app()")
        
    def test_daftar_dengan_data_sudah_digunakan(self):
        try:
            # Isi formulir pendaftaran
            WebDriverWait(self.driver, 1).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_nama))
            ).send_keys(nama_lengkap)
            
            WebDriverWait(self.driver, 1).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_username))
            ).send_keys(input_username)
            
            WebDriverWait(self.driver, 1).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_email))
            ).send_keys(input_email)
            
            WebDriverWait(self.driver, 1).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_nohp))
            ).send_keys(input_nohp)
            
            WebDriverWait(self.driver, 1).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_pass))
            ).send_keys(input_password)
            
            WebDriverWait(self.driver, 1).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_konfirmasi))
            ).send_keys(input_konfirmasi_password)
            
            cb_kebijakan = WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable((AppiumBy.ID, checkbox))
            )
            cb_kebijakan.click()
            
            daftar = WebDriverWait(self.driver, 2).until(
                EC.element_to_be_clickable((AppiumBy.ID, btn_daftar))
            )
            daftar.click()
            
            try:
                error_message = WebDriverWait(self.driver, 4).until(
                    EC.presence_of_element_located((AppiumBy.XPATH, toast_error))
                )
                if error_message:
                    print("Negative Test Case sukses: Pesan error muncul dengan benar (Data user has been added!).")
                else:
                    print("Negative Test Case gagal: Pesan error tidak muncul.")
                    
            except Exception as e:
                print("Pesan error tidak terdeteksi atau tidak muncul dalam waktu yang ditentukan.")
                print(f"Terjadi kesalahan: {e}")          
        except Exception as e:
            print(f"Test gagal: {e}")

    def tearDown(self) -> None:
        if hasattr(self, 'driver') and self.driver:
            self.driver.quit()

if __name__ == "__main__":
    unittest.main()
