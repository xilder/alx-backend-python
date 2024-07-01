#!/usr/bin/env python3
"""test file for clients class"""
from typing import Dict
from unittest.mock import MagicMock, Mock, PropertyMock, patch
from parameterized import parameterized, parameterized_class
from requests import HTTPError
from fixtures import TEST_PAYLOAD
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

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({"v": {"k": "other_license"}}, "my_license", False)
    ])
    def test_has_license(
        self,
        repo: Dict[str, Dict],
        license_key: str,
        returned_value: bool
    ):
        """test cases for has_license method"""
        google_client = GithubOrgClient("google")
        bool = google_client.has_license(repo, license_key)
        self.assertEqual(bool, returned_value)




@parameterized_class(
    [
        {
            "org_payload": TEST_PAYLOAD[0][0],
            "repos_payload": TEST_PAYLOAD[0][1],
            "expected_repos": TEST_PAYLOAD[0][2],
            "apache2_repos": TEST_PAYLOAD[0][3]
        },
    ]
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """class test"""
    @classmethod
    def setUpClass(cls) -> None:
        """sets up the class"""
        route_payload = {
            'https://api.github.com/orgs/google': cls.org_payload,
            'https://api.github.com/orgs/google/repos': cls.repos_payload,
        }

        def get_payload(url):
            if url in route_payload:
                return Mock(**{"json.return_value": route_payload[url]})
            return HTTPError

        cls.get_patcher = patch("requests.get", side_effect=get_payload)
        cls.get_patcher.start()

    def test_public_repos(self) -> None:
        """test the public_repos method"""
        self.assertEqual(
            GithubOrgClient("google").public_repos(),
            self.expected_repos,
        )

    def test_public_repos_with_license(self) -> None:
        """test public repos method of the GithubOrgClient"""
        self.assertEqual(
            GithubOrgClient("google").public_repos(license="apache-2.0"),
            self.apache2_repos,
        )

    @classmethod
    def tearDownClass(cls) -> None:
        """tears down the setup class"""
        cls.get_patcher.stop()