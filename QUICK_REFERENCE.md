# 🚀 Quick Reference Guide

A cheat sheet for common Android development tasks with this template.

## 📋 Essential Commands

### Building

```bash
# Build debug APK
./gradlew assembleDebug

# Build release APK
./gradlew assembleRelease

# Build app bundle (for Play Store)
./gradlew bundleRelease

# Clean build
./gradlew clean
```

### Installing

```bash
# Install debug version on connected device
./gradlew installDebug

# Install release version
./gradlew installRelease

# Uninstall app
adb uninstall com.androidcommandcenter
```

### Testing

```bash
# Run unit tests
./gradlew test

# Run tests on connected device
./gradlew connectedAndroidTest

# Run specific test
./gradlew test --tests "TestClassName"
```

### Debugging

```bash
# View logs
adb logcat

# View logs for your app only
adb logcat | grep "com.androidcommandcenter"

# Clear logs
adb logcat -c

# Take screenshot
adb shell screencap -p /sdcard/screenshot.png
adb pull /sdcard/screenshot.png

# Record screen video
adb shell screenrecord /sdcard/video.mp4
adb pull /sdcard/video.mp4
```

## 📱 Device Management

```bash
# List connected devices
adb devices

# Check device info
adb shell getprop ro.product.model
adb shell getprop ro.build.version.release

# Install APK
adb install app/build/outputs/apk/debug/app-debug.apk

# Push file to device
adb push local-file.txt /sdcard/

# Pull file from device
adb pull /sdcard/remote-file.txt
```

## 🎨 Common File Locations

### Source Code
```
app/src/main/java/com/lindy/android/
├── MainActivity.kt          # Main screen
└── [Add your activities here]
```

### Layouts
```
app/src/main/res/layout/
├── activity_main.xml        # Main screen layout
└── [Add your layouts here]
```

### Resources
```
app/src/main/res/
├── values/
│   ├── strings.xml         # Text strings
│   ├── colors.xml          # Color definitions
│   └── themes.xml          # App themes
├── drawable/               # Images and icons
└── mipmap-*/              # App launcher icons
```

## 🔧 Common Modifications

### Change App Name
**File**: `app/src/main/res/values/strings.xml`
```xml
<string name="app_name">Your App Name</string>
```

### Change Package Name
1. Refactor package in Android Studio
2. **File**: `app/build.gradle.kts`
```kotlin
applicationId = "com.yourcompany.yourapp"
```
3. **File**: `app/src/main/AndroidManifest.xml`
```xml
<manifest package="com.yourcompany.yourapp">
```

### Change App Version
**File**: `app/build.gradle.kts`
```kotlin
versionCode = 2           // Increment by 1
versionName = "1.1"       // Your version string
```

### Change Theme Color
**File**: `app/src/main/res/values/colors.xml`
```xml
<color name="lindy_primary">#FF2196F3</color>
```

### Add Permission
**File**: `app/src/main/AndroidManifest.xml`
```xml
<uses-permission android:name="android.permission.CAMERA" />
```

## 📚 Android Studio Shortcuts

### Navigation
- **Ctrl/Cmd + N**: Open class
- **Ctrl/Cmd + Shift + N**: Open file
- **Ctrl/Cmd + B**: Go to declaration
- **Ctrl/Cmd + Alt + Left/Right**: Navigate back/forward

### Editing
- **Ctrl/Cmd + Space**: Code completion
- **Alt + Enter**: Quick fix
- **Ctrl/Cmd + Alt + L**: Format code
- **Ctrl/Cmd + D**: Duplicate line
- **Ctrl/Cmd + Y**: Delete line

### Refactoring
- **Shift + F6**: Rename
- **Ctrl/Cmd + Alt + M**: Extract method
- **Ctrl/Cmd + Alt + V**: Extract variable

### Building
- **Ctrl/Cmd + F9**: Build project
- **Shift + F10**: Run app
- **Shift + F9**: Debug app

## 🐛 Debugging Tips

### Check Logs
```kotlin
import android.util.Log

Log.d("TAG", "Debug message")
Log.i("TAG", "Info message")
Log.w("TAG", "Warning message")
Log.e("TAG", "Error message")
```

### Breakpoints
1. Click line number gutter to set breakpoint
2. Run in Debug mode (Shift + F9)
3. Step through: F8 (over), F7 (into), Shift + F8 (out)

### Common Issues

#### App Crashes
1. Check Logcat for stack trace
2. Look for red error messages
3. Check line numbers in stack trace

#### UI Not Updating
1. Verify layout file name matches in `setContentView()`
2. Clean and rebuild project
3. Invalidate caches: File → Invalidate Caches

#### Gradle Sync Failed
1. Check build.gradle.kts syntax
2. File → Sync Project with Gradle Files
3. Update Gradle wrapper if needed

## 📦 Adding Dependencies

**File**: `app/build.gradle.kts`

```kotlin
dependencies {
    // Add library
    implementation("androidx.recyclerview:recyclerview:1.3.2")
    
    // For testing
    testImplementation("junit:junit:4.13.2")
}
```

After adding, click "Sync Now" in the banner.

## 🎨 Material Design Components

### Buttons
```xml
<com.google.android.material.button.MaterialButton
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="Click Me" />
```

### Text Input
```xml
<com.google.android.material.textfield.TextInputLayout
    android:layout_width="match_parent"
    android:layout_height="wrap_content">
    
    <com.google.android.material.textfield.TextInputEditText
        android:layout_width="match_parent"
        android:layout_height="wrap_content"
        android:hint="Enter text" />
</com.google.android.material.textfield.TextInputLayout>
```

### CardView
```xml
<com.google.android.material.card.MaterialCardView
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    app:cardCornerRadius="8dp"
    app:cardElevation="4dp">
    
    <!-- Content here -->
    
</com.google.android.material.card.MaterialCardView>
```

## 🔄 Git Commands

```bash
# Check status
git status

# Add files
git add .

# Commit changes
git commit -m "Your commit message"

# Push to remote
git push origin main

# Pull latest changes
git pull origin main

# Create new branch
git checkout -b feature/new-feature

# View commit history
git log --oneline
```

## 📊 Performance Tips

### Optimize Images
- Use WebP format
- Compress images before adding
- Use vector drawables when possible

### Reduce APK Size
- Enable ProGuard (already configured)
- Remove unused resources
- Use App Bundle instead of APK

### Improve Speed
- Use ViewBinding (already configured)
- Avoid doing work on main thread
- Use Kotlin Coroutines for async work

## 🆘 Emergency Fixes

### Reset Git Changes
```bash
git checkout .
git clean -fd
```

### Reset Gradle
```bash
./gradlew clean
rm -rf .gradle/
```

### Clear Android Studio Cache
```
File → Invalidate Caches → Invalidate and Restart
```

### Reinstall App
```bash
adb uninstall com.androidcommandcenter
./gradlew installDebug
```

## 📞 Quick Links

- [Android Docs](https://developer.android.com/docs)
- [Kotlin Docs](https://kotlinlang.org/docs/)
- [Material Design](https://m3.material.io/)
- [Stack Overflow](https://stackoverflow.com/questions/tagged/android)

## 💡 Pro Tips

1. **Use TODO comments**: `// TODO: Implement this feature`
2. **Extract strings**: Always use string resources
3. **Test on rotation**: Cmd/Ctrl + F11 in emulator
4. **Use Layout Inspector**: Tools → Layout Inspector
5. **Profile your app**: Tools → Profiler

---

Keep this reference handy while developing! 📌
