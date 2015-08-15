orgco
=====

.. image:: https://travis-ci.org/paetzke/orgco.svg?branch=master
  :target: https://travis-ci.org/paetzke/orgco
.. image:: https://coveralls.io/repos/paetzke/orgco/badge.svg?branch=master
  :target: https://coveralls.io/r/paetzke/orgco?branch=master
.. image:: https://badge.fury.io/py/orgco.svg
  :target: https://pypi.python.org/pypi/orgco/

With orgco you can convert Emacs' orgmode to other formats.

Supported output formats:

* HTML
* reStructuredText (rst)

Supported orgmode tags:

* headers
* code (inline and multi-line)
* lists (ordered, unordered and definition lists)
* tables
* links (external and images)
* italic, bold, underlined, stroked markups

To use orgco install it from PyPI:

.. code:: bash

    $ pip install orgco

Orgco provides 2 simple functions to convert orgmode to html (``convert_html()``) and rst (``convert_rst()``).

.. code:: python

    from orgco import convert_html
    
    with open('my_orgmode.org') as f:
        html = convert_html(f.read())
    print(html)

The HTML converter takes some optional parameters:

* ``header=True``: To decide if the output should only contain the inner body or act as a normal HTML file with header and body.
* ``highlight=True``: To enable code highlighting.
* ``includes=['style.css']``: To include some additional CSS files.

Orgco comes also with a command line tool:

.. code:: bash

    usage: orgco.py [-h] -i INPUT -o OUTPUT -f FORMAT [--header] [--highlight]
                    [--includes INCLUDES [INCLUDES ...]]
    
    optional arguments:
      -h, --help            show this help message and exit
      -i INPUT, --input INPUT
      -o OUTPUT, --output OUTPUT
      -f FORMAT, --format FORMAT
      --header
      --highlight
      --includes INCLUDES [INCLUDES ...]

Copyright (c) 2013-2015, Friedrich Paetzke (paetzke@fastmail.fm). All rights reserved.

