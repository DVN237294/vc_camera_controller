# coding: utf-8

"""
    vc_webapi

    Web API for the Virtual Classroom project  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: 237294@via.dk
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest

import openapi_client
from openapi_client.api.schedule_api import ScheduleApi  # noqa: E501
from openapi_client.rest import ApiException


class TestScheduleApi(unittest.TestCase):
    """ScheduleApi unit test stubs"""

    def setUp(self):
        self.api = openapi_client.api.schedule_api.ScheduleApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_api_schedule_add_room_post(self):
        """Test case for api_schedule_add_room_post

        """
        pass

    def test_api_schedule_for_room_room_name_get(self):
        """Test case for api_schedule_for_room_room_name_get

        """
        pass

    def test_api_schedule_get_rooms_get(self):
        """Test case for api_schedule_get_rooms_get

        """
        pass

    def test_api_schedule_post(self):
        """Test case for api_schedule_post

        """
        pass


if __name__ == '__main__':
    unittest.main()