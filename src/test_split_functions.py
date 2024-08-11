import unittest
from textnode import TextNode
from split_functions import (
    split_md_blocks,
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
)


class TestSplitNodeFunctions(unittest.TestCase):
    # Text Split by Delimiter
    def test_delimiter_eq_split_code_delimiter(self):
        node = TextNode("`code` This is text and this is `code`", "text")
        node_comparison = [
            TextNode("code", "code", None),
            TextNode(" This is text and this is ", "text", None),
            TextNode("code", "code", None),
        ]
        split_nodes = split_nodes_delimiter([node], "`")
        self.assertEqual(split_nodes, node_comparison)

    def test_delimiter_eq_split_no_delimiter(self):
        node = TextNode("This is text and this is", "text")
        node_comparison = [TextNode("This is text and this is", "text")]
        split_nodes = split_nodes_delimiter([node], None)
        self.assertEqual(split_nodes, node_comparison)

    def test_delimiter_raises_missing_list_wrapper(self):
        node = TextNode("This is text and this is", "text")
        with self.assertRaises(TypeError):
            split_nodes_delimiter(node, None)

    # Text Split by image
    def test_image_eq_split(self):
        nodes = [
            TextNode(
                "This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
                "text",
            )
        ]
        nodes_comparison = [
            TextNode("This is text with a link ", "text", None),
            TextNode("to boot dev", "image", "https://www.boot.dev"),
            TextNode(" and ", "text", None),
            TextNode("to youtube", "image", "https://www.youtube.com/@bootdotdev"),
        ]
        split_nodes = split_nodes_image(nodes)
        self.assertEqual(split_nodes, nodes_comparison)

    def test_image_eq_split_without_images(self):
        nodes = [
            TextNode(
                "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
                "text",
            )
        ]
        split_nodes = split_nodes_image(nodes)
        self.assertEqual(split_nodes, nodes)

    # Text Split by link
    def test_link_eq_split(self):
        nodes = [
            TextNode(
                "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
                "text",
            )
        ]
        nodes_comparison = [
            TextNode("This is text with a link ", "text", None),
            TextNode("to boot dev", "link", "https://www.boot.dev"),
            TextNode(" and ", "text", None),
            TextNode("to youtube", "link", "https://www.youtube.com/@bootdotdev"),
        ]
        split_nodes = split_nodes_link(nodes)
        self.assertEqual(split_nodes, nodes_comparison)

    def test_link_eq_split_without_links(self):
        nodes = [
            TextNode(
                "This is text with a link ![to boot dev](https://www.boot.dev) and ![to youtube](https://www.youtube.com/@bootdotdev)",
                "text",
            )
        ]
        split_nodes = split_nodes_link(nodes)
        self.assertEqual(split_nodes, nodes)

    # Text Split by link
    def test_block_eq_split(self):
        blocks = split_md_blocks(
            "# This is a heading\n\nThis is a paragraph of text. It has some **bold** and *italic* words inside of it.\n\n* This is the first list item in a list block\n* This is a list item\n* This is another list item"
        )
        block_comparison = [
            "# This is a heading",
            "This is a paragraph of text. It has some **bold** and *italic* words inside of it.",
            "* This is the first list item in a list block\n* This is a list item\n* This is another list item",
        ]
        self.assertListEqual(blocks, block_comparison)

    def test_block_raises_wrong_type(self):
        with self.assertRaises(TypeError):
            split_md_blocks([])


if __name__ == "__main__":
    unittest.main()
