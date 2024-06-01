import subprocess
from unittest import TestCase, main
from unittest.mock import Mock, patch

from df_utility import ExecuterBase, DFExecuter, DFInodeExecuter, DFHumanExecuter


class ExecutorsTest(TestCase):
    test_lines = "header\none two three four five six\nsix five four three two one\n"
    len_lines = 2
    len_elements = 6

    def test_abstract_class_instantiation(self):
        self.assertRaises(TypeError, ExecuterBase)

    def executer_additional_test(self, mock_popen, class_executer, params):
        mock_parser = Mock()
        mock_process = Mock()

        mock_popen.return_value = mock_process

        mock_process.communicate.return_value = (b'output', b'')

        mock_parser.parse.return_value = ['parsed_output']

        executer = class_executer(mock_parser)
        result = executer.execute()

        self.assertEqual(result, ['parsed_output'])
        mock_popen.assert_called_once_with(params, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        mock_parser.parse.assert_called_once_with('output')

    @patch('subprocess.Popen')
    def test_df_executer(self, mock_popen):
        self.executer_additional_test(mock_popen, DFExecuter, ['df'])

    @patch('subprocess.Popen')
    def test_df_human_executer(self, mock_popen):
        self.executer_additional_test(mock_popen, DFHumanExecuter, ['df', '-h'])

    @patch('subprocess.Popen')
    def test_df_inode_executer(self, mock_popen):
        self.executer_additional_test(mock_popen, DFInodeExecuter, ['df', '-i'])


if __name__ == "__main__":
    main()
