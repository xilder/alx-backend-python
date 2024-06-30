#!/usr/bin/env python3
"""unit tests for nest_map function"""
import unittest
from parameterized import parameterized


access_nested_map = __import__("utils").access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """unittest class"""
    parameterized.expand(
            ({"a": {"b": 2}}, ("a", "b"), 2),
            ({"a": {"b": 2}}, ("a",), {"b": 2}),
            ({"a": 1}, ("a",), 1)
        )

    def test_access_nested_map(self, nested_map, path, expected_output):
        """tests the access_nested_map function"""
        result = access_nested_map(nested_map, path)
        self.assertEqual(result, expected_output)
