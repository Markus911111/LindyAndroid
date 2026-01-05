#!/usr/bin/env python3
"""
Build Script for Android Command Center
Automates the build process with Python

Usage:
    python build.py [options]
    python build.py --variant debug
    python build.py --clean
"""

import subprocess
import sys
import os
from pathlib import Path
from datetime import datetime
import argparse

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))
from manifest import PROJECT, CONFIG


class AndroidBuilder:
    """Handles Android project building"""
    
    def __init__(self, project_root="."):
        self.project_root = Path(project_root)
        self.gradlew = self.project_root / "gradlew"
        if sys.platform == "win32":
            self.gradlew = self.project_root / "gradlew.bat"
        
        # Make gradlew executable (Unix/Linux/Termux)
        if not sys.platform == "win32":
            os.chmod(self.gradlew, 0o755)
    
    def run_gradle(self, *tasks, **kwargs):
        """Execute Gradle command"""
        cmd = [str(self.gradlew)] + list(tasks)
        
        print(f"\n🔨 Running: {' '.join(cmd)}\n")
        
        try:
            result = subprocess.run(
                cmd,
                cwd=self.project_root,
                capture_output=kwargs.get('capture_output', False),
                text=True,
                check=True
            )
            return result
        except subprocess.CalledProcessError as e:
            print(f"❌ Error: Build failed with exit code {e.returncode}")
            if e.output:
                print(e.output)
            return None
        except FileNotFoundError:
            print(f"❌ Error: gradlew not found at {self.gradlew}")
            return None
    
    def clean(self):
        """Clean build directories"""
        print("🧹 Cleaning build directories...")
        return self.run_gradle("clean")
    
    def build_debug(self):
        """Build debug APK"""
        print("📦 Building debug APK...")
        return self.run_gradle("assembleDebug")
    
    def build_release(self):
        """Build release APK"""
        print("📦 Building release APK...")
        return self.run_gradle("assembleRelease")
    
    def build_bundle(self):
        """Build Android App Bundle"""
        print("📦 Building AAB...")
        return self.run_gradle("bundleRelease")
    
    def lint(self):
        """Run lint checks"""
        print("🔍 Running lint checks...")
        return self.run_gradle("lintDebug")
    
    def get_apk_path(self, variant="debug"):
        """Get path to built APK"""
        if variant == "debug":
            return self.project_root / "app/build/outputs/apk/debug/app-debug.apk"
        else:
            return self.project_root / "app/build/outputs/apk/release/app-release.apk"
    
    def get_apk_info(self, variant="debug"):
        """Get information about built APK"""
        apk_path = self.get_apk_path(variant)
        
        if not apk_path.exists():
            return None
        
        size = apk_path.stat().st_size
        size_mb = size / (1024 * 1024)
        modified = datetime.fromtimestamp(apk_path.stat().st_mtime)
        
        return {
            "path": str(apk_path),
            "size": f"{size_mb:.2f} MB",
            "modified": modified.strftime("%Y-%m-%d %H:%M:%S")
        }


def main():
    """Main build script"""
    parser = argparse.ArgumentParser(
        description="Build Android Command Center"
    )
    parser.add_argument(
        "--variant",
        choices=["debug", "release"],
        default="debug",
        help="Build variant (default: debug)"
    )
    parser.add_argument(
        "--clean",
        action="store_true",
        help="Clean before building"
    )
    parser.add_argument(
        "--lint",
        action="store_true",
        help="Run lint checks"
    )
    parser.add_argument(
        "--bundle",
        action="store_true",
        help="Build AAB instead of APK"
    )
    parser.add_argument(
        "--info",
        action="store_true",
        help="Show APK info only"
    )
    
    args = parser.parse_args()
    
    print("="*60)
    print(f"  {PROJECT['name']} - Build Script")
    print("="*60)
    
    builder = AndroidBuilder()
    
    # Show info only
    if args.info:
        info = builder.get_apk_info(args.variant)
        if info:
            print(f"\n📦 APK Information:")
            print(f"   Path: {info['path']}")
            print(f"   Size: {info['size']}")
            print(f"   Modified: {info['modified']}\n")
        else:
            print(f"\n❌ No APK found for variant: {args.variant}\n")
        return
    
    # Clean if requested
    if args.clean:
        result = builder.clean()
        if not result:
            sys.exit(1)
    
    # Run lint if requested
    if args.lint:
        result = builder.lint()
        if not result:
            print("⚠️  Lint found issues, continuing with build...")
    
    # Build
    if args.bundle:
        result = builder.build_bundle()
    elif args.variant == "release":
        result = builder.build_release()
    else:
        result = builder.build_debug()
    
    if not result:
        print("\n❌ Build failed!\n")
        sys.exit(1)
    
    # Show result
    info = builder.get_apk_info(args.variant)
    if info:
        print("\n" + "="*60)
        print("✅ Build Successful!")
        print("="*60)
        print(f"📦 APK: {info['path']}")
        print(f"📏 Size: {info['size']}")
        print(f"🕐 Built: {info['modified']}")
        print("="*60 + "\n")
    else:
        print("\n✅ Build completed but APK not found\n")


if __name__ == "__main__":
    main()
