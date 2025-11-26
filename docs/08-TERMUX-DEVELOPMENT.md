# 📱 Termux Development Guide for Galaxy S24

Develop Android apps directly on your Galaxy S24 using Termux - a powerful Linux terminal emulator for Android!

## 📋 Table of Contents

1. [What is Termux?](#what-is-termux)
2. [Installing Termux](#installing-termux)
3. [Setting Up Development Environment](#setting-up-development-environment)
4. [Building Android Apps in Termux](#building-android-apps-in-termux)
5. [Using Git in Termux](#using-git-in-termux)
6. [Advanced Termux Configuration](#advanced-termux-configuration)
7. [Termux with Android Studio](#termux-with-android-studio)
8. [Troubleshooting](#troubleshooting)

## 🎯 What is Termux?

**Termux** is a powerful Linux terminal emulator for Android that provides:
- ✅ Full Linux environment on Android
- ✅ Package manager (apt/pkg)
- ✅ Development tools (Git, Python, Node.js, etc.)
- ✅ SSH access to your device
- ✅ No root required!

### Why Use Termux for Android Development?

- 📱 **On-Device Development**: Code directly on your Galaxy S24
- 🚀 **Quick Testing**: Instant builds without computer
- 🔄 **Git Integration**: Clone, commit, push from your phone
- 🛠️ **Full Toolchain**: Access to Linux development tools
- 📶 **Work Anywhere**: No need for a desktop computer

### What You Can Do

- ✅ Clone and manage Git repositories
- ✅ Edit code with vim, nano, or micro
- ✅ Run Gradle builds
- ✅ Execute Git commands
- ✅ Install development tools
- ✅ Run scripts and automation
- ❌ Cannot compile full Android apps (no Android SDK support)
- ❌ Cannot run Android emulator

**Note**: Termux is excellent for Git operations, scripting, and lightweight development, but full Android app compilation still requires a desktop or cloud build system.

## 📲 Installing Termux

### Step 1: Download Termux

**⚠️ IMPORTANT**: Do NOT install from Google Play Store (outdated version)!

Install from **F-Droid** (recommended):

1. **Download F-Droid**: https://f-droid.org/
2. Install F-Droid APK
3. Open F-Droid app
4. Search for "Termux"
5. Install **Termux** (main app)
6. Optionally install:
   - **Termux:API** - Access Android features
   - **Termux:Widget** - Home screen shortcuts
   - **Termux:Styling** - Customize appearance

**OR Download Directly**:
- GitHub Releases: https://github.com/termux/termux-app/releases
- Download latest APK (e.g., `termux-app_v0.118.0+github-debug.apk`)

### Step 2: Initial Setup

1. Open Termux
2. Wait for initialization (first time only)
3. You'll see a command prompt: `$`

### Step 3: Update Packages

```bash
# Update package lists
pkg update

# Upgrade installed packages
pkg upgrade
```

Press **Y** when prompted.

## 🔧 Setting Up Development Environment

### Essential Tools Installation

```bash
# Update system
pkg update && pkg upgrade

# Install essential tools
pkg install git curl wget openssh

# Install text editors
pkg install vim nano micro

# Install development tools
pkg install python nodejs-lts

# Install build tools
pkg install make cmake clang

# Install utilities
pkg install tmux tree htop
```

### Configure Storage Access

Access your phone's storage:

```bash
termux-setup-storage
```

Grant storage permission when prompted. This creates shortcuts:
- `~/storage/shared` - Internal storage
- `~/storage/downloads` - Downloads folder
- `~/storage/dcim` - Camera photos

### Install Oh My Zsh (Optional but Recommended)

Enhanced shell with better features:

```bash
# Install zsh
pkg install zsh

# Install Oh My Zsh
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"

# Set as default shell
chsh -s zsh
```

## 🏗️ Building Android Apps in Termux

### Method 1: Using Gradle Wrapper (Lightweight)

While you can't compile full APKs without Android SDK, you can:

1. **Clone the Repository**:
```bash
cd ~/storage/shared
git clone https://github.com/Markus911111/AndroidCommandCenter.git
cd AndroidCommandCenter
```

2. **Edit Code**:
```bash
# Install code editor
pkg install micro

# Edit files
micro app/src/main/java/com/lindy/android/MainActivity.kt
```

3. **Run Gradle Tasks** (limited without Android SDK):
```bash
# Make gradlew executable
chmod +x gradlew

# View available tasks
./gradlew tasks

# Clean project
./gradlew clean

# Some tasks will fail without Android SDK
```

### Method 2: Remote Build Server

Use a cloud build service or remote machine:

1. **Set up SSH Connection**:
```bash
# Install SSH client
pkg install openssh

# Connect to remote server
ssh user@your-build-server.com

# Work on remote machine
cd /path/to/project
./gradlew assembleDebug
```

2. **Transfer Built APK**:
```bash
# Download APK from server
scp user@server:/path/to/app.apk ~/storage/downloads/
```

### Method 3: GitHub Actions (Recommended)

Build in the cloud automatically:

1. **Commit and Push Changes**:
```bash
git add .
git commit -m "Updated MainActivity"
git push origin main
```

2. **GitHub Actions builds automatically** (if configured)

3. **Download APK** from GitHub Actions artifacts

## 📦 Using Git in Termux

### Initial Git Configuration

```bash
# Set your name and email
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"

# Set default editor
git config --global core.editor "micro"

# View configuration
git config --list
```

### Clone Repository

```bash
# Navigate to storage
cd ~/storage/shared

# Clone this template
git clone https://github.com/Markus911111/AndroidCommandCenter.git

# Enter directory
cd AndroidCommandCenter
```

### Basic Git Workflow

```bash
# Check status
git status

# Create new branch
git checkout -b feature/my-feature

# Make changes (edit files)
micro app/src/main/java/com/lindy/android/MainActivity.kt

# Stage changes
git add .

# Commit changes
git commit -m "Add new feature"

# Push to GitHub
git push origin feature/my-feature

# Switch branches
git checkout main

# Pull latest changes
git pull origin main

# View commit history
git log --oneline --graph --all

# View differences
git diff
```

### GitHub Authentication

#### Using Personal Access Token (Recommended)

1. **Generate Token on GitHub**:
   - Go to GitHub → Settings → Developer settings
   - Personal access tokens → Generate new token
   - Select scopes: `repo`, `workflow`
   - Copy the token

2. **Use Token for Authentication**:
```bash
# When pushing, use token as password
git push origin main
# Username: your-github-username
# Password: [paste-your-token]
```

3. **Cache Credentials**:
```bash
# Cache for 1 hour
git config --global credential.helper 'cache --timeout=3600'

# Or store permanently (less secure)
git config --global credential.helper store
```

#### Using SSH Keys

```bash
# Generate SSH key
ssh-keygen -t ed25519 -C "your.email@example.com"

# Press Enter for default location
# Optionally set a passphrase

# Display public key
cat ~/.ssh/id_ed25519.pub

# Copy the output and add to GitHub:
# GitHub → Settings → SSH and GPG keys → New SSH key
```

Update remote URL to use SSH:
```bash
git remote set-url origin git@github.com:Markus911111/AndroidCommandCenter.git
```

## 🎨 Advanced Termux Configuration

### Customize Appearance

```bash
# Install Termux:Styling from F-Droid for GUI options

# Or manually edit colors
mkdir -p ~/.termux
nano ~/.termux/colors.properties
```

Example color scheme:
```properties
# Background and foreground
background=#1e1e1e
foreground=#d4d4d4

# Cursor
cursor=#aeafad

# Colors
color0=#000000
color1=#cd3131
color2=#0dbc79
color3=#e5e510
color4=#2472c8
color5=#bc3fbc
color6=#11a8cd
color7=#e5e5e5
```

### Keyboard Shortcuts

Create custom keys:

```bash
nano ~/.termux/termux.properties
```

Add extra keys:
```properties
extra-keys = [ \
 ['ESC','/','-','HOME','UP','END','PGUP'], \
 ['TAB','CTRL','ALT','LEFT','DOWN','RIGHT','PGDN'] \
]
```

Restart Termux to apply.

### Create Aliases

```bash
# Edit shell config
nano ~/.bashrc  # or ~/.zshrc if using zsh

# Add aliases
alias ll='ls -lah'
alias gs='git status'
alias ga='git add'
alias gc='git commit'
alias gp='git push'
alias gl='git log --oneline --graph'
alias gd='git diff'
alias update='pkg update && pkg upgrade'

# Save and reload
source ~/.bashrc  # or source ~/.zshrc
```

### Tmux for Multiple Sessions

```bash
# Install tmux
pkg install tmux

# Start tmux
tmux

# Tmux commands (prefix: Ctrl+B)
# Ctrl+B, C     - New window
# Ctrl+B, N     - Next window
# Ctrl+B, P     - Previous window
# Ctrl+B, %     - Split vertical
# Ctrl+B, "     - Split horizontal
# Ctrl+B, D     - Detach session
# tmux attach   - Reattach session
```

## 💻 Termux with Android Studio

### Install Termux:API

Termux:API enables interaction with Android features:

```bash
# Install from F-Droid
# Then install package
pkg install termux-api

# Test API
termux-battery-status
termux-notification "Hello from Termux!"
```

### Useful Termux:API Commands

```bash
# Show notification
termux-notification -t "Build Complete" -c "Your app is ready!"

# Get device info
termux-wifi-connectioninfo
termux-telephony-deviceinfo

# Share file
termux-share /path/to/file.apk

# Open URL
termux-open-url https://github.com

# Vibrate device
termux-vibrate -d 1000

# Text to speech
termux-tts-speak "Build successful"

# Take photo
termux-camera-photo ~/photo.jpg
```

### Automate Builds with Scripts

Create a build script:

```bash
#!/data/data/com.termux/files/usr/bin/bash

# build-and-notify.sh
cd ~/storage/shared/AndroidCommandCenter

echo "Starting build..."
termux-notification -t "Build Started" -c "Building your app..."

# Attempt build (will fail without SDK, but demonstrates concept)
./gradlew assembleDebug 2>&1 | tee build.log

if [ $? -eq 0 ]; then
    termux-notification -t "Build Success" -c "APK ready!"
    termux-tts-speak "Build successful"
else
    termux-notification -t "Build Failed" -c "Check logs"
    termux-tts-speak "Build failed"
fi
```

Make executable:
```bash
chmod +x build-and-notify.sh
./build-and-notify.sh
```

### Termux Widget (Home Screen Shortcuts)

1. Install **Termux:Widget** from F-Droid
2. Create shortcuts folder:
```bash
mkdir -p ~/.shortcuts
```

3. Create script in shortcuts:
```bash
#!/data/data/com.termux/files/usr/bin/bash
cd ~/storage/shared/AndroidCommandCenter
git pull origin main
termux-notification -t "Git Pull" -c "Repository updated!"
```

4. Save as `~/.shortcuts/update-repo.sh`
5. Make executable: `chmod +x ~/.shortcuts/update-repo.sh`
6. Add Termux widget to home screen
7. Tap to run script!

## 🌐 Setting Up SSH Server

Access Termux from your computer:

```bash
# Install SSH server
pkg install openssh

# Set password
passwd

# Start SSH server
sshd

# Find your IP address
ifconfig wlan0

# On your computer, connect:
# ssh -p 8022 u0_a123@192.168.1.XXX
# (use the IP address shown by ifconfig)
```

From computer, you can:
```bash
# Transfer files
scp -P 8022 file.txt u0_a123@192.168.1.XXX:~/

# Remote development
ssh -p 8022 u0_a123@192.168.1.XXX
```

## 🔧 Development Workflow on Galaxy S24

### Recommended Setup

1. **Termux** - Git operations, code editing, scripts
2. **AIDE or Code Editor** - Android app for code editing with syntax highlighting
3. **GitHub Actions** - Cloud builds
4. **Termux:API** - Notifications and automation

### Example Daily Workflow

```bash
# Morning: Update repository
cd ~/storage/shared/AndroidCommandCenter
git pull origin main

# Edit code using micro editor
micro app/src/main/java/com/lindy/android/MainActivity.kt

# Stage and commit changes
git add .
git commit -m "Updated MainActivity"

# Push to GitHub (triggers cloud build)
git push origin main

# Check build status on GitHub
termux-open-url "https://github.com/Markus911111/AndroidCommandCenter/actions"

# Download APK when build completes
# Install and test on device
```

## 🎯 Practical Examples

### Quick Code Edit and Push

```bash
# Navigate to project
cd ~/storage/shared/AndroidCommandCenter

# Edit file
micro app/src/main/res/values/strings.xml

# Quick commit and push
git add .
git commit -m "Update strings"
git push

# Notification when done
termux-notification -t "Pushed" -c "Changes uploaded to GitHub"
```

### Automated Daily Backup

```bash
#!/data/data/com.termux/files/usr/bin/bash
# backup-daily.sh

cd ~/storage/shared/AndroidCommandCenter

# Commit any changes
git add .
git commit -m "Auto backup $(date +%Y-%m-%d)"

# Push to GitHub
git push origin main

# Notify
termux-notification -t "Backup Complete" -c "Project backed up to GitHub"
```

Schedule with cron:
```bash
pkg install cronie
crontab -e

# Add line (daily at 8 PM):
0 20 * * * ~/backup-daily.sh
```

## 🐛 Troubleshooting

### Issue: Permission Denied

```bash
# Fix: Make script executable
chmod +x script.sh
```

### Issue: Command Not Found

```bash
# Update package database
pkg update

# Search for package
pkg search package-name

# Install package
pkg install package-name
```

### Issue: Storage Access Denied

```bash
# Re-run storage setup
termux-setup-storage

# Check permissions in Android Settings
# Settings → Apps → Termux → Permissions → Storage
```

### Issue: Git Push Fails

```bash
# Check remote URL
git remote -v

# Set credential helper
git config --global credential.helper cache

# Try push again with token as password
git push
```

### Issue: Gradle Daemon Issues

```bash
# Gradle might have memory issues
# Stop all Gradle daemons
./gradlew --stop

# Clean and try again
./gradlew clean
```

### Issue: Out of Space

```bash
# Check storage
df -h

# Clean package cache
pkg clean

# Remove unused packages
pkg autoremove
```

## 📚 Useful Termux Packages

```bash
# Productivity
pkg install tmux htop tree ncdu

# Development
pkg install git vim micro python nodejs

# Network tools
pkg install curl wget openssh rsync

# Build tools
pkg install make cmake clang

# File management
pkg install mc ranger

# Documentation
pkg install man tldr

# Media
pkg install ffmpeg imagemagick

# Utilities
pkg install zip unzip tar gzip
```

## 💡 Tips for Galaxy S24 Development

### Use Samsung DeX Mode

Connect to external display for desktop-like experience:
1. Enable DeX mode
2. Use keyboard and mouse
3. Run Termux in windowed mode
4. Much easier for coding!

### Split Screen

Use Android split screen:
1. Open Termux
2. Open browser with documentation
3. Use split screen for reference while coding

### Bluetooth Keyboard

Pair Bluetooth keyboard:
1. Settings → Bluetooth
2. Pair keyboard
3. Much faster typing in Termux!

### Stylus Support

Galaxy S24 S Pen (if available):
- Use with code editors
- Precise touch selection
- Gestures for copy/paste

## 🚀 Next Level: Cloud Development

### GitHub Codespaces

1. Open repository on GitHub
2. Click **Code** → **Codespaces**
3. Create codespace
4. Full VS Code in browser
5. Access from Galaxy S24 browser!

### Gitpod

Similar to Codespaces:
1. Prefix GitHub URL with `gitpod.io/#`
2. Example: `gitpod.io/#https://github.com/Markus911111/AndroidCommandCenter`
3. Full IDE in browser
4. Works on Galaxy S24!

## 📖 Learning Resources

- **Termux Wiki**: https://wiki.termux.com/
- **Termux GitHub**: https://github.com/termux/termux-app
- **F-Droid**: https://f-droid.org/
- **Linux Commands**: https://ss64.com/bash/
- **Git Documentation**: https://git-scm.com/doc

## ✅ Termux Development Checklist

- [ ] Installed Termux from F-Droid
- [ ] Updated packages
- [ ] Configured storage access
- [ ] Installed Git
- [ ] Configured Git identity
- [ ] Installed text editor
- [ ] Cloned AndroidCommandCenter repository
- [ ] Set up GitHub authentication
- [ ] Created useful aliases
- [ ] Installed Termux:API (optional)
- [ ] Set up SSH (optional)

## 🎓 Conclusion

Termux transforms your Galaxy S24 into a portable development machine! While you can't compile full Android apps without the SDK, you can:

✅ Manage Git repositories  
✅ Edit code on the go  
✅ Run scripts and automation  
✅ Trigger cloud builds  
✅ Learn Linux and command line  
✅ Be productive anywhere  

Combined with cloud build services, Termux makes your Galaxy S24 a powerful development device!

---

**Navigation**:  
← [07-TROUBLESHOOTING.md](07-TROUBLESHOOTING.md) | [INDEX.md](INDEX.md) | [Back to README](../README.md) →
