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

# Install remaining dependencies (avoiding nn-template-core's old pytorch-lightning dependency)
pip install lightning torchmetrics hydra-core fastparquet torch_geometric wandb streamlit rich dvc python-dotenv stqdm anypy
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
