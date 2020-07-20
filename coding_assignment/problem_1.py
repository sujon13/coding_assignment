
# list to hold the answer
answer = []


def dfs(dictionary, depth):
    for key, value in dictionary.items():
        answer.append((key, depth))

        if type(value) == dict:
            dfs(value, depth + 1)


def print_depth(dictionary):
    print("Input dictionary:")
    print(dictionary)

    dfs(dictionary, 1)
    print("Output: ")
    for value in answer:
        print(value[0], value[1])

di = {
    'name': 'sujon',
    'key1': {
        'name': 'aaa',
        'age': 10
    }
}
print_depth(di)
