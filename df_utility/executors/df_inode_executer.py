from .df_executer import DFExecuter


class DFInodeExecuter(DFExecuter):

    DF_INODE_OPTION = ['df', '-i']

    def __init__(self, parser):
        super().__init__(parser=parser, option=self.DF_INODE_OPTION)
