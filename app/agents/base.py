from abc import ABC, abstractmethod
from typing import Any, Dict

class Agent(ABC):
    def __init__(self, name: str, role: str):
        self.name = name
        self.role = role

    @abstractmethod
    def execute(self, query: str) -> Any:
        pass
