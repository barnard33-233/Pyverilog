from __future__ import absolute_import
from __future__ import print_function
import os
import sys
from pyverilog.vparser.parser import VerilogCodeParser

try:
    from StringIO import StringIO
except:
    from io import StringIO

codedir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) + '/verilogcode/'

expected = """Source:  (at 1)
  Description:  (at 1)
    ModuleDef: ansi_localparam1 (from 1 to 10)
      Paramlist:  (at 1)
        Decl:  (at 2)
          Localparam: WIDTH, False (at 2)
            Rvalue:  (at 2)
              IntConst: 2 (at 2)
      Portlist:  (at 3)
        Ioport:  (at 4)
          Input: a, False (at 4)
            Width:  (at 4)
              Minus:  (at 4)
                Identifier: WIDTH (at 4)
                IntConst: 1 (at 4)
              IntConst: 0 (at 4)
        Ioport:  (at 5)
          Output: b, False (at 5)
            Width:  (at 5)
              Minus:  (at 5)
                Identifier: WIDTH (at 5)
                IntConst: 1 (at 5)
              IntConst: 0 (at 5)
      Assign:  (from 8 to 8)
        Lvalue:  (at 8)
          Identifier: b (at 8)
        Rvalue:  (at 8)
          Identifier: a (at 8)
    ModuleDef: ansi_localparam2 (from 12 to 25)
      Paramlist:  (at 12)
        Decl:  (at 13)
          Localparam: WIDTH, False (at 13)
            Rvalue:  (at 13)
              IntConst: 2 (at 13)
        Decl:  (at 14)
          Localparam: DEPTH, False (at 14)
            Rvalue:  (at 14)
              IntConst: 2 (at 14)
      Portlist:  (at 15)
        Ioport:  (at 16)
          Input: a, False (at 16)
            Width:  (at 16)
              Minus:  (at 16)
                Identifier: WIDTH (at 16)
                IntConst: 1 (at 16)
              IntConst: 0 (at 16)
        Ioport:  (at 17)
          Output: b, False (at 17)
            Width:  (at 17)
              Minus:  (at 17)
                Identifier: WIDTH (at 17)
                IntConst: 1 (at 17)
              IntConst: 0 (at 17)
        Ioport:  (at 18)
          Input: c, False (at 18)
            Width:  (at 18)
              Minus:  (at 18)
                Identifier: DEPTH (at 18)
                IntConst: 1 (at 18)
              IntConst: 0 (at 18)
        Ioport:  (at 19)
          Output: d, False (at 19)
            Width:  (at 19)
              Minus:  (at 19)
                Identifier: DEPTH (at 19)
                IntConst: 1 (at 19)
              IntConst: 0 (at 19)
      Assign:  (from 22 to 22)
        Lvalue:  (at 22)
          Identifier: b (at 22)
        Rvalue:  (at 22)
          Identifier: a (at 22)
      Assign:  (from 23 to 23)
        Lvalue:  (at 23)
          Identifier: d (at 23)
        Rvalue:  (at 23)
          Identifier: c (at 23)
    ModuleDef: ansi_localparam3 (from 27 to 41)
      Paramlist:  (at 27)
        Decl:  (at 28)
          Parameter: FIRST, False (at 28)
            Rvalue:  (at 28)
              IntConst: 2 (at 28)
        Decl:  (at 29)
          Localparam: WIDTH, False (at 29)
            Rvalue:  (at 29)
              IntConst: 2 (at 29)
        Decl:  (at 30)
          Localparam: DEPTH, False (at 30)
            Rvalue:  (at 30)
              IntConst: 2 (at 30)
      Portlist:  (at 31)
        Ioport:  (at 32)
          Input: a, False (at 32)
            Width:  (at 32)
              Minus:  (at 32)
                Identifier: WIDTH (at 32)
                IntConst: 1 (at 32)
              IntConst: 0 (at 32)
        Ioport:  (at 33)
          Output: b, False (at 33)
            Width:  (at 33)
              Minus:  (at 33)
                Identifier: WIDTH (at 33)
                IntConst: 1 (at 33)
              IntConst: 0 (at 33)
        Ioport:  (at 34)
          Input: c, False (at 34)
            Width:  (at 34)
              Minus:  (at 34)
                Identifier: DEPTH (at 34)
                IntConst: 1 (at 34)
              IntConst: 0 (at 34)
        Ioport:  (at 35)
          Output: d, False (at 35)
            Width:  (at 35)
              Minus:  (at 35)
                Identifier: DEPTH (at 35)
                IntConst: 1 (at 35)
              IntConst: 0 (at 35)
      Assign:  (from 38 to 38)
        Lvalue:  (at 38)
          Identifier: b (at 38)
        Rvalue:  (at 38)
          Identifier: a (at 38)
      Assign:  (from 39 to 39)
        Lvalue:  (at 39)
          Identifier: d (at 39)
        Rvalue:  (at 39)
          Identifier: c (at 39)
    ModuleDef: ansi_localparam4 (from 43 to 57)
      Paramlist:  (at 43)
        Decl:  (at 44)
          Localparam: WIDTH, False (at 44)
            Rvalue:  (at 44)
              IntConst: 2 (at 44)
        Decl:  (at 45)
          Localparam: DEPTH, False (at 45)
            Rvalue:  (at 45)
              IntConst: 2 (at 45)
        Decl:  (at 46)
          Parameter: LAST, False (at 46)
            Rvalue:  (at 46)
              IntConst: 2 (at 46)
      Portlist:  (at 47)
        Ioport:  (at 48)
          Input: a, False (at 48)
            Width:  (at 48)
              Minus:  (at 48)
                Identifier: WIDTH (at 48)
                IntConst: 1 (at 48)
              IntConst: 0 (at 48)
        Ioport:  (at 49)
          Output: b, False (at 49)
            Width:  (at 49)
              Minus:  (at 49)
                Identifier: WIDTH (at 49)
                IntConst: 1 (at 49)
              IntConst: 0 (at 49)
        Ioport:  (at 50)
          Input: c, False (at 50)
            Width:  (at 50)
              Minus:  (at 50)
                Identifier: DEPTH (at 50)
                IntConst: 1 (at 50)
              IntConst: 0 (at 50)
        Ioport:  (at 51)
          Output: d, False (at 51)
            Width:  (at 51)
              Minus:  (at 51)
                Identifier: DEPTH (at 51)
                IntConst: 1 (at 51)
              IntConst: 0 (at 51)
      Assign:  (from 54 to 54)
        Lvalue:  (at 54)
          Identifier: b (at 54)
        Rvalue:  (at 54)
          Identifier: a (at 54)
      Assign:  (from 55 to 55)
        Lvalue:  (at 55)
          Identifier: d (at 55)
        Rvalue:  (at 55)
          Identifier: c (at 55)
"""

def test():
    filelist = [codedir + 'ansi_localparam.v']
    output = 'preprocess.out'
    include = [codedir]
    define = []

    parser = VerilogCodeParser(filelist,
                               preprocess_include=include,
                               preprocess_define=define)
    ast = parser.parse()
    directives = parser.get_directives()

    output = StringIO()
    ast.show(buf=output)

    for lineno, directive in directives:
        output.write('Line %d : %s' % (lineno, directive))

    rslt = output.getvalue()

    print(rslt)
    assert(expected == rslt)

if __name__ == '__main__':
    test()