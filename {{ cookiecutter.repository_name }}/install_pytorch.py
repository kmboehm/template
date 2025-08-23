#!/usr/bin/env python3
"""
Platform-aware PyTorch installation script.

Installs PyTorch with CUDA support on Linux and CPU-only on macOS.
"""

import platform
import subprocess
import sys

def install_pytorch():
    """Install PyTorch based on the platform."""
    system = platform.system()
    machine = platform.machine()
    
    print(f"Detected platform: {system} {machine}")
    
    if system == "Linux":
        print("Installing PyTorch with CUDA 12.6 support...")
        cmd = [
            sys.executable, "-m", "pip", "install",
            "torch", "torchvision",
            "--index-url", "https://download.pytorch.org/whl/cu126"
        ]
    elif system == "Darwin":  # macOS
        if machine == "arm64":  # Apple Silicon
            print("Installing PyTorch for Apple Silicon (M1/M2)...")
            cmd = [
                sys.executable, "-m", "pip", "install",
                "torch", "torchvision"
            ]
        else:  # Intel Mac
            print("Installing PyTorch for Intel Mac...")
            cmd = [
                sys.executable, "-m", "pip", "install",
                "torch", "torchvision"
            ]
    else:
        print("Installing PyTorch for other platforms...")
        cmd = [
            sys.executable, "-m", "pip", "install",
            "torch", "torchvision"
        ]
    
    try:
        subprocess.run(cmd, check=True)
        print("✅ PyTorch installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install PyTorch: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_pytorch()
