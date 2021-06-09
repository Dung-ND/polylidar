# -*- coding: utf-8 -*-
# Pulled from Open3D
# Polylidar documentation build configuration file, created by
# sphinx-quickstart on Mon Apr  3 14:18:28 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

import sys
import os
import re
import subprocess


def get_git_short_hash():
    rc = subprocess.check_output(['git', 'rev-parse', '--short', 'HEAD'])
    rc = rc.decode("utf-8").strip()
    return rc


# Import polylidar raw python package with the highest priority
# This is a trick to show polylidar.polylidar as polylidar in the docs
# Only tested to work on Unix
current_file_dir = os.path.dirname(os.path.realpath(__file__))
sys.path.insert(
    0,
    os.path.join(current_file_dir, "..", "build", "lib", "python_package",
                 "polylidar"))

# -- General configuration ------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.mathjax', 'sphinx.ext.autodoc', 'sphinx.ext.autosummary',
    'sphinx.ext.napoleon', 'breathe', 'exhale', 'm2r', 'nbsphinx','nbsphinx_link',
]

# Setup the breathe extension
breathe_projects = {
    "Polylidar_CPP": "./_out/xml"
}

breathe_default_project = "Polylidar_CPP"

# Setup the exhale extension
exhale_args = {
    # These arguments are required
    "containmentFolder":     "./cpp_api",
    "rootFileName":          "cpp_library_root.rst",
    "rootFileTitle":         "C++ Library API",
    "doxygenStripFromPath":  "..",
    # Suggested optional arguments
    "createTreeView":        True,
    # TIP: if using the sphinx-bootstrap-theme, you need
    # "treeViewIsBootstrap": True,
    "exhaleExecutesDoxygen": True,
    "exhaleDoxygenStdin":    "INPUT = ../include"
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Polylidar3D'
copyright = u'2020, Jeremy Castagno'
author = u'Jeremy Castagno'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.

# This value can be overwritten in make_docs.py when sphinx-build is called.
# Usually, the `version` value is set to the current git commit hash.
# At Open3D releases, the `version` value is set to Open3D version number.
current_hash = get_git_short_hash()
version = "latest ({})".format(current_hash)
release = version

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False

# -- Options for HTML output ----------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
# html_theme = 'alabaster'
# theme_path = os.path.join(current_file_dir, "..", "3rdparty",
#                           "open3d_sphinx_theme")
html_theme = "sphinx_rtd_theme"
# html_theme_path = [theme_path]
html_favicon = ""
html_logo = '_static/pl_logo.png'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    # 'display_version': True
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

# '_static' contains the theme overwrite
# static_path = os.path.join(theme_path, "sphinx_rtd_theme", "static")
# html_static_path = [static_path, '_static']
html_static_path = ['_static']

# Force table wrap: https://rackerlabs.github.io/docs-rackspace/tools/rtd-tables.html
html_context = {
    'css_files': [
        '_static/theme_overrides.css',  # override wide tables in RTD theme
    ],
}

# added by Jaesik to hide "View page source"
html_show_sourcelink = False

# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'Polylidardoc'

# -- Options for LaTeX output ---------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
# latex_documents = [
#     (master_doc, 'Open3D.tex', u'Open3D Documentation', u'Qianyi Zhou',
#      'manual'),
# ]

# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, 'polylidar', u'Polylidar3D Documentation', [author], 1)]

# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'polylidar', u'Polylidar3D Documentation', author, 'Polylidar',
     'Extract Polygons from 3D Data', 'Miscellaneous'),
]

# Version 0: Added by Jaesik to list Python members using the source order
# Version 1: Changed to 'groupwise': __init__ first, then methods, then
#            properties. Within each, sorted alphabetically.
autodoc_member_order = 'groupwise'


def is_enum_class(func, func_name):

    def import_from_str(class_name):
        components = class_name.split('.')
        mod = __import__(components[0])
        for comp in components[1:]:
            mod = getattr(mod, comp)
        return mod

    is_enum = False
    try:
        if func_name == "name" and "self: handle" in func.__doc__:
            is_enum = True
        else:
            pattern = re.escape(func_name) + r"\(self: ([a-zA-Z0-9_\.]*).*\)"
            m = re.match(pattern, func.__doc__)
            if m:
                c_name = m.groups()[0]
                c = import_from_str(c_name)
                if hasattr(c, "__entries"):
                    is_enum = True
    except:
        pass
    return is_enum


# Keep the __init__ function doc
def skip(app, what, name, obj, would_skip, options):
    if name in {"__init__", "name"}:
        if is_enum_class(obj, name):
            return True
        else:
            return False
    return would_skip


def setup(app):
    app.connect("autodoc-skip-member", skip)
