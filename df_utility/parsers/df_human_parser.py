from .df_parser import DFParser


class DFHumanParser(DFParser):

    DF_HUMAN_HEADER = ['Filesystem', 'Size', 'Used', 'Avail', 'Use%', 'Mounted on']

    def __init__(self):
        super().__init__(header=self.DF_HUMAN_HEADER)
