# Coding Assignment #
## How to run locally ##
You need to follow below steps

0. Assumed python is already installed. Otherwise please install it.
1. Type ` git clone <copied url> `
2. Then ` cd coding_assignment`
3. For running all unit test together type`python -m unittest discover -s tests` 
4. For running individual solution type `cd coding_assignment` and then `python <file_name>`

## Runtime and Memory  Requirement ##

## Problem 1 ##
**Runtime**
`If n = number of keys in inpuit dictionary
Then  Runtime is O(n) .` 

Because here key(main) function is a dfs call. It will run once for each dictionary key.

**Memory**
`Like runtime if n = number of keys in inpuit dictionary
Then memory requirement is also O(n) .`

Because each key and its depth are stored in a list (`answer variable`).
Dfs also takes `O(depth of dictionary)` memory. 
So total memory is `  O(n) + O(depth of dictionary) .`
As total number of keys are larger than depth of dictionary, in big O notation overall memory is `O(n) .`

## Problem 2 ##

If we assume python object as dictionary then runtime and memory complexity will be same as Problem 1.
The reason of it is ultimately we need to convert object to dictionary.

**Runtime**
`If n = number of keys in inpuit dictionary
Then  Runtime is O(n) .` 

Because here key(main) function is a dfs call. It will run once for each dictionary key. But one more thing needs to be considered.
During dfs call we also need to convert object to dictionary for key which is a python object but it is not significant compared to total number of keys in dictionary. In spite of considering it overall time will be ` O(2n)` which is equivalent`O(n)` in terms of big O notation.

**Memory**
`Like runtime if n = number of keys in inpuit dictionary
Then memory requirement is also O(n) `

Because each key and its depth are stored in a list (`answer variable`).
Dfs also takes `O(depth of dictionary)` memory. 
So total memory is `  O(n) + O(depth of dictionary) .`
As total key is larger than depth of dictionary so in big O notation overall memory is` O(n)  .`

## problem 3 ##

**Runtime**

Let assume ` h = height of the tree `

Here we can divide it by four parts
1. `get_distance_from_root()` It is called two times. Each time it needs atmost `O(h)` time.
2.  `swap two variables` It is also called two times. Each of which takes `O(1)` time.
3. `Ensure that two nodes are in same level`. It takes `O(h)` time.
4. `get_lca_of_two_same_leveled_node()` It is called one time and it takes `O(h)` time.

so total time complexity is ` (O(h) * 2) + (O(1) * 2) + O(h) + O(h)   = O(h) ` 

**Memory**

Here only some temporary variables have been used. Each of which requires `O(1)` memory.

so overall memory requirement is `O(1) .`
