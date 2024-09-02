import os
import sys
sys.path.insert(0, os.path.abspath('..'))

project = 'Cipher_Craftt'
author = 'Mayur Tembhare'
release = '0.1.6'

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon']

templates_path = ['_templates']
exclude_patterns = []

html_theme = 'alabaster'
html_static_path = ['_static']

# Add any paths that contain custom themes here, relative to this directory.
html_theme_path = []
