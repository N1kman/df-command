from abc import ABC, abstractmethod
from typing import List, Dict


class ExecuterBase(ABC):

    @abstractmethod
    def execute(self) -> List[Dict]:
        pass
