# **Appium Desktop / Install Appium Server Node.js**

**Note:** Anda juga bisa menggunakan **[Appium Desktop](https://github.com/appium/appium-desktop)**.

**Appium Desktop** adalah aplikasi untuk Mac, Windows, dan Linux yang menyediakan antarmuka grafis untuk Server Appium. Dengan Appium Desktop, Anda dapat:

- **Mengatur opsi server** - Konfigurasi mudah melalui UI.
- **Mengelola server** - Memulai atau menghentikan server dengan klik tombol.
- **Melihat log** - Pantau log secara real-time.

Tidak perlu Node.js atau NPM karena Appium Desktop sudah mencakup runtime Node.js.

**Appium Server Node.js**

- **Appium Server** -  Mengatur dan menjalankan pengujian otomatis untuk aplikasi Android dan iOS.
- **Node.js** - Runtime JavaScript yang diperlukan untuk menjalankan Appium Server.
- **NPM** - Alat untuk menginstal Appium Server di Node.js.

### Berikut install Appium menggunakan node.js 
1. **Instal Node.js**

Appium membutuhkan Node.js untuk berjalan. Jika Node.js belum terinstal di sistem Anda, Anda dapat mengunduh dan menginstalnya dari **[situs resmi Node.js](https://nodejs.org/)**. Pilih versi LTS (Long Term Support) untuk stabilitas yang lebih baik.

2. **Instal Appium Server melalui npm**

Setelah Node.js terinstal, Anda dapat menginstal Appium server menggunakan npm (Node Package Manager), yang merupakan bagian dari instalasi Node.js.

Buka terminal atau command prompt, dan jalankan perintah berikut:

```bash
npm install -g appium
```

Perintah di atas akan menginstal Appium secara global di sistem Anda, sehingga Anda dapat menjalankannya dari mana saja.

3. **Jalankan Appium Server**

Setelah instalasi selesai, Anda bisa menjalankan Appium server dengan perintah berikut:

```bash
appium
```

Ini akan memulai Appium server pada port default (`4723`). Jika Anda ingin menjalankannya di port yang berbeda atau menyesuaikan konfigurasi lainnya, Anda dapat menggunakan flag tambahan seperti berikut:

```bash
appium server -p 4723 -a 127.0.0.1 -pa /wd/hub --allow-cors
```

- **`p 4723`**: Mengatur port server Appium ke 4723.
- **`a 127.0.0.1`**: Mengatur alamat IP server ke `127.0.0.1` (localhost).
- **`pa /wd/hub`**: Mengatur path dasar (base path) ke `/wd/hub`.
- **`-allow-cors`**: Mengaktifkan CORS untuk memungkinkan permintaan dari domain yang berbeda`

4. **Verifikasi Instalasi**

Untuk memastikan bahwa Appium telah terinstal dengan benar, Anda dapat menjalankan:

```bash
appium -v
```

Ini akan menampilkan versi Appium yang terinstal.


### Note adb :

1. **Cara mencari AppPackage & MainActivity***

```shell
adb shell dumpsys window | find "mCurrentFocus"
```

2. **Cara Check semua sms & sms terbaru**
```shell
adb shell content query --uri content://sms/inbox --projection body,address,date
```

3. **Cara mencari OTP terbaru dari SMS AUTHMSG**

```shell
$messages = adb shell content query --uri content://sms/inbox --projection body,address,date
$filtered = $messages | Where-Object { $_ -match "AUTHMSG" }
$sorted = $filtered | Sort-Object { [long]($_ -replace ".*date=(\d+)", '$1') } -Descending
$latest = $sorted | Select-Object -First 1
$otp = [regex]::Match($latest, "\d{6}").Value
$otp

```