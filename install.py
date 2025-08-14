#!/usr/bin/env python3
"""
PyObfuscator - Simple Installation Script
Installs dependencies using pip without requiring sudo
"""

import sys
import subprocess
import importlib.util
import os

def check_python_version():
    """Check if Python version is 3.7 or higher"""
    if sys.version_info < (3, 7):
        print("Error: Python 3.7 or higher is required")
        print(f"Current version: {sys.version}")
        sys.exit(1)
    print(f"✓ Python version: {sys.version}")

def install_package(package):
    """Install a Python package using pip"""
    try:
        print(f"Installing {package}...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        print(f"✓ {package} installed successfully")
        return True
    except subprocess.CalledProcessError:
        print(f"✗ Failed to install {package}")
        return False

def check_package(package_name, import_name=None):
    """Check if a package is installed"""
    if import_name is None:
        import_name = package_name
    
    spec = importlib.util.find_spec(import_name)
    return spec is not None

def main():
    """Main installation function"""
    print("=" * 50)
    print("PyObfuscator Installation")
    print("=" * 50)
    
    # Check Python version
    check_python_version()
    
    # Required packages
    packages = [
        ("cryptography", "cryptography"),
        ("psutil", "psutil")
    ]
    
    installed_count = 0
    
    for package_name, import_name in packages:
        if check_package(package_name, import_name):
            print(f"✓ {package_name} is already installed")
            installed_count += 1
        else:
            if install_package(package_name):
                installed_count += 1
    
    print("\n" + "=" * 50)
    if installed_count == len(packages):
        print("✓ All dependencies installed successfully!")
        print("\nInstallation completed. You can now use PyObfuscator:")
        print(f"  python3 {os.path.join(os.path.dirname(__file__), 'main.py')} --help")
    else:
        print("✗ Some dependencies failed to install")
        print("Please install them manually using: pip install cryptography psutil")
        sys.exit(1)

if __name__ == "__main__":
    main()