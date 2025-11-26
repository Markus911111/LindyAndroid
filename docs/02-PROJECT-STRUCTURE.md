# 📂 Project Structure Guide

This guide explains the organization of the Android Command Center project and what each file and folder does.

## 🗂️ Complete Project Structure

```
AndroidCommandCenter/
├── 📁 .git/                        # Git version control (hidden)
├── 📁 .gradle/                     # Gradle cache (auto-generated)
├── 📁 .idea/                       # Android Studio settings (auto-generated)
├── 📁 app/                         # Main application module
│   ├── 📁 build/                   # Compiled files (auto-generated)
│   ├── 📁 src/
│   │   ├── 📁 main/
│   │   │   ├── 📁 java/com/lindy/android/
│   │   │   │   └── 📄 MainActivity.kt
│   │   │   ├── 📁 res/
│   │   │   │   ├── 📁 drawable/
│   │   │   │   ├── 📁 layout/
│   │   │   │   ├── 📁 mipmap-*/
│   │   │   │   ├── 📁 values/
│   │   │   │   └── 📁 xml/
│   │   │   └── 📄 AndroidManifest.xml
│   │   ├── 📁 test/                # Unit tests
│   │   └── 📁 androidTest/         # Instrumented tests
│   ├── 📄 build.gradle.kts         # App-level build config
│   └── 📄 proguard-rules.pro       # Code obfuscation rules
├── 📁 docs/                        # Documentation
│   ├── 📄 INDEX.md
│   ├── 📄 01-GETTING-STARTED.md
│   ├── 📄 02-PROJECT-STRUCTURE.md  # This file
│   └── ...
├── 📁 gradle/
│   └── 📁 wrapper/                 # Gradle wrapper files
├── 📄 .gitignore                   # Git ignore rules
├── 📄 build.gradle.kts             # Project-level build config
├── 📄 gradle.properties            # Gradle settings
├── 📄 gradlew                      # Gradle wrapper (Unix/Mac)
├── 📄 gradlew.bat                  # Gradle wrapper (Windows)
├── 📄 settings.gradle.kts          # Project settings
├── 📄 README.md                    # Project overview
└── 📄 QUICK_REFERENCE.md           # Command reference
```

## 📱 The `app/` Module

The `app/` folder contains your entire Android application.

### Source Code: `app/src/main/java/`

This is where your Kotlin/Java code lives.

```
app/src/main/java/com/lindy/android/
├── MainActivity.kt              # Main screen of your app
├── [YourActivity.kt]           # Add more screens here
├── models/                      # Data classes
├── adapters/                    # RecyclerView adapters
├── viewmodels/                  # ViewModel classes
└── utils/                       # Helper functions
```

**MainActivity.kt** - The entry point of your app:
```kotlin
class MainActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_main)
        // Your initialization code
    }
}
```

### Resources: `app/src/main/res/`

All non-code resources (layouts, images, strings, colors).

#### 📐 `layout/` - User Interface XML Files

```xml
<!-- activity_main.xml -->
<androidx.constraintlayout.widget.ConstraintLayout>
    <TextView android:text="Hello" />
    <Button android:id="@+id/button" />
</androidx.constraintlayout.widget.ConstraintLayout>
```

**Files**:
- `activity_main.xml` - Main screen layout
- `fragment_*.xml` - Fragment layouts
- `item_*.xml` - RecyclerView item layouts

#### 🎨 `values/` - Resource Values

**strings.xml** - Text strings:
```xml
<resources>
    <string name="app_name">Android Command Center</string>
    <string name="welcome">Welcome!</string>
</resources>
```

**colors.xml** - Color definitions:
```xml
<resources>
    <color name="lindy_primary">#FF2196F3</color>
    <color name="lindy_accent">#FFFF4081</color>
</resources>
```

**themes.xml** - App themes:
```xml
<resources>
    <style name="Theme.AndroidCommandCenter" parent="Theme.Material3">
        <item name="colorPrimary">@color/lindy_primary</item>
    </style>
</resources>
```

**dimens.xml** - Dimensions (create if needed):
```xml
<resources>
    <dimen name="padding_small">8dp</dimen>
    <dimen name="padding_normal">16dp</dimen>
</resources>
```

#### 🖼️ `drawable/` - Images and Graphics

- Vector drawables (`.xml`)
- PNG images (`.png`)
- JPG photos (`.jpg`)
- Drawable resources

```xml
<!-- ic_custom_icon.xml - Vector drawable -->
<vector xmlns:android="http://schemas.android.com/apk/res/android"
    android:width="24dp"
    android:height="24dp">
    <path android:fillColor="#000000"
          android:pathData="M10,20v-6h4v6h5v-8h3L12,3 2,12h3v8z"/>
</vector>
```

#### 🚀 `mipmap-*/` - App Launcher Icons

Different densities for various screen resolutions:
- `mipmap-mdpi/` - ~160 dpi (48x48px)
- `mipmap-hdpi/` - ~240 dpi (72x72px)
- `mipmap-xhdpi/` - ~320 dpi (96x96px)
- `mipmap-xxhdpi/` - ~480 dpi (144x144px)
- `mipmap-xxxhdpi/` - ~640 dpi (192x192px) **← Galaxy S24**
- `mipmap-anydpi-v26/` - Adaptive icons (Android 8.0+)

#### ⚙️ `xml/` - Configuration Files

- `backup_rules.xml` - Backup configuration
- `data_extraction_rules.xml` - Data transfer rules
- `network_security_config.xml` - Network security (add if needed)

### Android Manifest: `AndroidManifest.xml`

The main configuration file for your app.

```xml
<?xml version="1.0" encoding="utf-8"?>
<manifest xmlns:android="http://schemas.android.com/apk/res/android"
    package="com.androidcommandcenter">

    <!-- Permissions your app needs -->
    <uses-permission android:name="android.permission.INTERNET" />
    
    <!-- Hardware features -->
    <uses-feature android:name="android.hardware.camera" 
                  android:required="false" />

    <application
        android:icon="@mipmap/ic_launcher"
        android:label="@string/app_name"
        android:theme="@style/Theme.AndroidCommandCenter">
        
        <!-- Activities -->
        <activity android:name=".MainActivity"
            android:exported="true">
            <intent-filter>
                <action android:name="android.intent.action.MAIN" />
                <category android:name="android.intent.category.LAUNCHER" />
            </intent-filter>
        </activity>
        
        <!-- Add more activities here -->
        
    </application>
</manifest>
```

**Key Attributes**:
- `android:icon` - App icon
- `android:label` - App name
- `android:theme` - App theme
- `android:exported` - Can other apps start this activity?

### App Build Configuration: `build.gradle.kts`

Configures how your app is built.

```kotlin
android {
    namespace = "com.androidcommandcenter"
    
    // SDK versions
    compileSdk = 35      // Compile against Android 15
    
    defaultConfig {
        applicationId = "com.androidcommandcenter"  // Unique app ID
        minSdk = 31          // Android 12+
        targetSdk = 35       // Target Android 15
        versionCode = 1      // Internal version number
        versionName = "1.0"  // User-visible version
    }
    
    buildTypes {
        release {
            isMinifyEnabled = true  // Shrink code
            proguardFiles(...)      // Obfuscation rules
        }
    }
    
    compileOptions {
        sourceCompatibility = JavaVersion.VERSION_17
        targetCompatibility = JavaVersion.VERSION_17
    }
    
    kotlinOptions {
        jvmTarget = "17"
    }
}

dependencies {
    // Libraries your app uses
    implementation("androidx.core:core-ktx:1.15.0")
    implementation("com.google.android.material:material:1.12.0")
}
```

### ProGuard Rules: `proguard-rules.pro`

Code shrinking and obfuscation rules for release builds.

```proguard
# Keep your main classes
-keep class com.androidcommandcenter.** { *; }

# Keep Kotlin metadata
-keep class kotlin.Metadata { *; }

# Keep Android components
-keep class androidx.** { *; }
```

## 🔧 Root Configuration Files

### `build.gradle.kts` (Project Level)

Configures plugins for all modules:

```kotlin
plugins {
    id("com.android.application") version "8.7.3" apply false
    id("org.jetbrains.kotlin.android") version "2.1.0" apply false
}
```

### `settings.gradle.kts`

Defines project structure:

```kotlin
rootProject.name = "AndroidCommandCenter"
include(":app")  // Includes the app module
```

### `gradle.properties`

Gradle build settings:

```properties
# Memory settings
org.gradle.jvmargs=-Xmx2048m

# AndroidX
android.useAndroidX=true

# Build cache
org.gradle.caching=true
```

### `.gitignore`

Files to exclude from version control:

```
# Build outputs
build/
*.apk
*.aab

# IDE files
.idea/
*.iml

# Local config
local.properties
```

## 📱 Galaxy S24 Specific Configurations

### Display Configuration

Galaxy S24 specifications:
- **Resolution**: 1080 x 2340 pixels
- **Density**: ~425 dpi (xxxhdpi)
- **Aspect Ratio**: 19.5:9
- **Display**: Dynamic AMOLED 2X, 120Hz

**Your app automatically handles this through:**

1. **Density-specific resources**: Uses `xxxhdpi` assets
2. **ConstraintLayout**: Adapts to any screen size
3. **Vector drawables**: Scale perfectly
4. **Material Design**: Responds to screen dimensions

### AMOLED Optimization

**Dark theme** (`values-night/themes.xml`):
```xml
<!-- True black background for AMOLED -->
<item name="android:colorBackground">@color/black</item>
```

Benefits:
- 🔋 Saves battery (AMOLED pixels off when black)
- 👁️ Reduces eye strain
- 🎨 Better contrast

### Performance Optimization

**build.gradle.kts**:
```kotlin
defaultConfig {
    // Enable R8 compiler
    isMinifyEnabled = true
    isShrinkResources = true
}
```

**Smooth animations**:
- Uses Material Motion
- Hardware-accelerated rendering
- Optimized for 120Hz display

## 🧪 Test Directories

### `app/src/test/` - Unit Tests

Local tests that run on your computer:

```kotlin
class ExampleUnitTest {
    @Test
    fun addition_isCorrect() {
        assertEquals(4, 2 + 2)
    }
}
```

Run with: `./gradlew test`

### `app/src/androidTest/` - Instrumented Tests

Tests that run on device/emulator:

```kotlin
@RunWith(AndroidJUnit4::class)
class ExampleInstrumentedTest {
    @Test
    fun useAppContext() {
        val context = InstrumentationRegistry
            .getInstrumentation().targetContext
        assertEquals("com.androidcommandcenter", context.packageName)
    }
}
```

Run with: `./gradlew connectedAndroidTest`

## 📦 Generated Directories (Don't Edit)

### `build/` - Build Outputs

Generated during compilation:
- APK files
- AAB files
- Compiled code
- Resources

**Action**: Add to `.gitignore`

### `.gradle/` - Gradle Cache

Gradle's working directory:
- Downloaded dependencies
- Build cache
- Temporary files

**Action**: Add to `.gitignore`

### `.idea/` - IDE Settings

Android Studio configuration:
- Project settings
- Code style
- Run configurations

**Action**: Mostly in `.gitignore` (keep some shared settings)

## 🎯 Common File Modifications

### Adding a New Screen

1. **Create Activity**:
```kotlin
// SettingsActivity.kt
class SettingsActivity : AppCompatActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContentView(R.layout.activity_settings)
    }
}
```

2. **Create Layout**:
```xml
<!-- activity_settings.xml -->
<LinearLayout>
    <!-- Your UI here -->
</LinearLayout>
```

3. **Register in Manifest**:
```xml
<activity android:name=".SettingsActivity" />
```

### Adding a Library

Edit `app/build.gradle.kts`:
```kotlin
dependencies {
    implementation("com.squareup.retrofit2:retrofit:2.9.0")
}
```

Click "Sync Now" in Android Studio.

### Changing Package Name

1. Refactor in Android Studio
2. Update `applicationId` in `build.gradle.kts`
3. Update `package` in `AndroidManifest.xml`

## 📚 Best Practices

### Organization

✅ **DO**:
- Group related files in packages
- Use meaningful names
- Keep Activities small and focused
- Extract reusable code

❌ **DON'T**:
- Put everything in one package
- Use generic names like `Utils`
- Create god classes
- Duplicate code

### Resources

✅ **DO**:
- Use string resources for all text
- Use dimension resources for sizes
- Use color resources for colors
- Use vector drawables when possible

❌ **DON'T**:
- Hardcode strings in layouts
- Use pixel values directly
- Use hex colors in layouts
- Use large PNG files

### Configuration

✅ **DO**:
- Keep `minSdk` reasonable
- Target latest `targetSdk`
- Use semantic versioning
- Enable ProGuard for release

❌ **DON'T**:
- Set `minSdk` too low
- Ignore SDK warnings
- Forget to increment versions
- Skip obfuscation

## 🔍 Finding Files

### In Android Studio

- **Ctrl/Cmd + N**: Find class
- **Ctrl/Cmd + Shift + N**: Find file
- **Ctrl/Cmd + Shift + F**: Find in files
- **Ctrl/Cmd + B**: Go to declaration

### Important Locations

- **App entry**: `MainActivity.kt`
- **Main layout**: `res/layout/activity_main.xml`
- **Strings**: `res/values/strings.xml`
- **Colors**: `res/values/colors.xml`
- **Theme**: `res/values/themes.xml`
- **Manifest**: `src/main/AndroidManifest.xml`
- **Build config**: `app/build.gradle.kts`

## 🆘 When Things Go Wrong

### Can't find a file?

1. Check you're in the correct source set (`main/`)
2. Refresh project: File → Sync Project with Gradle Files
3. Check if file was created in correct location

### Build fails?

1. Check `build.gradle.kts` syntax
2. Sync Gradle files
3. Clean and rebuild: Build → Clean Project

### Layout not showing?

1. Check XML syntax
2. Verify resource IDs match
3. Check layout file name

## 📖 Next Steps

Now that you understand the structure:

1. **Explore the code**: Open files and read comments
2. **Make changes**: Try modifying layouts and strings
3. **Add features**: Follow [04-DEVELOPMENT.md](04-DEVELOPMENT.md)
4. **Test your app**: See [05-TESTING.md](05-TESTING.md)

---

**Navigation**:  
← [01-GETTING-STARTED.md](01-GETTING-STARTED.md) | [INDEX.md](INDEX.md) | [03-CUSTOMIZATION.md](03-CUSTOMIZATION.md) →
