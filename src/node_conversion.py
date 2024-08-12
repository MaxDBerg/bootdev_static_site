from parentnode import ParentNode
from text_type_dicts import dict_text_type
from textnode import TextNode
from leafnode import LeafNode
from split_functions import (
    split_md_blocks,
    split_nodes_delimiter,
    split_nodes_image,
    split_nodes_link,
)


def text_node_to_html_node(text_node):
    if type(text_node) is not TextNode:
        raise Exception(
            f"TextNode can has to be of type TextNode: Type is {type(text_node)}"
        )
    if not dict_text_type.__contains__(text_node.text_type):
        raise Exception(f"Invalid text type: {text_node.text_type}")

    if dict_text_type.__contains__(text_node.text_type) and not [
        "image",
        "link",
    ].__contains__(text_node.text_type):
        return LeafNode(dict_text_type[text_node.text_type]["tag"], text_node.text)
    if text_node.text_type == "link":
        return LeafNode(
            dict_text_type[text_node.text_type]["tag"],
            text_node.text,
            {"href": text_node.url},
        )
    if text_node.text_type == "image":
        return LeafNode(
            dict_text_type[text_node.text_type]["tag"],
            None,
            [{"src": text_node.url}, {"alt": text_node.text}],
        )


def text_to_textnode(text):
    if type(text) is not str:
        raise TypeError("Type of text has to be string")
    new_nodes = [TextNode(text, "text")]
    for k, v in dict_text_type.items():
        if ["text", "image", "link"].__contains__(k):
            continue
        else:
            new_nodes = split_nodes_delimiter(new_nodes, v["delimiter"])

    text_nodes = split_nodes_image(split_nodes_link(new_nodes))
    return text_nodes


def block_to_blocktype(block):
    if type(block) is not str:
        raise TypeError("Type of text has to be string")
    if block.startswith("#") and len(block.split(" ")[0]) <= 6:
        return "heading"
    elif block.startswith("```") and block.endswith("```"):
        return "code"
    elif all([block_line.startswith(">") for block_line in block.splitlines()]):
        return "quote"
    elif all(
        [
            block_line.startswith("* ") or block_line.startswith("- ")
            for block_line in block.splitlines()
        ]
    ):
        return "unordered_list"
    elif all(
        [
            block_line.startswith(f"{index + 1}. ")
            for index, block_line in enumerate(block.splitlines())
        ]
    ):
        return "ordered_list"
    return "paragraph"


def markdown_to_htmlnode(markdown):
    if type(markdown) is not str:
        raise TypeError("Type of markdown has to be string")
    nodes = []
    blocks = split_md_blocks(markdown)

    for block in blocks:
        nodes.append(block_to_htmlnode(block))

    return ParentNode(nodes, "div")


def block_to_htmlnode(block: str):
    blocktype = block_to_blocktype(block)
    nodes = []
    if blocktype == "heading":
        heading_tag = len(block.split(" ")[0])
        for textnode in text_to_textnode(block.removeprefix("#" * heading_tag + " ")):
            nodes.append(text_node_to_html_node(textnode))
        return ParentNode(nodes, "h" + str(heading_tag))
    elif blocktype == "code":
        for textnode in text_to_textnode(
            block.removeprefix("```\n").removesuffix("\n```")
        ):
            nodes.append(text_node_to_html_node(textnode))
        return ParentNode([ParentNode(nodes, "code")], "pre")
    elif blocktype == "quote":
        block_trimmed = ""
        for index, quote_line in enumerate(block.splitlines()):
            if index is len(block.splitlines()) - 1:
                block_trimmed += quote_line.removeprefix("> ")
            else:
                block_trimmed += quote_line.removeprefix("> ") + "\n"
        for textnode in text_to_textnode(block_trimmed):
            nodes.append(text_node_to_html_node(textnode))
        return ParentNode(nodes, "blockquote")
    elif blocktype == "unordered_list":
        list_items = []
        for list_item in block.splitlines():
            for textnode in text_to_textnode(
                list_item.removeprefix("- ").removeprefix("* ")
            ):
                htmlnode = text_node_to_html_node(textnode)
                nodes.append(htmlnode)
            list_items.append(ParentNode(nodes, "li"))
            nodes = []
        return ParentNode(list_items, "ul")
    elif blocktype == "ordered_list":
        list_items = []
        for index, list_item in enumerate(block.splitlines()):
            for textnode in text_to_textnode(
                list_item.removeprefix(str(index + 1) + ". ")
            ):
                htmlnode = text_node_to_html_node(textnode)
                nodes.append(htmlnode)
            list_items.append(ParentNode(nodes, "li"))
            nodes = []
        return ParentNode(list_items, "ol")
    else:
        block_trimmed = ""
        for index, line in enumerate(block.splitlines()):
            if index is len(block.splitlines()) - 1:
                block_trimmed += line
            else:
                block_trimmed += line + "\n"
        for textnode in text_to_textnode(block_trimmed):
            nodes.append(text_node_to_html_node(textnode))
        return ParentNode(nodes, "p")
