# -*- coding: utf-8 -*-

from unittest import TestCase
from mock import patch

from bambou.exceptions import BambouHTTPError
from bambou.tests.utils import MockUtils
from bambou.tests.functionnal import get_login_as_user


class Count(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user = get_login_as_user()

    @classmethod
    def tearDownClass(cls):
        pass

    def test_count_all(self):
        """ HEAD /enterprises count all enterprises """

        user = self.user
        headers = {'X-Nuage-Count': 4}

        mock = MockUtils.create_mock_response(status_code=200, data=None, headers=headers)

        with patch('requests.request', mock):
            (fetcher, user, count) = self.user.enterprises_fetcher.count()

        method = MockUtils.get_mock_parameter(mock, 'method')
        url = MockUtils.get_mock_parameter(mock, 'url')
        headers = MockUtils.get_mock_parameter(mock, 'headers')

        self.assertEqual(url, u'https://<host>:<port>/nuage/api/v3_0/enterprises')
        self.assertEqual(method, u'HEAD')
        self.assertEqual(headers['Authorization'], u'XREST dXNlcjo1MWYzMTA0Mi1iMDQ3LTQ4Y2EtYTg4Yi02ODM2ODYwOGUzZGE=')
        self.assertEqual(headers['X-Nuage-Organization'], u'enterprise')
        self.assertEqual(headers['Content-Type'], u'application/json')

        self.assertEqual(fetcher, self.user.enterprises_fetcher)
        self.assertEqual(user, self.user)
        self.assertEqual(count, 4)

    def test_count_with_filter(self):
        """ HEAD /enterprises count enterprises with filters """

        user = self.user
        headers = {'X-Nuage-Count': 2}

        mock = MockUtils.create_mock_response(status_code=200, data=None, headers=headers)

        with patch('requests.request', mock):
            (fetcher, user, count) = self.user.enterprises_fetcher.count(filter=u"name == 'Enterprise 2'")

        headers = MockUtils.get_mock_parameter(mock, 'headers')
        self.assertEqual(headers['X-Nuage-Filter'], u"name == 'Enterprise 2'")
        self.assertEqual(count, 2)

    def test_count_all_should_raise_exception(self):
        """ HEAD /enterprises count all enterprises should raise exception """

        user = self.user
        mock = MockUtils.create_mock_response(status_code=500, data=[], error=u"Internal error")

        with patch('requests.request', mock):
            with self.assertRaises(BambouHTTPError):
                (fetcher, user, count) = self.user.enterprises_fetcher.count()