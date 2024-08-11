import re


def extract_markdown_images(text):
    if text is None:
        raise ValueError("text cannot be None")
    if type(text) is not str:
        raise TypeError("Type of text has too be string")

    images = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return images


def extract_markdown_links(text):
    if text is None:
        raise ValueError("text cannot be None")
    if type(text) is not str:
        raise TypeError("Type of text has too be string")

    links = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return links
