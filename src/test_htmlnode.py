import unittest

from htmlnode import HTMLNode

class TestHTMLNode(unittest.TestCase):
    def test_props_to_html_1(self):
        node = HTMLNode(
            "a",
            "some random value",
            None,
            dict([("href", "https://www.google.com"), ("target", "_blank")])
        )
        node_props_to_html = node.props_to_html()
        self.assertEqual(
            node_props_to_html,
            ' href="https://www.google.com" target="_blank"'
        )

    def test_props_to_html_2(self):
        node = HTMLNode(
            "a",
            "some random value",
            None,
            dict([("href", "https://www.google.com")])
        )
        node_props_to_html = node.props_to_html()
        self.assertEqual(
            node_props_to_html,
            ' href="https://www.google.com"'
        )
    
    def test_props_to_html_3(self):
        node = HTMLNode(
            "a",
            "some random value",
            None,
            dict([("href", "https://www.google.com"), ("target", "_blank"), ("target2", "_blank"), ("target3", "_blank")])
        )
        node_props_to_html = node.props_to_html()
        self.assertEqual(
            node_props_to_html,
            ' href="https://www.google.com" target="_blank" target2="_blank" target3="_blank"'
        )

if __name__ == "__main__":
    unittest.main()
