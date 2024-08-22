import subprocess
import re

def monitor_logcat_for_otp():
    # Mulai proses adb logcat
    process = subprocess.Popen(['adb', 'logcat'], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    try:
        # Monitor logcat output secara real-time
        while True:
            line = process.stdout.readline()
            if not line:
                break
            
            # Cek apakah baris tersebut mengandung OTP 6 digit, termasuk yang diawali dengan nol
            otp_match = re.search(r'\b\d{6}\b', line)  # OTP 6 digit
            if otp_match:
                otp_code = otp_match.group(0)
                print(f"OTP ditemukan: {otp_code}")
                return otp_code  # Kembalikan OTP yang ditemukan
    except KeyboardInterrupt:
        print("Monitoring dihentikan.")
    finally:
        process.terminate()

# Menggunakan fungsi untuk memonitor logcat
otp_code = monitor_logcat_for_otp()
if otp_code:
    print(f"OTP yang diterima: {otp_code}")
    # Gunakan Appium untuk menginput OTP ini ke aplikasi
    # otp_input = WebDriverWait(self.driver, 10).until(
    #     EC.visibility_of_element_located((AppiumBy.ID, 'otp_input_field_id'))
    # )
    # otp_input.send_keys(otp_code)
