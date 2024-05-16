class Treenode:
    def __init__(self, data):
        self.data=data
        self.l = None
        self.r = None



def insert(root,data):
    if root == None:
        root = Treenode(data)
        return root
    if data < root.data:
        root.l = insert(root.l, data)
    else:
        root.r = insert(root.r, data)
    return root

def display_inorder(root):
    if root != None:
        display_inorder(root.l)
        print(root.data)
        display_inorder(root.r)
        
def display_preorder(root):
    if root != None:
        print(root.data)
        display_preorder(root.l)
        display_preorder(root.r)
        
        
def display_postorder(root):
    if root != None:
        display_postorder(root.l)
        display_postorder(root.r)
        print(root.data)
                
def bstsearch(root, key):
    if root == None:
        return -1
    if key == root.data:
        return root
    if key < root.data:
        return bstsearch(root.l,key)
    else:
        return bstsearch(root.r,key)




       
r = Treenode(50)
r = insert(r, 30)
r = insert(r, 20)
r = insert(r, 40)
r = insert(r, 70)
r = insert(r, 60)
r = insert(r, 80)
print("Inorder:")
display_inorder(r)
print("Preorder:")
display_preorder(r)
print("Postorder:")
display_postorder(r)

search = bstsearch(r,70)
print(search)