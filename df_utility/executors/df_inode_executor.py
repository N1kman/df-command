from .df_executor import DFExecutor


class DFInodeExecutor(DFExecutor):

    DF_INODE_OPTION = ['df', '-i']

    def __init__(self, parser):
        super().__init__(parser=parser, option=self.DF_INODE_OPTION)
