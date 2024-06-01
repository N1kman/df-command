from unittest import TestCase, main
from df_utility import ParserBase, DFParser, DFHumanParser, DFInodeParser


class ParsersTest(TestCase):

    test_lines = "header\none two three four five six\nsix five four three two one\n"
    len_lines = 2
    len_elements = 6

    def test_abstract_class_instantiation(self) -> None:
        self.assertRaises(TypeError, ParserBase)

    def test_df_parser(self) -> None:
        df_parser = DFParser()
        result = df_parser.parse(self.test_lines)
        self.assertEqual(len(result), self.len_lines)
        self.assertEqual(len(result[0]), self.len_elements)
        self.assertEqual(len(result[1]), self.len_elements)
        for name_header in DFParser.DF_HEADER:
            self.assertIn(name_header, list(result[0].keys()))

    def test_df_human_parser(self) -> None:
        df_human_parser = DFHumanParser()
        result = df_human_parser.parse(self.test_lines)
        self.assertEqual(len(result), self.len_lines)
        self.assertEqual(len(result[0]), self.len_elements)
        self.assertEqual(len(result[1]), self.len_elements)
        for name_header in DFHumanParser.DF_HUMAN_HEADER:
            self.assertIn(name_header, list(result[0].keys()))

    def test_df_inode_parser(self) -> None:
        df_inode_parser = DFInodeParser()
        result = df_inode_parser.parse(self.test_lines)
        self.assertEqual(len(result), self.len_lines)
        self.assertEqual(len(result[0]), self.len_elements)
        self.assertEqual(len(result[1]), self.len_elements)
        for name_header in DFInodeParser.DF_INODE_HEADER:
            self.assertIn(name_header, list(result[0].keys()))


if __name__ == "__main__":
    main()
