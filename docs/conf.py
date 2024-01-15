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
    'sphinx_immaterial',
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
html_title = "SuperCollider wiki"
html_theme = 'sphinx_immaterial'
html_static_path = ['_static']
html_logo = "_static/logo.svg"
html_css_files = [
    'custom.css',
]

html_theme_options = {
    "site_url": "https://capital-g.github.io/supercollider-wiki/",
    "repo_url": "https://github.com/capital-g/supercollider-wiki",
    "repo_name": "SuperCollider wiki",
    "edit_uri": "blob/main/docs",
    "globaltoc_collapse": True,
    "features": [
        "navigation.expand",
        # "navigation.tabs",
        # "toc.integrate",
        "navigation.sections",
        "navigation.instant",
        # "header.autohide",
        "navigation.top",
        # "navigation.tracking",
        # "search.highlight",
        "search.share",
        "toc.follow",
        "toc.sticky",
        "content.tabs.link",
        "announce.dismiss",
    ],
    "palette": [
        {
            "media": "(prefers-color-scheme: light)",
            "scheme": "default",
            "primary": "grey",
            "accent": "pink",
            "toggle": {
                "icon": "material/lightbulb-outline",
                "name": "Switch to dark mode",
            },
        },
        {
            "media": "(prefers-color-scheme: dark)",
            "scheme": "slate",
            "primary": "grey",
            "accent": "pink",
            "toggle": {
                "icon": "material/lightbulb-outline",
                "name": "Switch to light mode",
            },
        },
    ],
    "toc_title_is_page_title": True,
    "social": [
        {
            "icon": "fontawesome/brands/github",
            "link": "https://github.com/capital-g/supercollider-wiki",
            "name": "Source on github.com",
        },
        {
            "icon": "fontawesome/brands/discourse",
            "link": "https://scsynth.org/",
        },
        {
            "icon": "fontawesome/brands/discord",
            "link": "https://discord.gg/PVUmDyx7p8",
        },
        {
            "icon": "fontawesome/brands/slack",
            "link": "https://join.slack.com/t/scsynth/shared_invite/zt-ezoyz15j-SVM7JVul94pxtDiUDRnd0w",
        },
    ],
}
