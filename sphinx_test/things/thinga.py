"""thing_a content here
"""

from sphinx_test.obja import ObjA


class ThingA:
    """thing a is here!"""

    def __init__(self, val: ObjA) -> None:
        self.val = val

    def return_val(self) -> ObjA:
        """return val"""
        return self.val
