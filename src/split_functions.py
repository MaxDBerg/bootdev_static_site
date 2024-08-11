from text_type_dicts import dict_text_type

from textnode import TextNode
from extract_inline_element import extract_markdown_images,extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter):
    new_nodes = []
    if not any([True for k,v in dict_text_type.items() if v["delimiter"] == delimiter]):
        raise ValueError("Not a valid delimiter " + f": {delimiter}")
    if not type(old_nodes) == list:
        raise TypeError("Type of old_nodes must be a list " + f": {type(old_nodes)}")
    if delimiter == None:
        return old_nodes
    for node in old_nodes:
        if not type(node) == TextNode:
            raise TypeError("Type of node must be TextNode " + f": {type(node)}")
        if not node.text_type == "text":
            new_nodes.append(node)
            continue
        for index, item in enumerate(node.text.split(delimiter)):
            if item == "":
                continue
            if index % 2 == 0:
                new_nodes.append(TextNode(item, "text"))
            else:
                for k,v in dict_text_type.items():
                    if v["delimiter"] == delimiter:
                        new_nodes.append(TextNode(item, k))
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    if not type(old_nodes) == list:
        raise TypeError("Type of old_nodes must be a list " + f": {type(old_nodes)}")
    for node in old_nodes:
        text_to_split = node.text
        if not type(node) == TextNode:
            raise TypeError("Type of node must be TextNode " + f": {type(node)}")
        if not node.text_type == "text":
            new_nodes.append(node)
            continue
        extracted_images = extract_markdown_images(node.text)
        if extracted_images == []:
            new_nodes.append(node)
            continue
        for index_extract, image in enumerate(extracted_images):
            alt = image[0]
            url = image[1]
            section = text_to_split.split(f"![{alt}]({url})", 1)
            if (section[0].strip(" ") != ""):
                new_nodes.append(TextNode(section[0], "text"))
            else:
                continue
            new_nodes.append(TextNode(alt, "image", url))
            text_to_split = section[1]
            if(index_extract == len(extracted_images) - 1 and section[1].strip(" ") != ""):
                new_nodes.append(TextNode(section[1], "text"))
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    if not type(old_nodes) == list:
        raise TypeError("Type of old_nodes must be a list " + f": {type(old_nodes)}")
    for node in old_nodes:
        text_to_split = node.text
        if not type(node) == TextNode:
            raise TypeError("Type of node must be TextNode " + f": {type(node)}")
        if not node.text_type == "text":
            new_nodes.append(node)
            continue
        extracted_links = extract_markdown_links(node.text)
        if extracted_links == []:
            new_nodes.append(node)
            continue
        for index_extract, link in enumerate(extracted_links):
            link_text = link[0]
            link_url = link[1]
            section = text_to_split.split(f"[{link_text}]({link_url})", 1)
            if (section[0].strip(" ") != ""):
                new_nodes.append(TextNode(section[0], "text"))
            else:
                continue
            new_nodes.append(TextNode(link_text, "link", link_url))
            text_to_split = section[1]
            if(index_extract == len(extracted_links) - 1 and section[1].strip(" ") != ""):
                new_nodes.append(TextNode(section[1], "text"))
    return new_nodes

def split_md_blocks(markdown: str):
    blocks = []
    block = ""
    if type(markdown) is not str:
        raise TypeError("Type of markdown has to be string")

    for index, line in enumerate(markdown.split("\n")):
        if index == 0 and line.strip(" ") == "":
            continue
        elif line.strip(" ") == "":
            blocks.append(block[:-1])
            block = ""
            continue
        else:
            block += f"{line}\n"
        if index == len(markdown.split("\n")) - 1:
            blocks.append(block[:-1])

    return blocks