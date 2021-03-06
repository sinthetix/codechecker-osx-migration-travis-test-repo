# -----------------------------------------------------------------------------
#                     The CodeChecker Infrastructure
#   This file is distributed under the University of Illinois Open Source
#   License. See LICENSE.TXT for details.
# -----------------------------------------------------------------------------

"""Test the parsing of the plist generated by multiple clang versions."""

import os
import unittest

from codechecker_lib import plist_parser


class PlistParserTestCaseNose(unittest.TestCase):
    """Test the parsing of the plist generated by multiple clang versions."""

    @classmethod
    def setup_class(cls):
        """Initialize test source file."""
        # Bugs found by these checkers in the test source files.
        cls.__found_checker_names = [
            'core.DivideZero',
            'core.StackAddressEscape',
            'deadcode.DeadStores']

        # Previous clang versions do not generate the checker name into the
        # plist output.
        cls.__not_found_checker_names = ['NOT FOUND']

        # Bug id hash values generated by codechecker framework.
        cls.__framework_generated_hashes = [
            'e9fb5a280e64610cfa82472117c8d0ac',
            '9536c46411df42db29014729867146fa',
            'b1bc0e8364a255659522055d1e15cd16']

        # Bug were found in these test files.
        cls.__found_file_names = ['test.cpp', './test.h']

        # Already generated plist files for the tests.
        cls.__this_dir = os.path.dirname(__file__)
        cls.__plist_test_files = os.path.join(
            cls.__this_dir, 'plist_test_files')

    def __core_div_bug_event(self, bug_event):
        """Check the core.dividezero checker last event position."""
        self.assertEqual(bug_event.start_pos.line, 7)
        self.assertEqual(bug_event.start_pos.col, 12)
        self.assertEqual(bug_event.start_pos.file_path, './test.h')
        self.assertEqual(bug_event.end_pos.line, 7)
        self.assertEqual(bug_event.end_pos.col, 17)
        self.assertEqual(bug_event.end_pos.file_path, './test.h')

    def __core_stack_addr_esc_event(self, bug_event):
        """Check the core.StackAddressEscape checker last event position."""
        self.assertEqual(bug_event.start_pos.line, 14)
        self.assertEqual(bug_event.start_pos.col, 3)
        self.assertEqual(bug_event.start_pos.file_path, 'test.cpp')
        self.assertEqual(bug_event.end_pos.line, 14)
        self.assertEqual(bug_event.end_pos.col, 29)
        self.assertEqual(bug_event.end_pos.file_path, 'test.cpp')

    def test_empty_file(self):
        """Plist file is empty."""
        empty_plist = os.path.join(self.__plist_test_files, 'empty_file')
        files, bugs = plist_parser.parse_plist(empty_plist)
        self.assertEquals(files, [])
        self.assertEquals(bugs, [])

    def test_no_bug_file(self):
        """There was no bug in the checked file."""
        no_bug_plist = os.path.join(
            self.__plist_test_files, 'clang-3.7-noerror.plist')
        files, bugs = plist_parser.parse_plist(no_bug_plist)
        self.assertEquals(files, [])
        self.assertEquals(bugs, [])

    def test_clang34_plist(self):
        """
        Check plist generated by clang 3.4 checker name is not in the plist
        file plist parser tries to find out the name.
        """
        clang34_plist = os.path.join(
            self.__plist_test_files, 'clang-3.4.plist')
        files, bugs = plist_parser.parse_plist(clang34_plist)
        self.assertEquals(files, self.__found_file_names)
        self.assertEquals(len(bugs), 3)

        valid_checker_names = []
        valid_checker_names.extend(self.__found_checker_names)
        valid_checker_names.extend(self.__not_found_checker_names)

        for bug in bugs:
            self.assertIn(bug.checker_name, valid_checker_names)
            if bug.checker_name == 'core.DivideZero':
                self.__core_div_bug_event(bug.get_last_event())
            if bug.checker_name == 'NOT FOUND':
                self.__core_stack_addr_esc_event(bug.get_last_event())

            self.assertIn(bug.hash_value, self.__framework_generated_hashes)

    def test_clang35_plist(self):
        """
        Check plist generated by clang 3.5 checker name is not in the plist
        file plist parser tries to find out the name.
        """
        clang35_plist = os.path.join(
            self.__plist_test_files, 'clang-3.5.plist')
        files, bugs = plist_parser.parse_plist(clang35_plist)
        self.assertEquals(files, self.__found_file_names)
        self.assertEquals(len(bugs), 3)

        valid_checker_names = []
        valid_checker_names.extend(self.__found_checker_names)
        valid_checker_names.extend(self.__not_found_checker_names)

        for bug in bugs:
            self.assertIn(bug.checker_name, valid_checker_names)
            if bug.checker_name == 'core.DivideZero':
                self.__core_div_bug_event(bug.get_last_event())
            if bug.checker_name == 'NOT FOUND':
                self.__core_stack_addr_esc_event(bug.get_last_event())

            self.assertIn(bug.hash_value, self.__framework_generated_hashes)

    def test_clang36_plist(self):
        """
        Check plist generated by clang 3.6 checker name is not in the plist
        file plist parser tries to find out the name.
        """
        clang36_plist = os.path.join(
            self.__plist_test_files, 'clang-3.6.plist')
        files, bugs = plist_parser.parse_plist(clang36_plist)
        self.assertEquals(files, self.__found_file_names)
        self.assertEquals(len(bugs), 3)

        valid_checker_names = []
        valid_checker_names.extend(self.__found_checker_names)
        valid_checker_names.extend(self.__not_found_checker_names)

        for bug in bugs:
            self.assertIn(bug.checker_name, valid_checker_names)
            if bug.checker_name == 'core.DivideZero':
                self.__core_div_bug_event(bug.get_last_event())
            if bug.checker_name == 'NOT FOUND':
                self.__core_stack_addr_esc_event(bug.get_last_event())

            self.assertIn(bug.hash_value, self.__framework_generated_hashes)

    def test_clang37_plist(self):
        """
        Check plist generated by clang 3.7 checker name should be in the plist
        file.
        """
        clang37_plist = os.path.join(
            self.__plist_test_files, 'clang-3.7.plist')
        files, bugs = plist_parser.parse_plist(clang37_plist)

        self.assertEquals(files, self.__found_file_names)
        self.assertEquals(len(bugs), 3)

        valid_checker_names = []
        valid_checker_names.extend(self.__found_checker_names)

        for bug in bugs:
            # Checker name should be in the plist file.
            self.assertNotEqual(bug.checker_name, 'NOT FOUND')

            self.assertIn(bug.checker_name, valid_checker_names)

            if bug.checker_name == 'core.DivideZero':
                self.__core_div_bug_event(bug.get_last_event())
            if bug.checker_name == 'core.StackAddressEscape':
                self.__core_stack_addr_esc_event(bug.get_last_event())

            self.assertNotEquals(bug.hash_value, '')

    def test_clang38_trunk_plist(self):
        """
        Check plist generated by clang 3.8 trunk checker name and bug hash
        should be in the plist file.
        """
        clang38_plist = os.path.join(
            self.__plist_test_files, 'clang-3.8-trunk.plist')
        files, bugs = plist_parser.parse_plist(clang38_plist)

        self.assertEquals(files, self.__found_file_names)
        self.assertEquals(len(bugs), 3)

        valid_checker_names = []
        valid_checker_names.extend(self.__found_checker_names)

        for bug in bugs:
            # Checker name should be in the plist file.
            self.assertNotEqual(bug.checker_name, 'NOT FOUND')

            self.assertIn(bug.checker_name, valid_checker_names)

            if bug.checker_name == 'core.DivideZero':
                self.__core_div_bug_event(bug.get_last_event())
                self.assertEquals(
                    bug.hash_value, '79e31a6ba028f0b7d9779faf4a6cb9cf')
            if bug.checker_name == 'core.StackAddressEscape':
                self.__core_stack_addr_esc_event(bug.get_last_event())
                self.assertEquals(
                    bug.hash_value, 'f7b5072d428e890f2d309217f3ead16f')
            if bug.checker_name == 'deadcode.DeadStores':
                self.assertEquals(
                    bug.hash_value, '8714f42d8328bc78d5d7bff6ced918cc')
