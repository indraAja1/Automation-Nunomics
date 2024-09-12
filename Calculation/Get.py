import unittest
import sys
import time
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.insert(0, r'D:\\ngetesappium\\touch')
from touch import click_at_coordinates 
from touch import perform_swipe

sys.path.insert(0, r'D:\\ngetesappium\\Open App')
from akses_login import AksesLogin

# Variable ID
tab_emas = 'com.nunomics.app.debug:id/tvEmas'
halaman_emas = 'com.nunomics.app.debug:id/llBottom'
pnl_a = 'com.nunomics.app.debug:id/tvEstimated'
avt = 'com.nunomics.app.debug:id/tvAvgTotalCost'
see_home = 'com.nunomics.app.debug:id/ivSeeHide'
see_rped = 'com.nunomics.app.debug:id/ivSee'
pnl_f_p = 'com.nunomics.app.debug:id/tvPnlPercent'
pnl_f_a = 'com.nunomics.app.debug:id/tvPnl'
pnl_f_p_home = 'com.nunomics.app.debug:id/tvPnlPercent'
pnl_f_a_home = 'com.nunomics.app.debug:id/tvNo'
kontrak_satu = 'new UiSelector().resourceId("com.nunomics.app.debug:id/ivArrow").instance(0)'
kontrak_dua = 'new UiSelector().resourceId("com.nunomics.app.debug:id/ivArrow").instance(1)'
kontrak_tiga = 'new UiSelector().resourceId("com.nunomics.app.debug:id/ivArrow").instance(2)'
kontrak_empat = 'new UiSelector().resourceId("com.nunomics.app.debug:id/ivArrow").instance(3)'

def parse_rupiah_to_float(rupiah_str):
    try:
        # Hilangkan karakter non-numerik dan konversi ke float
        return float(rupiah_str.replace('Rp', '').replace('.', '').replace(',', '.'))
    except ValueError:
        return 0.0
    
def parse_percentage_to_float(percentage_str):
    try:
        # Hilangkan karakter non-numerik dan konversi ke float
        return float(percentage_str.replace('%', '').replace(',', '.'))
    except ValueError:
        return 0.0


class TestHomePage(unittest.TestCase):
    def setUp(self) -> None:
        # Inisialisasi instance dari AksesLogin
        self.login_test = AksesLogin()
        self.login_test.test_login_succes()  # Lakukan login sebelum melanjutkan

        # Mewariskan driver dari AksesLogin
        self.driver = self.login_test.driver

    def test_access_homepage(self):
        try:

            time.sleep(5)
            
            # Klik pada koordinat yang diinginkan
            click_at_coordinates(self.driver, 1100, 688)
            
            # Klik pada tab emas
            WebDriverWait(self.driver, 9).until(
                EC.element_to_be_clickable((AppiumBy.ID, tab_emas))
            ).click()
            
            WebDriverWait(self.driver, 9).until(
                EC.element_to_be_clickable((AppiumBy.ID, see_home))
            ).click()
            
            # Konversi nilai dari elemen tersebut
            pnl_f_p_element_home = WebDriverWait(self.driver, 9).until(
                EC.presence_of_element_located((AppiumBy.ID, pnl_f_p_home))
            )
            pnl_f_a_element_home = WebDriverWait(self.driver, 9).until(
                EC.presence_of_element_located((AppiumBy.ID, pnl_f_a_home))
            )
            pnl_f_p_value_str = pnl_f_p_element_home.text
            pnl_f_p_value_home = parse_percentage_to_float(pnl_f_p_value_str)

            pnl_f_a_value_str = pnl_f_a_element_home.text
            pnl_f_a_value_home = parse_rupiah_to_float(pnl_f_a_value_str)

            # Cetak nilai yang diambil dari elemen
            print(f"Nilai PnL (Amount) dari UI Home : Rp{pnl_f_a_value_home:,.2f}")
            print(f"Nilai PnL (%) dari UI Home: {pnl_f_p_value_home:.2f}%")
            

            # Klik pada halaman emas
            WebDriverWait(self.driver, 9).until(
                EC.element_to_be_clickable((AppiumBy.ID, halaman_emas))
            ).click()
            

            time.sleep(5)
            WebDriverWait(self.driver, 9).until(
                EC.element_to_be_clickable((AppiumBy.ID, see_rped))
            ).click()
            
            perform_swipe(self.driver, 613, 361, 595, 2182) # Scroll
            
            # Ambil elemen untuk `pnl_f_p` dan `pnl_f_a`
            pnl_f_p_element = WebDriverWait(self.driver, 9).until(
                EC.presence_of_element_located((AppiumBy.ID, pnl_f_p))
            )
            pnl_f_a_element = WebDriverWait(self.driver, 9).until(
                EC.presence_of_element_located((AppiumBy.ID, pnl_f_a))
            )

            # Konversi nilai dari elemen tersebut
            pnl_f_p_value_str = pnl_f_p_element.text
            pnl_f_p_value = parse_percentage_to_float(pnl_f_p_value_str)

            pnl_f_a_value_str = pnl_f_a_element.text
            pnl_f_a_value = parse_rupiah_to_float(pnl_f_a_value_str)

            # Cetak nilai yang diambil dari elemen
            print(f"Nilai PnL (Amount) dari UI: Rp{pnl_f_a_value:,.2f}")
            print(f"Nilai PnL (%) dari UI: {pnl_f_p_value:.2f}%")

            # Klik pada kontrak pertama
            WebDriverWait(self.driver, 9).until(
                EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, kontrak_satu))
            ).click()
            
            time.sleep(5)

            # Ambil elemen-elemen untuk kontrak pertama
            elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((AppiumBy.ID, pnl_a))
            )
            
            if len(elements) >= 1:
                one_value_str = elements[0].text
                one_value = parse_rupiah_to_float(one_value_str)
                print(f"Nilai P/L kontrak pertama: Rp{one_value:,.2f}")
            else:
                print("Tidak cukup elemen ditemukan.")
            
            # Ambil nilai `avt` dari kontrak pertama
            avt_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((AppiumBy.ID, avt))
            )
            if len(avt_element) >= 1:
                one_avt_str = avt_element[0].text
                one_avt = parse_rupiah_to_float(one_avt_str)
                print(f"Nilai avt dari kontrak pertama: Rp{one_avt:,.2f}")
            else:
                print("Total AVT tidak ditemukan")
                    
            WebDriverWait(self.driver, 9).until(
                EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, kontrak_satu))
            ).click()

            perform_swipe(self.driver, 609, 1695, 609, 969) # Scroll
            
            # Klik pada kontrak kedua
            WebDriverWait(self.driver, 9).until(
                EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, kontrak_satu))
            ).click()

            # Ambil elemen untuk kontrak kedua
            elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((AppiumBy.ID, pnl_a))
            )

            if len(elements) > 1:
                second_value_str = elements[1].text
                second_value = parse_rupiah_to_float(second_value_str)
                print(f"Nilai P/L kontrak kedua: Rp{second_value:,.2f}")
            else:
                print("Elemen kedua untuk kontrak kedua tidak ditemukan")

            avt_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((AppiumBy.ID, avt))
            )

            if len(avt_element) >= 1:
                two_avt_str = avt_element[0].text
                two_avt = parse_rupiah_to_float(two_avt_str)
                print(f"Nilai avt dari kontrak kedua: Rp{two_avt:,.2f}")
            else:
                print("Total AVT tidak ditemukan untuk kontrak kedua")
            
            WebDriverWait(self.driver, 9).until(
                EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, kontrak_satu))
            ).click()
            
            WebDriverWait(self.driver, 9).until(
                EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, kontrak_dua))
            ).click()
            time.sleep(5)  # Tunggu sebentar setelah klik
            
            # Ambil elemen untuk kontrak ketiga
            elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((AppiumBy.ID, pnl_a))
            )

            if len(elements) >= 3:
                third_value_str = elements[2].text
                third_value = parse_rupiah_to_float(third_value_str)
                print(f"Nilai P/L kontrak ketiga: Rp{third_value:,.2f}")
            else:
                print("Elemen ketiga tidak ditemukan")

            avt_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((AppiumBy.ID, avt))
            )

            if len(avt_element) >= 1:
                three_avt_str = avt_element[0].text
                three_avt = parse_rupiah_to_float(three_avt_str)
                print(f"Nilai avt dari kontrak ketiga: Rp{three_avt:,.2f}")
            else:
                print("Total AVT tidak ditemukan untuk kontrak ketiga")
                
            WebDriverWait(self.driver, 9).until(
                EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, kontrak_dua))
            ).click()
            
            WebDriverWait(self.driver, 9).until(
                EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, kontrak_tiga))
            ).click()
            
            perform_swipe(self.driver, 609, 1695, 609, 969) # Scroll
            
            # Ambil elemen untuk kontrak ketiga
            elements = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((AppiumBy.ID, pnl_a))
            )

            if len(elements) >= 3:
                four_value_str = elements[2].text
                four_value = parse_rupiah_to_float(four_value_str)
                print(f"Nilai P/L kontrak empat: Rp{four_value:,.2f}")
            else:
                print("Elemen empat tidak ditemukan")
            
            avt_element = WebDriverWait(self.driver, 10).until(
                EC.presence_of_all_elements_located((AppiumBy.ID, avt))
            )

            if len(avt_element) >= 1:
                four_avt_str = avt_element[0].text
                four_avt = parse_rupiah_to_float(four_avt_str)
                print(f"Nilai avt dari kontrak empat: Rp{four_avt:,.2f}")
            else:
                print("Total AVT tidak ditemukan untuk kontrak empat")
            

            # Total PnL (Amount)
            total_pnl_amount = one_value + second_value + third_value + four_value
            print(f"Total PnL (Amount): Rp{total_pnl_amount:,.2f}")
            
            # Averages Total metal cost include FeeTax (contoh nilai, pastikan ini float)
            avg_total = one_avt + two_avt + three_avt + four_avt
            if avg_total != 0:
                total_pnl_percent = (total_pnl_amount / avg_total) * 100
                print(f"Total PnL (%): {total_pnl_percent:.2f}%")
            else:
                print("Averages Total metal cost termasuk FeeTax tidak boleh nol.")
                
            # Bandingkan nilai PnL (Amount) dengan yang dihitung
            if round(total_pnl_amount, 2) == round(pnl_f_a_value, 2):
                print("\033[92mTotal PnL (Amount) di halaman saldo rped sesuai dengan nilai yang dihitung.\033[0m")
            else:
                print("\033[91mTotal PnL (Amount) di halaman saldo rped tidak sesuai dengan nilai yang dihitung.\033[0m")

            # Bandingkan nilai PnL (%) dengan yang dihitung
            if round(total_pnl_percent, 2) == round(pnl_f_p_value, 2):
                print("\033[92mTotal PnL (%) di halaman saldo rped sesuai dengan nilai yang dihitung.\033[0m")
            else:
                print("\033[91mTotal PnL (%) di halaman saldo rped tidak sesuai dengan nilai yang dihitung.\033[0m")

            # Bandingkan nilai PnL (Amount) di halaman beranda dengan yang dihitung
            if round(pnl_f_a_value_home, 2) == round(pnl_f_a_value, 2):
                print("\033[92mNilai PnL (Amount) di halaman beranda sesuai dengan nilai yang dihitung.\033[0m")
            else:
                print("\033[91mNilai PnL (Amount) di halaman beranda tidak sesuai dengan nilai yang dihitung.\033[0m")

            # Bandingkan nilai PnL (%) di halaman beranda dengan yang dihitung
            if round(pnl_f_p_value_home, 2) == round(pnl_f_p_value, 2):
                print("\033[92mNilai PnL (%) di halaman beranda sesuai dengan nilai yang dihitung.\033[0m")
            else:
                print("\033[91mNilai PnL (%) di halaman beranda tidak sesuai dengan nilai yang dihitung.\033[0m")

        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

    def tearDown(self) -> None:
        self.login_test.tearDown()

if __name__ == "__main__":
    unittest.main()
