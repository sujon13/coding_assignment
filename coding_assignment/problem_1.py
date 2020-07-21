class Solution1(object):
    def __init__(self):
        # answer will ne a list where every element will be a tuple of key and depth like ('key': 1)
        self.answer = []

    def dfs(self, dictionary, depth):
        for key, value in dictionary.items():
            self.answer.append((key, depth))

            if type(value) == dict:
                self.dfs(value, depth + 1)

    def print_depth(self, dictionary):
        if not isinstance(dictionary, dict):
            error_message = 'Data type of parameter is incorrect. It should be a dictionary'
            raise TypeError(error_message)

        print("Input dictionary: {}".format(dictionary))

        self.dfs(dictionary, 1)
        return self.answer


if __name__ == '__main__':
    solution = Solution1()
    input_dictionary = {
        'key1': 1,
        'key2': 2,
        'key3': {
            'key4': 4,
            'key5': 5,
        },
        'key6': 6
    }

    answer = solution.print_depth(input_dictionary)
    for value in answer:
        print(value[0], value[1])
