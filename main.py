import antlr4
from parser.sqlLexer import sqlLexer
from parser.sqlParser import sqlParser
from spj import SQLLogic
from nodes import AbstractNode
import sys


INPUT_FILE = 'input.txt'


def print_bin_tree(node: AbstractNode, ind):
    print('--' * ind + str(node))

    if (node.give_LChind() is not None):
        print_bin_tree(node.give_LChind(), ind+1)
    if (node.give_RChind() is not None):
        print_bin_tree(node.give_RChind(), ind+1)


def test(argv):
    print('TEST:')
    lexer = sqlLexer(antlr4.FileStream(INPUT_FILE))
    stream = antlr4.CommonTokenStream(lexer)
    parser = sqlParser(stream)
    tree = parser.query()

    print(tree.toStringTree(recog=parser))

    listener = SQLLogic()
    antlr4.ParseTreeWalker().walk(listener, tree)
    root = listener.getRoot()
    print_bin_tree(root, 0)
    root.open()


def main(argv):
    if '--test' in argv:
        test(argv)
        return

    input_text = input('> ')
    lexer = sqlLexer(InputStream(input_text))
    # lexer = sqlLexer(antlr4.FileStream(INPUT_FILE))
    stream = antlr4.CommonTokenStream(lexer)
    parser = sqlParser(stream)
    tree = parser.query()

    listener = SQLLogic()
    antlr4.ParseTreeWalker().walk(listener, tree)
    root = listener.getRoot()

    root.open()

    data_block = root.get_next()
    res = []
    while (data_block is not None):
        res += data_block
        data_block = root.get_next()
    print(*res, sep='\n')

    root.close()


if __name__ == '__main__':
    while True:
        main(sys.argv)
