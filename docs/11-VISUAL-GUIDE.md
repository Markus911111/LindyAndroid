# 📸 Visual Guide for Beginners

This guide uses diagrams, flowcharts, and visual aids to help you understand complex concepts in Android development.

## 📋 Table of Contents

1. [Android Studio Installation](#android-studio-installation)
2. [Project Structure Visualization](#project-structure-visualization)
3. [Building and Running](#building-and-running)
4. [Git Workflow](#git-workflow)
5. [Termux Setup](#termux-setup)
6. [GitHub Actions](#github-actions)
7. [Troubleshooting Visuals](#troubleshooting-visuals)

---

## 🖥️ Android Studio Installation

### Step-by-Step Installation (Visual Guide)

```
┌─────────────────────────────────────────────────────────────┐
│ Step 1: Download Android Studio                            │
│                                                             │
│  [Browser]                                                  │
│  ┌──────────────────────────────────────┐                  │
│  │ https://developer.android.com/studio │                  │
│  └──────────────────────────────────────┘                  │
│                    ↓                                        │
│         [Download Android Studio]                           │
│                    ↓                                        │
│  💾 android-studio-2023.x.x.x-windows.exe                  │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ Step 2: Run Installer                                       │
│                                                             │
│  ┌────────────────────────────────────┐                    │
│  │  Android Studio Setup              │                    │
│  │  ────────────────────────────       │                    │
│  │                                    │                    │
│  │  Choose Installation Type:         │                    │
│  │  ● Standard (Recommended)          │ ← Click This      │
│  │  ○ Custom                          │                    │
│  │                                    │                    │
│  │      [Next]  [Cancel]              │                    │
│  └────────────────────────────────────┘                    │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ Step 3: First Launch - SDK Download                         │
│                                                             │
│  ┌────────────────────────────────────┐                    │
│  │  Downloading Components             │                    │
│  │  ────────────────────────────       │                    │
│  │                                    │                    │
│  │  ████████░░░░░░░░░░░ 45%          │                    │
│  │                                    │                    │
│  │  Downloading Android SDK...        │                    │
│  │  (This may take 10-30 minutes)    │                    │
│  │                                    │                    │
│  └────────────────────────────────────┘                    │
│                                                             │
│  ⏳ Wait for download to complete                          │
└─────────────────────────────────────────────────────────────┘
```

**📷 Screenshot Location**: Save screenshot of your installation here:
- `docs/images/01-android-studio-install.png` (When you install)

---

## 📂 Project Structure Visualization

### Complete Project Tree

```
AndroidCommandCenter/
│
├── 📱 app/                          ← Your application code
│   ├── build/                       ← Generated files (don't edit)
│   ├── src/
│   │   ├── main/
│   │   │   ├── java/com/androidcommandcenter/
│   │   │   │   └── MainActivity.kt  ← ⭐ START HERE
│   │   │   │
│   │   │   ├── res/                 ← Resources
│   │   │   │   ├── layout/
│   │   │   │   │   └── activity_main.xml  ← ⭐ UI LAYOUT
│   │   │   │   │
│   │   │   │   ├── values/
│   │   │   │   │   ├── strings.xml  ← ⭐ TEXT
│   │   │   │   │   ├── colors.xml   ← ⭐ COLORS
│   │   │   │   │   └── themes.xml   ← ⭐ THEME
│   │   │   │   │
│   │   │   │   ├── drawable/        ← Images
│   │   │   │   └── mipmap-*/        ← App icons
│   │   │   │
│   │   │   └── AndroidManifest.xml  ← ⭐ APP CONFIG
│   │   │
│   │   ├── test/                    ← Unit tests
│   │   └── androidTest/             ← UI tests
│   │
│   ├── build.gradle.kts             ← ⭐ APP SETTINGS
│   └── proguard-rules.pro
│
├── 📁 docs/                         ← Documentation
│   ├── INDEX.md                     ← Documentation hub
│   ├── 01-GETTING-STARTED.md
│   └── ...
│
├── 📁 .github/workflows/            ← Automation
│   ├── android-build.yml
│   └── ...
│
├── build.gradle.kts                 ← Project settings
├── settings.gradle.kts              ← Module config
├── gradle.properties                ← Build properties
│
└── README.md                        ← Project overview

⭐ = Files you'll edit most often
📱 = Contains your app
📁 = Documentation/config
```

### What Each Part Does

```
┌──────────────────────────────────────────────────────────────┐
│                    Android App Components                     │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  MainActivity.kt           ←───→   activity_main.xml        │
│  (Kotlin Code Logic)               (Visual Layout)          │
│         │                                  │                │
│         │                                  │                │
│         ├─ Controls UI behavior            ├─ Defines UI    │
│         ├─ Handles button clicks           ├─ Buttons       │
│         ├─ Loads data                      ├─ Text          │
│         └─ Updates screen                  └─ Images        │
│                                                              │
│         Both work together to create your app!              │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**📷 Screenshot Guide**:
1. Open Android Studio
2. Expand folders in left panel
3. Screenshot showing the project structure
4. Save as: `docs/images/02-project-structure.png`

---

## 🏗️ Building and Running

### Visual Build Process

```
┌─────────────────────────────────────────────────────────────┐
│                    Build Process Flow                        │
└─────────────────────────────────────────────────────────────┘

Your Code                Gradle Build             APK File
─────────               ─────────────            ─────────

MainActivity.kt    ┐
activity_main.xml  ├──→  Compile Code     ──→   📦 app.apk
strings.xml        │      ↓
colors.xml         │     Package Resources      (Ready to
themes.xml         │      ↓                      install)
images            ┘      Sign APK
                         ↓
                    Generate APK


┌───────────────────────────────────────────────────────────┐
│ In Android Studio - Look for these buttons:              │
│                                                           │
│  Top Toolbar:                                            │
│  ┌─────────────────────────────────────────────────┐    │
│  │ ⚙️ │ 🔨 Build │ ▶️ Run │ 🐛 Debug │ 🛑 Stop    │    │
│  └─────────────────────────────────────────────────┘    │
│         │         │                                      │
│         │         └─→ Click "Run" to build & install    │
│         └───────────→ Click "Build" to just compile     │
│                                                           │
└───────────────────────────────────────────────────────────┘
```

### Connecting Galaxy S24

```
Step 1: Enable Developer Options
═══════════════════════════════════════════════════════════

[Your Galaxy S24]
  │
  ├─ Open Settings ⚙️
  │   │
  │   └─ Scroll to "About Phone"
  │       │
  │       └─ Tap "Build Number" 7 times
  │           │
  │           └─ ✅ "You are now a developer!"


Step 2: Enable USB Debugging
═══════════════════════════════════════════════════════════

[Settings] → [Developer Options]
  │
  └─ Find "USB Debugging"
      │
      └─ Toggle ON ✅


Step 3: Connect to Computer
═══════════════════════════════════════════════════════════

[Galaxy S24] ────USB Cable────→ [Computer]
      │
      └─ Allow USB Debugging popup
          │
          ┌───────────────────────────────┐
          │ Allow USB debugging?           │
          │ The computer's RSA key:        │
          │ AB:CD:EF:12:34...             │
          │                                │
          │ [✓] Always allow from this     │
          │     computer                   │
          │                                │
          │    [Cancel]  [OK] ← Click     │
          └───────────────────────────────┘
```

**📷 Critical Screenshots Needed**:
1. Settings → About Phone → Build Number
   Save as: `docs/images/03-enable-developer.png`

2. Developer Options → USB Debugging
   Save as: `docs/images/04-usb-debugging.png`

3. "Allow USB debugging" popup
   Save as: `docs/images/05-allow-usb.png`

---

## 🔄 Git Workflow

### Visual Git Process

```
┌──────────────────────────────────────────────────────────────┐
│                 Git Version Control Flow                      │
└──────────────────────────────────────────────────────────────┘

Local Computer          GitHub (Cloud)          Team Members
──────────────          ──────────────          ────────────

Your Project                                    
    │                                           
    ├─ Make changes                            
    │  (Edit code)                             
    │                                           
    ├─ git add .                               
    │  (Stage changes)                         
    │                                           
    ├─ git commit                              
    │  (Save locally)                          
    │                                           
    └─ git push         ─────→  GitHub  ─────→  Others can
       (Upload)                  Repo           see changes
                                  │
                                  │
                                  └──→  Others git pull
                                        (Download updates)


┌──────────────────────────────────────────────────────────────┐
│                Terminal Commands (Step by Step)               │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  $ git status                    ← See what changed         │
│  Modified: MainActivity.kt                                  │
│                                                              │
│  $ git add .                     ← Stage all changes        │
│  ✓ Files staged                                            │
│                                                              │
│  $ git commit -m "Added feature" ← Save with message       │
│  ✓ Changes committed                                        │
│                                                              │
│  $ git push origin main          ← Upload to GitHub        │
│  ✓ Pushing to GitHub...                                    │
│  ✓ Done!                                                    │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### Git Branching Visual

```
Main Branch Timeline:
════════════════════════════════════════════════════════════

main    ●────●────●────●────●────────●────●───→
             │              │         ↑
             │              │         │
feature     └●────●────●───┘    merge back
branch       (Work here)       (when done)


How it works:
─────────────

1. Start:            main ●───────→
                           │
2. Create branch:          └●──→ feature
                            (work here)
                            
3. Make commits:           ●──●──●
                           (changes)
                           
4. Merge back:      main ●────●
                          ↑
                          └─(merge)
```

**📷 Screenshots for Git**:
1. GitHub repository page
   Save as: `docs/images/06-github-repo.png`

2. GitHub Actions tab showing build
   Save as: `docs/images/07-github-actions.png`

---

## 📱 Termux Setup

### Termux Installation Flow

```
┌──────────────────────────────────────────────────────────────┐
│           Installing Termux on Galaxy S24                     │
└──────────────────────────────────────────────────────────────┘

Step 1: Get F-Droid
═══════════════════

Browser
  │
  └─→ https://f-droid.org
        │
        └─→ Download F-Droid APK
              │
              └─→ Install F-Droid app


Step 2: Get Termux from F-Droid
════════════════════════════════

[F-Droid App]
  │
  ├─→ Search: "Termux"
  │     │
  │     └─→ [Termux] app
  │           │
  │           └─→ Tap "Install"
  │
  └─→ Optional installs:
        - Termux:API (Android features)
        - Termux:Widget (Home shortcuts)


Step 3: First Launch
═════════════════════

[Open Termux]
  │
  ├─→ First time setup (30 seconds)
  │     │
  │     └─→ You'll see:
  │           ┌────────────────────────┐
  │           │ $                      │ ← Command prompt
  │           │                        │
  │           └────────────────────────┘
  │
  └─→ Run: pkg update && pkg upgrade
        (Updates all packages)
```

### Termux Interface Explained

```
┌──────────────────────────────────────────────────────────────┐
│                    Termux Screen Layout                       │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  [Swipe from left for menu]                                 │
│                                                              │
│  ┌────────────────────────────────────────────────────┐    │
│  │ ~ $                                                 │    │
│  │                                                     │    │
│  │                                                     │    │
│  │ Type commands here                                 │    │
│  │                                                     │    │
│  │                                                     │    │
│  └────────────────────────────────────────────────────┘    │
│   ↑                                                         │
│   └─ Terminal prompt                                        │
│                                                              │
│  [Bottom: Extra keys row]                                   │
│  ┌────────────────────────────────────────────────────┐    │
│  │ ESC │ / │ - │ HOME │ ↑ │ END │ PGUP               │    │
│  │ TAB │CTL│ALT│  ←  │ ↓ │  →  │ PGDN               │    │
│  └────────────────────────────────────────────────────┘    │
│         └─ Use these for navigation                         │
│                                                              │
│  [Keyboard appears when you tap screen]                     │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### Termux Commands Visual Guide

```
┌──────────────────────────────────────────────────────────────┐
│              Common Termux Commands                           │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  Navigation:                                                 │
│  ─────────────                                              │
│   pwd             Show current directory                     │
│   ls              List files                                │
│   cd folder/      Change to folder                          │
│   cd ..           Go up one level                           │
│   cd ~            Go to home                                │
│                                                              │
│  File Operations:                                            │
│  ─────────────                                              │
│   touch file.txt  Create file                               │
│   mkdir folder    Create folder                             │
│   rm file.txt     Delete file                               │
│   cp file1 file2  Copy file                                 │
│   mv old new      Move/rename                               │
│                                                              │
│  Package Management:                                         │
│  ─────────────────                                          │
│   pkg search git  Search for package                        │
│   pkg install git Install package                           │
│   pkg update      Update package list                       │
│   pkg upgrade     Upgrade packages                          │
│                                                              │
│  Git Commands:                                               │
│  ─────────────                                              │
│   git clone URL   Download repository                       │
│   git status      Check changes                             │
│   git pull        Update repository                         │
│   git push        Upload changes                            │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

**📷 Critical Termux Screenshots**:
1. F-Droid app showing Termux
   Save as: `docs/images/08-fdroid-termux.png`

2. Termux first launch screen
   Save as: `docs/images/09-termux-first-launch.png`

3. Termux after `pkg update`
   Save as: `docs/images/10-termux-updated.png`

4. Termux running `git clone`
   Save as: `docs/images/11-termux-git-clone.png`

---

## ⚙️ GitHub Actions

### CI/CD Pipeline Visual

```
┌──────────────────────────────────────────────────────────────┐
│              GitHub Actions Workflow                          │
└──────────────────────────────────────────────────────────────┘

You Push Code
     │
     ↓
┌─────────────────────┐
│  GitHub Repository  │
└─────────────────────┘
          │
          ↓ (Triggers)
┌─────────────────────┐
│  GitHub Actions     │
│  ─────────────────  │
│                     │
│  Jobs:              │
│  ✓ Build APK        │ ← Compiles your app
│  ✓ Run Tests        │ ← Checks for bugs
│  ✓ Code Quality     │ ← Checks code style
│  ✓ Security Scan    │ ← Finds vulnerabilities
│                     │
└─────────────────────┘
          │
          ↓ (Results)
┌─────────────────────┐
│  ✅ All Passed      │
│  📦 APK Available   │
│  📊 Reports Ready   │
└─────────────────────┘
          │
          ↓
    You get notified!
```

### GitHub Actions Tab Guide

```
┌──────────────────────────────────────────────────────────────┐
│                  GitHub.com Interface                         │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  Your Repository: LindyAndroid                       │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ [Code] [Issues] [Pull requests] [Actions] [Settings] │  │
│  └──────────────────────────────────────────────────────┘  │
│              └────────────────────↑                          │
│                          Click here to see builds            │
│                                                              │
│  Actions Tab:                                                │
│  ┌──────────────────────────────────────────────────────┐  │
│  │ Workflows                                            │  │
│  │ ┌────────────────────────────────────────────────┐  │  │
│  │ │ ✅ Android CI Build         #42  main  5m ago  │  │  │
│  │ │ ✅ Automated Testing        #41  main  6m ago  │  │  │
│  │ │ ❌ Android CI Build         #40  main  10m ago │  │  │
│  │ │ ✅ Code Quality Analysis    #39  main  15m ago │  │  │
│  │ └────────────────────────────────────────────────┘  │  │
│  │                                                      │  │
│  │ ✅ = Success    ❌ = Failed    🟡 = Running         │  │
│  │                                                      │  │
│  │ Click any run to see details →                      │  │
│  └──────────────────────────────────────────────────────┘  │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### Build Status Flow

```
Workflow Execution Timeline:
════════════════════════════════════════════════════════════

Start   Build    Test     Quality   Deploy    Done
  ●───────●───────●────────●─────────●────────●
  │       │       │        │         │        │
  0s      2m      5m       8m        10m      12m
  
  └→ Setup
          └→ Compile
                  └→ Test
                           └→ Lint
                                    └→ Upload
                                             └→ ✅ Success!


If something fails:
═══════════════════

Start   Build    Test     ❌ FAIL
  ●───────●───────●────────●
  │       │       │        │
  0s      2m      5m       ❌ Error at 5m30s
  
                           You get email:
                           "Build failed"
                           
                           Click link → See error
                           Fix code → Push again
```

**📷 GitHub Actions Screenshots**:
1. GitHub Actions tab overview
   Save as: `docs/images/12-actions-overview.png`

2. Successful build details
   Save as: `docs/images/13-build-success.png`

3. Failed build with error
   Save as: `docs/images/14-build-failure.png`

4. Downloading artifacts
   Save as: `docs/images/15-download-artifacts.png`

---

## 🐛 Troubleshooting Visuals

### Common Error Locations

```
┌──────────────────────────────────────────────────────────────┐
│           Where to Find Error Messages                        │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  1. Android Studio Build Output:                             │
│  ┌────────────────────────────────────────────────────┐    │
│  │ Build                                              │    │
│  │ ┌──────────────────────────────────────────────┐  │    │
│  │ │ > Task :app:compileDebugKotlin FAILED         │  │    │
│  │ │ e: MainActivity.kt: (23, 5): Unresolved       │  │    │
│  │ │    reference: setContentViews                 │  │    │
│  │ │                                                │  │    │
│  │ │ * What went wrong:                            │  │    │
│  │ │ Compilation error                             │  │    │
│  │ └──────────────────────────────────────────────┘  │    │
│  │    └─ Bottom panel, "Build" tab                   │    │
│  └────────────────────────────────────────────────────┘    │
│                                                              │
│  2. Logcat (Runtime Errors):                                 │
│  ┌────────────────────────────────────────────────────┐    │
│  │ Logcat                                             │    │
│  │ ┌──────────────────────────────────────────────┐  │    │
│  │ │ E/AndroidRuntime: FATAL EXCEPTION: main       │  │    │
│  │ │ Process: com.androidcommandcenter             │  │    │
│  │ │ java.lang.NullPointerException                │  │    │
│  │ │   at MainActivity.onCreate(MainActivity.kt:25)│  │    │
│  │ └──────────────────────────────────────────────┘  │    │
│  │    └─ Bottom panel, "Logcat" tab                  │    │
│  └────────────────────────────────────────────────────┘    │
│                                                              │
│  3. Terminal/Gradle Output:                                  │
│  ┌────────────────────────────────────────────────────┐    │
│  │ Terminal                                           │    │
│  │ ┌──────────────────────────────────────────────┐  │    │
│  │ │ $ ./gradlew assembleDebug                     │  │    │
│  │ │                                                │  │    │
│  │ │ FAILURE: Build failed with an exception.      │  │    │
│  │ │ * What went wrong:                            │  │    │
│  │ │ Task 'assembleDebug' not found in root       │  │    │
│  │ └──────────────────────────────────────────────┘  │    │
│  │    └─ Bottom panel, "Terminal" tab                │    │
│  └────────────────────────────────────────────────────┘    │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### Error Resolution Flowchart

```
┌────────────────────────────────────────┐
│    App Won't Build or Run?             │
└────────────────────────────────────────┘
                 │
                 ↓
        ┌─────────────────┐
        │ Where's the      │
        │ error shown?     │
        └─────────────────┘
                 │
      ┌──────────┼──────────┐
      │          │          │
   Build     Logcat    Terminal
   Output    (Red!)    (Failed!)
      │          │          │
      ↓          ↓          ↓
 Compile    Runtime     Gradle
 Error       Error      Error
      │          │          │
      ↓          ↓          ↓
  Fix code   Fix logic  Fix config
      │          │          │
      └──────────┴──────────┘
                 │
                 ↓
          Try again! ✅
```

### Device Connection Troubleshooting

```
Device Not Detected?
═══════════════════════════════════════════════════════════

Step 1: Check USB Connection
────────────────────────────
[Galaxy S24] ──USB──→ [Computer]
                        │
                        ├─ Try different USB port
                        ├─ Try different USB cable
                        └─ Check cable is data cable
                           (not charging-only)


Step 2: Check Phone Settings
────────────────────────────
Galaxy S24:
  ├─ USB Debugging ON? ✅
  ├─ "Allow USB debugging" popup? ✅
  └─ Try USB mode: "File Transfer" or "MTP"


Step 3: Check ADB
────────────────────────────
Terminal:
  $ adb devices
  
  ✅ Good output:
     List of devices attached
     RF8N1234567    device
     
  ❌ Bad output:
     List of devices attached
     (empty)
     
  If empty:
     - Reconnect phone
     - Check settings again
     - Restart ADB: adb kill-server && adb start-server


Step 4: Restart Everything
────────────────────────────
  1. Unplug phone
  2. Close Android Studio
  3. Restart phone
  4. Plug in phone
  5. Open Android Studio
  6. Try again
```

**📷 Error Screenshots to Capture**:
1. Build error in Android Studio
   Save as: `docs/images/16-build-error-example.png`

2. Logcat showing crash
   Save as: `docs/images/17-logcat-crash.png`

3. ADB devices output
   Save as: `docs/images/18-adb-devices.png`

4. USB debugging popup on phone
   Save as: `docs/images/19-usb-debug-popup.png`

---

## 📸 Creating Your Own Screenshots

### For Windows:
```
Press: Windows + Shift + S
       └─ Screenshot tool opens
       └─ Select area to capture
       └─ Image copied to clipboard
       └─ Open Paint and paste (Ctrl+V)
       └─ Save as PNG
```

### For Mac:
```
Press: Command + Shift + 4
       └─ Cursor changes to crosshair
       └─ Click and drag to select area
       └─ Screenshot saved to Desktop
```

### For Galaxy S24:
```
Method 1: Buttons
  Press: Power + Volume Down
         └─ Screen flashes
         └─ Screenshot saved to Gallery

Method 2: Palm Swipe
  Swipe: Side of hand across screen
         └─ Screen captured
```

### Screenshot Organization

Create this folder structure:

```
docs/
└── images/
    ├── setup/
    │   ├── 01-android-studio-install.png
    │   ├── 02-project-structure.png
    │   └── ...
    ├── termux/
    │   ├── 08-fdroid-termux.png
    │   ├── 09-termux-first-launch.png
    │   └── ...
    ├── github/
    │   ├── 12-actions-overview.png
    │   └── ...
    └── errors/
        ├── 16-build-error-example.png
        └── ...
```

---

## 🎨 Understanding UI Layouts

### Layout Components Visual

```
┌──────────────────────────────────────────────────────────────┐
│              activity_main.xml Components                     │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  XML Code                          What You See             │
│  ────────                          ───────────              │
│                                                              │
│  <TextView                         ┌─────────────────┐      │
│    android:text="Hello"            │ Hello           │      │
│    android:textSize="24sp" />      │                 │      │
│                                    └─────────────────┘      │
│                                                              │
│  <Button                           ┌─────────────────┐      │
│    android:text="Click Me"         │   Click Me      │      │
│    android:background="#FF0000"/>  │  (Red button)   │      │
│                                    └─────────────────┘      │
│                                                              │
│  <ImageView                        ┌─────────────────┐      │
│    android:src="@drawable/logo"    │     [LOGO]      │      │
│    android:width="100dp" />        │                 │      │
│                                    └─────────────────┘      │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

### Layout Preview in Android Studio

```
┌──────────────────────────────────────────────────────────────┐
│             Android Studio Layout Editor                      │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  ┌────────────┬─────────────────────┬──────────────────┐   │
│  │ Palette    │   Preview           │  Attributes      │   │
│  │            │                     │                  │   │
│  │ Text       │   ┌──────────┐     │  TextView        │   │
│  │ └TextView  │   │ Hello!   │     │  ├─ text: "..."  │   │
│  │ └EditText  │   │          │     │  ├─ textSize:24  │   │
│  │            │   │  [Button]│     │  └─ textColor:.. │   │
│  │ Buttons    │   │          │     │                  │   │
│  │ └Button    │   └──────────┘     │  Button          │   │
│  │ └ImageBtn  │     └─ Phone       │  ├─ text: "..."  │   │
│  │            │        preview      │  └─ onClick: ... │   │
│  │ (Drag here │                     │                  │   │
│  │  to add)   │                     │  (Edit here)     │   │
│  └────────────┴─────────────────────┴──────────────────┘   │
│                                                              │
│  Tabs: [Code] [Split] [Design]                              │
│          └─ Code view                                        │
│                └─ Both                                       │
│                       └─ Visual only                         │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## 📚 Quick Reference Card

Print this out and keep it handy!

```
┌──────────────────────────────────────────────────────────────┐
│        ANDROID COMMAND CENTER QUICK REFERENCE                 │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  BUILD COMMANDS:                                             │
│  ▸ ./gradlew clean              Clean build                 │
│  ▸ ./gradlew assembleDebug      Build debug APK             │
│  ▸ ./gradlew assembleRelease    Build release APK           │
│  ▸ ./gradlew installDebug       Install on device           │
│                                                              │
│  ADB COMMANDS:                                               │
│  ▸ adb devices                  List connected devices      │
│  ▸ adb install app.apk          Install APK                 │
│  ▸ adb uninstall <package>      Remove app                  │
│  ▸ adb logcat                   View logs                   │
│                                                              │
│  GIT COMMANDS:                                               │
│  ▸ git status                   Check changes               │
│  ▸ git add .                    Stage all files             │
│  ▸ git commit -m "message"      Commit changes              │
│  ▸ git push origin main         Upload to GitHub            │
│  ▸ git pull origin main         Download updates            │
│                                                              │
│  IMPORTANT FILES:                                            │
│  ▸ app/build.gradle.kts         App configuration           │
│  ▸ MainActivity.kt              Main app code               │
│  ▸ activity_main.xml            Main UI layout              │
│  ▸ strings.xml                  Text strings                │
│  ▸ AndroidManifest.xml          App manifest                │
│                                                              │
│  KEYBOARD SHORTCUTS (Android Studio):                        │
│  ▸ Shift + F10                  Run app                     │
│  ▸ Ctrl/Cmd + F9                Build project               │
│  ▸ Ctrl/Cmd + N                 Find class                  │
│  ▸ Ctrl/Cmd + Shift + N         Find file                   │
│  ▸ Alt + Enter                  Quick fix                   │
│                                                              │
│  HELP:                                                       │
│  ▸ docs/INDEX.md                Documentation hub            │
│  ▸ docs/07-TROUBLESHOOTING.md   Common problems             │
│  ▸ QUICK_REFERENCE.md           Command reference           │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

---

## 🎯 Next Steps

1. **Take Screenshots**: As you complete each step, take screenshots
2. **Save to docs/images/**: Organize by category
3. **Update README**: Add links to this visual guide
4. **Share with Team**: Help others learn faster

**Remember**: 
- 📸 One picture = 1000 words
- 🎨 Diagrams clarify complex concepts
- 🗺️ Visual guides reduce confusion
- ✅ Screenshots show exact steps

---

**Navigation**:  
← [10-AUTOMATION-GUIDE.md](10-AUTOMATION-GUIDE.md) | [INDEX.md](INDEX.md) | [Back to README](../README.md) →
