#!/usr/bin/env python3
"""
Project Analyzer Tool
Analyzes Android Command Center project structure and statistics

Usage:
    python project_analyzer.py
    python project_analyzer.py --detailed
"""

import sys
from pathlib import Path
import argparse
from collections import defaultdict

sys.path.insert(0, str(Path(__file__).parent.parent))
from manifest import PROJECT


class ProjectAnalyzer:
    """Analyzes project structure"""
    
    def __init__(self, project_root="."):
        self.project_root = Path(project_root)
        self.stats = defaultdict(int)
        self.file_types = defaultdict(int)
    
    def count_lines(self, file_path):
        """Count lines in a file"""
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                return len(f.readlines())
        except:
            return 0
    
    def analyze_file(self, file_path):
        """Analyze a single file"""
        ext = file_path.suffix
        self.file_types[ext] += 1
        
        if ext in ['.kt', '.java', '.py', '.xml', '.yml', '.yaml']:
            lines = self.count_lines(file_path)
            self.stats[f'lines_{ext}'] += lines
            self.stats['total_lines'] += lines
            self.stats['code_files'] += 1
    
    def analyze_directory(self, directory, exclude_dirs=None):
        """Analyze a directory recursively"""
        if exclude_dirs is None:
            exclude_dirs = {'.git', 'build', '.gradle', '.idea', '__pycache__', 'node_modules'}
        
        for item in directory.iterdir():
            if item.is_dir():
                if item.name not in exclude_dirs:
                    self.analyze_directory(item, exclude_dirs)
            else:
                self.analyze_file(item)
                self.stats['total_files'] += 1
    
    def analyze(self):
        """Run analysis"""
        print("="*60)
        print(f"  {PROJECT['name']} - Project Analysis")
        print("="*60)
        print("\n📊 Analyzing project...\n")
        
        self.analyze_directory(self.project_root)
        
        return self.stats, self.file_types
    
    def print_report(self, detailed=False):
        """Print analysis report"""
        stats, file_types = self.analyze()
        
        print("\n" + "="*60)
        print("  Project Statistics")
        print("="*60)
        
        print(f"\n📁 Total Files: {stats['total_files']}")
        print(f"📝 Code Files: {stats['code_files']}")
        print(f"📏 Total Lines of Code: {stats['total_lines']:,}")
        
        print(f"\n📊 Lines by Language:")
        for key, value in sorted(stats.items()):
            if key.startswith('lines_'):
                lang = key.replace('lines_', '')
                print(f"   {lang:>6}: {value:>8,} lines")
        
        if detailed:
            print(f"\n📂 File Types:")
            for ext, count in sorted(file_types.items(), key=lambda x: x[1], reverse=True)[:15]:
                ext_name = ext if ext else "(no extension)"
                print(f"   {ext_name:>10}: {count:>5} files")
        
        # Key files check
        print(f"\n🔍 Key Components:")
        key_files = {
            "MainActivity.kt": self.project_root / "app/src/main/java/com/androidcommandcenter/MainActivity.kt",
            "build.gradle.kts": self.project_root / "app/build.gradle.kts",
            "AndroidManifest.xml": self.project_root / "app/src/main/AndroidManifest.xml",
            "Python Manifest": self.project_root / "python/manifest.py",
        }
        
        for name, path in key_files.items():
            status = "✅" if path.exists() else "❌"
            print(f"   {status} {name}")
        
        print("\n" + "="*60 + "\n")


def main():
    """Main analyzer script"""
    parser = argparse.ArgumentParser(
        description="Analyze Android Command Center project"
    )
    parser.add_argument(
        "--detailed",
        action="store_true",
        help="Show detailed file type breakdown"
    )
    
    args = parser.parse_args()
    
    analyzer = ProjectAnalyzer()
    analyzer.print_report(detailed=args.detailed)


if __name__ == "__main__":
    main()
