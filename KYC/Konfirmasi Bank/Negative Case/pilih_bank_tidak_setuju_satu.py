import unittest
import sys
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Case : Pembukaan Rekening (KYC) dengan Konfirmasi Bank (Tidak Setuju dengan Pernyataan Pertama) 

# Import touch actions untuk swipe
sys.path.insert(0, r'D:\\ngetesappium\\touch')
from touch import perform_swipe

# Tambahkan jalur ke sys.path
sys.path.insert(0, r'D:\\ngetesappium\\Open App')
from open_app_kyc import AksesLogin

# Variable ID/XPATH
btn_kyc = 'com.nunomics.app.debug:id/btnInfo'
field_promotor = 'com.nunomics.app.debug:id/etReferral'
btn_mulai = 'com.nunomics.app.debug:id/btnStart'
toast_message = '//android.widget.TextView[@resource-id="com.nunomics.app.debug:id/tvBottom"]'
rped = 'com.nunomics.app.debug:id/tvRped'
tutup_rped = 'com.nunomics.app.debug:id/btnClose'
agi = 'com.nunomics.app.debug:id/rbAgi'
agreement2 = '//android.widget.TextView[@resource-id="com.nunomics.app.debug:id/tvCheckbox2"]'
agreement3 = '//android.widget.TextView[@resource-id="com.nunomics.app.debug:id/tvCheckbox3"]'
setuju = 'com.nunomics.app.debug:id/btnAgree'
lanjut = 'com.nunomics.app.debug:id/btnNext'


# Variable Input
input_promotor = '0TPUZDY7'

class TestComfirmBank(unittest.TestCase):
    def setUp(self):
        # Inisialisasi instance dari OpenNunomics
        self.login_test = AksesLogin()
        self.login_test.test_login_succes()  # Lakukan login sebelum melanjutkan
        # Ambil driver dari login_test
        self.driver = self.login_test.driver
            
    def test_corfirm_bank(self):
        try:
            kyc = WebDriverWait(self.driver, 9).until(
                EC.element_to_be_clickable((AppiumBy.ID, btn_kyc))
            )
            kyc.click()
            print("Step 6: Klik tombol 'Lakukan Registrasi KYC'")

            input_code = WebDriverWait(self.driver, 9).until(
                EC.visibility_of_element_located((AppiumBy.ID, field_promotor))
            )
            input_code.send_keys(input_promotor)
            print(f"Step 7: Masukkan Kode Promotor '{input_promotor} ke field Kode Promotor'")
            
            mulai = WebDriverWait(self.driver, 8).until(
                EC.element_to_be_clickable((AppiumBy.ID, btn_mulai))
            )
            print("Step 8: Klik tombol 'Mulai'")

            # Cek dan ambil pesan toast
            message = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.XPATH, toast_message))
            )
            if message:
                toast_text = message.text  # Mendapatkan teks dari elemen toast
                print(f"Pesan valid muncul dengan benar - '{toast_text}'")
            else:
                print("Pesan valid tidak muncul.")

            # Klik button mulai
            mulai.click()

            WebDriverWait(self.driver, 8).until(
                EC.element_to_be_clickable((AppiumBy.ID, rped))
            ).click()
            print("Step 9: Klik teks 'Apa itu RPED?'")
            
            WebDriverWait(self.driver, 8).until(
                EC.element_to_be_clickable((AppiumBy.ID, tutup_rped))
            ).click()
            print("Step 10: Klik tombol 'Tutup'")
            
            WebDriverWait(self.driver, 8).until(
                EC.element_to_be_clickable((AppiumBy.ID, agi))   
            ).click()
            print("Step 11: Klik chechbox 'Artha Graha International'")
            
            # Abaikan Centang agreement 1
            
            # Centang agreement 2
            toast_agrement2 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, agreement2))   
            )
            if toast_agrement2:
                toast_text2 = toast_agrement2.text
                print(f"Step 12: Klik chechbox atau teks: '{toast_text2}' ")
            else:
                print(f"Step 12: Tesk pada '{toast_text2}' tidak muncul")
            toast_agrement2.click()
                        
            # Scroll ke bawah lagi
            perform_swipe(self.driver, 581, 2599, 623, 403) # Scroll pertama
            perform_swipe(self.driver, 581, 2599, 1023, 703) # Scroll kedua
            
            WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.ID, setuju))   
            ).click()
            print("Step 13: Klik tombol 'Setuju'")
            
            # Centang agreement 3
            toast_agrement3 = WebDriverWait(self.driver, 10).until(
                EC.element_to_be_clickable((AppiumBy.XPATH, agreement3))   
            )
            if toast_agrement3:
                toast_text3 = toast_agrement3.text
                print(f"Step 14: Klik chechbox atau teks: '{toast_text3}' ")
            else:
                print(f"Step 14: Tesk pada '{toast_text3}' tidak muncul")
            toast_agrement3.click()
            
            btn_lanjut = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((AppiumBy.ID, lanjut))   
            )
            if btn_lanjut.is_enabled():
                print("Button aktif")
                print("Step 15: Klik tombol 'Lanjut'")
                btn_lanjut.click()  # Klik tombol daftar jika aktif
            else:
                print("Button tidak aktif karena : ")
                print("Step 15: Tombol 'Lanjut' tidak aktif jika checkbox 'Pernyataan Pertama' tidak dicentang.")                

        except Exception as e:
            print(f"Terjadi kesalahan saat mengakses halaman Pilih Bank: {e}")

    def tearDown(self) -> None:
        self.login_test.tearDown()

if __name__ == "__main__":
    unittest.main()
