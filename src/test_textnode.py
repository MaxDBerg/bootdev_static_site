import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold", "http://www.url.url")
        node2 = TextNode("This is a text node", "bold", "http://www.url.url")
        self.assertEqual(node, node2)

    def test_eq_empty_url(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold", "http://www.url.url")
        self.assertNotEqual(node, node2)

    def test_eq_empty_text_type(self):
        node = TextNode("This is a text node", None, "http://www.url.url")
        node2 = TextNode("This is a text node", "bold", "http://www.url.url")
        self.assertNotEqual(node, node2)

    def test_eq_empty_text(self):
        node = TextNode(None, "bold", "http://www.url.url")
        node2 = TextNode("This is a text node", "bold", "http://www.url.url")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()
