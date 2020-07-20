
# list to hold the answer
answer = []


def dfs(dictionary, depth):
    for key, value in dictionary.items():
        answer.append((key, depth))

        # converting object to dictionary
        if hasattr(value, '__dict__'):
            value = value.__dict__

        if type(value) == dict:
            dfs(value, depth + 1)


def print_depth(dictionary):
    print("Input dictionary:")
    print(dictionary)

    dfs(dictionary, 1)
    print("Output: ")
    for value in answer:
        print(value[0], value[1])


class Person:
    def __init__(self, name, age, father=None):
        self.name = name
        self.age = age
        self.father = father


father = Person("shahjahan", 60)
ob = Person("sujon", 10, father)

di = {
    'key1': 'value1',
    'key2': {
        'key3': 1,
        'key4': {
            'key5': 5,
            'key6': ob
        }
    }
}
print_depth(di)
