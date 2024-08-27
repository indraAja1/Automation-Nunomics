import unittest
import sys
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Tambahkan jalur ke sys.path
sys.path.insert(0, r'D:\\ngetesappium\\Layanan Kami Case\\')
from akses_login import OpenNunomics

class TestHomePage(unittest.TestCase):
    def setUp(self) -> None:
        # Inisialisasi instance dari OpenNunomics
        self.login_test = OpenNunomics()
        self.login_test.test_loginsucces()  # Lakukan login sebelum melanjutkan

    def test_access_homepage(self):
        try:
            # Lanjutkan dengan tindakan lain setelah login berhasil
            # Contoh: Memastikan elemen tertentu di halaman utama muncul setelah login

            print("Test case untuk mengakses halaman utama setelah login sukses dijalankan.")
        except Exception as e:
            print(f"Terjadi kesalahan saat mengakses halaman utama: {e}")

    def tearDown(self) -> None:
        self.login_test.tearDown()

if __name__ == "__main__":
    unittest.main()
