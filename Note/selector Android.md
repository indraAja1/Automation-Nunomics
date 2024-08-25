# **[Android Selectors](https://medium.com/@begunova/finding-mobile-elements-with-robust-appium-locator-strategies-and-selectors-1ea4a7815538)**
Android Selectors in Appium are methods used to identify and locate UI elements within an Android application under test. These selectors allow Appium to interact with elements such as buttons, text, input fields, and more within the app.

## Tools for Identifying Elements:
- **[Appium Inspector Apps](https://github.com/appium/appium-inspector/releases)**
- **[Appium Inspector Website](https://inspector.appiumpro.com/)**

### Below are examples of Selectors and how to use them:
1. **AppiumBy.ID**
    - **Description:** Identifies an element based on the Android resource-id.
    - **Example:**
      ```python
      (AppiumBy.ID, "com.example.app:id/username_input")
      ```

2. **AppiumBy.CLASS_NAME**
    - **Description:** Identifies an element based on the Android class name.
    - **Example:**
      ```python
      (AppiumBy.CLASS_NAME, "android.widget.EditText")
      ```

3. **AppiumBy.ACCESSIBILITY_ID**
    - **Description:** Identifies an element based on the Android content-description.
    - **Example:**
      ```python
      (AppiumBy.ACCESSIBILITY_ID, "login_button")
      ```

4. **AppiumBy.ANDROID_UIAUTOMATOR**
    - **Description:** Uses a UiAutomator string to identify an element.
    - **Example:**
      ```python
      (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Login")')
      (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.example.app:id/login_button")')
      ```

5. **AppiumBy.XPATH**
    - **Description:** Uses XPath to identify an element.
    - **Example:**
      ```python
      (AppiumBy.XPATH, "//android.widget.Button[@text='Login']")
      ```

6. **AppiumBy.NAME**
    - **Description:** Identifies an element based on the "name" attribute (usually the displayed text).
    - **Example:**
      ```python
      (AppiumBy.NAME, "Login")
      ```

7. **AppiumBy.TAG_NAME**
    - **Description:** Identifies an element based on the Android widget type.
    - **Example:**
      ```python
      (AppiumBy.TAG_NAME, "android.widget.Button")
      ```

## Example Usage with Variables

```python
# Variable IDs taken from Appium Selector
uid = (AppiumBy.ID, "com.example.app:id/username_input")
et = (AppiumBy.CLASS_NAME, "android.widget.EditText")
login_btn_aid = (AppiumBy.ACCESSIBILITY_ID, "login_button")
login_txt = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().text("Login")')
login_resid = (AppiumBy.ANDROID_UIAUTOMATOR, 'new UiSelector().resourceId("com.example.app:id/login_button")')
login_xpath = (AppiumBy.XPATH, "//android.widget.Button[@text='Login']")
login_name = (AppiumBy.NAME, "Login")
btn_tag = (AppiumBy.TAG_NAME, "android.widget.Button")

# Example usage of the shortened variables with WebDriverWait

# Wait for and find the element using ID
username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(uid)
)
username.send_keys("your_username")

# Wait for and find the element using CLASS_NAME
edit_text = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(et)
)

# Wait for and find the element using ACCESSIBILITY_ID
login_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(login_btn_aid)
)
login_btn.click()

# Wait for and find the element using ANDROID_UIAUTOMATOR (based on text)
login_txt_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(login_txt)
)
login_txt_btn.click()

# Wait for and find the element using ANDROID_UIAUTOMATOR (based on resource ID)
login_resid_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(login_resid)
)
login_resid_btn.click()

# Wait for and find the element using XPath
login_xpath_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(login_xpath)
)
login_xpath_btn.click()

# Wait for and find the element using NAME
login_name_btn = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable(login_name)
)
login_name_btn.click()

# Wait for and find the element using TAG_NAME
btn = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located(btn_tag)
)
btn.click()

