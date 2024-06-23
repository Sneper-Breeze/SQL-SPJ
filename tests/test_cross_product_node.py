import unittest
import nodes


correct_table = [{'Stats.item': 'sword', 'Stats.damage': '10', 'Stats.cost': '5', 'SellingsSmall.id': '1',
                  'SellingsSmall.userId': '2', 'SellingsSmall.item': 'sword'},
                 {'Stats.item': 'shield', 'Stats.damage': '1', 'Stats.cost': '2', 'SellingsSmall.id': '1',
                  'SellingsSmall.userId': '2', 'SellingsSmall.item': 'sword'},
                 {'Stats.item': 'fireball', 'Stats.damage': '20', 'Stats.cost': '10', 'SellingsSmall.id': '1',
                 'SellingsSmall.userId': '2', 'SellingsSmall.item': 'sword'},
                 {'Stats.item': 'bow', 'Stats.damage': '7', 'Stats.cost': '7', 'SellingsSmall.id': '1',
                 'SellingsSmall.userId': '2', 'SellingsSmall.item': 'sword'},
                 {'Stats.item': 'sword', 'Stats.damage': '10', 'Stats.cost': '5', 'SellingsSmall.id': '2',
                 'SellingsSmall.userId': '4', 'SellingsSmall.item': 'shield'},
                 {'Stats.item': 'shield', 'Stats.damage': '1', 'Stats.cost': '2', 'SellingsSmall.id': '2',
                 'SellingsSmall.userId': '4', 'SellingsSmall.item': 'shield'},
                 {'Stats.item': 'fireball', 'Stats.damage': '20', 'Stats.cost': '10', 'SellingsSmall.id':
                 '2', 'SellingsSmall.userId': '4', 'SellingsSmall.item': 'shield'},
                 {'Stats.item': 'bow', 'Stats.damage': '7', 'Stats.cost': '7', 'SellingsSmall.id': '2',
                 'SellingsSmall.userId': '4', 'SellingsSmall.item': 'shield'}]


class TestCrossProductNode(unittest.TestCase):
    def test_cross_product_get_next(self):
        """
        Test that check if get_next is correct
        """

        rtable_node = nodes.TableReaderNode('SellingsSmall', 'tests/data')
        ltable_node = nodes.TableReaderNode('Stats', 'tests/data')
        cross_product_node = nodes.CrossProductNode()
        cross_product_node.set_LChild(ltable_node)
        cross_product_node.set_RChild(rtable_node)
        cross_product_node.open()
        result = []

        data_block = cross_product_node.get_next()
        while (data_block is not None):
            result += data_block
            data_block = cross_product_node.get_next()
        cross_product_node.close()

        self.assertListEqual(result, correct_table)

    def test_cross_product_reset_scen_1(self):
        """
        Test that check if reset is correct
        """

        rtable_node = nodes.TableReaderNode('SellingsSmall', 'tests/data')
        ltable_node = nodes.TableReaderNode('Stats', 'tests/data')
        cross_product_node = nodes.CrossProductNode()
        cross_product_node.set_LChild(ltable_node)
        cross_product_node.set_RChild(rtable_node)
        cross_product_node.open()

        result = []

        # take all data until the end
        while (cross_product_node.get_next() is not None):
            pass

        cross_product_node.reset()
        result = []

        data_block = cross_product_node.get_next()
        while (data_block is not None):
            result += data_block
            data_block = cross_product_node.get_next()

        cross_product_node.close()

        self.assertListEqual(result, correct_table)

    def test_cross_product_reset_scen_2(self):
        """
        Test that check if reset is correct
        """

        rtable_node = nodes.TableReaderNode('SellingsSmall', 'tests/data')
        ltable_node = nodes.TableReaderNode('Stats', 'tests/data')
        cross_product_node = nodes.CrossProductNode()
        cross_product_node.set_LChild(ltable_node)
        cross_product_node.set_RChild(rtable_node)
        cross_product_node.open()

        result = []

        # take first n blocks of data
        for _ in range(5):
            cross_product_node.get_next()

        cross_product_node.reset()
        result = []

        data_block = cross_product_node.get_next()
        while (data_block is not None):
            result += data_block
            data_block = cross_product_node.get_next()

        cross_product_node.close()

        self.assertListEqual(result, correct_table)


if __name__ == '__main__':
    unittest.main()
