class Solution2(object):
    def __init__(self):
        # answer will ne a list where every element will be a tuple of key and depth like ('key': 1)
        self.answer = []

    def dfs(self, dictionary, depth):
        for key, value in dictionary.items():
            self.answer.append((key, depth))

            # converting object to dictionary
            if hasattr(value, '__dict__'):
                value = value.__dict__

            if type(value) == dict:
                self.dfs(value, depth + 1)

    def print_depth(self, dictionary):
        if not isinstance(dictionary, dict):
            error_message = 'Data type of parameter is incorrect. It should be a dictionary'
            raise TypeError(error_message)

        # print("Input dictionary: {}".format(dictionary))

        self.dfs(dictionary, 1)
        return self.answer


class Person:
    def __init__(self, name, father=None):
        self.name = name
        self.father = father


if __name__ == '__main__':
    solution = Solution2()

    father = Person('Mr X')
    person = Person('Mr Y', father)
    input_dictionary = {
        'person': person,
        'address': 'Dhaka'
    }

    answer = solution.print_depth(input_dictionary)
    for value in answer:
        print(value[0], value[1])
