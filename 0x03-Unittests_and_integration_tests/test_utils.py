#!/usr/bin/env python3
"""unit tests for nest_map function"""
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json


class TestAccessNestedMap(unittest.TestCase):
    """unittest class for"""
    @parameterized.expand(
            [
                ({"a": 1}, ("a",), 1),
                ({"a": {"b": 2}}, ("a",), {"b": 2}),
                ({"a": {"b": 2}}, ("a", "b"), 2)
            ]
        )
    def test_access_nested_map(self, nested_map, path, expected_output):
        """tests the access_nested_map function"""
        self.assertEqual(access_nested_map(nested_map, path), expected_output)

    @parameterized.expand(
            [
                ({}, ("a",)),
                ({"a": 1}, ("a", "b"))
            ]
    )
    def test_access_nested_map_exception(self, nested_map, path):
        """tests the access_nested_map function with exception"""
        with self.assertRaises(KeyError):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """mock function tests for the get_json method"""

    @parameterized.expand(
        [
            ("http://example.com", {"payload": True}),
            ("http://holberton.io", {"payload": False})
        ]
    )
    def test_get_json(self, url, expected_output):
        """mocks requests.get"""
        mock_response = Mock()
        mock_response.json.return_value = expected_output
        with patch("requests.get", return_value=mock_response):
            response = get_json(url)
            self.assertEqual(response, expected_output)


