class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def __eq__(self, other):
        return self.same_tree(self, other)

    def same_tree(self,p,q):
        if not p and not q: return True
        if not p or not q: return False
        if p.val != q.val: return False

        return self.same_tree(p.left, q.left) and self.same_tree(p.right, q.right)

def convert_array_to_bt_level_order_fashion(arr):
    return convert_array_to_bt_level_order_fashion_recursive(arr, None, 0, len(arr))

def convert_array_to_bt_level_order_fashion_recursive(arr, root, index, length):
    if index < length:
        elem = arr[index]

        if elem is None:
            return None
        else:
            temp = TreeNode(elem)
            root = temp

        root.left = convert_array_to_bt_level_order_fashion_recursive(arr, root.left, (index * 2) + 1, length)
        root.right = convert_array_to_bt_level_order_fashion_recursive(arr, root.right, (index * 2) + 2, length)

    return root

# tests
import unittest
class TestArrayToBinraryTree(unittest.TestCase):
    one = TreeNode(1)
    three = TreeNode(3)
    four = TreeNode(4)
    eight = TreeNode(8)
    eleven = TreeNode(11)
    seventeen = TreeNode(17)
    eighteen = TreeNode(18)

    def test_init(self):
        self.one.left = self.three.left = self.four.left = self.eight.left = self.eleven.left = self.seventeen.left = self.eighteen.left = None
        self.one.left = self.three.right = self.four.right = self.eight.right = self.eleven.right = self.seventeen.right = self.eighteen.right = None


    def test_addition(self):
        # general case (fully balanced)
        self.test_init()
        self.one.left, self.one.right = self.three, self.seventeen
        self.three.left, self.three.right = self.four, self.eight
        self.seventeen.left, self.seventeen.right = self.eleven, self.eighteen

        test_one_arr = [1, 3, 17, 4, 8, 11, 18]
        self.assertTrue(convert_array_to_bt_level_order_fashion(test_one_arr) == self.one)

        # case where leafs are at different levels
        self.test_init()
        self.one.left, self.one.right = self.three, self.seventeen
        self.three.left = self.four
        self.four.right = self.eight

        test_two_arr = [1, 3, 17, 4, None, None, None, None, 8]
        self.assertTrue(convert_array_to_bt_level_order_fashion(test_two_arr) == self.one)

        # case where binary tree is linear (only right childs)
        self.test_init()
        self.one.right = self.four
        self.four.right = self.seventeen
        self.seventeen.right = self.eighteen

        test_three_arr = [1, None, 4, None, None, None, 17, None, None, None, None, None, None, None, 18]
        self.assertTrue(convert_array_to_bt_level_order_fashion(test_three_arr) == self.one)

        # case where binary tree is singleton
        self.test_init()
        test_four_arr = [17]
        self.assertTrue(convert_array_to_bt_level_order_fashion((test_four_arr)) == self.seventeen)

        # edge case -- empty list
        self.test_init()
        self.assertTrue(convert_array_to_bt_level_order_fashion([]) is None)

unittest.main()