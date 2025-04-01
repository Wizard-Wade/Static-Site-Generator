class HTMLNode():
    def __init__(self, tag = None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError
    
    def props_to_html(self):
        l1 = ""
        for prop in self.props:
            l1 += (f' {prop}=\"{self.props[prop]}\"')
        return l1
    
    def __repr__(self):
        message = ""
        for value in vars(self).items():
            if value[1] is not None:
                message += f"{value}, "
        return message

    