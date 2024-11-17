#abstract base class for Serializer
from abc import ABC, abstractmethod

class Serializer(ABC):

    def __init__(self) -> None:
        pass
    
    @abstractmethod
    def serialize(self):
        pass
    
    @abstractmethod
    def deserialize(self):
        pass
    
    @abstractmethod
    def display(self):
        pass