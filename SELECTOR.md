## **[Selector Android](https://medium.com/@begunova/finding-mobile-elements-with-robust-appium-locator-strategies-and-selectors-1ea4a7815538)**


1. **AppiumBy.ID**
    - **Deskripsi:** Mengidentifikasi elemen berdasarkan resource-id Android.
    - **Contoh:**
      ```python
      (AppiumBy.ID, "com.example.app:id/username_input")
      ```

2. **AppiumBy.CLASS_NAME**
    - **Deskripsi:** Mengidentifikasi elemen berdasarkan nama kelas Android.
    - **Contoh:**
      ```python
      (AppiumBy.CLASS_NAME, "android.widget.EditText")
      ```

3. **AppiumBy.ACCESSIBILITY_ID**
    - **Deskripsi:** Mengidentifikasi elemen berdasarkan content-description Android.
    - **Contoh:**
      ```python
      (AppiumBy.ACCESSIBILITY_ID, "login_button")
      ```

4. **AppiumBy.ANDROID_UIAUTOMATOR**
    - **Deskripsi:** Menggunakan UiAutomator string untuk mengidentifikasi elemen.
    - **Contoh:**
      ```python
      (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Login")')
      (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.example.app:id/login_button")')
      ```

5. **AppiumBy.XPATH**
    - **Deskripsi:** Menggunakan XPath untuk mengidentifikasi elemen.
    - **Contoh:**
      ```python
      (AppiumBy.XPATH, "//android.widget.Button[@text='Login']")
      ```

6. **AppiumBy.NAME**
    - **Deskripsi:** Mengidentifikasi elemen berdasarkan atribut "name" (biasanya sama dengan teks yang ditampilkan).
    - **Contoh:**
      ```python
      (AppiumBy.NAME, "Login")
      ```

7. **AppiumBy.TAG_NAME**
    - **Deskripsi:** Mengidentifikasi elemen berdasarkan jenis widget Android.
    - **Contoh:**
      ```python
      (AppiumBy.TAG_NAME, "android.widget.Button")
      ```

## Contoh Penggunaan dengan Variable

```python
# Variable ID
# Di ambil dari APPIUM INSPECTOR
# Variabel selector dengan penamaan singkat
uid = (AppiumBy.ID, "com.example.app:id/username_input")
et = (AppiumBy.CLASS_NAME, "android.widget.EditText")
login_btn_aid = (AppiumBy.ACCESSIBILITY_ID, "login_button")
login_txt = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Login")')
login_resid = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.example.app:id/login_button")')
login_xpath = (AppiumBy.XPATH, "//android.widget.Button[@text='Login']")
login_name = (AppiumBy.NAME, "Login")
btn_tag = (AppiumBy.TAG_NAME, "android.widget.Button")

# Penggunaan variabel singkat dengan WebDriverWait

# Menunggu dan menemukan elemen menggunakan ID
username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(uid)
)
username.send_keys("your_username")

# Menunggu dan menemukan elemen menggunakan CLASS_NAME
edit_text = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(et)
)

# Menunggu dan menemukan elemen menggunakan ACCESSIBILITY_ID
login_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(login_btn_aid)
)
login_btn.click()

# Menunggu dan menemukan elemen menggunakan ANDROID_UIAUTOMATOR (berdasarkan teks)
login_txt_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(login_txt)
)
login_txt_btn.click()

# Menunggu dan menemukan elemen menggunakan ANDROID_UIAUTOMATOR (berdasarkan resource ID)
login_resid_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(login_resid)
)
login_resid_btn.click()

# Menunggu dan menemukan elemen menggunakan XPath
login_xpath_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(login_xpath)
)
login_xpath_btn.click()

# Menunggu dan menemukan elemen menggunakan NAME
login_name_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(login_name)
)
login_name_btn.click()

# Menunggu dan menemukan elemen menggunakan TAG_NAME
btn = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(btn_tag)
)
btn.click()

```