import time
import subprocess
import re
import unittest
from openapp import open_app
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Variable ID/checkbox/btn/XPATH
field_nama = 'com.nunomics.app.debug:id/etFullName'
field_username = 'com.nunomics.app.debug:id/etUsername'
field_email = 'com.nunomics.app.debug:id/etEmail'
field_nohp = 'com.nunomics.app.debug:id/etNomorTelepon'
field_pass = 'com.nunomics.app.debug:id/etPassword'
field_konfirmasi = 'com.nunomics.app.debug:id/etConfirmPassword'
checkbox = 'com.nunomics.app.debug:id/cbAgreement2'
btn_daftar = 'com.nunomics.app.debug:id/btnApply'
input_otp = 'com.nunomics.app.debug:id/firstPinView'

# Variable input
nama_lengkap = "SiapaHayo"
input_username = "Testing99"
input_email = "ngetesappium@gmail.com"
input_nohp = "082137006458"
input_password = "Testing1"
input_konfirmasi_password = "Testing1"

def get_latest_sms():
    result = subprocess.run(
        ["adb", "shell", "content", "query", "--uri", "content://sms/inbox", "--projection", "body,address,date"],
        capture_output=True,
        text=True
    )
    messages = result.stdout.splitlines()
    
    # Filter messages where address is 'AUTHMSG'
    filtered_messages = [msg for msg in messages if "AUTHMSG" in msg]
    
    # Sort messages by date descending
    sorted_messages = sorted(
        filtered_messages,
        key=lambda x: int(re.search(r'date=(\d+)', x).group(1)),
        reverse=True
    )
    
    # Get the latest message
    latest_message = sorted_messages[0] if sorted_messages else ""
    
    return latest_message

def parse_otp(sms_body):
    match = re.search(r'\b\d{6}\b', sms_body)
    if match:
        return match.group(0)
    return None

def get_otp_with_timeout(timeout=120, poll_interval=10):
    """
    Fungsi untuk menunggu dan mendapatkan OTP terbaru dengan waktu tunggu yang ditentukan.

    Args:
        timeout (int): Waktu maksimal dalam detik untuk menunggu OTP.
        poll_interval (int): Interval waktu dalam detik untuk memeriksa pesan SMS.

    Returns:
        str: OTP terbaru jika ditemukan dalam batas waktu, None jika tidak ditemukan.
    """
    start_time = time.time()
    last_otp = None

    while time.time() - start_time < timeout:
        # Tambahkan penundaan sebelum memulai pengambilan SMS
        time.sleep(5)
        sms_info = get_latest_sms()
        otp = parse_otp(sms_info)
        if otp and otp != last_otp:
            last_otp = otp
            print(f"New OTP found: {otp}")
            return otp
        time.sleep(poll_interval)  # Tunggu beberapa detik sebelum mencoba lagi

    print("Gagal mendapatkan OTP dari SMS dalam batas waktu yang ditentukan.")
    return None

class Daftar(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = open_app()  # Pastikan open_app() mengembalikan driver
        if not self.driver:
            raise Exception("Driver tidak berhasil diinisialisasi dari open_app()")
        
    def test_daftar(self):
        try:
            # Isi formulir pendaftaran
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_nama))
            ).send_keys(nama_lengkap)
            
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_username))
            ).send_keys(input_username)
            
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_email))
            ).send_keys(input_email)
            
            WebDriverWait(self.driver, 10).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_nohp))
            ).send_keys(input_nohp)
            
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_pass))
            ).send_keys(input_password)
            
            WebDriverWait(self.driver, 5).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_konfirmasi))
            ).send_keys(input_konfirmasi_password)
            
            cb_kebijakan = WebDriverWait(self.driver, 12).until(
                EC.element_to_be_clickable((AppiumBy.ID, checkbox))
            )
            cb_kebijakan.click()
            
            daftar = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ID, btn_daftar))
            )
            daftar.click()

            # Tunggu OTP dengan batas waktu yang ditentukan
            print("Menunggu OTP...")
            otp_code = get_otp_with_timeout(timeout=120, poll_interval=10)
            if otp_code:
                otp_field = WebDriverWait(self.driver, 10).until(
                    EC.visibility_of_element_located((AppiumBy.ID, input_otp))
                )
                otp_field.send_keys(otp_code)
                print(f"OTP '{otp_code}' berhasil dimasukkan")
            else:
                print("Gagal mendapatkan OTP dari SMS dalam batas waktu yang ditentukan")

        except Exception as e:
            print(f"Test gagal: {e}")
          
if __name__ == "__main__":
    unittest.main()
