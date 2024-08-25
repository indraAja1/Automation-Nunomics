# **Appium Desktop / Install Appium Server Node.js**

**Note:** Note: You can also use **[Appium Desktop](https://github.com/appium/appium-desktop)**.

**Appium Desktop** Appium Desktop is an application for Mac, Windows, and Linux that provides a graphical interface for the Appium Server. With Appium Desktop, you can:

- **Configure server options** - Easily configure through the UI.
- **Manage the server** - Start or stop the server with a click of a button.
- **View logs** - Monitor logs in real-time.

No need for Node.js or NPM because Appium Desktop includes a Node.js runtime.

**Appium Server Node.js**

- **Appium Server** - Set up and run automated tests for Android and iOS applications.
- **Node.js** - The JavaScript runtime required to run the Appium Server.
- **NPM** - A tool to install the Appium Server in Node.js.

### Here’s how to install Appium using Node.js

1. **Instal Node.js**

Appium requires Node.js to run. If Node.js is not installed on your system, you can download and install it from the official **[Node.js](https://nodejs.org/)** website. Choose the LTS (Long Term Support) version for better stability.

2. **Install Appium Server via npm**

Once Node.js is installed, you can install the Appium server using npm (Node Package Manager), which is part of the Node.js installation.

Open a terminal or command prompt, and run the following command:

```bash
npm install -g appium
```

The above command will install Appium globally on your system, so you can run it from anywhere.

3. **Start the appium server**

After installation is complete, you can start the Appium server with the following command:

```bash
appium
```

This will start the Appium server on the default port (`4723`). If you want to run it on a different port or customize other configurations, you can use additional flags like this:

```bash
appium server -p 4723 -a 127.0.0.1 -pa /wd/hub --allow-cors
```

- **`p 4723`**: Sets the Appium server port to `4723`.
- **`a 127.0.0.1`**: Sets the server IP address to `127.0.0.1` (localhost).
- **`pa /wd/hub`**: Sets the base path to `/wd/hub`.
- **`-allow-cors`**: Enables CORS to allow requests from different domains.

4. **Verify Installation**

To ensure that Appium has been installed correctly, you can run:

```bash
appium -v
```

This will display the installed version of Appium.

### Note on adb :

1. **How to find AppPackage & MainActivity**

```shell
adb shell dumpsys window | find "mCurrentFocus"
```

2. **How to check all SMS & the latest SMS**

```shell
adb shell content query --uri content://sms/inbox --projection body,address,date
```

3. **How to find the latest OTP from SMS AUTHMSG**

```shell
$messages = adb shell content query --uri content://sms/inbox --projection body,address,date
$filtered = $messages | Where-Object { $_ -match "AUTHMSG" }
$sorted = $filtered | Sort-Object { [long]($_ -replace ".*date=(\d+)", '$1') } -Descending
$latest = $sorted | Select-Object -First 1
$otp = [regex]::Match($latest, "\d{6}").Value
$otp

```