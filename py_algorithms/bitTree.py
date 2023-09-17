class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


#递归方法
#递归方法是最简单的方式之一，它通过递归函数来遍历二叉树。
def preorderTraversal(root):
    if root is None:
        return []

    result = []
    result.append(root.value)  # 访问当前节点
    result += preorderTraversal(root.left)  # 递归遍历左子树
    result += preorderTraversal(root.right)  # 递归遍历右子树

    return result


#迭代方法
#迭代方法使用栈数据结构来模拟递归的过程，这是一种非递归的实现方式。
def preorderTraversal_1(root):
    if root is None:
        return []

    result = []
    stack = [root]

    while stack:
        node = stack.pop()  # 弹出栈顶节点
        result.append(node.value)  # 访问当前节点

        # 注意顺序，因为栈是先入后出的，所以右子树先入栈，左子树后入栈
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

    return result

if __name__ == '__main__':
    # 创建一个示例二叉树
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    # 进行前序遍历
    result = preorderTraversal_1(root)
    print(result)  # 输出 [1, 2, 4, 5, 3]
