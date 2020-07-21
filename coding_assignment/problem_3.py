class Node:
    def __init__(self, value, parent=None):
        self.value = value
        self.parent = parent


class Solution3(object):
    def __init__(self):
        pass

    def lca(self, node1, node2):
        """
        The function to find lca of two nodes.

        Parameters:
            node1 (Node): First node.
            node2 (Node): Second node.

        Returns:
            Node: A Node which is lowest/least common ancestor (lca) of two given nodes.
        """

        if not isinstance(node1, Node) or not isinstance(node2, Node):
            error_message = 'Types of parameters are incorrect. They should be of type Node'
            raise TypeError(error_message)

        dist_of_node1_from_root = self.get_distance_from_root(node1)
        dist_of_node2_from_root = self.get_distance_from_root(node2)

        # First we will make sure node1 is the distant node from root
        if dist_of_node2_from_root > dist_of_node1_from_root:
            node1, node2 = node2, node1
            dist_of_node1_from_root, dist_of_node2_from_root = dist_of_node2_from_root, dist_of_node1_from_root

        # Now need to ensure two nodes are in same level
        while dist_of_node1_from_root > dist_of_node2_from_root:
            dist_of_node1_from_root -= 1
            node1 = node1.parent

        # now both nodes have equal distance from root node
        lca_node = self.get_lca_of_two_same_leveled_node(node1, node2)
        return lca_node

    def get_lca_of_two_same_leveled_node(self, node1, node2):
        # if they are from same tree then lca will be found
        # otherwise None will be encountered and loop will be break
        while node1 and node1 != node2:
            node1 = node1.parent
            node2 = node2.parent
        return node1

    def get_distance_from_root(self, node):
        distance = 0
        while node.parent:
            distance += 1
            node = node.parent
        return distance


if __name__ == '__main__':
    # tree creation
    root_node = Node(1)
    node_2 = Node(2, root_node)
    node_3 = Node(3, root_node)
    node_20 = Node(20, root_node)
    node_4 = Node(4, node_2)
    node_5 = Node(5, node_2)
    node_6 = Node(6, node_3)
    node_7 = Node(7, node_3)
    node_8 = Node(8, node_4)
    node_9 = Node(9, node_4)

    # separate tree
    node_100 = Node(100)

    solution = Solution3()
    answer = solution.lca(node_4, node_5)
    print(answer.value)
