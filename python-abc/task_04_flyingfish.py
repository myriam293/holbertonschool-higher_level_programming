#!/usr/bin/python3
"""Construct a FlyingFish class that inherits from both
a Fish class and a Bird class."""


class Fish:
    """Create a Fish class with methods swim and habitat."""

    def swim(self):
        """Print 'The fish is swimming'."""
        print("The fish is swimming")

    def habitat(self):
        """Print 'The fish lives in water'."""
        print("The fish lives in water")


class Bird:
    """Create a Bird class with methods fly and habitat."""

    def fly(self):
        """Print 'The bird is flying'."""
        print("The bird is flying")

    def habitat(self):
        """Print 'The bird lives in the sky'."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Construct a FlyingFish class that inherits from both Fish and Bird."""

    def fly(self):
        """Override the fly method."""
        print("The flying fish is soaring!")

    def swim(self):
        """Override the swim method."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Override the habitat method."""
        print("The flying fish lives both in water and the sky!")
