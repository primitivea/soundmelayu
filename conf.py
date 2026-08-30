# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------
project = 'Sound of Text Malaysia'
copyright = '2026, Pelajar Malaysia'
author = 'Pelajar Malaysia'

release = '1.0'
version = '1.0'

language = 'ms'
root_doc = 'index'

# -- General configuration ---------------------------------------------------
extensions = [
    'myst_parser',
]

source_suffix = ['.md']

# -- Options for HTML output -------------------------------------------------
html_theme = 'alabaster'
html_static_path = []
