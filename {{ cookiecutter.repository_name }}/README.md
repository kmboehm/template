# {{ cookiecutter.project_name }}

<p align="center">
    <a href="https://github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.repository_name }}/actions/workflows/test_suite.yml"><img alt="CI" src=https://img.shields.io/github/workflow/status/{{ cookiecutter.github_user }}/{{ cookiecutter.repository_name }}/Test%20Suite/main?label=main%20checks></a>
    <a href="https://{{ cookiecutter.github_user }}.github.io/{{ cookiecutter.repository_name }}"><img alt="Docs" src=https://img.shields.io/github/deployments/{{ cookiecutter.github_user }}/{{ cookiecutter.repository_name }}/github-pages?label=docs></a>
    <a href="https://github.com/grok-ai/nn-template"><img alt="NN Template" src="https://shields.io/badge/nn--template-{{ cookiecutter.__version }}-emerald?style=flat&labelColor=gray"></a>
    <a href="https://www.python.org/downloads/"><img alt="Python" src="https://img.shields.io/badge/python-{{ cookiecutter.python_version }}-blue.svg"></a>
    <a href="https://black.readthedocs.io/en/stable/"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>
</p>

{{ cookiecutter.project_description }}


## Installation

```bash
pip install git+ssh://git@github.com/{{ cookiecutter.github_user }}/{{ cookiecutter.repository_name }}.git
```


## Quickstart

[comment]: <> (> Fill me!)


## Development installation

Setup the development environment:

```bash
git clone git@github.com:{{ cookiecutter.github_user }}/{{ cookiecutter.repository_name }}.git
cd {{ cookiecutter.repository_name }}

# Create environment using mamba (faster than conda)
mamba env create -f env.yaml
mamba activate {{ cookiecutter.conda_env_name }}

# Install PyTorch with platform-specific support
python install_pytorch.py

# Install the project in dev mode (avoiding dependency conflicts)
pip install -e . --no-deps

# Install remaining dependencies in correct order to avoid conflicts
pip install lightning torchmetrics hydra-core fastparquet torch_geometric wandb streamlit rich dvc python-dotenv stqdm
pip install anypy==0.0.5
pip install nn-template-core --no-deps

# Set environment variable for macOS OpenMP compatibility (if on macOS)
export KMP_DUPLICATE_LIB_OK=TRUE

# Test the installation
python test_installation.py

# Install development dependencies (for pre-commit, testing, docs)
pip install black flake8 isort pre-commit bandit pytest pytest-cov mkdocs mkdocs-material mike

# Install pre-commit hooks
pre-commit install
```

**Note:** This template now uses modern dependencies:
- Python 3.12
- PyTorch 2.8+ (with CUDA 12.6 support on Linux, CPU-only on macOS)
- Lightning 2.5+
- Hydra 1.3+
- All major data science libraries (pandas, scikit-learn, scipy, h5py, statsmodels, fastparquet)
- Visualization libraries (matplotlib, contourpy, seaborn)
- PyTorch Geometric for graph neural networks
- Development tools (wandb, streamlit, rich, dvc, etc.)

**Platform Notes:**
- **Linux**: PyTorch will be installed with CUDA 12.6 support automatically
- **macOS**: PyTorch will be installed as CPU-only version, and you'll need to set `KMP_DUPLICATE_LIB_OK=TRUE` to avoid OpenMP conflicts
- **Windows**: PyTorch will be installed with CUDA 12.6 support automatically

Run the tests:

```bash
pre-commit run --all-files
pytest -v
```

## Troubleshooting

### Common Installation Issues

#### 1. Dependency Version Conflicts

**Problem**: You may encounter version conflicts during installation, particularly with `anypy` and `nn-template-core`.

**Solution**: Install dependencies in the correct order to avoid conflicts:
```bash
# Install the project first without dependencies
pip install -e . --no-deps

# Install core dependencies
pip install lightning torchmetrics hydra-core fastparquet torch_geometric wandb streamlit rich dvc python-dotenv stqdm

# Install anypy with specific version to avoid conflicts
pip install anypy==0.0.5

# Install nn-template-core without dependencies to avoid version conflicts
pip install nn-template-core --no-deps
```

#### 2. Hugging Face Token Issues

**Problem**: Tests may fail with Hugging Face authentication errors when downloading datasets.

**Solution**: The template has been updated to use `token=False` for public datasets. For private datasets, set your token:
```bash
export HUGGING_FACE_HUB_TOKEN=your_token_here
```

#### 3. PyTorch Installation Issues

**Problem**: PyTorch installation may fail on different platforms.

**Solution**: Use the provided platform-specific installation script:
```bash
python install_pytorch.py
```

#### 4. macOS OpenMP Conflicts

**Problem**: On macOS, you may encounter OpenMP library conflicts.

**Solution**: Set the environment variable before running:
```bash
export KMP_DUPLICATE_LIB_OK=TRUE
```

#### 5. Pre-commit Hook Failures

**Problem**: Pre-commit hooks may fail due to code formatting issues.

**Solution**: The hooks will automatically fix most formatting issues. Run them again:
```bash
pre-commit run --all-files
```

#### 6. Test Failures

**Problem**: Some tests may fail, particularly checkpoint-related tests.

**Expected**: All 18 tests should pass, including checkpoint functionality tests.

**Solution**: If you see test failures, check:
1. All dependencies are installed correctly
2. PyTorch version is compatible
3. Environment variables are set correctly
4. You're using the latest version of the template (checkpoint tests have been fixed)

### Verification Checklist

After installation, verify everything is working:

1. ✅ Environment activated: `mamba activate {{ cookiecutter.conda_env_name }}`
2. ✅ PyTorch installed: `python -c "import torch; print(torch.__version__)"`
3. ✅ Project installed: `python -c "import {{ cookiecutter.package_name }}; print('OK')"`
4. ✅ Tests passing: `pytest -v` (expect 18 passing)


### Update the dependencies

Re-install the project in edit mode:

```bash
pip install -e .[dev]
```

### Test the installation

Run the dependency test to verify everything is working:

```bash
python test_installation.py
```
