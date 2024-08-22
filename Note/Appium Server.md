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

Ini akan menjalankan server Appium di port `4725,` host `127.0.0.1` , remote path `/wd/hub`

4. **Verifikasi Instalasi**

Untuk memastikan bahwa Appium telah terinstal dengan benar, Anda dapat menjalankan:

```bash
appium -v
```

Ini akan menampilkan versi Appium yang terinstal.
