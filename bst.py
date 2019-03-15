class Node:
    def __init__(self, data):
        self.right = None
        self.left = None
        self.data = data
        self.height = 1
        
class Tree:
    def __init__(self):
        self.root = None
        self.len = 0
        
    def insert(self, data):
        if self.root:
            self.root = self.insert_node(self.root, data)
        else:
            self.root = Node(data)
        self.len += 1
            
    def insert_node(self, node, data):
        if node:
            if data < node.data:
                node.left = self.insert_node(node.left, data)
            else:
                node.right = self.insert_node(node.right, data)

        else:
            return Node(data)
            
        node.height = 1 + max(self.getHeight(node.left), 
                        self.getHeight(node.right))
        
        balance = self.getBalance(node)
        
        if balance > 1 and data < node.left.data: 
            return self.rightRotate(node)
        
        if balance < -1 and data > node.right.data: 
            return self.leftRotate(node)
        
        
        if balance > 1 and data > node.left.val: 
            node.left = self.leftRotate(node.left) 
            return self.rightRotate(node) 

        # Case 4 - Right Left 
        if balance < -1 and data < node.right.val: 
            node.right = self.rightRotate(node.right) 
            return self.leftRotate(node) 

        return node  
            
            
    def getHeight(self, root): 
        if not root: 
            return 0

        return root.height 
    
    def getBalance(self, root): 
        if not root: 
            return 0

        return self.getHeight(root.left) - self.getHeight(root.right)
    
    def leftRotate(self, z): 

        y = z.right 
        T2 = y.left 

        # Perform rotation 
        y.left = z 
        z.right = T2 

        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                        self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                        self.getHeight(y.right)) 

        # Return the new root 
        return y 

    def rightRotate(self, z): 

        y = z.left 
        T3 = y.right 

        # Perform rotation 
        y.right = z 
        z.left = T3 

        # Update heights 
        z.height = 1 + max(self.getHeight(z.left), 
                        self.getHeight(z.right)) 
        y.height = 1 + max(self.getHeight(y.left), 
                        self.getHeight(y.right)) 

        # Return the new root 
        return y
    
    def delete(self, data):
        self.root, found = self.deleteNode(self.root, data)
        if found: self.len += 1
        return found
    
    def deleteNode(self, root, key):
        if root is None: 
            return root, False 
        
        if key < root.data: 
            root.left, found = self.deleteNode(root.left, key) 
            
        elif(key > root.data): 
            root.right, found = self.deleteNode(root.right, key)
            
        else: 
        
        # Node with only one child or no child 
            if root.left is None : 
                temp = root.right 
                root = None
                return temp, True 
            
            elif root.right is None : 
                temp = root.left 
                root = None
                return temp, True 

        # Node with two children: Get the inorder successor 
        # (smallest in the right subtree) 
            temp = self.minValueNode(root.right) 

        # Copy the inorder successor's content to this node 
            root.data = temp.data 

        # Delete the inorder successor 
            root.right, found = self.deleteNode(root.right , temp.data) 


        return root, found
    
    def minValueNode(self, node): 
        current = node 

    # loop down to find the leftmost leaf 
        while(current.left is not None): 
            current = current.left 

        return current 
            
#tree = Tree()
#tree.insert(10)
#tree.insert(20)
#tree.insert(100)
#print(tree.delete(30))
#pass
        
