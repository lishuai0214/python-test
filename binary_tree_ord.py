class BiTreeNode:
    def __init__(self, data):
        self.data = data
        self.lchild = None
        self.rchild = None

class CreateBiTree:
    """
    str_tree: 传入字符串
    return: 返回根结点
    """
    def __init__(self, str_tree):
        self.str_tree = str_tree

    def create_tree(self):
        l1 = list(self.str_tree)
        l1 = [None if i == '#' else i for i in l1] # 将#转为None
        nodes = [BiTreeNode(l1[i]) for i in range(len(l1))] # 初始化各个结点
        root = nodes[0]
        for i in range(len(l1)):
            if 2*i+2 > len(l1): # 循环到最后的右孩子结束
                break
            cur_node = nodes[i]
            if nodes[2*i+1].data:
                cur_node.lchild = nodes[2*i+1] # 当前结点的左孩子
            if nodes[2*i+2].data:
                cur_node.rchild = nodes[2*i+2] # 当前结点的右孩子
        return root

    def __call__(self):
        return self.create_tree()

def pre_order(root):
    # 前序排列
    if root:
        print(root.data, end=',')
        pre_order(root.lchild)
        pre_order(root.rchild)

def in_order(root):
    # 中序排列
    if root:
        in_order(root.lchild)
        print(root.data, end=',')
        in_order(root.rchild)

def post_order(root):
    # 后序排列
    if root:
        post_order(root.lchild)
        post_order(root.rchild)
        print(root.data, end=',')


a = CreateBiTree('ABCDE#F##G#####')
root = a() # 调用__call__方法
print('根结点为：', root.data)

pre_order(root)
print('')
in_order(root)
print('')
post_order(root)