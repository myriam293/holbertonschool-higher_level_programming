#!/usr/bin/python3
"""Design mixins SwimMixin and FlyMixin, and a class Dragon
that inherits from both these mixins."""


class SwimMixin:
    """A mixin class with a swim method that prints 'The creature swims!'."""

    def swim(self):
        """Print 'The creature swims!'."""
        print("The creature swims!")


class FlyMixin:
    """A mixin class with a fly method that prints 'The creature flies!'."""

    def fly(self):
        """Print 'The creature flies!'."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Construct a class Dragon that inherits from SwimMixin and FlyMixin."""

    def roar(self):
        """Print 'The dragon roars!'."""
        print("The dragon roars!")
