# -*- coding: utf-8 -*-
# Copyright (c) 2011-2012 Alcatel, Alcatel-Lucent, Inc. All Rights Reserved.
#
# This source code contains confidential information which is proprietary to Alcatel.
# No part of its contents may be used, copied, disclosed or conveyed to any party
# in any manner whatsoever without prior written permission from Alcatel.
#
# Alcatel-Lucent is a trademark of Alcatel-Lucent, Inc.



class NURESTResponse(object):
    """ Response that will be received via the connection """

    def __init__(self, status_code, headers=None, data=None, reason=None, errors=None):
        """ Initializes a request """

        self._status_code = status_code
        self._data = data
        self._reason = reason
        self._headers = headers
        self.errors = dict()

    def __str__(self):
        """ Print request """

        return "[%s]\n%s" % (self.status_code, self.data)

    # Properties

    def _get_status_code(self):
        """ Get method """

        return self._status_code

    status_code = property(_get_status_code, None)

    def _get_data(self):
        """ Get data """

        return self._data

    data = property(_get_data, None)

    def _get_reason(self):
        """ Get error reason """

        return self._reason

    reason = property(_get_reason, None)

    def _get_headers(self):
        """ Get headers """

        return self._headers

    headers = property(_get_headers, None)
