import unittest
import nodes


correct_table = [{'Sellings.id': '1', 'Sellings.userId': '2', 'Sellings.item': 'sword'},
                 {'Sellings.id': '2', 'Sellings.userId': '4', 'Sellings.item': 'shield'},
                 {'Sellings.id': '3', 'Sellings.userId': '2', 'Sellings.item': 'fireball'}]


class TestTableNode(unittest.TestCase):
    def test_table_get_next(self):
        """
        Test that check if get_next is correct
        """

        table_node = nodes.TableNode('Sellings', 'tests/data')
        table_node.open()
        result = []

        data_block = table_node.get_next()
        while (data_block is not None):
            result += data_block
            data_block = table_node.get_next()

        table_node.close()

        self.assertListEqual(result, correct_table)

    def test_table_reset_scen_1(self):
        """
        Test that check if reset is correct
        """

        table_node = nodes.TableNode('Sellings', 'tests/data')
        table_node.open()

        # take all data until the end
        while (table_node.get_next() is not None):
            pass

        table_node.reset()
        result = []

        data_block = table_node.get_next()
        while (data_block is not None):
            result += data_block
            data_block = table_node.get_next()

        table_node.close()

        self.assertListEqual(result, correct_table)

    def test_table_reset_scen_2(self):
        """
        Test that check if reset is correct
        """

        table_node = nodes.TableNode('Sellings', 'tests/data')
        table_node.open()

        # take first n blocks of data
        for _ in range(2):
            table_node.get_next()

        table_node.reset()
        result = []

        data_block = table_node.get_next()
        while (data_block is not None):
            result += data_block
            data_block = table_node.get_next()

        table_node.close()

        self.assertListEqual(result, correct_table)


if __name__ == '__main__':
    unittest.main()
