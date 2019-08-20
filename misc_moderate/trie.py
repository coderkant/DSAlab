
class Node:
    # children = [0] * 26  Nope. Big Mistake.
    def __init__(self,alphabet,isterminal):
        self.alphabet = alphabet
        self.isTerminal = isterminal
        self.children = [0] * 26    # Yep. Better

    def addChild(self,Node):
        alphabet = Node.alphabet
        self.children[ord(alphabet) - ord('a')] = Node

class trie():
    root= None
    def __init__(self,root):
        self.root = root


    @classmethod
    def fromList(self,arr):
        root = Node('root',False)
        tr = trie(root)
        for word in arr:
            # print(word)
            tr.addToTrie(word)
        return tr

    def addToTrie(self,word):
        curNode = self.root
        added = False
        for i in range(0,len(word)):
            char = word[i]
            index = ord(char) - ord('a')
            # print(curNode.alphabet,char)
            if curNode.children[index] ==0:
                newNode = Node(char,i==len(word)-1)
                curNode.addChild(newNode)
                added = True
            elif i==len(word)-1 and not curNode.children[index].isTerminal:
                curNode.children[index].isTerminal = True
                added = True
            curNode = curNode.children[index]
        # print('---')
        return added

    def searchInTrie(self,word):
        curNode = self.root
        for i in range(0,len(word)):
            char = word[i]
            index = ord(char) - ord('a')
            # print(i == len(word) - 1, curNode.alphabet,curNode.children[index].isTerminal)
            if curNode.children[index] ==0:
                return False
            elif i==len(word)-1 and not curNode.children[index].isTerminal:
                return False
            curNode = curNode.children[index]
        return True

    def printTrie(self, node: Node):
        if node==None:
            node = self.root
        self.__printPathToLeaves__(node,[])

    def __printPathToLeaves__(self,node: Node,pathSoFar):
        # print(node.alphabet,pathSoFar)
        pathSoFar.append(node.alphabet)
        children = [x for x in node.children if x != 0]
        print(node.alphabet +' : '+','.join([x.alphabet for x in children]))
        if node.isTerminal:
            print('->'.join(pathSoFar))
            print([x.alphabet for x in children])
        if children != []:
            for child in children:
                print('call params: '+child.alphabet+' / '+','.join(pathSoFar))
                self.__printPathToLeaves__(child,pathSoFar)
        else:
            print('endofline')
            return

    def levelOrderTraversal(self):
        queue=[self.root,Node('eol',False)]
        while(queue!=[]):
            curNode = queue[0]
            queue = queue[1:]
            children = [x for x in curNode.children if x != 0]
            queue.extend(children)
            level = []
            while(curNode.alphabet != 'eol'):
                level.append(curNode)
                curNode = queue[0]
                queue = queue[1:]
                children = [x for x in curNode.children if x != 0]
                queue.extend(children)
            queue.append(Node('eol',False))
            print(','.join([x.alphabet for x in level]))
            print('---')
            # children = [x for x in curNode.children if x != 0]
            # queue.append(Node('eol',False))
            # queue.extend(children)
            # for q in queue:



root = Node('root',False)
a = Node('a',True)
c = Node('c',False)
z= Node('z',False)
root.addChild(a)
root.addChild(c)
root.addChild(z)
a.addChild(Node('t',False))
tr = trie(root)
# print([x.alphabet for x in tr.root.children if x != 0])