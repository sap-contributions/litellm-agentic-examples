# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Agentic examples LiteLLM Gen AI Hub'
copyright = '2025, Vasilisa Karim Mathis'
author = 'Vasilisa Parshikova (LeverX), Karim Mohraz (SAP), Mathis Boerner (SAP)'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'nbsphinx',
    'sphinx.ext.mathjax',
]

templates_path = ['_templates']
exclude_patterns = ['_build', '**.ipynb_checkpoints']

# nbsphinx configuration
nbsphinx_allow_errors = True  # Continue building even if notebooks have errors
nbsphinx_execute = 'never'    # Don't execute notebooks during build

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']
