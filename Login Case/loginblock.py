from openapp import open_app  # Impor dari openapp.py
import unittest
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class OpenNunomics(unittest.TestCase):
    def setUp(self) -> None:
        # Buka aplikasi dan inisialisasi driver menggunakan open_app
        self.driver = open_app()  # Pastikan open_app() mengembalikan driver
        if not self.driver:
            raise Exception("Driver tidak berhasil diinisialisasi dari open_app()")

    def test_login(self):
        try:
            # Tunggu beberapa detik untuk memastikan halaman login dimuat
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.ID, 'com.nunomics.app.debug:id/etUsernameEmail'))
            )

            # Input email/username/no.hp
            input_field = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((AppiumBy.ID, 'com.nunomics.app.debug:id/etUsernameEmail'))
            )
            input_field.clear()  # hapus email yang sudah keinput
            input_field.send_keys("saskiaaa")

            # Input password
            input_field_password = WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((AppiumBy.ID, 'com.nunomics.app.debug:id/etPassword'))
            )
            input_field_password.clear()  # hapus password yang sudah keinput
            input_field_password.send_keys("Testing13")

            # Klik tombol login sampai pesan error muncul atau batas klik tercapai
            max_retries = 14
            error_detected = False
            
            for _ in range(max_retries):
                btn_login = WebDriverWait(self.driver, 15).until(
                    EC.element_to_be_clickable((AppiumBy.ID, 'com.nunomics.app.debug:id/btnApply'))
                )
                btn_login.click()
                
                # Verifikasi pesan error
                try:
                    error_message = WebDriverWait(self.driver, 4).until(
                        EC.presence_of_element_located((AppiumBy.XPATH, "//android.widget.Toast[@text='Your account has been blocked, please check your email!']"))
                    )
                    if error_message:
                        print("Negative Test Case sukses: Pesan error muncul dengan benar.")
                        error_detected = True
                        break
                except Exception:
                    # Jika pesan error tidak terdeteksi, lanjutkan ke klik berikutnya
                    pass

            if not error_detected:
                print("Negative Test Case gagal: Pesan error tidak muncul setelah beberapa kali klik.")
                
        except Exception as e:
            print(f"Terjadi kesalahan saat login: {e}")

if __name__ == "__main__":
    unittest.main()
