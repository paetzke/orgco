# -*- coding: utf-8 -*-
"""
orgco

Copyright (c) 2013, Friedrich Paetzke (f.paetzke@gmail.com)
All rights reserved.

"""
import re


class Liner:

    def __init__(self, content):
        self.cnt = 0
        self.lines = [line.rstrip() for line in content.split('\n')]

    def pushback(self, times=1):
        self.cnt -= times

    def __iter__(self):
        return self

    def __next__(self):
        if self.cnt == len(self.lines):
            raise StopIteration

        line = self.lines[self.cnt]
        self.cnt += 1
        return line

    def next(self):
        return self.__next__()


class OrgDoc:

    def __init__(self, content=None):
        self.things = []
        self._separated = False

        if content:
            liner = Liner(content)
            self._analyze(liner)

    def _get_thing_by_level(self, cls, level):
        thing = self
        for i in range(level):
            clss = cls
            if cls == DefinitionList and i < level - 1:
                clss = List
            thing = self._get_thing(clss, thing=thing)
        return thing

    def _get_thing(self, cls, level=None, thing=None):
        if level:
            return self._get_thing_by_level(cls, level)

        thing = thing if thing else self

        if thing.things and not self._separated:
            last_thing = thing.things[-1]
            if isinstance(last_thing, cls):
                return last_thing
        if self._separated:
            self._separated = False
        new_thing = cls()
        thing.things.append(new_thing)
        return new_thing

    def _analyze(self, liner):
        for line in liner:
            if line == '':
                self._separated = True
                continue

            definitionlist, level = DefinitionItem.from_string(line)
            if definitionlist:
                lst = self._get_thing(DefinitionList, level=level)
                lst.add(definitionlist)
                continue

            header = Header.from_string(line)
            if header:
                self.things.append(header)
                continue

            listitem, level, ordered = ListItem.from_string(line, liner)
            if listitem:
                lst = self._get_thing(List, level=level)
                lst.ordered = ordered
                lst.add(listitem)
                continue

            if line.startswith('|-'):
                table = self._get_thing(Table)
                table.things[-1].is_header = True
                continue

            if line.startswith('| '):
                table_row = TableRow.from_string(line)
                table = self._get_thing(Table)
                table.add(table_row)
                continue

            if line.startswith('#+BEGIN_SRC'):
                code = Code.from_string(line, liner)
                self.things.append(code)
            elif line:
                paragraph = self._get_thing(Paragraph)
                paragraph.add(line)


class Container:

    def __init__(self):
        self.things = []

    def add(self, thing):
        self.things.append(thing)


class Code:

    def __init__(self, lines, language=None):
        self.lines = lines
        self.language = language

    def __str__(self):
        return '\n'.join(self.lines)

    @classmethod
    def from_string(cls, line, liners):
        lines = []
        language = line[len('#+BEGIN_SRC '):]
        for line in liners:
            if line.startswith('#+END_SRC'):
                break
            lines.append(line)
        code = cls(lines, language)
        return code


class DefinitionList(Container):
    pass


class DefinitionItem:

    def __init__(self, term, description):
        self.term = term
        self.description = description

    @classmethod
    def from_string(cls, line):
        mat = re.match(r'^([ ]*)- (.+) :: (.+)', line)
        if mat:
            level = len(mat.group(1)) // 2 + 1
            return cls(mat.group(2), mat.group(3)), level
        return None, 0


class Header:

    def __init__(self, level, text):
        self.level = level
        self.text = text

    def __str__(self):
        return self.text

    @classmethod
    def from_string(cls, line):
        mat = re.match(r'^(\*+)\s+(.+)$', line)
        if mat:
            return cls(level=len(mat.group(1)), text=mat.group(2))
        return None


class List(Container):

    def __init__(self, ordered=False):
        Container.__init__(self)
        self.ordered = ordered


class ListItem:

    def __init__(self, lines):
        self.lines = []
        lines = (line for line in lines)
        for line in lines:
            if not line:
                break
            self.lines.append(line)

        orgdoc = OrgDoc('\n'.join(lines))
        self.things = orgdoc.things

    def __str__(self):
        return ' '.join(self.lines)

    @classmethod
    def from_string(cls, line, liner):
        regexps = [r'^([ ]*)(\d+\.) (.+)$', r'^([ ]*)(-) (.+)$']
        for regexp in regexps:
            mat = re.match(regexp, line)
            if mat:
                is_ordered = mat.group(2) != '-'
                level = len(mat.group(1)) // 2 + 1
                spaces = (len(mat.group(1)) + 2) * ' '
                if is_ordered:
                    spaces += (len(mat.group(2)) - 1) * ' '

                lines = [mat.group(3)]
                found_blank_line = False
                if len(spaces) > len(mat.group(1)):
                    for line in liner:
                        if not line:
                            if found_blank_line:
                                liner.pushback(2)
                                break
                            found_blank_line = True
                            continue

                        if found_blank_line:
                            lines.append('')
                            found_blank_line = False

                        if line.startswith(spaces) and not line.startswith('%s-' % spaces):
                            lines.append(line[len(spaces):])
                        else:
                            liner.pushback()
                            break

                return cls(lines), level, is_ordered
        return None, 0, False


class Paragraph:

    def __init__(self):
        self.lines = []

    def __str__(self):
        return ' '.join(self.lines)

    def add(self, line):
        self.lines.append(line)


class TableRow:

    def __init__(self):
        self.cols = []
        self.is_header = False

    @classmethod
    def from_string(cls, line):
        row = cls()
        cols = (col.strip() for col in line.split('|')[1:-1])
        for col in cols:
            row.cols.append(col)
        return row


class Table(Container):
    pass
