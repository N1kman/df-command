from .df_parser import DFParser


class DFInodeParser(DFParser):
    DF_INODE_HEADER = ['Filesystem', 'Inodes', 'IUsed', 'IFree', 'IUse%', 'Mounted on']

    def __init__(self):
        super().__init__(header=self.DF_INODE_HEADER)
