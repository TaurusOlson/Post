#!/usr/bin/python
#----------------------------------------------
# post.py
# @Author        : Taurus Olson
# @License       : GPL (see http://www.gnu.org/licenses/gpl.txt)
# @Created       : 2010-08-05.
# @Revision      : 0.0
#----------------------------------------------

import sys, os, markdown

INSERT_CSS=True
INSERT_HEADER=True

##########
# HEADER #
##########

if INSERT_HEADER:
    header = """
<div id="container">
<p class="header">
    AT THE SPEED OF LIFE:
    MY NOTES AND IDEAS...
</p>
</div>

"""
else:
    header = ""


#######
# CSS #
#######

if INSERT_CSS:
    css = """
<head>
<link rel="stylesheet" type="text/css" href="style.css" />
</head>

"""
else:
    css = ""


#########
# QUOTE #
#########

begin_quote = '<div class=quote>'
end_quote = '</div>\n'


########
# MAIN #
########

def write_file(fname, message, mode='a'):
    """Simply write data to a file"""
    
    f = open(fname, mode)
    f.write(message)
    f.write("\n")
    f.close()


def read_file(fname):
    """docstring for read_file"""
    
    post = ""
    f = open(fname, 'r')
    for line in f.readlines():
        post += line
    f.close()
    return post

# Constants
DIR = 'Documents/Blog'
MKD_FILE = 'posts.mkd'
HTML_FILE = 'posts.html'
MKD_FILE_PATH = os.path.join(os.getenv('HOME'), DIR, MKD_FILE)
HTML_FILE_PATH = os.path.join(os.getenv('HOME'), DIR, HTML_FILE)

# If input is a file
if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
    print 'Post %s added...' % sys.argv[1]
    post = read_file(sys.argv[1])
    write_file(MKD_FILE_PATH, post)
    write_file(MKD_FILE_PATH, "\n- - - -\n")

    html = markdown.markdown(read_file(MKD_FILE_PATH))
    write_file(HTML_FILE_PATH, html)

# If input is stdin
elif len(sys.argv) > 1 and not os.path.exists(sys.argv[1])\
        and not sys.argv[1].startswith('-'):
    print 'Quote added...'
    quote = begin_quote + '\n' + sys.argv[1] + '\n' + end_quote
    write_file(MKD_FILE_PATH, quote)
    write_file(MKD_FILE_PATH, "- - - -\n")

    html = markdown.markdown(quote)
    write_file(HTML_FILE_PATH, html)

# Simply remove the old html file convert the markdown file to html
elif len(sys.argv) > 1 and sys.argv[1].startswith('-2html'):
    os.remove(HTML_FILE_PATH)
    html = markdown.markdown(read_file(MKD_FILE_PATH))
    write_file(HTML_FILE_PATH, header + css + html)
    print "%s has been converted to %s" % (MKD_FILE_PATH, HTML_FILE_PATH)

