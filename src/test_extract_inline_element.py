import unittest

from extract_inline_element import extract_markdown_images, extract_markdown_links

class TestExtractInlineElement(unittest.TestCase):
    def test_eq_extract_images(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        images = extract_markdown_images(text)
        image_references = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]

        self.assertEqual(images,image_references)

    def test_eq_extract_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        links = extract_markdown_links(text)
        links_references = [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]

        self.assertEqual(links,links_references)

if __name__ == "__main__":
    unittest.main()
