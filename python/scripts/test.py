#!/usr/bin/env python3
"""
Test Script for Android Command Center
Automates running Android tests

Usage:
    python test.py
    python test.py --unit
    python test.py --instrumented
"""

import subprocess
import sys
from pathlib import Path
import argparse

sys.path.insert(0, str(Path(__file__).parent.parent))
from manifest import PROJECT


class AndroidTester:
    """Handles Android project testing"""
    
    def __init__(self, project_root="."):
        self.project_root = Path(project_root)
        self.gradlew = self.project_root / "gradlew"
        if sys.platform == "win32":
            self.gradlew = self.project_root / "gradlew.bat"
    
    def run_gradle(self, *tasks):
        """Execute Gradle command"""
        cmd = [str(self.gradlew)] + list(tasks)
        print(f"\n🧪 Running: {' '.join(cmd)}\n")
        
        try:
            subprocess.run(cmd, cwd=self.project_root, check=True)
            return True
        except subprocess.CalledProcessError:
            return False
    
    def check_device(self):
        """Check if device is connected"""
        try:
            result = subprocess.run(
                ["adb", "devices"],
                capture_output=True,
                text=True,
                check=True
            )
            lines = result.stdout.strip().split('\n')
            devices = [l for l in lines[1:] if l.strip() and 'device' in l]
            return len(devices) > 0
        except:
            return False
    
    def run_unit_tests(self):
        """Run unit tests"""
        print("🧪 Running unit tests...")
        return self.run_gradle("testDebugUnitTest")
    
    def run_instrumented_tests(self):
        """Run instrumented tests on device"""
        if not self.check_device():
            print("❌ No device connected!")
            print("   Connect device and enable USB debugging")
            return False
        
        print("🧪 Running instrumented tests...")
        return self.run_gradle("connectedDebugAndroidTest")
    
    def run_all_tests(self):
        """Run all tests"""
        print("🧪 Running all tests...")
        success = self.run_unit_tests()
        if success and self.check_device():
            success = self.run_instrumented_tests()
        return success


def main():
    """Main test script"""
    parser = argparse.ArgumentParser(
        description="Test Android Command Center"
    )
    parser.add_argument(
        "--unit",
        action="store_true",
        help="Run unit tests only"
    )
    parser.add_argument(
        "--instrumented",
        action="store_true",
        help="Run instrumented tests only"
    )
    
    args = parser.parse_args()
    
    print("="*60)
    print(f"  {PROJECT['name']} - Test Script")
    print("="*60)
    
    tester = AndroidTester()
    
    if args.unit:
        success = tester.run_unit_tests()
    elif args.instrumented:
        success = tester.run_instrumented_tests()
    else:
        success = tester.run_all_tests()
    
    if success:
        print("\n✅ All tests passed!\n")
        sys.exit(0)
    else:
        print("\n❌ Tests failed!\n")
        sys.exit(1)


if __name__ == "__main__":
    main()
