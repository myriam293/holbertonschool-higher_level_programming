#!/usr/bin/python3
"""Module containing CustomObject class with
pickle serialization and deserialization"""
import pickle


class CustomObject:
    """Custom class with name, age, and is_student attributes"""

    def __init__(self, name: str, age: int, is_student: bool):
        """Initialize a CustomObject with name, age, and is_student"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object attributes in the required format"""
        print(f"Name: {self.name}\nAge: {self.age}\nIs Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance and
        save it to the provided filename"""
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self, file)
        except Exception:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Load and return an instance of
        CustomObject from the provided filename"""
        try:
            with open(filename, 'rb') as file:
                return pickle.load(file)
        except Exception:
            return None
