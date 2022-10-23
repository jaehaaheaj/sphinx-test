"""thing_b content here
"""

from sphinx_test.objb import ObjB


class ThingB:
    """thing a is here!"""

    def __init__(self, val: ObjB) -> None:
        self.val = val

    def return_val(self) -> ObjB:
        """return val"""
        return self.val
