import unittest
import nodes


class TestWhereNode(unittest.TestCase):
    def test_where_get_next_scen_1(self):
        """
        Test that check if get_next is correct
        """
        answer = [{'Stats.item': 'sword', 'Stats.damage': '10', 'Stats.cost': '5'}]

        ltable_node = nodes.TableNode('Stats', 'tests/data')
        where_node = nodes.WhereNode('Stats.item', 'sword', ['='])
        where_node.set_LChild(ltable_node)
        where_node.open()

        result = []

        data_block = where_node.get_next()
        while (data_block is not None):
            result += data_block
            data_block = where_node.get_next()

        where_node.close()
        self.assertListEqual(result, answer)

    def test_where_get_next_scen_2(self):
        """
        Test that check if get_next is correct
        """
        answer = [{'Stats.item': 'shield', 'Stats.damage': '1', 'Stats.cost': '2'},
                  {'Stats.item': 'bow', 'Stats.damage': '7', 'Stats.cost': '7'},]

        ltable_node = nodes.TableNode('Stats', 'tests/data')
        where_node = nodes.WhereNode('Stats.damage', 'Stats.cost', ['<', '='])
        where_node.set_LChild(ltable_node)
        where_node.open()

        result = []

        data_block = where_node.get_next()
        while (data_block is not None):
            result += data_block
            data_block = where_node.get_next()

        where_node.close()
        self.assertListEqual(result, answer)

    def test_where_get_next_scen_3(self):
        """
        Test that check if get_next is correct
        """
        answer = [{'Stats.item': 'sword', 'Stats.damage': '10', 'Stats.cost': '5'}]

        ltable_node = nodes.TableNode('Stats', 'tests/data')
        where_node = nodes.WhereNode('shield', 'Stats.item', ['<'])
        where_node.set_LChild(ltable_node)
        where_node.open()

        result = []

        data_block = where_node.get_next()
        while (data_block is not None):
            result += data_block
            data_block = where_node.get_next()

        where_node.close()
        self.assertListEqual(result, answer)

    def test_where_reset_scen_1(self):
        """
        Test that check if reset is correct
        """
        answer = [{'Stats.item': 'shield', 'Stats.damage': '1', 'Stats.cost': '2'},
                  {'Stats.item': 'bow', 'Stats.damage': '7', 'Stats.cost': '7'},]

        ltable_node = nodes.TableNode('Stats', 'tests/data')
        where_node = nodes.WhereNode('Stats.damage', 'Stats.cost', ['<', '='])
        where_node.set_LChild(ltable_node)
        where_node.open()

        result = []

        # take all data until the end
        while (where_node.get_next() is not None):
            pass

        where_node.reset()
        result = []

        data_block = where_node.get_next()
        while (data_block is not None):
            result += data_block
            data_block = where_node.get_next()

        where_node.close()

        self.assertListEqual(result, answer)

    def test_where_reset_scen_2(self):
        """
        Test that check if reset is correct
        """

        answer = [{'Stats.item': 'shield', 'Stats.damage': '1', 'Stats.cost': '2'},
                  {'Stats.item': 'bow', 'Stats.damage': '7', 'Stats.cost': '7'},]

        ltable_node = nodes.TableNode('Stats', 'tests/data')
        where_node = nodes.WhereNode('Stats.damage', 'Stats.cost', ['<', '='])
        where_node.set_LChild(ltable_node)
        where_node.open()

        result = []

        # take first n blocks of data
        for _ in range(1):
            where_node.get_next()

        where_node.reset()
        result = []

        data_block = where_node.get_next()
        while (data_block is not None):
            result += data_block
            data_block = where_node.get_next()

        where_node.close()

        self.assertListEqual(result, answer)


if __name__ == '__main__':
    unittest.main()
