# Documentation Setup Guide

This repository has Sphinx documentation that is automatically generated from Jupyter notebooks and committed to the repository for easy access.

## Overview

The documentation system is **already configured** and ready to use:
- All 12 Jupyter notebooks are included in the documentation
- GitHub Actions workflow automatically builds and deploys documentation to GitHub Pages
- Built documentation is published to the `gh-pages` branch and served via GitHub Pages

## How It Works

1. **Automatic Building**: When you push changes to the `main` branch, a GitHub Actions workflow:
   - Installs Pandoc (system package) and Sphinx dependencies from `requirements-docs.txt`
   - Copies notebooks to a temporary `_notebooks` directory
   - Builds HTML documentation from all Jupyter notebooks
   - Deploys the generated HTML to the `gh-pages` branch
   - GitHub Pages automatically serves the documentation

2. **Accessing Documentation**:
   - **GitHub Pages**: `https://sap-contributions.github.io/litellm-agentic-examples/`
   - **Locally**: Run Sphinx locally (see below) and view the results at `docs/build/html/index.html`

## Local Documentation Build

To build the documentation locally:

```bash
# 1. Install Pandoc (system package - required!)
brew install pandoc  # macOS
# or
sudo apt-get install pandoc  # Linux

# 2. Install Python documentation dependencies
pip install -r requirements-docs.txt

# 3. Copy notebooks to docs source directory
./copy_notebooks.sh

# 4. Build the documentation
sphinx-build -b html docs/source docs/build/html

# 5. View the result
open docs/build/html/index.html  # macOS
# or
xdg-open docs/build/html/index.html  # Linux
# or
start docs/build/html/index.html  # Windows
```

**Important Notes**:
- **Pandoc must be installed as a system package** - it's required by nbsphinx but cannot be installed via pip
- The `copy_notebooks.sh` script copies only the `.ipynb` files (not Python files or other content) from each example directory to `docs/source/_notebooks/`
- The `_notebooks` directory is temporary and excluded from git via `.gitignore`

## Project Structure

```
.
├── docs/
│   ├── source/
│   │   ├── conf.py          # Sphinx configuration
│   │   └── index.rst        # Main documentation page (includes all notebooks)
│   └── build/
│       └── html/            # Generated HTML (not committed - local only)
├── copy_notebooks.sh        # Script to copy notebooks for Sphinx
├── requirements-docs.txt    # Documentation dependencies
└── .github/workflows/docs.yml  # Automated documentation workflow

Note: The gh-pages branch contains the published documentation (auto-generated)
```

## Configuration Details

### Included Notebooks

The documentation includes all example notebooks:
- Langgraph (`langgraph_example/langgraph_agent.ipynb`)
- CrewAI Library (`crewai_example/crewai_litellm_lib.ipynb`)
- CrewAI Proxy (`crewai_example/crewai_litellm_proxy.ipynb`)
- PydanticAI (`pydantic_ai_example/pydantic_ai_litellm_proxy.ipynb`)
- Google ADK (`google_adk_example/google_adk.ipynb`)
- OpenAI ADK (`openai_adk_example/openai_adk.ipynb`)
- AWS Strands (`aws_strands_example/aws_strands.ipynb`)
- LlamaIndex (`LlamaIndex_example/LlamaIndex_litellm.ipynb`)
- SmoLAgents (`smolagents_example/smolagents_litellm.ipynb`)
- Microsoft Agent (`microsoft_agent_example/microsoft_agent_litellm_proxy.ipynb`)
- AgentScope (`agentscope_example/agentscope_litellm.ipynb`)
- AG2 (`ag2_example/ag2_litellm_proxy.ipynb`)

### Sphinx Configuration (`docs/source/conf.py`)

Key settings:
- **Extensions**: `nbsphinx` for Jupyter notebook rendering, `sphinx.ext.mathjax` for math
- **Theme**: `sphinx_rtd_theme` (Read the Docs theme)
- **nbsphinx settings**:
  - `nbsphinx_allow_errors = True` - Continue building even if notebooks have errors
  - `nbsphinx_execute = 'never'` - Don't execute notebooks during build

### Dependencies

**Python packages** (`requirements-docs.txt`):
```
sphinx>=7.0
sphinx-rtd-theme
nbsphinx
ipython
```

**System package**:
- `pandoc` - Required by nbsphinx for converting notebooks. Install via:
  - **macOS**: `brew install pandoc`
  - **Linux**: `sudo apt-get install pandoc`
  - **Windows**: Download from [pandoc.org](https://pandoc.org/installing.html)

## Modifying Documentation

### Adding New Notebooks

To add a new notebook to the documentation:

1. Update the `copy_notebooks.sh` script to include your new notebook directory:
   ```bash
   cp -r your_new_example/*.ipynb docs/source/_notebooks/
   ```

2. Add the notebook path to `docs/source/index.rst` in the `toctree` section:
   ```rst
   .. toctree::
      :maxdepth: 2
      :caption: Agent Framework Examples:

      _notebooks/your_new_notebook.ipynb
   ```

3. Push your changes - the workflow will automatically rebuild the documentation

### Updating Configuration

To modify Sphinx settings, edit `docs/source/conf.py`. Common modifications:
- Change theme or theme options
- Add additional Sphinx extensions
- Modify nbsphinx behavior
- Customize HTML output

### Manual Workflow Trigger

You can manually trigger the documentation build:
1. Go to the Actions tab in GitHub
2. Select "Build Documentation" workflow
3. Click "Run workflow"

## Troubleshooting

### Build Fails Locally

**Problem**: `No module named 'sphinx'`
**Solution**: Install dependencies: `pip install -r requirements-docs.txt`

### Notebooks Don't Render

**Problem**: Notebooks appear as raw text
**Solution**: Ensure `nbsphinx` is in `extensions` list in `conf.py`

### Workflow Fails to Deploy

**Problem**: GitHub Actions workflow fails at deployment step
**Solution**:
- Check that the workflow has `contents: write` permissions (set in `.github/workflows/docs.yml`)
- Verify the `gh-pages` branch exists (it will be created automatically on first run)
- Check the Actions logs for specific error messages

### GitHub Pages Not Working

**Problem**: GitHub Pages shows 404 or doesn't update
**Solution**:
1. Go to repository **Settings → Pages**
2. Under "Build and deployment" → "Source", select **Deploy from a branch**
3. Under "Branch", select `gh-pages` and `/ (root)`
4. Click **Save**
5. Wait 1-2 minutes for GitHub to rebuild the site

## Advanced Topics

### Customizing the Theme

Edit `docs/source/conf.py` to customize the Read the Docs theme:

```python
html_theme_options = {
    'navigation_depth': 4,
    'titles_only': False,
    'collapse_navigation': False,
}
```

### Adding Custom CSS/JavaScript

1. Create files in `docs/source/_static/`
2. Reference them in `conf.py`:
   ```python
   html_static_path = ['_static']
   html_css_files = ['custom.css']
   html_js_files = ['custom.js']
   ```

### Excluding Specific Notebooks

To exclude a notebook from documentation:
1. Remove it from the `toctree` in `docs/source/index.rst`
2. The workflow will still build successfully

## Notes

- The repository is a collection of examples, not an installable library
- Documentation dependencies are managed separately in `requirements-docs.txt`
- The `.gitignore` is configured to commit `docs/build/html/` while ignoring build artifacts
- The workflow includes `[skip ci]` in commit messages to prevent infinite loops
