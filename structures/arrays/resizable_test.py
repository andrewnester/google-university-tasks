import unittest
from .resizable import ResizableArray


class ResizableArrayTest(unittest.TestCase):
    def test_init_capacity(self):
        init_capacity = 4
        arr = ResizableArray(init_capacity)
        self.assertEqual(arr.capacity, init_capacity)
        self.assertEqual(len(arr), 0)

    def test_capacity_doubled(self):
        arr = ResizableArray(1)
        arr.append(1)
        self.assertEqual(arr.capacity, 1)

        arr.append(2)
        self.assertEqual(arr.capacity, 2)

        arr.append(3)
        self.assertEqual(arr.capacity, 4)
        arr.append(4)
        self.assertEqual(arr.capacity, 4)

        arr.append(5)
        self.assertEqual(arr.capacity, 8)

    def test_get(self):
        arr = ResizableArray(1)
        arr.append(1)
        self.assertEqual(arr[0], 1)

    def test_get_out_of_range(self):
        arr = ResizableArray(1)
        arr.append(1)

        with self.assertRaises(IndexError):
            value = arr[2]

    def test_set(self):
        arr = ResizableArray(4)
        arr.append(0)
        arr.append(1)
        arr.append(2)
        arr[1] = 2

        self.assertEqual(arr[0], 0)
        self.assertEqual(arr[1], 2)
        self.assertEqual(arr[2], 2)

    def test_set_out_of_range(self):
        arr = ResizableArray(4)

        with self.assertRaises(IndexError):
            arr[2] = 4


    def test_append(self):
        arr = ResizableArray(4)
        arr.append(0)
        arr.append(1)
        arr.append(2)
        arr.append(3)
        arr.append(4)

        self.assertEqual(len(arr), 5)

    def test_delete(self):
        arr = ResizableArray(4)
        arr.append(0)
        arr.append(1)
        arr.append(2)

        self.assertEqual(len(arr), 3)

        del arr[1]
        self.assertEqual(len(arr), 2)
        self.assertEqual(arr[0], 0)
        self.assertEqual(arr[1], 2)

        with self.assertRaises(IndexError):
            value = arr[2]

        arr.append(3)
        del arr[0]
        self.assertEqual(arr[0], 2)
        self.assertEqual(arr[1], 3)

    def test_delete_out_of_range(self):
        arr = ResizableArray(4)
        arr.append(0)

        with self.assertRaises(IndexError):
            del arr[2]

    def test_delete_edge_case(self):
        arr = ResizableArray(1)
        arr.append(1)

        del arr[0]
        self.assertEqual(len(arr), 0)
        self.assertEqual(arr.capacity, 1)

        arr.append(1)
        arr.append(2)
        arr.append(3)

        self.assertEqual(arr.capacity, 4)
        self.assertEqual(len(arr), 3)
        del arr[0]

        self.assertEqual(arr.capacity, 2)
        self.assertEqual(len(arr), 2)
        del arr[0]

        self.assertEqual(arr.capacity, 1)
        self.assertEqual(len(arr), 1)
        del arr[0]

        self.assertEqual(arr.capacity, 1)
