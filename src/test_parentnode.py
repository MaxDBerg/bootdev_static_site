import unittest

from leafnode import LeafNode

from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_eq_only_leafnode_children(self):
        node = ParentNode(
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            "p",
        )
        nodeHTML = node.to_html()
        nodeReference = (
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        )
        self.assertEqual(nodeHTML, nodeReference)

    def test_eq_with_nested_parentnode(self):
        node = ParentNode(
            [
                ParentNode([LeafNode("b", "Bold text")], "p"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
            "p",
        )
        nodeHTML = node.to_html()
        nodeReference = (
            "<p><p><b>Bold text</b></p>Normal text<i>italic text</i>Normal text</p>"
        )
        self.assertEqual(nodeHTML, nodeReference)

    def test_eq_no_children(self):
        node = ParentNode(None, "a")
        with self.assertRaises(ValueError):
            node.to_html()

    def test_eq_no_tag(self):
        node = ParentNode([LeafNode("b", "Bold text")], None)
        with self.assertRaises(ValueError):
            node.to_html()


if __name__ == "__main__":
    unittest.main()
