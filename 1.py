class Node:
    def __init__(self,value):
        self.left = None
        self.data = value
        self.right = None

class BST:
    def __init__(self):
        self.root = None

    def insert(self,new_node):
        if self.root is None:
            self.root = new_node
        else:
            temp = self.root
            while True:
                if new_node.data < temp.data:
                    if temp.left is None:
                        temp.left = new_node
                        return
                    else:
                        temp = temp.left
                else:
                     if temp.right is None:
                         temp.right = new_node
                         return
                     else:
                         temp = temp.right

    def inorder(self,rt):
        if rt is None:
            return 
        else:
            self.inorder(rt.left)
            print(rt.data,end=" ")
            self.inorder(rt.right)

    def preorder(self,rt):
        if rt is None:
            return
        else:
            print(rt.data,end=" ")
            self.preorder(rt.left)
            self.preorder(rt.right)

    def postorder(self,rt):
        if rt is None:
            return
        else:
            self.postorder(rt.left)
            self.postorder(rt.right)
            print(rt.data,end=" ")

    def count_nodes(self,rt):
        if rt is None:
            return 0
        else:
          return 1 + self.count_nodes(rt.left) + self.count_nodes(rt.right)

    def count_nonleaf(self,rt):
        if rt is None:
            return 0 
        else:
            if rt.left is None and rt.right is None:
                    return 0
            return 1 +self.count_nonleaf(rt.left) + self.count_nonleaf(rt.right)

    def count_leaf(self,rt):
        if rt is None:
            return 0
        else:
            if rt.left is None and rt.right is None:
                return 1
            return self.count_leaf(rt.left) + self.count_leaf(rt.right)
        
    def findminmax(self):
        if self.root is None:
            print("Tree is empty")
            return
        temp = self.root
        while temp.left:
            temp = temp.left
        print("\nMin:",temp.data)

        temp = self.root
        while temp.right:
            temp = temp.right
        print("\nMax",temp.data)

b1=BST()
b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(65))
b1.insert(Node(4))
b1.insert(Node(50))
b1.insert(Node(450))
b1.insert(Node(500))

print("\n Inorder:")
b1.inorder(b1.root)

print("\n Preorder:")
b1.preorder(b1.root)

print("\n Postorder:")
b1.postorder(b1.root)

print("\nTotal Nodes:",b1.count_nodes(b1.root))
print("\nLeaf Nodes:",b1.count_leaf(b1.root))
print("\nNon-leaf Nodes:",b1.count_nonleaf(b1.root))

b1.findminmax()