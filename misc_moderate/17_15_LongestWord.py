#  Longest Word: Given a list of words, write a program to find the longest word made of other words
# in the list.
# EXAMPLE
# lnput:cat, banana, dog, nana, walk, walker, dogwalker
# Output: dogwalker


from trie import trie

arr = ['cat', 'banana', 'dog', 'nana', 'walk', 'walker', 'dogwalker']
# arr = ['dog', 'walker']
a = trie.fromList(arr)
# a.printTrie(None)
a.levelOrderTraversal()
# print(a.searchInTrie('banana'))
# print(a.root.alphabet)
# a.addToTrie('shook')
# print(a.root.alphabet)
# print([x.alphabet for x in a.root.children if x.alphabet == 'a' and x != 0])
print([x.alphabet for x in a.root.children if x != 0])

print(a.root.alphabet)
a.addToTrie('shook')
print(a.root.alphabet)

print([x.alphabet for x in a.root.children if x != 0])
children = [x for x in a.root.children if x != 0]
c = children[0]
print([x.alphabet for x in c.children if x != 0])


