class BST:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

    def insert (self,value):
        currentnode = self
        while True:
            if value < currentnode.value:
                if currentnode.left = None:
                    currentnode.left = BST(value)
                    break
                else:
                    currentnode = currentnode.left
            else:
                if currentnode.right = None:
                    currentnode.right = BST(value)
                    break
                else: 
                    currentnode = currentnode.right
        return self
    
    def contain (self, value):
        currentnode = self
        while currentnode is not None:
            if value < currentnode.value:
                currentnode = currentnode.left
            elif value > currentnode.value:
                currentnode = currentnode.right
            else:
                return True
        return False



