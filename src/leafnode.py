from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, TAG=None, VALUE=None, PROPS=None):
        super().__init__(TAG, VALUE, None, PROPS)

    def to_html(self):
        if self.value is None:
            raise ValueError("LeafNode must have a value")
        if self.tag is None:
            return f"{self.value}"
        if self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        return f"<{self.tag}{super().props_to_html()}>{self.value}</{self.tag}>"
