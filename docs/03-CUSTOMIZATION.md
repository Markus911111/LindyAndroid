# 🎨 Customization Guide

Learn how to customize the Android Command Center template to make it your own app.

## 📋 Table of Contents

1. [Changing App Name](#changing-app-name)
2. [Changing Package Name](#changing-package-name)
3. [Customizing Colors](#customizing-colors)
4. [Changing App Icon](#changing-app-icon)
5. [Modifying Layouts](#modifying-layouts)
6. [Updating Theme](#updating-theme)
7. [Adding New Strings](#adding-new-strings)
8. [Customizing Welcome Screen](#customizing-welcome-screen)

## 📱 Changing App Name

The app name appears in the launcher and app header.

### Step 1: Update strings.xml

**File**: `app/src/main/res/values/strings.xml`

```xml
<resources>
    <string name="app_name">Your App Name</string>
</resources>
```

### Step 2: Verify in AndroidManifest.xml

**File**: `app/src/main/AndroidManifest.xml`

```xml
<application
    android:label="@string/app_name">
```

### Step 3: Build and Run

```bash
./gradlew clean assembleDebug
```

Your app now displays the new name! 🎉

---

## 📦 Changing Package Name

Package name is your app's unique identifier (e.g., `com.yourcompany.yourapp`).

### Method 1: Using Android Studio (Recommended)

1. **Open Android Studio**
2. Switch to **Project** view (dropdown at top-left)
3. Navigate to: `app/src/main/java/com/lindy/android`
4. **Right-click** on the package folder
5. Select **Refactor** → **Rename**
6. Choose **Rename Package**
7. Enter new name: `com.yourcompany.yourapp`
8. Click **Refactor**
9. Review changes and click **Do Refactor**

### Method 2: Manual Steps

#### 1. Update Gradle Configuration

**File**: `app/build.gradle.kts`

```kotlin
android {
    namespace = "com.yourcompany.yourapp"
    
    defaultConfig {
        applicationId = "com.yourcompany.yourapp"
        // ... rest of config
    }
}
```

#### 2. Update AndroidManifest.xml

**File**: `app/src/main/AndroidManifest.xml`

```xml
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.yourcompany.yourapp">
```

#### 3. Move Source Files

```bash
# Create new package structure
mkdir -p app/src/main/java/com/yourcompany/yourapp

# Move files
mv app/src/main/java/com/lindy/android/* \
   app/src/main/java/com/yourcompany/yourapp/

# Remove old directory
rm -rf app/src/main/java/com/lindy
```

#### 4. Update Package Declaration in Kotlin Files

**File**: `MainActivity.kt`

```kotlin
package com.yourcompany.yourapp  // Update this line

import android.os.Bundle
// ... rest of imports

class MainActivity : AppCompatActivity() {
    // ... rest of code
}
```

#### 5. Clean and Rebuild

```bash
./gradlew clean
./gradlew build
```

### ⚠️ Important Notes

- Package name must be unique on Google Play
- Use reverse domain notation: `com.company.app`
- Use lowercase letters and dots only
- Cannot start with numbers
- Once published, **cannot be changed**

---

## 🎨 Customizing Colors

Change the color scheme to match your brand.

### Primary Colors

**File**: `app/src/main/res/values/colors.xml`

```xml
<resources>
    <!-- Your brand colors -->
    <color name="lindy_primary">#FF2196F3</color>        <!-- Main color -->
    <color name="lindy_primary_dark">#FF1976D2</color>   <!-- Darker shade -->
    <color name="lindy_accent">#FFFF4081</color>         <!-- Accent color -->
    <color name="lindy_background">#FFF5F5F5</color>     <!-- Background -->
    
    <!-- Add your custom colors -->
    <color name="my_brand_color">#FF009688</color>
</resources>
```

### Apply Colors to Theme

**File**: `app/src/main/res/values/themes.xml`

```xml
<style name="Theme.AndroidCommandCenter" parent="Theme.Material3.DayNight.NoActionBar">
    <item name="colorPrimary">@color/lindy_primary</item>
    <item name="colorPrimaryVariant">@color/lindy_primary_dark</item>
    <item name="colorOnPrimary">@color/white</item>
    <item name="colorSecondary">@color/lindy_accent</item>
</style>
```

### Dark Theme Colors

**File**: `app/src/main/res/values-night/themes.xml`

```xml
<style name="Theme.AndroidCommandCenter" parent="Theme.Material3.DayNight.NoActionBar">
    <item name="colorPrimary">@color/purple_200</item>
    <item name="android:colorBackground">@color/black</item>  <!-- AMOLED black -->
</style>
```

### Color Picker Tools

- [Material Design Color Tool](https://material.io/resources/color/)
- [Coolors.co](https://coolors.co/)
- [Adobe Color](https://color.adobe.com/)

### Testing Colors

1. Build app: `./gradlew assembleDebug`
2. Run on device
3. Toggle dark mode: Settings → Display → Dark theme
4. Verify both themes look good

---

## 🖼️ Changing App Icon

Replace the default launcher icon with your own.

### Icon Requirements

- **Size**: 512x512 pixels minimum
- **Format**: PNG with transparency
- **Shapes**: Square or round
- **Colors**: Match your brand

### Method 1: Using Android Studio (Easiest)

1. **Right-click** `res` folder
2. Select **New** → **Image Asset**
3. Choose **Launcher Icons (Adaptive and Legacy)**
4. Select image file or clip art
5. Configure foreground and background
6. Click **Next** → **Finish**
7. Studio generates all sizes automatically

### Method 2: Manual Replacement

Create icons for each density:

```
mipmap-mdpi/ic_launcher.png       48x48px
mipmap-hdpi/ic_launcher.png       72x72px
mipmap-xhdpi/ic_launcher.png      96x96px
mipmap-xxhdpi/ic_launcher.png     144x144px
mipmap-xxxhdpi/ic_launcher.png    192x192px  ← Galaxy S24
```

Replace files in each `mipmap-*` folder.

### Method 3: Adaptive Icon (Android 8.0+)

**File**: `mipmap-anydpi-v26/ic_launcher.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<adaptive-icon xmlns:android="http://schemas.android.com/apk/res/android">
    <background android:drawable="@color/lindy_primary"/>
    <foreground android:drawable="@drawable/ic_launcher_foreground"/>
</adaptive-icon>
```

Create foreground drawable:

**File**: `drawable/ic_launcher_foreground.xml`

```xml
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="108dp"
    android:height="108dp"
    android:viewportWidth="108"
    android:viewportHeight="108">
    <!-- Your icon vector paths -->
</vector>
```

### Icon Design Tools

- [Android Asset Studio](https://romannurik.github.io/AndroidAssetStudio/)
- [Figma](https://www.figma.com/)
- [Canva](https://www.canva.com/)
- [GIMP](https://www.gimp.org/) (free)

### Testing Your Icon

1. Build and install: `./gradlew installDebug`
2. Check launcher (home screen)
3. Check app switcher (recent apps)
4. Check settings (app info)
5. Test on different backgrounds

---

## 📐 Modifying Layouts

Change the user interface design.

### Main Screen Layout

**File**: `app/src/main/res/layout/activity_main.xml`

```xml
<?xml version="1.0" encoding="utf-8"?>
<androidx.constraintlayout.widget.ConstraintLayout 
    xmlns:android="http://schemas.android.com/apk/res/android"
    xmlns:app="http://schemas.android.com/apk/res-auto"
    android:layout_width="match_parent"
    android:layout_height="match_parent">

    <!-- Add your views here -->
    
    <TextView
        android:id="@+id/my_text"
        android:layout_width="wrap_content"
        android:layout_height="wrap_content"
        android:text="@string/my_string"
        android:textSize="20sp"
        app:layout_constraintTop_toTopOf="parent"
        app:layout_constraintStart_toStartOf="parent"
        app:layout_constraintEnd_toEndOf="parent" />

</androidx.constraintlayout.widget.ConstraintLayout>
```

### Common UI Components

#### TextView (Display Text)

```xml
<TextView
    android:id="@+id/title_text"
    android:layout_width="wrap_content"
    android:layout_height="wrap_content"
    android:text="@string/title"
    android:textSize="24sp"
    android:textStyle="bold"
    android:textColor="?attr/colorPrimary" />
```

#### Button (Material Design)

```xml
<com.google.android.material.button.MaterialButton
    android:id="@+id/action_button"
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:text="@string/button_text"
    app:cornerRadius="8dp" />
```

#### EditText (Text Input)

```xml
<com.google.android.material.textfield.TextInputLayout
    android:layout_width="match_parent"
    android:layout_height="wrap_content"
    android:hint="@string/hint_text">
    
    <com.google.android.material.textfield.TextInputEditText
        android:id="@+id/input_field"
        android:layout_width="match_parent"
        android:layout_height="wrap_content" />
        
</com.google.android.material.textfield.TextInputLayout>
```

#### ImageView (Display Image)

```xml
<ImageView
    android:id="@+id/image_view"
    android:layout_width="200dp"
    android:layout_height="200dp"
    android:src="@drawable/my_image"
    android:contentDescription="@string/image_description"
    android:scaleType="centerCrop" />
```

### Layout Preview

In Android Studio:
1. Open layout XML file
2. Click **Split** or **Design** tab
3. See live preview
4. Test different device sizes

---

## 🎭 Updating Theme

Customize the overall look and feel.

### Theme Structure

**File**: `app/src/main/res/values/themes.xml`

```xml
<resources>
    <style name="Theme.AndroidCommandCenter" parent="Theme.Material3.DayNight.NoActionBar">
        <!-- Colors -->
        <item name="colorPrimary">@color/lindy_primary</item>
        <item name="colorOnPrimary">@color/white</item>
        <item name="colorSecondary">@color/lindy_accent</item>
        
        <!-- Status bar -->
        <item name="android:statusBarColor">@color/lindy_primary_dark</item>
        <item name="android:windowLightStatusBar">false</item>
        
        <!-- Navigation bar -->
        <item name="android:navigationBarColor">@color/lindy_primary_dark</item>
        
        <!-- Background -->
        <item name="android:colorBackground">@color/lindy_background</item>
        
        <!-- Text -->
        <item name="android:textColorPrimary">@color/black</item>
        
        <!-- Shapes -->
        <item name="shapeAppearanceSmallComponent">@style/ShapeAppearance.App.SmallComponent</item>
    </style>
    
    <!-- Custom shape for rounded corners -->
    <style name="ShapeAppearance.App.SmallComponent" parent="">
        <item name="cornerFamily">rounded</item>
        <item name="cornerSize">12dp</item>
    </style>
</resources>
```

### Material Theme Builder

Use [Material Theme Builder](https://m3.material.io/theme-builder) to:
1. Upload your brand colors
2. Generate complete theme
3. Download XML files
4. Replace existing theme files

---

## 📝 Adding New Strings

Always use string resources, never hardcoded text.

**File**: `app/src/main/res/values/strings.xml`

```xml
<resources>
    <!-- App info -->
    <string name="app_name">Android Command Center</string>
    
    <!-- Welcome screen -->
    <string name="welcome_message">Welcome to Android Command Center!</string>
    <string name="description">A template for Galaxy S24</string>
    
    <!-- Buttons -->
    <string name="get_started">Get Started</string>
    <string name="button_next">Next</string>
    <string name="button_cancel">Cancel</string>
    
    <!-- Messages -->
    <string name="loading">Loading...</string>
    <string name="error_message">Something went wrong</string>
    
    <!-- Format strings -->
    <string name="greeting">Hello, %1$s!</string>
    <string name="items_count">You have %1$d items</string>
</resources>
```

### Using Strings in Code

```kotlin
// In Activity or Fragment
val message = getString(R.string.welcome_message)
textView.text = message

// With format arguments
val name = "User"
val greeting = getString(R.string.greeting, name)  // "Hello, User!"

val count = 5
val items = getString(R.string.items_count, count)  // "You have 5 items"
```

### Using Strings in XML

```xml
<TextView
    android:text="@string/welcome_message" />
```

### Localization (Multiple Languages)

Create language-specific folders:

```
values/strings.xml          # Default (English)
values-es/strings.xml       # Spanish
values-fr/strings.xml       # French
values-de/strings.xml       # German
values-ko/strings.xml       # Korean (for Galaxy S24 home market)
```

---

## 🏠 Customizing Welcome Screen

Modify the default welcome screen.

### Update Text Content

**File**: `app/src/main/res/values/strings.xml`

```xml
<string name="welcome_message">Welcome to MyApp!</string>
<string name="description">Your app description here</string>
<string name="get_started">Start Now</string>
```

### Modify Layout

**File**: `app/src/main/res/layout/activity_main.xml`

Change existing views or add new ones:

```xml
<!-- Change welcome text -->
<TextView
    android:id="@+id/welcome_text"
    android:text="@string/welcome_message"
    android:textSize="32sp"
    android:textColor="@color/lindy_primary" />

<!-- Add your logo -->
<ImageView
    android:id="@+id/app_logo"
    android:layout_width="150dp"
    android:layout_height="150dp"
    android:src="@drawable/my_logo" />
```

### Update Button Action

**File**: `app/src/main/java/com/lindy/android/MainActivity.kt`

```kotlin
class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        
        val actionButton = findViewById<MaterialButton>(R.id.action_button)
        actionButton.setOnClickListener {
            // Your custom action
            Toast.makeText(this, "Button clicked!", Toast.LENGTH_SHORT).show()
            
            // Or navigate to another screen
            // val intent = Intent(this, NextActivity::class.java)
            // startActivity(intent)
        }
    }
}
```

---

## ✅ Customization Checklist

After customizing, verify:

- [ ] App name changed in launcher
- [ ] Package name is unique
- [ ] Colors match your brand
- [ ] App icon looks good
- [ ] Layout displays correctly
- [ ] Theme works in light/dark mode
- [ ] All strings use resources
- [ ] No hardcoded text
- [ ] Buttons work as expected
- [ ] Tested on Galaxy S24 or similar device

---

## 🎯 Next Steps

Now that you've customized the template:

1. **Add Features**: See [04-DEVELOPMENT.md](04-DEVELOPMENT.md)
2. **Test Your Changes**: See [05-TESTING.md](05-TESTING.md)
3. **Prepare for Release**: See [06-DEPLOYMENT.md](06-DEPLOYMENT.md)

---

## 💡 Tips

- **Start Small**: Change one thing at a time
- **Test Often**: Build and run after each change
- **Use Preview**: Android Studio layout editor
- **Keep Backups**: Commit to Git frequently
- **Follow Material Design**: Use Material components
- **Think Dark Mode**: Test both themes

---

**Navigation**:  
← [02-PROJECT-STRUCTURE.md](02-PROJECT-STRUCTURE.md) | [INDEX.md](INDEX.md) | [04-DEVELOPMENT.md](04-DEVELOPMENT.md) →
