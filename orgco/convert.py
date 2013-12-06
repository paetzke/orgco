"""
orgco

Copyright (c) 2013, Friedrich Paetzke (f.paetzke@gmail.com)
All rights reserved.

"""
import os

from .orgalyzer import Code, DefinitionList, DefinitionItem, Header, List, \
    ListItem, Paragraph, Table, TableRow


def convert(orgdoc, outputtype, **kwargs):
    if outputtype == 'html':
        return to_html(orgdoc, **kwargs)
    elif outputtype == 'rst':
        return to_rst(orgdoc, **kwargs)


def find_markup(s, i):
    looking_for = [
        ('=', '='),
        ('*', '*'),
        ('_', '_'),
        ('/', '/'),
        ('+', '+'),
        ('[[', ']]'),
    ]
    valid_after = lambda c: c.isspace() or c in ',.):'

    for start, end in looking_for:
        if s[i:].startswith(start):
            for j in range(i + 1, len(s)):
                if s[j:].startswith(end) and \
                        (len(s[j:]) == len(end) or valid_after(s[j:][len(end)])):
                    markup = s[i:j + len(end)]
                    if len(markup) > len(start) + len(end):
                        return markup, i + len(markup)
    return s[i], i + 1


def textify(s, outputtype):
    pos = 0
    s = str(s)
    result = []
    while pos < len(s):
        markup, pos = find_markup(s, pos)

        if len(markup) > 1:
            if outputtype == 'html':
                markup = replace_html(markup)
            elif outputtype == 'rst':
                markup = replace_rst(markup)
        result.append(markup)

    text = ''.join(result)
    if text.endswith(r' \\'):
        if outputtype == 'html':
            text = '%s<br />' % text[:-3]
        elif outputtype == 'rst':
            text = '| %s' % text[:-3]

    return text


def to_html(orgdoc, header=False):
    result = []
    if header:
        result.extend([
            '<!DOCTYPE html>',
            '<html>',
            '<head>',
            '<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />',
            '</head>',
            '<body>'
        ])
    result.extend(_to_html(orgdoc.things))
    if header:
        result.extend([
            '</body>',
            '</html>'
        ])
    result.append('')
    return result


def _to_html(things):
    result = []
    textify_html = lambda s: textify(s, 'html')
    for thing in things:
        if isinstance(thing, Code):
            text = '<pre>%s</pre>' % thing
            result.append(text)
        elif isinstance(thing, DefinitionList):
            result.append('<dl>')
            result.extend(_to_html(thing.things))
            result.append('</dl>')
        elif isinstance(thing, DefinitionItem):
            result.append('<dt>%s</dt>' % textify_html(thing.term))
            result.append('<dd>%s</dd>' % textify_html(thing.description))
        elif isinstance(thing, Header):
            args = {
                'level': thing.level,
                'text': textify_html(thing)}
            text = '<h%(level)d>%(text)s</h%(level)d>' % args
            result.append(text)
        elif isinstance(thing, List):
            tag = 'ol' if thing.ordered else 'ul'
            result.append('<%s>' % tag)
            result.extend(_to_html(thing.things))
            result.append('</%s>' % tag)
        elif isinstance(thing, ListItem):
            if thing.things:
                result.append('<li>%s' % textify_html(thing))
                result.extend(_to_html(thing.things))
                result.append('</li>')
            else:
                text = '<li>%s</li>' % textify_html(thing)
                result.append(text)
        elif isinstance(thing, Paragraph):
            lines = (textify_html(line) for line in thing.lines)
            text = '<p>%s</p>' % ' '.join(lines)
            result.append(text)
        elif isinstance(thing, Table):
            result.append('<table>')
            result.extend(_to_html(thing.things))
            result.append('</table>')
        elif isinstance(thing, TableRow):
            tag = 'th' if thing.is_header else 'td'
            fmt = '</%(tag)s><%(tag)s>' % {'tag': tag}
            args = {
                'tag': tag,
                'text': fmt.join(textify_html(col) for col in thing.cols)
            }
            text = '<%(tag)s>%(text)s</%(tag)s>' % args
            result.append('<tr>')
            result.append(text)
            result.append('</tr>')

    return result


def replace_html(markup):
    replacements = {
        '=': 'code',
        '*': 'b',
        '_': 'u',
        '/': 'i',
        '+': 'del'}

    if markup[0] == '[':
        link = markup[2:-2]

        link_name = link.split('][')
        if len(link_name) == 2:
            args = {
                'link': link_name[0],
                'name': link_name[1],
            }
        else:
            _unused, ext = os.path.splitext(link)

            if ext in ['.bmp', '.jpg', '.png', '.svg']:
                return '<img src="%s" />' % link
            args = {
                'link': link,
                'name': link,
            }

        return '<a href="%(link)s">%(name)s</a>' % args
    else:
        args = {
            'tag': replacements[markup[0]],
            'text': markup[1:-1]
        }
        return '<%(tag)s>%(text)s</%(tag)s>' % args


def replace_rst(markup):
    replacements = {
        '=': '``',  # code
        '*': '**',  # bold
        '_': '',  # underline
        '/': '*',  # italic
        '+': ''}  # strike

    if markup[0] == '[':

        link = markup[2:-2]

        link_name = link.split('][')
        if len(link_name) == 2:
            args = {
                'link': link_name[0],
                'name': link_name[1],
            }
        else:
            _unused, ext = os.path.splitext(link)

            if ext in ['.bmp', '.jpg', '.png', '.svg']:
                return '.. image:: %s' % link
            args = {
                'link': link,
                'name': link,
            }

        return '`%(name)s <%(link)s>`_' % args
    else:
        args = {
            'markup': replacements[markup[0]],
            'text': markup[1:-1]
        }
        return '%(markup)s%(text)s%(markup)s' % args

    return markup


def to_markdown(orgdoc):
    return _to_markdown(orgdoc.things)


def _to_markdown(things):
    result = []
    for thing in things:
        if isinstance(thing, Code):
            text = '`\n%s\n`\n' % thing
        elif isinstance(thing, Header):
            text = '%s %s\n' % ('#' * thing.level, thing)
        elif isinstance(thing, Paragraph):
            text = '%s\n' % thing

        result.append(text)
    return result


def to_rst(orgdoc):
    return _to_rst(orgdoc.things)


def _to_rst(things, level=0, **kwargs):
    result = []
    textify_rst = lambda s: textify(s, 'rst')
    for i, thing in enumerate(things):
        if isinstance(thing, Code):
            result.append('.. code:: %s' % thing.language)
            result.append('')
            result.extend(('    %s' % line for line in thing.lines))
            result.append('')
        elif isinstance(thing, DefinitionList):
            result.extend(_to_rst(thing.things))
        elif isinstance(thing, DefinitionItem):
            result.append('%s' % textify_rst(thing.term))
            result.append('    %s' % textify_rst(thing.description))
            result.append('')
        elif isinstance(thing, Header):
            levels = ['=', '-', '~']
            result.append('%s' % textify_rst(thing))
            result.append('%s' % levels[thing.level - 1] * len(str(thing)))
            result.append('')
        elif isinstance(thing, List):
            result.extend(_to_rst(thing.things, level + 1, ordered=thing.ordered))
            if level == 0:
                result.append('')
        elif isinstance(thing, ListItem):
            if kwargs['ordered']:
                text = '%d. %s' % (i + 1, textify_rst(thing))
            else:
                text = '%s* %s' % ('  ' * (level - 1), textify_rst(thing))
            result.append(text)
        elif isinstance(thing, Paragraph):
            for line in thing.lines:
                result.append(textify_rst(line))
            result.append('')
        else:
            raise NotImplementedError('BNG')
    return result
