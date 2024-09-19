from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys

# Case : Akses Login dengan usernmae 

# import open app
sys.path.insert(0, r'D:\\ngetesappium\\Open App')
from open_app_login_pin import open_app_pin, options

# Variable ID
field_username = 'com.nunomics.app.debug:id/etUsernameEmail'
field_pass = 'com.nunomics.app.debug:id/etPassword'
btn_login_id = 'com.nunomics.app.debug:id/btnApply'
btn_notif_id = 'com.android.permissioncontroller:id/permission_allow_button'

# Variable Input
input_username = "saskiamaulansyah"
input_pass = "Testing1"

class AksesLogin:
    def __init__(self):
        self.driver = open_app_pin()  # Pastikan open_app() mengembalikan driver
        if not self.driver:
            raise Exception("Driver tidak berhasil diinisialisasi dari open_app()")

    def test_login_succes(self):
        try:
            # Tunggu dan Masukkan Username
            input_field = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_username))
            )
            input_field.clear()
            input_field.send_keys(input_username)
            print(f"Step 3: Masukkan Username '{input_username}' ke dalam field Username/ Email/ No Hp")


            # Tunggu dan Masukkan Password
            input_field_password = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_pass))
            )
            input_field_password.clear()
            input_field_password.send_keys(input_pass)
            print(f"Step 4: Masukkan Password '{input_pass}' ke dalam field Password")


            # Tunggu dan klik tombol login
            btn_login = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((AppiumBy.ID, btn_login_id))
            )
            btn_login.click()
            print("Step 5: Klik tombol 'Masuk Sekarang'")


            # Verifikasi izin notifikasi 
            WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located((AppiumBy.ID, btn_notif_id))
            )
            btn_notif = WebDriverWait(self.driver, 15).until(
                EC.element_to_be_clickable((AppiumBy.ID, btn_notif_id))
            )
            btn_notif.click()

            print("Sukses Login berhasil menggunakan Username")

        except Exception as e:
            print(f"Terjadi kesalahan saat login: {e}")

    def tearDown(self) -> None:
        if hasattr(self, 'driver') and self.driver:
            self.driver.terminate_app(options.app_package)
            self.driver.quit()

