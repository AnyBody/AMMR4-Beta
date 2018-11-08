#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# AMMR documentation build configuration file, created by
# sphinx-quickstart on Wed Aug 23 14:56:19 2017.
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


# -- General configuration ------------------------------------------------


import os
import re
import sys
import subprocess
from datetime import datetime

import cloud_sptheme


sys.path.insert(0, os.path.abspath("exts"))
sys.path.insert(0, os.path.abspath("exts/sphinx_gallery-0.1.13-py3.6.egg"))


try:
    import pygments_anyscript
except ImportError:
    raise ImportError("Please install pygments_anyscript to get AnyScript highlighting")


def tagged_commit():
    """Check if we are on a tagged commit"""
    try:
        subprocess.check_call(
            ["git", "describe", "--tags", "--exact-match", "HEAD"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
        )
    except subprocess.CalledProcessError:
        return False
    else:
        return True


if tags.has("offline"):
    # building offline version
    pass


if not tagged_commit() and not tags.has("offline"):
    tags.add("draft")


# `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = tags.has("draft")


# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx.ext.mathjax",
    "sphinx.ext.githubpages",
    # 3rd party extensions
    # 'sphinxcontrib.fulltoc',
    "sphinx_gallery.gen_gallery",
    "cloud_sptheme.ext.index_styling",
    "cloud_sptheme.ext.relbar_toc",
    "cloud_sptheme.ext.escaped_samp_literals",
    "cloud_sptheme.ext.issue_tracker",
    "cloud_sptheme.ext.table_styling",
    "ammr-directives",
    "inline_highlight",
]


sphinx_gallery_conf = {
    # path to your examples scripts
    "examples_dirs": "Applications",
    # path where to save gallery generated examples
    "gallery_dirs": "auto_examples",
    "backreferences_dir": "auto_examples/backreferences",
    "doc_module": ("gallery",),
    "backreferences_heading": False,
    # directory where function granular galleries are stored
    "download_section_examples": False,
    "download_all_examples": False,
    "min_reported_time": 100,
    "show_code_section": False,
    "default_thumb_file": "_static/no_image.png",
    "thumbnail_size": (320, 280),
    "is_egg_file": True,
}


# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = ".rst"

# The master toctree document.
master_doc = "contents"

# The frontpage document.
index_doc = "index"


# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ["_build", "README.rst", "Thumbs.db", ".DS_Store"]

# The name of the Pygments (syntax highlighting) style to use.
highlight_language = "AnyScriptDoc"
pygments_style = "AnyScript"


current_year = os.environ.get("YEAR", datetime.now().year)

ams_version = os.environ.get("AMS_VERSION", "7.2.0")
if not re.match("^\d\.\d\.\d", ams_version):
    raise ValueError("Wrong format for AMS version, environment variable")
ams_version_short = ams_version.rpartition(".")[0]
ams_version_x = ams_version_short + ".x"

ammr_version = os.environ.get("AMMR_VERSION", "2.2.0-beta")
if not re.match("^\d\.\d\.\d", ammr_version):
    raise ValueError("Wrong format for AMMR version, environment variable")
ammr_version_short = ammr_version.rpartition(".")[0]


rst_epilog = f"""
.. include:: /bm_config/Substitutions.txt

.. |AMS| replace:: AnyBody Modeling System™
.. |AMS_VERSION_X| replace:: {ams_version_x}
.. |AMS_VERSION| replace:: {ams_version}
.. |AMS_VERSION_SHORT| replace:: {ams_version_short}
.. |AMMR_VERSION_SHORT| replace:: {ammr_version_short}
.. |AMMR_VERSION| replace:: {ammr_version}
.. |AMMR_DEMO_INST_DIR| replace:: :literal:`~/Documents/{ams_version_x}/AMMR.v{ammr_version}-Demo`
.. |CURRENT_YEAR| replace:: {current_year}
.. |WHAT_IS_NEW| replace:: :ref:`What's new in AMMR {ammr_version} <whats-new>`
.. |DOI| image:: https://zenodo.org/badge/DOI/10.5281/zenodo.1250764.svg
                 :target: https://doi.org/10.5281/zenodo.1250764
"""


no_index = """
.. meta::
   :robots: noindex
"""

if tags.has("draft"):
    rst_epilog = rst_epilog + no_index


# General information about the project.
project = "AMMR"
copyright = f"{current_year}, AnyBody Technology"
author = "AnyBody Technology"

github_doc_root = "https://gitlab.com/anybody/beta/ammr/tree/master/Docs"


# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = f"{ammr_version_short}"
# The full version, including alpha/beta/rc tags.
release = f"{ammr_version}"

if tags.has("draft") and not release.endswith("beta"):
    release = release + "-beta"


suppress_warnings = ["ref.citation"]


# -- Options for HTML output ----------------------------------------------


def setup(app):
    app.add_stylesheet("theme_override.css")


html_sidebars = {
    "**": ["searchbox.html", "globaltoc.html"],  # 'sourcelink.html', ],
    "using/windows": ["windowssidebar.html", "searchbox.html"],
}

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "cloud"

html_theme_path = [cloud_sptheme.get_theme_dir()]


html_title = "%s v%s Documentation" % (project, release)

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme = "redcloud"
# html_theme_options = {
#     'roottarget': index_doc,
#     'max_width': '1100px',
#     'minimal_width': '700px',
#     'borderless_decor': True,
#     'lighter_header_decor': False,
#     'sidebarwidth': "3.8in",
#     'fontcssurl': 'https://fonts.googleapis.com/css?family=Noticia+Text|Open+Sans|Droid+Sans+Mono',
#     'relbarbgcolor': '#999999',
#     'footerbgcolor': '#953337',
#     'sidebarlinkcolor': '#953337',
#     'headtextcolor': '#953337',
#     'headlinkcolor': '#953337',
# }

html_theme_options = {
    "roottarget": index_doc,
    "max_width": "1100px",
    "minimal_width": "700px",
    "borderless_decor": True,
    "lighter_header_decor": False,
    # 'sidebar_master_title':'TEST2'
    # 'sidebarwidth': "3.8in",
    "fontcssurl": "https://fonts.googleapis.com/css?family=Noticia+Text|Open+Sans|Droid+Sans+Mono",
}

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
html_logo = "_static/AMMR_Logo.png"

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = "_static/favicon.ico"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static", "body/_static"]

# Custom sidebar templates, maps document names to template names.
# html_sidebars = {'**': ['searchbox.html', 'globaltoc.html']}


# -- Options for HTMLHelp output ------------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = project

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
latex_documents = [
    (master_doc, "AMMR.tex", "AMMR Documentation", "AnyBody Technology", "manual")
]


# -- Options for manual page output ---------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [(master_doc, "ammr", "AMMR Documentation", [author], 1)]


# -- Options for Texinfo output -------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (
        master_doc,
        "AMMR",
        "AMMR Documentation",
        author,
        "AMMR",
        "One line description of project.",
        "Miscellaneous",
    )
]


intersphinx_mapping = {}
if tags.has("offline"):
    # Todo. Find a way to link to offline html versions.
    intersphinx_mapping["tutorials"] = ("https://anyscript.org/tutorials/", None)
else:
    if tags.has("draft"):
        intersphinx_mapping["tutorials"] = (
            "https://anyscript.org/tutorials/dev/",
            None,
        )
    else:
        intersphinx_mapping["tutorials"] = ("https://anyscript.org/tutorials/", None)

