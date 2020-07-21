from coding_assignment.problem_1 import Solution1
import unittest


class Person(object):
    def __init__(self, name):
        self.name = name


class TestProblem1(unittest.TestCase):
    def setUp(self):
        self.solution = Solution1()

    def tearDown(self):
        self.solution = None

    def test_wrong_parameters(self):
        with self.assertRaises(TypeError):
            self.solution.print_depth(1)

    def test_empty_dictionary(self):
        answer = self.solution.print_depth({})
        self.assertEqual(answer, [], 'Answer should be empty list')

    def test_normal_dictionary(self):
        """
        Test dictionary without nesting can be printed with depth info correctly

        Returns:
            list: A list where every element is dictionary keys and corresponding depth.
        """

        input_dictionary = {
            'name': 'sujon',
            'subject': 'cse'
        }
        answer = self.solution.print_depth(input_dictionary)

        actual_answer = [
            ('name', 1),
            ('subject', 1)
        ]
        self.assertEqual(answer, actual_answer, 'Answer is not correct')

    def test_nested_dictionary(self):
        input_dictionary = {
            'key1': 1,
            'key2': 2,
            'key3': {
                'key4': 4,
                'key5': 5,
            },
            'key6': 6
        }

        answer = self.solution.print_depth(input_dictionary)
        actual_answer = [
            ('key1', 1),
            ('key2', 1),
            ('key3', 1),
            ('key4', 2),
            ('key5', 2),
            ('key6', 1)
        ]
        self.assertEqual(answer, actual_answer, 'Answer is not correct')

    def test_using_object_as_dictionary_value_should_fail(self):
        """
        This solution will not handle object inside dictionary
        """

        person = Person('Mr X')
        input_dictionary = {
            'person': person,
            'address': 'Dhaka'
        }

        answer = self.solution.print_depth(input_dictionary)

        actual_answer = [
            ('person', 1),
            ('name', 2),
            ('address', 1)
        ]
        self.assertNotEqual(answer, actual_answer, 'Answer is incorrect')
        self.assertEqual(answer, actual_answer[::2], 'Answer is incorrect')


if __name__ == '__main__':
    unittest.main()