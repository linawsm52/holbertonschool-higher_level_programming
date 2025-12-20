#!/usr/bin/python3
"""
Square module
"""

Rectangle = __import__('8-rectangle').Rectangle


class Square(Rectangle):
    """Defines a square"""

    def __init__(self, size=0):
        """Initialize square"""
        super().__init__(size, size)

    def __str__(self):
        """Return string representation"""
        if self.width == 0:
            return ""
        return "\n".join("#" * self.width for _ in range(self.height))
