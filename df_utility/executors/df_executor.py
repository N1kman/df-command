from typing import Dict, List
import subprocess

from .executor_base import ExecutorBase


class DFExecutor(ExecutorBase):

    DF_OPTION = ['df']

    def __init__(self, parser, option=None):
        if option is None:
            option = self.DF_OPTION
        self.__option = option
        self.__parser = parser

    def execute(self) -> List[Dict]:
        process = subprocess.Popen(self.__option, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = process.communicate()

        if error:
            raise Exception(error.decode('utf-8'))

        return self.__parser.parse(output.decode('utf-8'))
