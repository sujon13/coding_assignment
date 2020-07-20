from coding_assignment.problem_3 import Node, lca
import unittest


class TestProblem3(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.root_node = Node(1)
        cls.node_2 = Node(2, cls.root_node)
        cls.node_3 = Node(3, cls.root_node)
        cls.node_20 = Node(20, cls.root_node)
        cls.node_4 = Node(4, cls.node_2)
        cls.node_5 = Node(5, cls.node_2)
        cls.node_6 = Node(6, cls.node_3)
        cls.node_7 = Node(7, cls.node_3)
        cls.node_8 = Node(8, cls.node_4)
        cls.node_9 = Node(9, cls.node_4)

        # separate tree
        cls.node_100 = Node(100)

    @classmethod
    def tearDownClass(cls) -> None:
        cls.root_node = None
        cls.node_2 = Node
        cls.node_3 = None
        cls.node_20 = None
        cls.node_4 = None
        cls.node_5 = None
        cls.node_6 = None
        cls.node_7 = None
        cls.node_8 = None
        cls.node_9 = None
        cls.node_100 = None

    def test_wrong_parameters(self):
        with self.assertRaises(TypeError):
            lca(1, 2)

    def test_every_node_is_ancestor_of_itself(self):
        answer = lca(self.node_2, self.node_2)
        self.assertEqual(answer, self.node_2, 'Answer should be node_2')

    def test_lca_of_node_8_and_9_should_be_4(self):
        answer = lca(self.node_8, self.node_9)
        self.assertEqual(answer, self.node_4, 'Answer should be node_4')

    def test_lca_of_root_and_6_should_be_1(self):
        answer = lca(self.root_node, self.node_6)
        self.assertEqual(answer, self.root_node, 'Answer should be root node')

    def test_nodes_of_two_tree_should_not_have_lca(self):
        answer = lca(self.node_8, self.node_100)
        self.assertEqual(answer, None, 'Answer should be None')


if __name__ == '__main__':
    unittest.main()