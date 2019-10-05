def merge(nums1, m, nums2, n):
    index = len(nums1) - 1
    u, v = m - 1, n - 1

    while v >= 0:
        if u == -1:
            copy_remaining(nums1, nums2, index, v)
            return

        if nums1[u] > nums2[v]:
            nums1[index] = nums1[u]
            u -= 1
        else:
            nums1[index] = nums2[v]
            v -= 1
        index -= 1


def copy_remaining(nums1, nums2, index, v):
    while v >= 0:
        nums1[index] = nums2[v]
        index -= 1
        v -= 1

        
# much cleaner code
'''
n1_pointer = m-1
n2_pointer = n-1

n1_tail = len(nums1) - 1
while n1_pointer >= 0 and n2_pointer >= 0:
    num_one = nums1[n1_pointer]
    num_two = nums2[n2_pointer]
    if num_one > num_two:
        nums1[n1_tail] = num_one
        n1_pointer -= 1
    else:
        nums1[n1_tail] = num_two
        n2_pointer -= 1
    n1_tail -= 1

nums1[0:n2_pointer+1] = nums2[0:n2_pointer+1]
'''

# tests
import unittest
class TestCheckNumEquality(unittest.TestCase):
    def test_addition(self):
        nums1 = [1, 2, 3, 0, 0, 0]
        nums2 = [4, 5, 6]
        merge(nums1, 3, nums2, 3)
        self.assertEqual(nums1, [1, 2, 3, 4, 5, 6])

        nums1 = [1, 3, 5, 0, 0, 0]
        nums2 = [2, 4, 6]
        merge(nums1, 3, nums2, 3)
        self.assertEqual(nums1, [1,2,3,4,5,6])


        nums1 = [7,8,0,0,0,0]
        nums2 = [2,3,4,5]
        merge(nums1, 2, nums2, 4)
        self.assertEqual(nums1, [2,3,4,5,7,8])


        nums1 = [1,0]
        nums2 = [0]
        merge(nums1, 1, nums2, 1)
        self.assertEqual(nums1, [0,1])


        nums1 = [0]
        nums2 = [5]
        merge(nums1, 0, nums2, 1)
        self.assertEqual(nums1, [5])

        nums1 = [1]
        nums2 = []
        merge(nums1, 1, nums2, 0)
        self.assertEqual(nums1, [1])

        nums1 = []
        nums2 = []
        merge(nums1, 0, nums2, 0)
        self.assertEqual(nums1,  [])

unittest.main()
