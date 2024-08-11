class TextNode:
    def __init__(self, TEXT=None, TEXT_TYPE=None, URL=None):
        self.text = TEXT
        self.text_type = TEXT_TYPE
        self.url = URL

    def __eq__(self, value: object) -> bool:
        if (
            self.text == value.text
            and self.text_type == value.text_type
            and self.url == value.url
        ):
            return True

    def __repr__(self) -> str:
        return f"TextNode({self.text}, {self.text_type}, {self.url})"
