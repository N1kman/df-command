from abc import ABC, abstractmethod
from typing import List, Dict


class ParserBase(ABC):
    @abstractmethod
    def parse(self, output) -> List[Dict]:
        pass
