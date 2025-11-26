# 🐍 Pydroid 3 Development Guide

Complete guide to using Python and Pydroid 3 for Android development on your Galaxy S24.

## 📋 Table of Contents

1. [What is Pydroid 3?](#what-is-pydroid-3)
2. [Installing Pydroid 3](#installing-pydroid-3)
3. [Python Manifest System](#python-manifest-system)
4. [Running Python Scripts](#running-python-scripts)
5. [Build Automation with Python](#build-automation-with-python)
6. [Git Integration](#git-integration)
7. [Creating Widgets](#creating-widgets)
8. [Advanced Features](#advanced-features)
9. [Python vs Termux](#python-vs-termux)
10. [Troubleshooting](#troubleshooting)

## 🎯 What is Pydroid 3?

**Pydroid 3** is a full-featured Python 3 IDE for Android that runs directly on your Galaxy S24.

### Key Features

```
✅ Full Python 3.11 support
✅ pip package manager
✅ GUI applications (Tkinter, Kivy)
✅ Scientific libraries (NumPy, Pandas)
✅ Code editor with syntax highlighting
✅ Terminal emulator
✅ Home screen widgets
✅ Background execution
✅ No root required
```

### Why Use Pydroid for Android Development?

```
┌──────────────────────────────────────────────────────────────┐
│         Pydroid 3 vs Termux for Android Dev                   │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  Pydroid 3:                    Termux:                      │
│  ──────────                    ───────                      │
│  ✅ Easy to use GUI            ✅ Full Linux environment     │
│  ✅ Built-in editor            ✅ More powerful             │
│  ✅ Quick testing              ✅ Better for power users    │
│  ✅ Home widgets               ✅ SSH server               │
│  ✅ Background tasks           ✅ Multiple terminals        │
│  ✅ Beginner friendly          ⚠️  Command line only       │
│                                                              │
│  Best for:                     Best for:                    │
│  • Quick scripts               • Complex workflows          │
│  • Automation                  • Git operations            │
│  • Testing                     • Advanced development      │
│  • Learning Python             • SSH access                │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## 📱 Installing Pydroid 3

### Step 1: Download from Play Store

```
[Galaxy S24]
  │
  ├─ Open Play Store
  │
  ├─ Search: "Pydroid 3"
  │
  └─ Install "Pydroid 3 - IDE for Python 3"
      (by IIEC)
```

**Direct Link**: https://play.google.com/store/apps/details?id=ru.iiec.pydroid3

### Step 2: First Launch Setup

```
┌──────────────────────────────────────────────────────────────┐
│                  Pydroid 3 First Launch                       │
└──────────────────────────────────────────────────────────────┘

1. Open Pydroid 3
   └─ Wait for initialization (30-60 seconds)

2. Grant Permissions
   ├─ Storage Access ✅ (Required)
   ├─ Install Dependencies ✅ (Optional but recommended)
   └─ Allow notifications ✅ (For build alerts)

3. Download Python Libraries
   └─ "Download" button appears
       └─ Downloads Python 3.11 (~100MB)
       └─ Wait 2-5 minutes

4. Ready to Use! ✅
```

### Step 3: Install pip (Package Manager)

```python
# In Pydroid 3:
# Menu → Terminal → Run:

pip install --upgrade pip
```

## 📦 Python Manifest System

Our project includes a **Python Manifest** (equivalent to `AndroidManifest.xml` for Android).

### Location

```
python/
├── manifest.py          ← Main manifest file
├── requirements.txt     ← Python dependencies
├── scripts/
│   ├── build.py        ← Build automation
│   └── test.py         ← Test automation
├── automation/
│   └── git_sync.py     ← Git sync script
└── tools/
    └── project_analyzer.py ← Project analysis
```

### Understanding manifest.py

```python
# python/manifest.py

PROJECT = {
    "name": "AndroidCommandCenter",
    "package": "com.androidcommandcenter",
    "version": "1.0.0",
    "version_code": 1,
    "min_python_version": "3.8"
}

SCRIPTS = {
    "build": {
        "path": "scripts/build.py",
        "description": "Build Android project",
        "permissions": ["file_system", "execute_gradle"]
    },
    "test": {
        "path": "scripts/test.py",
        "description": "Run automated tests"
    }
}

DEPENDENCIES = {
    "core": ["requests", "gitpython", "pyyaml"],
    "automation": ["invoke", "click", "rich"],
    "development": ["black", "pylint", "pytest"]
}
```

### Viewing Manifest

```bash
# In Pydroid 3 Terminal:
cd /storage/emulated/0/AndroidCommandCenter/python
python manifest.py
```

Output:
```
============================================================
  AndroidCommandCenter - Python Manifest
============================================================

Version: 1.0.0
Package: com.androidcommandcenter
Description: Complete Android template with Python automation

Registered Scripts:
  • build: Build Android project
  • test: Run automated tests
  • deploy: Deploy app to device or store
  • git_sync: Automated Git synchronization
  • code_generator: Generate boilerplate code
  • project_analyzer: Analyze project structure

Total Dependencies: 15
Automation Tasks: 3
Pydroid Compatible: True
```

## 🚀 Running Python Scripts

### Method 1: Using Pydroid IDE

```
┌──────────────────────────────────────────────────────────────┐
│              Running Scripts in Pydroid 3                     │
└──────────────────────────────────────────────────────────────┘

1. Open Pydroid 3

2. Menu → Open
   └─ Navigate to: AndroidCommandCenter/python/scripts/

3. Open file (e.g., build.py)

4. Press ▶️ Play button (top right)
   └─ Script executes
   └─ Output shown in terminal

5. View Results
   └─ Scroll through output
   └─ Check for errors
```

### Method 2: Using Terminal

```bash
# In Pydroid 3:
# Menu → Terminal

cd /storage/emulated/0/AndroidCommandCenter/python

# Run build script
python scripts/build.py --variant debug

# Run test script
python scripts/test.py --unit

# Run git sync
python automation/git_sync.py --auto-commit

# Run project analyzer
python tools/project_analyzer.py --detailed
```

### Method 3: Quick Run Mode

```python
# Create a launcher script: run.py

import sys
from pathlib import Path

# Add python directory to path
sys.path.insert(0, str(Path(__file__).parent))

from manifest import SCRIPTS, get_script_info

def main():
    print("AndroidCommandCenter - Quick Runner\n")
    print("Available scripts:")
    
    scripts = list(SCRIPTS.keys())
    for i, name in enumerate(scripts, 1):
        info = get_script_info(name)
        print(f"  {i}. {name}: {info['description']}")
    
    choice = input("\nEnter number to run: ")
    
    try:
        idx = int(choice) - 1
        script_name = scripts[idx]
        script_info = SCRIPTS[script_name]
        
        # Import and run
        module = __import__(
            script_info['path'].replace('/', '.').replace('.py', ''),
            fromlist=['main']
        )
        module.main()
    except:
        print("Invalid choice!")

if __name__ == "__main__":
    main()
```

## 🏗️ Build Automation with Python

### Installing Dependencies

```bash
# In Pydroid 3 Terminal:
cd /storage/emulated/0/AndroidCommandCenter/python
pip install -r requirements.txt
```

**Note**: Some packages may not install on Pydroid. The core automation scripts work without them.

### Building Your App

```bash
# Debug build
python scripts/build.py --variant debug

# Release build
python scripts/build.py --variant release

# Clean build
python scripts/build.py --clean --variant debug

# Build with lint
python scripts/build.py --lint --variant debug

# Show APK info
python scripts/build.py --info --variant debug
```

### Build Script Output

```
============================================================
  AndroidCommandCenter - Build Script
============================================================

🧹 Cleaning build directories...

🔨 Running: ./gradlew clean

> Task :clean

BUILD SUCCESSFUL in 2s
1 actionable task: 1 executed
✅ Clean completed

📦 Building debug APK...

🔨 Running: ./gradlew assembleDebug

> Task :app:compileDebugKotlin
> Task :app:assembleDebug

BUILD SUCCESSFUL in 45s
87 actionable tasks: 87 executed

============================================================
✅ Build Successful!
============================================================
📦 APK: app/build/outputs/apk/debug/app-debug.apk
📏 Size: 8.42 MB
🕐 Built: 2024-11-26 14:30:15
============================================================
```

### Automated Testing

```bash
# Run unit tests only
python scripts/test.py --unit

# Run instrumented tests (requires device)
python scripts/test.py --instrumented

# Run all tests
python scripts/test.py
```

## 🔄 Git Integration

### Git Sync Script

```bash
# Check status (no changes made)
python automation/git_sync.py

# Auto-commit changes
python automation/git_sync.py --auto-commit

# Auto-commit and push
python automation/git_sync.py --auto-commit --push
```

### Example Output

```
============================================================
  AndroidCommandCenter - Git Sync
============================================================
📥 Pulling latest changes...
Already up to date.

📝 Changes detected:
 M app/src/main/java/com/androidcommandcenter/MainActivity.kt
 M python/scripts/build.py

📝 Staging changes...
💾 Committing: Auto sync 2024-11-26 14:35:21
[main a1b2c3d] Auto sync 2024-11-26 14:35:21
 2 files changed, 45 insertions(+), 12 deletions(-)
 
📤 Pushing to GitHub...
To https://github.com/Markus911111/AndroidCommandCenter.git
   d4e5f6g..a1b2c3d  main -> main

✅ Sync complete!
```

### Git Configuration

```python
# Create python/config.py

GIT_CONFIG = {
    "auto_commit": True,
    "auto_push": False,
    "commit_message_template": "Auto sync {timestamp}",
    "excluded_files": [
        "*.pyc",
        "__pycache__",
        ".cache",
        "*.log"
    ]
}
```

## 🔧 Creating Widgets

### Step 1: Create Widget Script

```python
# python/widgets/quick_build.py

"""
Quick Build Widget
Builds debug APK with one tap from home screen
"""

import sys
from pathlib import Path

# Add parent to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from scripts.build import AndroidBuilder

def main():
    """Widget entry point"""
    try:
        # Show notification (Pydroid API)
        try:
            import androidhelper
            droid = androidhelper.Android()
            droid.makeToast("Building app...")
        except:
            pass
        
        # Build
        builder = AndroidBuilder()
        result = builder.build_debug()
        
        # Notify result
        try:
            if result:
                droid.makeToast("✅ Build successful!")
                droid.notify("Build Complete", "APK ready")
            else:
                droid.makeToast("❌ Build failed")
                droid.notify("Build Failed", "Check logs")
        except:
            print("Build completed")
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
```

### Step 2: Add Widget to Home Screen

```
1. Long press on Galaxy S24 home screen

2. Tap "Widgets"

3. Find "Pydroid 3" section

4. Drag "Pydroid script" widget to home screen

5. Configure widget:
   ├─ Name: "Quick Build"
   ├─ Script: /storage/emulated/0/AndroidCommandCenter/python/widgets/quick_build.py
   └─ Icon: Choose build icon

6. Tap widget to run! ⚡
```

### Widget Ideas

```python
# python/widgets/git_sync_widget.py
"""One-tap Git sync"""

# python/widgets/run_tests_widget.py
"""One-tap test execution"""

# python/widgets/project_stats_widget.py
"""Show project statistics"""

# python/widgets/deploy_widget.py
"""One-tap deployment"""
```

## 📊 Project Analysis

### Running Analyzer

```bash
python tools/project_analyzer.py

# Detailed analysis
python tools/project_analyzer.py --detailed
```

### Example Output

```
============================================================
  AndroidCommandCenter - Project Analysis
============================================================

📊 Analyzing project...


============================================================
  Project Statistics
============================================================

📁 Total Files: 187
📝 Code Files: 95
📏 Total Lines of Code: 12,453

📊 Lines by Language:
      .kt:    3,245 lines
      .py:    2,156 lines
     .xml:    1,892 lines
     .yml:      456 lines
     .md:    4,704 lines

🔍 Key Components:
   ✅ MainActivity.kt
   ✅ build.gradle.kts
   ✅ AndroidManifest.xml
   ✅ Python Manifest

============================================================
```

## 🎨 Advanced Features

### Custom Automation Tasks

```python
# python/automation/custom_task.py

import schedule
import time
from datetime import datetime

def automated_build():
    """Run automated build"""
    print(f"[{datetime.now()}] Starting automated build...")
    # Your build logic here

def automated_sync():
    """Run automated sync"""
    print(f"[{datetime.now()}] Syncing with Git...")
    # Your sync logic here

# Schedule tasks
schedule.every().day.at("02:00").do(automated_build)
schedule.every().hour.do(automated_sync)

# Run scheduler
while True:
    schedule.run_pending()
    time.sleep(60)
```

### Notifications

```python
# Using Pydroid's Android API

try:
    import androidhelper
    droid = androidhelper.Android()
    
    # Show toast
    droid.makeToast("Hello from Python!")
    
    # Show notification
    droid.notify("Title", "Message body")
    
    # Vibrate
    droid.vibrate(300)  # milliseconds
    
except ImportError:
    print("Not running on Android")
```

### File System Access

```python
# Access Android storage

from pathlib import Path

# Internal storage
storage = Path("/storage/emulated/0")

# Project directory
project = storage / "AndroidCommandCenter"

# Downloads
downloads = storage / "Download"

# DCIM (Camera)
camera = storage / "DCIM"

# List files
for file in project.glob("*.md"):
    print(file.name)
```

## 🆚 Python vs Termux

### When to Use Pydroid 3

```
✅ Quick automation scripts
✅ Testing Python code
✅ Building small utilities
✅ Learning Python
✅ Creating home screen widgets
✅ GUI development (Tkinter/Kivy)
✅ Beginner-friendly environment
```

### When to Use Termux

```
✅ Complex Git operations
✅ SSH server/client
✅ Multiple terminal sessions
✅ Advanced shell scripting
✅ Installing Linux packages
✅ Running background services
✅ System administration
```

### Best Practice: Use Both!

```
┌──────────────────────────────────────────────────────────────┐
│              Optimal Workflow                                 │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  Pydroid 3:                  Termux:                        │
│  ──────────                  ───────                        │
│  • Quick builds              • Git operations               │
│  • Test automation           • Clone repositories           │
│  • Project analysis          • SSH access                   │
│  • Home widgets              • Complex workflows            │
│  • Python development        • System tasks                 │
│                                                              │
│              Work together seamlessly!                       │
│                                                              │
└──────────────────────────────────────────────────────────────┘
```

## 🐛 Troubleshooting

### Issue: pip install fails

**Solution**:
```bash
# Update pip
pip install --upgrade pip

# Try with --user flag
pip install --user package-name

# Check space
df -h /storage/emulated/0
```

### Issue: Import errors

**Solution**:
```python
# Add to top of script
import sys
from pathlib import Path

# Add python directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))
```

### Issue: Script can't find files

**Solution**:
```python
# Use absolute paths
from pathlib import Path

# Get script directory
script_dir = Path(__file__).parent

# Get project root
project_root = script_dir.parent.parent

# Construct paths
apk_path = project_root / "app/build/outputs/apk/debug/app-debug.apk"
```

### Issue: Gradlew not executable

**Solution**:
```python
import os
import stat

# Make gradlew executable
gradlew = Path("gradlew")
os.chmod(gradlew, os.stat(gradlew).st_mode | stat.S_IEXEC)
```

### Issue: "Permission denied"

**Solution**:
```
1. Pydroid 3 → Menu → Settings
2. Enable "Storage permissions"
3. Grant all permissions
4. Restart Pydroid 3
```

## 📚 Learning Resources

### Python Basics
- [Python.org Tutorial](https://docs.python.org/3/tutorial/)
- [Real Python](https://realpython.com/)
- [Python for Beginners](https://www.python.org/about/gettingstarted/)

### Pydroid 3
- [Pydroid 3 Wiki](https://github.com/IIEC-IS/Pydroid-3-Docs)
- [Android Scripting](https://github.com/kuri65536/sl4a)

### Python for Android
- [Kivy](https://kivy.org/) - GUI framework
- [BeeWare](https://beeware.org/) - Python on mobile
- [python-for-android](https://python-for-android.readthedocs.io/)

## ✅ Pydroid 3 Checklist

- [ ] Installed Pydroid 3 from Play Store
- [ ] Downloaded Python 3.11 runtime
- [ ] Granted storage permissions
- [ ] Installed pip packages
- [ ] Tested manifest.py
- [ ] Ran build.py successfully
- [ ] Created home screen widget
- [ ] Configured git sync automation
- [ ] Ran project analyzer

## 🎯 Quick Start Commands

```bash
# Navigate to project
cd /storage/emulated/0/AndroidCommandCenter/python

# View manifest
python manifest.py

# Build app
python scripts/build.py

# Run tests
python scripts/test.py

# Sync Git
python automation/git_sync.py --auto-commit

# Analyze project
python tools/project_analyzer.py
```

## 🎓 Next Steps

1. **Explore Scripts**: Try each Python script
2. **Customize**: Modify scripts for your needs
3. **Create Widgets**: Add home screen shortcuts
4. **Automate**: Set up scheduled tasks
5. **Learn**: Study Python and improve scripts

---

**Navigation**:  
← [11-VISUAL-GUIDE.md](11-VISUAL-GUIDE.md) | [INDEX.md](INDEX.md) | [Back to README](../README.md) →
