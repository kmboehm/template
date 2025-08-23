# Troubleshooting Guide

This document provides quick fixes for common issues encountered when setting up the project.

## Quick Fixes

### 1. Dependency Conflicts
```bash
# If you get version conflicts, reinstall in this order:
pip install -e . --no-deps
pip install lightning torchmetrics hydra-core fastparquet torch_geometric wandb streamlit rich dvc python-dotenv stqdm
pip install anypy==0.0.5
pip install nn-template-core --no-deps
```

### 2. Hugging Face Token Error
```bash
# For public datasets (like MNIST), the code should work automatically
# For private datasets, set your token:
export HUGGING_FACE_HUB_TOKEN=your_token_here
```

### 3. PyTorch Installation
```bash
# Use the provided script for platform-specific installation:
python install_pytorch.py
```

### 4. macOS OpenMP Issues
```bash
export KMP_DUPLICATE_LIB_OK=TRUE
```

### 5. Code Formatting Issues
```bash
# Fix formatting automatically:
pre-commit run --all-files
```

## Common Error Messages and Solutions

### "ERROR: Cannot install anypy==0.0.5"
**Solution**: Install with specific version constraint:
```bash
pip install "anypy==0.0.5"
```

### "HuggingFaceHubError: 401 Client Error: Unauthorized"
**Solution**: The code has been updated to use `token=False` for public datasets. If you still get this error, check your internet connection.

### "ImportError: cannot import name 'X' from 'torch'"
**Solution**: Reinstall PyTorch using the provided script:
```bash
python install_pytorch.py
```

### "AssertionError: CUDA not available"
**Solution**: This is expected on macOS or systems without CUDA. The code will fall back to CPU.

## Test Results Expectations

When running `pytest -v`, you should expect:
- ✅ **18 tests passing** (all functionality including checkpoint tests)
- ⚠️ **34 warnings** (mostly informational)

**Note**: The checkpoint tests have been fixed and should now pass. If you see failing checkpoint tests, it may be due to an outdated version of the template.

## Still Having Issues?

1. Check that you're using the correct Python version (3.12)
2. Ensure your conda environment is activated: `mamba activate {{ cookiecutter.project_name }}`
3. Try reinstalling from scratch:
   ```bash
   mamba env remove -n {{ cookiecutter.project_name }}
   mamba env create -f env.yaml
   mamba activate {{ cookiecutter.project_name }}
   # Then follow the installation steps again
   ```
