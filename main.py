from antlr4 import *
from parser.sqlLexer import sqlLexer
from parser.sqlParser import sqlParser
from spj import SQLLogic
from nodes import *
import sys



def print_bin_tree(node : AbstractNode, ind):
    print('--' * ind + str(node))

    if(node.give_LChind() != None):
        print_bin_tree(node.give_LChind(), ind+1)
    if(node.give_RChind() != None):
        print_bin_tree(node.give_RChind(), ind+1)


def test(argv):
    print('TEST:')

    joinNodeUp = JoinNode('Stats.item', 'Sellings.item')
    joinNodeBot = JoinNode('Sellings.userId', 'Users.id')

    rtable_node = TableNode('Users')
    ltable_node = TableNode('Sellings')
    rrtable_node = TableNode('Stats')

    joinNodeBot.set_LChild(ltable_node)
    joinNodeBot.set_RChild(rtable_node)

    joinNodeUp.set_LChild(joinNodeBot)
    joinNodeUp.set_RChild(rrtable_node)

    whereNode = WhereNode('Stats.cost', 'Stats.damage', list('>'))
    whereNode.set_LChild(joinNodeUp)

    selectNode = SelectNode(['Stats.item', 'Sellings.item', 'Sellings.userId', 'Users.id', 'Stats.cost', 'Stats.damage'])
    selectNode.set_LChild(whereNode)
    selectNode.open()
    print(*[selectNode.get_next() for _ in range(4)])

    selectNode.close()


def main(argv):
    # input_text = input('> ')
    # lexer = sqlLexer(InputStream(input_text))
    if '--test' in argv:
        test(argv)
        return

    lexer = sqlLexer(FileStream('test/input.txt'))
    stream = CommonTokenStream(lexer)
    parser = sqlParser(stream)
    tree = parser.query()

    # print(tree.toStringTree(recog=parser))

    listener = SQLLogic()
    ParseTreeWalker().walk(listener, tree)
    root = listener.getRoot()
    print_bin_tree(root, 0)
    root.open()
    print(root.get_next())

if __name__ == '__main__':
    main(sys.argv)