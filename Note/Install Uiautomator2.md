# **Instalasi UiAutomator2 secara Otomatis dengan Appium**

1. **Pastikan Appium Terinstal**:
    - Pastikan Anda sudah menginstal Appium di sistem Anda. Jika belum, Anda dapat menginstalnya menggunakan npm:
        
        ```
        npm install -g appium
        
        ```
        
2. **Jalankan Appium Server**:
    - Jalankan Appium server dari Command Prompt atau Terminal:
        
        ```
        appium
        
        ```
3. **Siapkan Desired Capabilities**:
    - Buat desired capabilities untuk mengonfigurasi sesi Appium dengan `UiAutomator2`. Berikut adalah contoh desired capabilities:
        
        ```json
        {
          "platformName": "Android",
          "deviceName": "emulator-5554",
          "automationName": "UiAutomator2",
          "app": "path/to/your/app.apk"
        }
        
        ```
        
4. **Mulai Sesi Appium**:
    - Mulai sesi Appium dengan desired capabilities yang sudah disiapkan. Appium akan secara otomatis menginstal server UiAutomator2 di perangkat atau emulator jika belum terinstal.


# ** Instalasi UiAutomator2 secara Manual dengan Appium**

### Langkah-langkah Instalasi UiAutomator2 secara Manual

1. **Unduh File APK UiAutomator2**:
    - Unduh file APK untuk UiAutomator2 server dan test server dari repositori GitHub Appium:
        - [UiAutomator2 Server APK](https://github.com/appium/appium-uiautomator2-server/releases)
        - [UiAutomator2 Server Test APK](https://github.com/appium/appium-uiautomator2-server/releases)
2. **Instal APK di Perangkat atau Emulator**:
    - Instal APK menggunakan ADB. Jalankan perintah berikut untuk masing-masing APK:
        
        ```
        adb install path/to/appium-uiautomator2-server-debug-androidTest.apk
        adb install path/to/appium-uiautomator2-server-vX.X.X.apk
        
        ```
        
    - Gantilah `path/to/` dengan path yang sesuai ke file APK yang telah diunduh.

### Contoh Lengkap Menggunakan Desired Capabilities

Berikut adalah contoh lengkap konfigurasi desired capabilities yang digunakan untuk memulai sesi Appium dengan UiAutomator2:

```json
{
  "platformName": "Android",
  "deviceName": "emulator-5554",
  "automationName": "UiAutomator2",
  "app": "path/to/your/app.apk"
}

```

### Verifikasi Instalasi

Setelah memulai sesi Appium, Anda dapat memverifikasi apakah server UiAutomator2 terinstal dan berjalan dengan benar dengan memeriksa log Appium. Anda harus melihat sesuatu seperti ini di log:

```
Installing 'io.appium.uiautomator2.server' and 'io.appium.uiautomator2.server.test'
Starting UiAutomator2 server

```
