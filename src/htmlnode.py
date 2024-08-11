class HTMLNode:
    def __init__(self, TAG=None, VALUE=None, CHILDREN=None, PROPS=None):
        self.tag = TAG
        self.value = VALUE
        self.children = CHILDREN
        self.props = PROPS

    def to_html():
        raise NotImplementedError

    def props_to_html(self):
        htmlString = ""
        if type(self.props) is dict:
            for key, value in self.props.items():
                htmlString += f' {key}="{value}"'
        return htmlString

    def __repr__(self) -> str:
        return f"HTMLNode: tag = {self.tag}, value = {self.value}, children = {self.children}, props = {self.props}"

    def __eq__(self, value: object) -> bool:
        if (
            self.tag == value.tag
            and self.value == value.value
            and self.children == value.children
            and self.props == value.props
        ):
            return True
        return False
