#!/usr/bin/env python3
"""test file for clients class"""
from typing import Dict
from unittest.mock import MagicMock, patch
from parameterized import parameterized
import unittest
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """test cases for client.py"""
    @parameterized.expand(
        [
            ("google", {"login": "google"}),
            ("abc", {"login": "abc"})
        ]
    )
    @patch("client.get_json")
    def test_org(self, org: str, expected_output: Dict,
                 mocked_function: MagicMock) -> None:
        """test the org method"""
        mocked_function.return_value = MagicMock(return_value=expected_output)
        client = GithubOrgClient(org)
        self.assertEqual(client.org(), expected_output)
        mocked_function.assert_called_once_with(
            f"https://api.github.com/orgs/{org}"
            )
