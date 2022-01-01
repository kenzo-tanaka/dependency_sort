import unittest
from unittest import mock
import dep_star_sort
from bs4 import BeautifulSoup

class DepStarSortTest(unittest.TestCase):
    def setUp(self) -> None:
      self.executor = dep_star_sort.DepStarSort("https://github.com/github/view_component")

    def tearDown(self) -> None:
        pass

    def _mock_get_soup(self):
        with open('index.html') as f:
            return(BeautifulSoup(f, "html.parser"))

    def test_dep_url(self):
        self.assertEqual(self.executor.dep_url(), "https://github.com/github/view_component/network/dependents")

    @mock.patch("dep_star_sort.DepStarSort.get_soup", new=_mock_get_soup)
    def test_evaluate_repos(self):
        expect = [{
            'repo': 'https://github.com/ledermann/templatus-hotwire',
            'star': 6,
        }]
        self.assertEqual(self.executor.evaluate_repos(), expect)

if __name__ == "__main__":
    unittest.main()
