# -*- coding: utf-8 -*-

from unittest import TestCase
from mock import patch

from bambou.exceptions import BambouHTTPError
from tests.utils import MockUtils
from tests.functionnal import start_session


class Count(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user = start_session()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_count_all(self):
        """ HEAD /enterprises count all enterprises """

        user = self.user
        headers = {'X-Nuage-Count': 4}

        mock = MockUtils.create_mock_response(status_code=200, data=None, headers=headers)

        with patch('requests.Session.request', mock):
            (fetcher, user, count) = self.user.enterprises.count()

        method = MockUtils.get_mock_parameter(mock, 'method')
        url = MockUtils.get_mock_parameter(mock, 'url')
        headers = MockUtils.get_mock_parameter(mock, 'headers')

        self.assertEqual(url, 'https://vsd:8443/api/v3_2/enterprises')
        self.assertEqual(method, 'HEAD')
        self.assertEqual(headers['Authorization'], 'XREST dXNlcjo1MWYzMTA0Mi1iMDQ3LTQ4Y2EtYTg4Yi02ODM2ODYwOGUzZGE=')
        self.assertEqual(headers['X-Nuage-Organization'], 'enterprise')
        self.assertEqual(headers['Content-Type'], 'application/json')

        self.assertEqual(fetcher, self.user.enterprises)
        self.assertEqual(user, self.user)
        self.assertEqual(count, 4)

    def test_count_with_filter(self):
        """ HEAD /enterprises count enterprises with filters """

        user = self.user
        headers = {'X-Nuage-Count': 2}

        mock = MockUtils.create_mock_response(status_code=200, data=None, headers=headers)

        with patch('requests.Session.request', mock):
            (fetcher, user, count) = self.user.enterprises.count(filter=u"name == 'Enterprise 2'")

        headers = MockUtils.get_mock_parameter(mock, 'headers')
        self.assertEqual(headers['X-Nuage-Filter'],"name == 'Enterprise 2'")
        self.assertEqual(count, 2)

    def test_count_with_order_by(self):
        """ HEAD /enterprises count enterprises with order_by """

        user = self.user
        headers = {'X-Nuage-Count': 2}

        mock = MockUtils.create_mock_response(status_code=200, data=None, headers=headers)

        with patch('requests.Session.request', mock):
            (fetcher, user, count) = self.user.enterprises.count(order_by='name ASC')

        headers = MockUtils.get_mock_parameter(mock, 'headers')
        self.assertEqual(headers['X-Nuage-OrderBy'], 'name ASC')

    def test_count_with_group_by(self):
        """ HEAD /enterprises count enterprises with group_by """

        user = self.user
        headers = {'X-Nuage-Count': 2}

        mock = MockUtils.create_mock_response(status_code=200, data=None, headers=headers)

        with patch('requests.Session.request', mock):
            (fetcher, user, count) = self.user.enterprises.count(group_by=['field1', 'field2'])

        headers = MockUtils.get_mock_parameter(mock, 'headers')
        self.assertEqual(headers['X-Nuage-GroupBy'], 'true')
        self.assertEqual(headers['X-Nuage-Attributes'], 'field1, field2')

    def test_count_with_page(self):
        """ HEAD /enterprises count enterprises with page """

        user = self.user
        headers = {'X-Nuage-Count': 2}

        mock = MockUtils.create_mock_response(status_code=200, data=None, headers=headers)

        with patch('requests.Session.request', mock):
            (fetcher, user, count) = self.user.enterprises.count(page=3)

        headers = MockUtils.get_mock_parameter(mock, 'headers')
        self.assertEqual(headers['X-Nuage-Page'], '3')

    def test_count_with_page_size(self):
        """ HEAD /enterprises count enterprises with page size """

        user = self.user
        headers = {'X-Nuage-Count': 2}

        mock = MockUtils.create_mock_response(status_code=200, data=None, headers=headers)

        with patch('requests.Session.request', mock):
            (fetcher, user, count) = self.user.enterprises.count(page_size=10)

        headers = MockUtils.get_mock_parameter(mock, 'headers')
        self.assertEqual(headers['X-Nuage-PageSize'], '10')

    def test_count_all_should_raise_exception(self):
        """ HEAD /enterprises count all enterprises should raise exception """

        user = self.user
        mock = MockUtils.create_mock_response(status_code=500, data=[], error=u"Internal error")

        with patch('requests.Session.request', mock):
            with self.assertRaises(BambouHTTPError):
                (fetcher, user, count) = self.user.enterprises.count()

    def test_direct_count_all(self):
        """ HEAD /enterprises direct count all enterprises """

        user = self.user
        headers = {'X-Nuage-Count': 4}

        mock = MockUtils.create_mock_response(status_code=200, data=None, headers=headers)

        with patch('requests.Session.request', mock):
            count = self.user.enterprises.get_count()

        self.assertEqual(count, 4)
