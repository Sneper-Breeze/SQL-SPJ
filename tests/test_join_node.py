import unittest
import nodes


correct_table = [{'Stats.item': 'sword', 'Stats.damage': '10', 'Stats.cost': '5',
                  'Sellings.id': '1', 'Sellings.userId': '2', 'Sellings.item': 'sword'},
                 {'Stats.item': 'shield', 'Stats.damage': '1', 'Stats.cost': '2',
                  'Sellings.id': '2', 'Sellings.userId': '4', 'Sellings.item': 'shield'},
                 {'Stats.item': 'fireball', 'Stats.damage': '20', 'Stats.cost': '10',
                 'Sellings.id': '3', 'Sellings.userId': '2', 'Sellings.item': 'fireball'}]


class TestJoinNode(unittest.TestCase):
    def test_join_get_next(self):
        """
        Test that check if get_next is correct
        """

        rtable_node = nodes.TableReaderNode('Sellings', 'tests/data')
        ltable_node = nodes.TableReaderNode('Stats', 'tests/data')
        join_node = nodes.JoinNode('Sellings.item', 'Stats.item')
        join_node.set_LChild(ltable_node)
        join_node.set_RChild(rtable_node)
        join_node.open()
        result = []

        data_block = join_node.get_next()
        while (data_block is not None):
            result += data_block
            data_block = join_node.get_next()

        join_node.close()

        self.assertListEqual(result, correct_table)

    def test_join_reset_scen_1(self):
        """
        Test that check if reset is correct
        """

        rtable_node = nodes.TableReaderNode('Sellings', 'tests/data')
        ltable_node = nodes.TableReaderNode('Stats', 'tests/data')
        join_node = nodes.JoinNode('Sellings.item', 'Stats.item')
        join_node.set_LChild(ltable_node)
        join_node.set_RChild(rtable_node)
        join_node.open()

        result = []

        # take all data until the end
        while (join_node.get_next() is not None):
            pass

        join_node.reset()
        result = []

        data_block = join_node.get_next()
        while (data_block is not None):
            result += data_block
            data_block = join_node.get_next()

        join_node.close()

        self.assertListEqual(result, correct_table)

    def test_join_reset_scen_2(self):
        """
        Test that check if reset is correct
        """

        rtable_node = nodes.TableReaderNode('Sellings', 'tests/data')
        ltable_node = nodes.TableReaderNode('Stats', 'tests/data')
        join_node = nodes.JoinNode('Sellings.item', 'Stats.item')
        join_node.set_LChild(ltable_node)
        join_node.set_RChild(rtable_node)
        join_node.open()

        result = []

        # take first n blocks of data
        for _ in range(2):
            join_node.get_next()

        join_node.reset()
        result = []

        data_block = join_node.get_next()
        while (data_block is not None):
            result += data_block
            data_block = join_node.get_next()

        join_node.close()

        self.assertListEqual(result, correct_table)


if __name__ == '__main__':
    unittest.main()
