# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'SuperCollider Wiki'
copyright = '2024, SuperCollider'
author = 'SuperCollider'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
]

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

templates_path = ['_templates']
exclude_patterns = ['venv/*']
root_doc = "index"

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_material'
html_static_path = ['_static']
html_logo = "_static/logo.svg"
html_css_files = [
    'custom.css',
]
html_theme_options = {
    "nav_title": "SuperCollider Wiki",
    'color_primary': 'grey',
    'color_accent': 'pink',
    'repo_url': 'https://github.com/supercollider/supercollider',
    'repo_name': 'SuperCollider',
    'master_doc': True,
    'globaltoc_includehidden': True,
    'globaltoc_depth': 3,
}

html_sidebars = {
    "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
}
