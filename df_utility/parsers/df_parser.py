from typing import List, Dict

from .parser_base import ParserBase


class DFParser(ParserBase):
    DF_HEADER = ['Filesystem', '1K-blocks', 'Used', 'Available', 'Use%', 'Mounted on']

    def __init__(self, header=None):
        if header is None or len(header) != len(self.DF_HEADER):
            header = self.DF_HEADER
        self.__header = header

    def parse(self, output) -> List[Dict]:
        lines = output.split('\n')[1:]
        return [dict(zip(self.__header, line.split())) for line in lines if line]
