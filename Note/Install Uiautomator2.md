# **Automatic Installation of UiAutomator2 with Appium**

1. **Ensure Appium is Installed**:
    - Make sure you have Appium installed on your system. If not, you can install it using npm:
        
        ```bash
        npm install -g appium
        ```
        
2. **Start the Appium Server**:
    - Start the Appium server from Command Prompt or Terminal:
        
        ```bash
        appium
        ```
        
3. **Set Up Desired Capabilities**:
    - Create desired capabilities to configure the Appium session with `UiAutomator2`. Here is an example of the desired capabilities:
        
        ```json
        {
          "platformName": "Android",
          "deviceName": "emulator-5554",
          "automationName": "UiAutomator2",
          "app": "path/to/your/app.apk"
        }
        ```
        
4. **Start the Appium Session**:
    - Start the Appium session with the desired capabilities you have set up. Appium will automatically install the UiAutomator2 server on the device or emulator if it is not already installed.

# **Manual Installation of UiAutomator2 with Appium**

### Steps for Manual Installation of UiAutomator2

1. **Download the UiAutomator2 APK Files**:
    - Download the APK files for the UiAutomator2 server and test server from the Appium GitHub repository:
        - [UiAutomator2 Server APK](https://github.com/appium/appium-uiautomator2-server/releases)
        - [UiAutomator2 Server Test APK](https://github.com/appium/appium-uiautomator2-server/releases)
        
2. **Install the APKs on the Device or Emulator**:
    - Install the APKs using ADB. Run the following commands for each APK:
        
        ```bash
        adb install path/to/appium-uiautomator2-server-debug-androidTest.apk
        adb install path/to/appium-uiautomator2-server-vX.X.X.apk
        ```
        
    - Replace `path/to/` with the appropriate path to the APK files you have downloaded.

### Complete Example Using Desired Capabilities

Here is a complete example of the desired capabilities configuration used to start an Appium session with UiAutomator2:

```json
{
  "platformName": "Android",
  "deviceName": "emulator-5554",
  "automationName": "UiAutomator2",
  "app": "path/to/your/app.apk"
}
```

### Verify Installation
After starting the Appium session, you can verify that the UiAutomator2 server is installed and running correctly by checking the Appium log. You should see something like this in the log:

```shell
Installing 'io.appium.uiautomator2.server' and 'io.appium.uiautomator2.server.test'
Starting UiAutomator2 server
```