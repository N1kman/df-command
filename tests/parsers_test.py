from unittest import TestCase, main
from df_utility import ParserBase


class ParsersTest(TestCase):
    def test_abstract_class_instantiation(self):
        self.assertRaises(TypeError, ParserBase)


if __name__ == "__main__":
    main()

