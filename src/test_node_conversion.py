import unittest
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextNode
from node_conversion import (
    block_to_blocktype,
    markdown_to_htmlnode,
    text_node_to_html_node,
    text_to_textnode,
)


class TestNodeConversion(unittest.TestCase):
    # TextNode to HTMLNode (LeafNode) conversions
    def test_eq_text_type(self):
        node = TextNode("This should only be text. No tags!", "text")
        node2 = LeafNode(None, "This should only be text. No tags!")
        converted_node = text_node_to_html_node(node)
        self.assertEqual(node2, converted_node)

    def test_eq_bold_type(self):
        node = TextNode("This text should be bold", "bold")
        node2 = LeafNode("b", "This text should be bold")
        converted_node = text_node_to_html_node(node)
        self.assertEqual(node2, converted_node)

    def test_eq_italic_type(self):
        node = TextNode("This text should be italic", "italic")
        node2 = LeafNode("i", "This text should be italic")
        converted_node = text_node_to_html_node(node)
        self.assertEqual(node2, converted_node)

    def test_eq_code_type(self):
        node = TextNode("This text should be code", "code")
        node2 = LeafNode("code", "This text should be code")
        converted_node = text_node_to_html_node(node)
        self.assertEqual(node2, converted_node)

    def test_eq_link_type(self):
        node = TextNode("This should be a link", "link", "http://www.url.url")
        node2 = LeafNode("a", "This should be a link", {"href": "http://www.url.url"})
        converted_node = text_node_to_html_node(node)
        self.assertEqual(node2, converted_node)

    def test_eq_image_type(self):
        node = TextNode("This should be an image", "image", "http://www.image.url")
        node2 = LeafNode(
            "img",
            None,
            [{"src": "http://www.image.url"}, {"alt": "This should be an image"}],
        )
        converted_node = text_node_to_html_node(node)
        self.assertEqual(node2, converted_node)

    # Text to TextNode conversions
    def test_eq_text_textnode(self):
        nodes = text_to_textnode(
            "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        )
        nodes_comparison = [
            TextNode("This is ", "text", None),
            TextNode("text", "bold", None),
            TextNode(" with an ", "text", None),
            TextNode("italic", "italic", None),
            TextNode(" word and a ", "text", None),
            TextNode("code block", "code", None),
            TextNode(" and an ", "text", None),
            TextNode("obi wan image", "image", "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", "text", None),
            TextNode("link", "link", "https://boot.dev"),
        ]
        self.assertEqual(nodes, nodes_comparison)

    # Block to BlockType
    def test_blocktype_heading(self):
        blocktype = block_to_blocktype("# This is a heading")
        self.assertEqual(blocktype, "heading")

    def test_blocktype_not_heading(self):
        blocktype = block_to_blocktype("####### This is a heading")
        self.assertEqual(blocktype, "paragraph")

    def test_blocktype_code(self):
        blocktype = block_to_blocktype("```This is some code```")
        self.assertEqual(blocktype, "code")

    def test_blocktype_not_code(self):
        blocktype = block_to_blocktype("```This is some code")
        self.assertEqual(blocktype, "paragraph")

    def test_blocktype_quote(self):
        blocktype = block_to_blocktype(
            ">This is a quote\n>This is a middle quote\n>This is another quote\n>This is the final quite"
        )
        self.assertEqual(blocktype, "quote")

    def test_blocktype_not_quote(self):
        blocktype = block_to_blocktype(
            ">This is a quote\n>This is a middle quote\n>This is another quote\nThis is the final quite"
        )
        self.assertEqual(blocktype, "paragraph")

    def test_blocktype_unordered_list(self):
        blocktype = block_to_blocktype(
            "- This is a list item\n* This is a middle list item\n- This is another list item\n* This is the final list item"
        )
        self.assertEqual(blocktype, "unordered_list")

    def test_blocktype_not_unordered_list(self):
        blocktype = block_to_blocktype(
            "- This is a quote\n>* This is a middle quote\n- This is another quote\nThis is the final quite"
        )
        self.assertEqual(blocktype, "paragraph")

    def test_blocktype_ordered_list(self):
        blocktype = block_to_blocktype(
            "1. This is a list item\n2. This is a middle list item\n3. This is another list item\n4. This is the final list item"
        )
        self.assertEqual(blocktype, "ordered_list")

    def test_blocktype_not_ordered_list(self):
        blocktype = block_to_blocktype(
            "1. This is a quote\n>2. This is a middle quote\n3. This is another quote\n5. This is the final quite"
        )
        self.assertEqual(blocktype, "paragraph")

    def test_blocktype_raises_not_str(self):
        with self.assertRaises(TypeError):
            block_to_blocktype([])

    # Markdown to HTMLNode
    def test_htmlnode_heading(self):
        markdown = "# This is a heading many wow\n\n###### This is another heading WOW"
        node_comparison = ParentNode(
            [
                ParentNode([LeafNode(None, "This is a heading many wow")], "h1"),
                ParentNode([LeafNode(None, "This is another heading WOW")], "h6"),
            ],
            "div",
        )
        node = markdown_to_htmlnode(markdown)
        self.assertEqual(node, node_comparison)

    def test_htmlnode_code(self):
        markdown = "```\nThis is a code snippet\n```"
        node_comparison = ParentNode(
            [
                ParentNode(
                    [
                        ParentNode([LeafNode(None, "This is a code snippet")], "code"),
                    ],
                    "pre",
                )
            ],
            "div",
        )
        node = markdown_to_htmlnode(markdown)
        self.assertEqual(node, node_comparison)

    def test_htmlnode_quote(self):
        markdown = "> This is a quote many wow\n> This is another quote WOW"
        node_comparison = ParentNode(
            [
                ParentNode(
                    [
                        LeafNode(
                            None, "This is a quote many wow\nThis is another quote WOW"
                        )
                    ],
                    "blockquote",
                ),
            ],
            "div",
        )
        node = markdown_to_htmlnode(markdown)
        self.assertEqual(node, node_comparison)

    def test_htmlnode_unordered_list(self):
        markdown = "- This is a list item many wow\n- This is another list item WOW"
        node_comparison = ParentNode(
            [
                ParentNode(
                    [
                        ParentNode(
                            [LeafNode(None, "This is a list item many wow")], "li"
                        ),
                        ParentNode(
                            [LeafNode(None, "This is another list item WOW")], "li"
                        ),
                    ],
                    "ul",
                )
            ],
            "div",
        )
        node = markdown_to_htmlnode(markdown)
        self.assertEqual(node, node_comparison)

    def test_htmlnode_ordered_list(self):
        markdown = "1. This is a list item many wow\n2. This is another list item WOW"
        node_comparison = ParentNode(
            [
                ParentNode(
                    [
                        ParentNode(
                            [LeafNode(None, "This is a list item many wow")], "li"
                        ),
                        ParentNode(
                            [LeafNode(None, "This is another list item WOW")], "li"
                        ),
                    ],
                    "ol",
                )
            ],
            "div",
        )
        node = markdown_to_htmlnode(markdown)
        self.assertEqual(node, node_comparison)


if __name__ == "__main__":
    unittest.main()
