from BinaryTree import BinaryTree
import random


def main():
    bt = BinaryTree()
    dataSet = set([])
    # values = ['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H']
    values = [25, 15, 40, 10, 20, 30, 50, 18, 22, 27, 45, 60, 42, 47, 49]
    for r in range(random.randint(7, 12)):
        n = random.randint(1, 100)
        dataSet.add(n)

    print ("Inserting into Binary Tree: ")
    # for data in dataSet:
    for data in values:
        bt.insert(data)
        print (data, sep=" ", end=" ")
    print ()

    print ("Inorder: ")
    bt.inorder()
    print ("Preorder: ")
    bt.preorder()
    print ("postorder: ")
    bt.postorder()
    print ("Binary Tree Size: ", bt.size())
    print ("Max Depth: ", bt.maxdepth())
    print ("Min value in BST: ", bt.minvalue())
    print ("Max value in BST: ", bt.maxvalue())

    targetsums = [50, 78, 82, 97, 150]
    for target in targetsums:
        ans = bt.haspathsum(target)
        print ("Sum: %d in binary tree: %s" % (target, ans))

    print ("print all the root to leaf paths in binary tree")
    bt.printpaths()
    print ("Mirroring the binary tree: ")
    bt.mirror()
    bt.inorder()

    bt = BinaryTree()
    values = [2, 3, 1]
    print ("Inserting into Binary Tree: ")
    # for data in dataSet:
    for data in values:
        bt.insert(data)
        print (data, sep=" ", end=" ")
    print ()
    bt.inorder()
    print ("After doing double tree: ")
    bt.doubletree()
    bt.inorder()

    bt1 = BinaryTree()
    bt2 = BinaryTree()
    # values = ['F', 'B', 'A', 'D', 'C', 'E', 'G', 'I', 'H']
    values = [25, 15, 40, 10, 20, 30, 50, 18, 22, 27, 45, 60, 42, 47, 49]
    print ("Inserting into Binary Tree: ")
    # for data in dataSet:
    for data in values:
        bt1.insert(data)
        bt2.insert(data)
        print (data, sep=" ", end=" ")
    print ()
    bt1.inorder()
    bt2.inorder()
    comp = bt1.sametree(bt2)
    print ("Are the trees same: ", comp)
    print ("is bt1 BST: ", bt1.isbst1())
    print ("is bt2 BST: ", bt2.isbst1())
    bt2.mirror()
    print ("is bt2 BST after mirroring: ", bt2.isbst1())

    bt1 = BinaryTree()
    bt2 = BinaryTree()
    for data in values:
        bt1.insert(data)
        bt2.insert(data)
        print (data, sep=" ", end=" ")
    print ()
    print ("is bt1 BST (efficient version): ", bt1.isbst2())
    print ("is bt2 BST (efficient version): ", bt2.isbst2())
    bt2.mirror()
    print ("is bt2 BST after mirroring(efficient version): ", bt2.isbst2())

    for i in range(1,13):
        tot = bt.counttrees(i)
        print ("%d nodes: %d unique BSTs" % (i, tot))


if __name__ == '__main__':
    main()
