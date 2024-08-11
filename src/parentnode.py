from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, CHILDREN, TAG=None, PROPS=None):
        super().__init__(TAG, None, CHILDREN, PROPS)

    def to_html(self):
        if self.tag is None:
            raise ValueError("ParentNode must have a tag")
        if self.children is None:
            raise ValueError("ParentNode must have children")
        html_string = f"<{self.tag}>"
        for child in self.children:
            html_string += f"{child.to_html()}"
        html_string += f"</{self.tag}>"
        return html_string