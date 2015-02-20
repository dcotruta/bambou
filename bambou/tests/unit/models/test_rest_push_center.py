# -*- coding:utf-8 -*-

from unittest import TestCase
from bambou import NURESTLoginController, NURESTPushCenter


class PushCenterSingletonTests(TestCase):

    def test_push_center_is_singleton(self):
        """ PushCenter is singleton """
        push_center_1 = NURESTPushCenter()
        push_center_1.url = u'http://www.google.fr'
        push_center_2 = NURESTPushCenter()

        self.assertEquals(push_center_1.url, u'http://www.google.fr')
        self.assertEquals(push_center_1, push_center_2)


class PushCenterRunningTests(TestCase):

    def test_start_stop_push_center(self):
        """ PushCenter can start and stop """

        push_center = NURESTPushCenter()
        push_center.url = u'http://www.google.fr'
        push_center.start()
        self.assertEquals(push_center.is_running, True)
        push_center.stop()
        self.assertEquals(push_center.is_running, False)