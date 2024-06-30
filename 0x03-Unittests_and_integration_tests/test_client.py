#!/usr/bin/env python3
"""test file for clients class"""
from typing import Dict
from unittest.mock import MagicMock, PropertyMock, patch
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


    def test_public_repos_url(self) -> None:
        """
        tests the _public_repos_url method
        of the GithubOrgClient
        """

        with patch(
            "client.GithubOrgClient.org",
            new_callable=PropertyMock
        ) as mock_org:
            mock_org.return_value = {
                "repos_url": "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos"
                )
