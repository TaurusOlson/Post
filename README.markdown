# POST.PY #


## DESCRIPTION ##

post.py is a naive blog engine I wrote to quickly keep my notes and ideas in a nice format.
The entries can be quotes with the command line or files written with *Markdown*.


## REQUIREMENT ##

Markdown module.


## CONFIGURATION ##

Modify the constants in post.py:

    INSERT_CSS=True
    INSERT_HEADER=True
    DIR = 'Documents/Blog'
    MKD_FILE = 'posts.mkd'
    HTML_FILE = 'posts.html'

If you choose to use a CSS file, change its name:

    <link rel="stylesheet" type="text/css" href="style.css" />


## USAGE ##

- Post a quote/note.

        post.py "My fantastic quote."

- Post a file.
    
        post.py file.mkd

- Convert the posts to HTML.

        post.py -2html


## TODO ##

- Find a way to easily edit/remove an entry.
