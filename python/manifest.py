#!/usr/bin/env python3
"""
Python Manifest System for Android Command Center
Equivalent to AndroidManifest.xml but for Python automation

This manifest defines Python scripts, dependencies, and automation tasks
for the Android Command Center project.
"""

__version__ = "1.0.0"
__author__ = "Android Command Center"

# Project Information
PROJECT = {
    "name": "AndroidCommandCenter",
    "package": "com.androidcommandcenter",
    "version": "1.0.0",
    "version_code": 1,
    "description": "Complete Android template with Python automation",
    "min_python_version": "3.8",
    "target_python_version": "3.11"
}

# Python Dependencies
DEPENDENCIES = {
    "core": [
        "requests>=2.31.0",
        "gitpython>=3.1.40",
        "pyyaml>=6.0.1",
        "python-dotenv>=1.0.0"
    ],
    "automation": [
        "invoke>=2.2.0",
        "click>=8.1.7",
        "rich>=13.7.0"
    ],
    "development": [
        "black>=23.12.0",
        "pylint>=3.0.3",
        "pytest>=7.4.3"
    ],
    "android": [
        "android-tools>=0.2.0"
    ],
    "optional": [
        "colorama>=0.4.6",
        "tqdm>=4.66.1"
    ]
}

# Python Scripts Registry
SCRIPTS = {
    "build": {
        "path": "scripts/build.py",
        "description": "Build Android project",
        "permissions": ["file_system", "execute_gradle"],
        "entry_point": "main"
    },
    "test": {
        "path": "scripts/test.py",
        "description": "Run automated tests",
        "permissions": ["file_system", "execute_gradle", "adb"],
        "entry_point": "main"
    },
    "deploy": {
        "path": "scripts/deploy.py",
        "description": "Deploy app to device or store",
        "permissions": ["file_system", "adb", "network"],
        "entry_point": "main"
    },
    "git_sync": {
        "path": "automation/git_sync.py",
        "description": "Automated Git synchronization",
        "permissions": ["file_system", "network", "git"],
        "entry_point": "sync"
    },
    "code_generator": {
        "path": "tools/code_generator.py",
        "description": "Generate boilerplate code",
        "permissions": ["file_system"],
        "entry_point": "generate"
    },
    "project_analyzer": {
        "path": "tools/project_analyzer.py",
        "description": "Analyze project structure and statistics",
        "permissions": ["file_system"],
        "entry_point": "analyze"
    }
}

# Automation Tasks (like Android Services)
AUTOMATION_TASKS = {
    "continuous_sync": {
        "script": "git_sync",
        "schedule": "*/30 * * * *",  # Every 30 minutes
        "enabled": False
    },
    "daily_backup": {
        "script": "git_sync",
        "schedule": "0 2 * * *",  # Daily at 2 AM
        "enabled": True
    },
    "auto_build": {
        "script": "build",
        "trigger": "on_commit",
        "enabled": False
    }
}

# Permissions (Python equivalent)
PERMISSIONS = {
    "file_system": "Read/write project files",
    "execute_gradle": "Execute Gradle commands",
    "adb": "Android Debug Bridge access",
    "network": "Network access for API calls",
    "git": "Git operations",
    "notifications": "Send system notifications (Pydroid)",
    "storage": "Access device storage"
}

# Features (Python capabilities)
FEATURES = {
    "build_automation": True,
    "test_automation": True,
    "git_integration": True,
    "code_generation": True,
    "project_analysis": True,
    "ci_cd_integration": True,
    "adb_tools": True
}

# Configuration
CONFIG = {
    "project_root": ".",
    "app_module": "app",
    "build_output": "app/build/outputs",
    "python_scripts": "python",
    "logs_dir": "python/logs",
    "cache_dir": "python/.cache"
}

# Pydroid 3 Specific Settings
PYDROID_CONFIG = {
    "compatible": True,
    "min_version": "5.0",
    "features_used": [
        "notifications",
        "storage_access",
        "background_execution"
    ],
    "widgets_supported": True
}


def get_script_info(script_name: str) -> dict:
    """Get information about a registered script"""
    return SCRIPTS.get(script_name, {})


def get_all_scripts() -> list:
    """Get list of all registered scripts"""
    return list(SCRIPTS.keys())


def get_dependencies(category: str = "all") -> list:
    """Get dependencies for a specific category or all"""
    if category == "all":
        all_deps = []
        for deps in DEPENDENCIES.values():
            all_deps.extend(deps)
        return all_deps
    return DEPENDENCIES.get(category, [])


def verify_permissions(script_name: str) -> bool:
    """Verify if script has required permissions"""
    script = SCRIPTS.get(script_name)
    if not script:
        return False
    return all(perm in PERMISSIONS for perm in script.get("permissions", []))


def print_manifest():
    """Print manifest information"""
    print(f"\n{'='*60}")
    print(f"  {PROJECT['name']} - Python Manifest")
    print(f"{'='*60}\n")
    
    print(f"Version: {PROJECT['version']}")
    print(f"Package: {PROJECT['package']}")
    print(f"Description: {PROJECT['description']}\n")
    
    print("Registered Scripts:")
    for name, info in SCRIPTS.items():
        print(f"  • {name}: {info['description']}")
    
    print(f"\nTotal Dependencies: {len(get_dependencies())}")
    print(f"Automation Tasks: {len(AUTOMATION_TASKS)}")
    print(f"Pydroid Compatible: {PYDROID_CONFIG['compatible']}")


if __name__ == "__main__":
    print_manifest()
