import unittest
import nodes


correct_table = [{'Users.name': 'Max', 'Users.surname': 'Emel'}, 
                 {'Users.name': 'Anna', 'Users.surname': 'Ask'}, 
                 {'Users.name': 'Georg', 'Users.surname': 'Chern'}, 
                 {'Users.name': 'Sem', 'Users.surname': 'Smirn'}]


class TestSelectNode(unittest.TestCase):
    def test_select_get_next(self):
        """
        Test that check if get_next is correct
        """

        ltable_node = nodes.TableNode('Users', 'tests/data')
        select_node = nodes.SelectNode(['Users.name', 'Users.surname'])
        select_node.set_LChild(ltable_node)
        select_node.open()

        result = []

        data_block = select_node.get_next()
        while(data_block != None):
            result += data_block
            data_block = select_node.get_next()

        select_node.close()
        self.assertListEqual(result, correct_table)
    
    def test_where_reset_scen_1(self):
        """
        Test that check if reset is correct
        """

        ltable_node = nodes.TableNode('Users', 'tests/data')
        select_node = nodes.SelectNode(['Users.name', 'Users.surname'])
        select_node.set_LChild(ltable_node)
        select_node.open()

        result = []

        # take all data until the end
        while(select_node.get_next() != None):
            pass
        
        select_node.reset()
        result = []

        data_block = select_node.get_next()
        while(data_block != None):
            result += data_block
            data_block = select_node.get_next()

        select_node.close()

        self.assertListEqual(result, correct_table)
    
    def test_where_reset_scen_2(self):
        """
        Test that check if reset is correct
        """
        
        ltable_node = nodes.TableNode('Users', 'tests/data')
        select_node = nodes.SelectNode(['Users.name', 'Users.surname'])
        select_node.set_LChild(ltable_node)
        select_node.open()

        result = []

        # take first n blocks of data
        for _ in range(2):
            select_node.get_next()
        
        select_node.reset()
        result = []

        data_block = select_node.get_next()
        while(data_block != None):
            result += data_block
            data_block = select_node.get_next()

        select_node.close()

        self.assertListEqual(result, correct_table)

    
if __name__ == '__main__':
    unittest.main()