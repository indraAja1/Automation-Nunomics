import time
import subprocess
import re

def get_latest_sms():
    result = subprocess.run(
        ["adb", "shell", "content", "query", "--uri", "content://sms/inbox", "--projection", "body,address,date"],
        capture_output=True,
        text=True
    )
    messages = result.stdout.splitlines()
    
    # Filter dari sms 'AUTHMSG'
    filtered_messages = [msg for msg in messages if "AUTHMSG" in msg]
    
    # Urutkan pesan berdasarkan tanggal secara menurun
    sorted_messages = sorted(
        filtered_messages,
        key=lambda x: int(re.search(r'date=(\d+)', x).group(1)),
        reverse=True
    )
    
    # Get pesan terbaru
    latest_message = sorted_messages[0] if sorted_messages else ""
    
    return latest_message

def parse_otp(sms_body):
    match = re.search(r'\b\d{6}\b', sms_body)
    if match:
        return match.group(0)
    return None

def get_otp_with_timeout(timeout=130, poll_interval=14):
    start_time = time.time()
    last_otp = None

    while time.time() - start_time < timeout:
        # Tambahkan penundaan sebelum memulai pengambilan SMS
        time.sleep(6)
        sms_info = get_latest_sms()
        otp = parse_otp(sms_info)
        if otp and otp != last_otp:
            last_otp = otp
            print(f"New OTP : {otp}")
            return otp
        time.sleep(poll_interval)  # Tunggu beberapa detik sebelum mencoba lagi

    print("Gagal mendapatkan OTP dari SMS dalam batas waktu yang ditentukan.")
    return None
