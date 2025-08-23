#!/usr/bin/env python3
"""
Test script to verify that the cookiecutter template generates correctly
with the updated dependencies.
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path

def run_command(cmd, cwd=None):
    """Run a command and return the result."""
    print(f"Running: {cmd}")
    result = subprocess.run(cmd, shell=True, capture_output=True, text=True, cwd=cwd)
    if result.returncode != 0:
        print(f"Command failed: {result.stderr}")
        return False
    print(f"Command succeeded: {result.stdout}")
    return True

def test_template_generation():
    """Test that the template generates correctly."""
    print("Testing template generation...")
    
    # Clean up any existing test project
    test_project_dir = Path("test-awesome-project")
    if test_project_dir.exists():
        shutil.rmtree(test_project_dir)
    
    # Generate the template
    cmd = f"cookiecutter . --no-input --output-dir ."
    if not run_command(cmd):
        print("❌ Template generation failed")
        return False
    
    print("✅ Template generated successfully")
    
    # Check that the generated files exist
    expected_files = [
        "test-awesome-project/env.yaml",
        "test-awesome-project/setup.cfg",
        "test-awesome-project/pyproject.toml",
        "test-awesome-project/test_installation.py"
    ]
    
    for file_path in expected_files:
        if not Path(file_path).exists():
            print(f"❌ Expected file {file_path} not found")
            return False
    
    print("✅ All expected files generated")
    
    # Check the content of key files
    env_yaml = Path("test-awesome-project/env.yaml").read_text()
    if "python=3.12" not in env_yaml:
        print("❌ Python 3.12 not found in env.yaml")
        return False
    
    if "pytorch>=2.8.0" not in env_yaml:
        print("❌ PyTorch 2.8+ not found in env.yaml")
        return False
    
    if "mamba" not in env_yaml:
        print("❌ mamba not found in env.yaml")
        return False
    
    setup_cfg = Path("test-awesome-project/setup.cfg").read_text()
    if "lightning>=" not in setup_cfg:
        print("❌ Lightning dependency not found in setup.cfg")
        return False
    
    if "pandas" not in setup_cfg:
        print("❌ pandas dependency not found in setup.cfg")
        return False
    
    if "torch_geometric" not in setup_cfg:
        print("❌ torch_geometric dependency not found in setup.cfg")
        return False
    
    print("✅ All dependency checks passed")
    
    # Clean up
    shutil.rmtree(test_project_dir)
    print("✅ Test completed successfully")
    
    return True

if __name__ == "__main__":
    success = test_template_generation()
    sys.exit(0 if success else 1)
