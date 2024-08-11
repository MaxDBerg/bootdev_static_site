import re

def extract_markdown_images(text):
    if(text == None):
        raise ValueError("text cannot be None")
    if(type(text) != str):
        raise TypeError("Type of text has too be string")

    images = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return images

def extract_markdown_links(text):
    if(text == None):
        raise ValueError("text cannot be None")
    if(type(text) != str):
        raise TypeError("Type of text has too be string")

    links = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return links
