# POST.PY #


## DESCRIPTION ##

post.py is a naive blog engine I wrote to quickly keep my notes and ideas in a nice format.
The entries can be quotes with the command line or files written with *Markdown*.


## REQUIREMENT ##

Markdown module.


## CONFIGURATION ##

In the file post.py, modify:

- the constants:

    INSERT_CSS=True
    INSERT_HEADER=True
    DIR = 'Documents/Blog'
    MKD_FILE = 'posts.mkd'
    HTML_FILE = 'posts.html'


- the header:

    <div id="container">
    <p class="header">
        AT THE SPEED OF LIFE:
        MY NOTES AND IDEAS...
    </p>
    </div>

and if you choose to use a CSS file, change its name:

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
