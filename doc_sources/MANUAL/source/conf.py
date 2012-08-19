# -*- coding: utf-8 -*-
#
# Google or-tools library documentation build configuration file, created by
# sphinx-quickstart on Thu Dec 15 21:34:26 2011.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

sys.path.append(os.path.abspath('../..'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.pngmath', 'sphinx.ext.ifconfig', 'sphinxcontrib.doxylink', 'sphinxortools.ortools']

# -- PNGmath configuration -----------------------------------------------------
pngmath_latex_preamble = r'\usepackage{color} \usepackage{cancel}  \usepackage[active]{preview}  \newcommand\TStrut{\rule{0pt}{2.6ex}}  \newcommand\BStrut{\rule[-1.2ex]{0pt}{0pt}}' 
pngmath_use_preview=True

pngmath_dvipng_args = ['-gamma 1.5', '-D 110', '-bg Transparent']

# -- PNGmath configuration -----------------------------------------------------

# Add any paths that contain templates here, relative to this directory.
templates_path = ['doctemplates']

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'User\'s Manual'
copyright = u'2012, Google'

#**************************************************************************************
#ADDED FUNCTIONNALITIES

# ortools extension 
#bitbucket_project_url = 'toto'

ortools_labels = {}
ortools_ext = 'rst'
ortools_chap_char = '='
ortools_basedirname = '/home/nikolaj/Documents/RESEARCH/google/new_tech_writer/SOURCES/MANUAL/source'

####
html_add_permalinks = None

doxylink = {
        'solver' : ('/home/nikolaj/Documents/RESEARCH/google/tech_writer/SOURCES/MANUAL/source/constraint_solver.tag', '/home/nikolaj/Documents/RESEARCH/google/tech_writer/SOURCES/DEPLOY/reference_manual/or-tools/constraint_solver'),
}

# sphinxfeed
feed_base_url = 'http://or-tools.googlecode.com/svn/trunk/documentation/user_manual'
feed_author = 'Google'


rst_prolog = open('../../global.rst', 'r').read()

# The setting for draft or final display. Uncomment the relevant line:
tags.add('draft')
#tags.add('final') 
#**************************************************************************************

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '0.1'
# The full version, including alpha/beta/rc tags.
release = 'doc version 0.0.1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = []

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []

# Trim unnecessary space before footnotes. 
trim_footnote_reference_space = True

# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'default'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
html_theme_options = {
#	"rightsidebar": "true",
	"relbarbgcolor": "black",
#	"stickysidebar": "False",
	"bodyfont": "Tahoma, Geneva, sans-serif",
#	"headtextcolor": "#4F8A10",
    "sidebarbgcolor": "#D8D8D8",
    "sidebartextcolor": "#909090",
    "sidebarlinkcolor": "#D80000",
    "footerbgcolor": "#0066CC",
    "headbgcolor": "#FFFFFF",
    "codebgcolor": "#F8F8F8"
	}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
html_title = "or-tools User's Manual"

# A shorter title for the navigation bar.  Default is the same as html_title.
html_short_title = "or-tools User's Manual"

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = 'docstatic/logo.png'

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
html_favicon = 'docstatic/logo.ico'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['docstatic']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
html_sidebars = {
	'**': ['sidetitle.html','mysearchbox.html','welcome.html','examples.html','relations.html','mylocaltoc.html'],
	'index': ['sidetitle.html','mysearchbox.html','welcome.html','examples.html','myglobaltoc.html'],
	'about': ['sidetitle.html','mysearchbox.html','welcome.html','examples.html','myglobaltoc.html'],
	'manual/introduction': ['sidetitle.html','mysearchbox.html','welcome.html','examples.html','myglobaltoc.html'],
	'manual/first_steps': ['sidetitle.html','mysearchbox.html','welcome.html','examples.html','myglobaltoc.html'],
	'manual/objectives': ['sidetitle.html','mysearchbox.html','welcome.html','examples.html','myglobaltoc.html'],
	'manual/search_primitives': ['sidetitle.html','mysearchbox.html','welcome.html','examples.html','myglobaltoc.html'],
	'manual/LNS': ['sidetitle.html','mysearchbox.html','welcome.html','examples.html','myglobaltoc.html'],
	'manual/LS': ['sidetitle.html','mysearchbox.html','welcome.html','examples.html','myglobaltoc.html'],
	'manual/custom_constraints': ['sidetitle.html','mysearchbox.html','welcome.html','examples.html','myglobaltoc.html'],
	'manual/modeling_tricks': ['sidetitle.html','mysearchbox.html','welcome.html','examples.html','myglobaltoc.html'],
	'manual/TSP': ['sidetitle.html','mysearchbox.html','welcome.html','examples.html','myglobaltoc.html'],
	'manual/VRP': ['sidetitle.html','mysearchbox.html','welcome.html','examples.html','myglobaltoc.html'],
	'manual/utilities': ['sidetitle.html','mysearchbox.html','welcome.html','examples.html','myglobaltoc.html'],
	'manual/reification': ['sidetitle.html','mysearchbox.html','welcome.html','examples.html','myglobaltoc.html'],
	'manual/under_the_hood': ['sidetitle.html','mysearchbox.html','welcome.html','examples.html','myglobaltoc.html'],

}

# Additional templates that should be rendered to pages, maps page names to
# template names.
html_additional_pages = {
  #about : about
}

# If false, no module index is generated.
html_domain_indices = False

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
html_show_sourcelink = False

#no need to copy source files because we use Google search.
html_copy_source = False

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'Googleor-toolslibrarydoc'


# -- Options for LaTeX output --------------------------------------------------

f = open('latex_preamble.tex', 'r+')
LATEX_PREAMBLE = f.read();

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
'pointsize': '12pt',

# Additional stuff for the LaTeX preamble.
'preamble': LATEX_PREAMBLE,

# Class options
# ,openany
'classoptions': ',twoside',

# Babel: this is needed, otherwise we got an error...
'babel' : '\\usepackage[english]{babel}',

'fncychap' : '\\usepackage[Bjarne]{fncychap}',

'tableofcontents' : ''
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'Googleor-toolslibrary.tex', u'or-tools User\'s Manual',
   u'Google', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = 'docstatic/doxy_logo.png'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
latex_domain_indices = True

latex_additional_files = ['images/logo.pdf',
                          'images/google.pdf',
                          'images/dialog-warning.pdf',
                          'images/code_example.pdf',
                          'images/command_line.pdf',
                          'images/cropped_anatomy1.pdf',
                          'images/cropped_anatomy2.pdf',
                          'images/cropped_anatomy3.pdf',
                          'images/cropped_anatomy4.pdf',
                          'latex_copyright.txt',
                          'latex_foreword.txt',
                          'images/sol_4x4_a.pdf',
                          'images/sol_4x4_b.pdf',
                          'images/tree0.pdf',
                          'images/tree1_w.pdf',
                          'images/tree2_w.pdf',
                          'images/tree3_w.pdf',
                          'images/tree4_w.pdf',
                          'images/tree5_w.pdf',
                          'images/tree6_w.pdf',
                          'images/tree7_w.pdf',
                          'images/tree8_w.pdf',
                          'images/real_tree1.pdf',
                          'images/real_tree2.pdf',
                          'images/real_tree3.pdf',
                          'images/real_tree4.pdf',
                          'images/real_tree5.pdf',
                          'images/real_tree6.pdf',
                          'images/real_tree7.pdf',
                          'images/real_tree8.pdf',
                          'images/viz0.pdf',
                          'images/viz1.pdf',
                          'images/viz2.pdf',
                          'images/viz3.pdf',
                          'images/viz4.pdf',
                          'images/viz5.pdf',
                          'images/viz6.pdf',
                          'images/viz7.pdf',
                          'images/viz8.pdf',
                          ]
# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'googleor-toolslibrary', u'Google or-tools library',
     [u'Google'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'Googleor-toolslibrary', u'Google or-tools library',
   u'Google', 'Googleor-toolslibrary', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
texinfo_show_urls = 'footnote'


# -- Options for Epub output ---------------------------------------------------

# Bibliographic Dublin Core info.
epub_title = u'Google or-tools library'
epub_author = u'Google'
epub_publisher = u'Google'
epub_copyright = u'2012, Google'

# The language of the text. It defaults to the language option
# or en if the language is not set.
#epub_language = ''

# The scheme of the identifier. Typical schemes are ISBN or URL.
epub_scheme = 'URL'

# The unique identifier of the text. This can be a ISBN number
# or the project homepage.
epub_identifier = 'http://or-tools.googlecode.com/'

# A unique identification for the text.
#epub_uid = ''

# A tuple containing the cover image and cover page html template filenames.
#epub_cover = ()

# HTML files that should be inserted before the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_pre_files = [('/home/nikolaj/Documents/RESEARCH/google/tech_writer/SOURCES/MANUAL/epub_title/output.html','title')]

# HTML files shat should be inserted after the pages created by sphinx.
# The format is a list of tuples containing the path and title.
#epub_post_files = []

# A list of files that should not be packed into the epub file.
#epub_exclude_files = []

# The depth of the table of contents in toc.ncx.
#epub_tocdepth = 3

# Allow duplicate toc entries.
#epub_tocdup = True

###########################################################################

