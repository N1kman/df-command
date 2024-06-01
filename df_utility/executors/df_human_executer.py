from .df_executer import DFExecuter


class DFHumanExecuter(DFExecuter):

    DF_HUMAN_OPTION = ['df', '-h']

    def __init__(self, parser):
        super().__init__(parser=parser, option=self.DF_HUMAN_OPTION)
