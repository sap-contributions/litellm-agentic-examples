# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Agentic examples LiteLLM Gen AI Hub'
copyright = '2025, Vasilisa Karim Mathis'
author = 'Vasilisa Parshikova (LeverX), Karim Mohraz (SAP SE), Mathis Boerner (SAP SE)'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
import pathlib
import sys
sys.path.insert(0, pathlib.Path(__file__).parents[2].resolve().as_posix())

extensions = [
    'nbsphinx',
    'sphinx.ext.mathjax',
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = ['_build', '**.ipynb_checkpoints']

# nbsphinx configuration
nbsphinx_allow_errors = True  # Continue building even if notebooks have errors
nbsphinx_execute = 'never'    # Don't execute notebooks during build

# Tell nbsphinx where to find notebooks relative to the source directory
nbsphinx_prolog = """
{% set docname = env.doc2path(env.docname, base=None) %}
"""

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinxawesome_theme'
html_static_path = ['_static']
html_css_files = [
    'custom.css',
]

# Disable the paragraph/permalink markers (¶)
html_permalinks = False

# Sphinx Awesome Theme options
html_theme_options = {
    "show_prev_next": True,
    "show_scrolltop": True,
    "show_breadcrumbs": True,
}

# Configure MyST-Parser to support both .md and .rst files
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
