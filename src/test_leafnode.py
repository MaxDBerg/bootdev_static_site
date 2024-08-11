import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_eq_no_props(self):
        node = LeafNode("p", "This is some text")
        
        nodeHTML = node.to_html()
        nodeReference = "<p>This is some text</p>"
        
        self.assertEqual(nodeHTML,nodeReference)

    def test_eq_with_props(self):
        node = LeafNode("a", "This is some text", {"href": "http://www.url.url"})
        
        nodeHTML = node.to_html()
        nodeReference = '<a href="http://www.url.url">This is some text</a>'
        
        self.assertEqual(nodeHTML,nodeReference)

    def test_eq_no_tag(self):
        node = LeafNode(None, "This is some text", {"href": "http://www.url.url"})
        
        nodeHTML = node.to_html()
        nodeReference = 'This is some text'
        
        self.assertEqual(nodeHTML,nodeReference)

if __name__ == "__main__":
    unittest.main()
