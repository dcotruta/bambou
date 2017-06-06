# -*- coding: utf-8 -*-

from unittest import TestCase
from mock import patch

from tests.utils import MockUtils
from tests.functionnal import start_session, get_valid_group
from tests.models import Employee


class Assign(TestCase):

    @classmethod
    def setUpClass(cls):
        cls.user = start_session()
        cls.group = get_valid_group(id='xxxx-xxx-xxx', name=u"TestGroup")

    @classmethod
    def tearDownClass(cls):
        pass

    def test_assign(self):
        """ PUT /groups/id/users assign users """

        mock = MockUtils.create_mock_response(status_code=204, data=None)

        employee1 = Employee(firstname=u"Steven", lastname=u"Gerrard")
        employee2 = Employee(firstname=u"Gerrard", lastname=u"Lampard")

        with patch('requests.Session.request', mock):
            (objects, connection) = self.group.assign([employee1, employee2], Employee)

        method = MockUtils.get_mock_parameter(mock, 'method')
        url = MockUtils.get_mock_parameter(mock, 'url')
        headers = MockUtils.get_mock_parameter(mock, 'headers')

        self.assertEqual(connection.response.status_code, 204)
        self.assertEqual(url, 'https://vsd:8443/api/v3_2/groups/' + self.group.id + '/users')
        self.assertEqual(method, 'PUT')
        self.assertEqual(headers['Authorization'], 'XREST dXNlcjo1MWYzMTA0Mi1iMDQ3LTQ4Y2EtYTg4Yi02ODM2ODYwOGUzZGE=')
        self.assertEqual(headers['X-Nuage-Organization'], 'enterprise')
        self.assertEqual(headers['Content-Type'], 'application/json')

        self.assertEqual(objects, [employee1, employee2])
        self.assertEqual(self.group.employees, [employee1, employee2])
        self.group.employees.flush()

    def test_assign_with_commit(self):
        """ PUT /groups/id/users assign users without commit """

        mock = MockUtils.create_mock_response(status_code=204, data=None)

        employee1 = Employee(firstname=u"Steven", lastname=u"Gerrard")
        employee2 = Employee(firstname=u"Gerrard", lastname=u"Lampard")

        with patch('requests.Session.request', mock):
            (objects, connection) = self.group.assign([employee1, employee2], Employee, commit=False)

        self.assertEqual(objects, [employee1, employee2])
        self.assertEqual(self.group.employees, [])

