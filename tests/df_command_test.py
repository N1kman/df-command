import json
import unittest
from unittest import TestCase
from unittest.mock import patch, Mock

from df_command import get_args, get_executor_by_arg, main
from df_utility import DFHumanExecuter, DFInodeExecuter, DFExecuter


class DFCommandTest(TestCase):

    @patch('argparse.ArgumentParser.parse_args')
    def test_get_args(self, mock_args):
        mock_args.return_value = Mock(human=True, inode=False)
        args = get_args()
        self.assertTrue(args.human)
        self.assertFalse(args.inode)

    @patch('df_command.get_args')
    def test_get_executor_by_arg(self, mock_get_args):
        self.assertIsInstance(get_executor_by_arg(Mock(human=False, inode=False)), DFExecuter)
        self.assertIsInstance(get_executor_by_arg(Mock(human=False, inode=True)), DFInodeExecuter)
        self.assertIsInstance(get_executor_by_arg(Mock(human=True, inode=False)), DFHumanExecuter)

    @patch('df_command.get_args')
    @patch('df_utility.DFHumanExecuter.execute')
    def test_main(self, mock_execute, mock_get_args):
        mock_get_args.return_value = Mock(human=True, inode=False)
        mock_execute.return_value = "test result"
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_once_with(
                json.dumps({"status": "success", "error": "None", "result": "test result"}, indent=4))


if __name__ == "__main__":
    unittest.main()
