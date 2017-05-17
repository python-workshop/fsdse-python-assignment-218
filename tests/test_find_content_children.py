from unittest import TestCase


class TestFind_content_children(TestCase):
    def test_find_content_children(self):
        try:
            from build import find_content_children
        except ImportError:
            self.assertFalse("no function found")

        self.assertRaises(TypeError, find_content_children, None, None)
        self.assertEqual(find_content_children([1, 2, 3],
                                                    [1, 1]), 1)
        self.assertEqual(find_content_children([1, 2],
                                                    [1, 2, 3]), 2)
        self.assertEqual(find_content_children([7, 8, 9, 10],
                                                    [5, 6, 7, 8]), 2)
