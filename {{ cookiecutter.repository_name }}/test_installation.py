#!/usr/bin/env python3
"""
Test script to verify that all dependencies can be imported correctly
after updating to modern versions.
"""

import sys
import importlib

def test_import(module_name, package_name=None):
    """Test if a module can be imported successfully."""
    try:
        if package_name:
            importlib.import_module(module_name, package_name)
        else:
            importlib.import_module(module_name)
        print(f"✅ {module_name} imported successfully")
        return True
    except ImportError as e:
        print(f"❌ {module_name} failed to import: {e}")
        return False
    except Exception as e:
        print(f"⚠️  {module_name} imported but had an issue: {e}")
        return True

def main():
    """Test all the dependencies."""
    print("Testing dependency imports...")
    print("=" * 50)
    
    # Core ML dependencies
    print("\n🔬 Core ML Dependencies:")
    test_import("lightning.pytorch")
    test_import("torchmetrics")
    test_import("hydra.core")
    
    # Data science and ML libraries
    print("\n📊 Data Science Libraries:")
    test_import("pandas")
    test_import("sklearn")
    test_import("scipy")
    test_import("h5py")
    test_import("statsmodels")
    test_import("fastparquet")
    
    # Visualization
    print("\n📈 Visualization Libraries:")
    test_import("matplotlib")
    test_import("contourpy")
    test_import("seaborn")
    
    # PyTorch ecosystem
    print("\n🔥 PyTorch Ecosystem:")
    test_import("torch")
    test_import("torchvision")
    test_import("torch_geometric")
    
    # Other dependencies
    print("\n🛠️ Other Dependencies:")
    test_import("wandb")
    test_import("streamlit")
    test_import("rich")
    test_import("dvc")
    test_import("dotenv")
    test_import("stqdm")
    
    # Template core
    print("\n🎯 Template Core:")
    test_import("nn_core")
    
    print("\n" + "=" * 50)
    print("Import test completed!")
    
    # Print Python and key package versions
    print(f"\nPython version: {sys.version}")
    
    try:
        import torch
        print(f"PyTorch version: {torch.__version__}")
    except ImportError:
        pass

    try:
        import lightning
        print(f"Lightning version: {lightning.__version__}")
    except ImportError:
        pass

    try:
        import hydra
        print(f"Hydra version: {hydra.__version__}")
    except ImportError:
        pass

if __name__ == "__main__":
    main()
