#!/usr/bin/python3
"""Defines MyInt class that inherits from int"""


class MyInt(int):
    """Invert int operators == and !=."""

    def __eq__(self, value):
        """Override == opeartor to != behavior."""
        return self.real != value

    def __ne__(self, value):
        """Override != operator to == behavior."""
        return self.real == value
