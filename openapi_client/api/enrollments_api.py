# coding: utf-8

"""
    vc_webapi

    Web API for the Virtual Classroom project  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: 237294@via.dk
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from openapi_client.api_client import ApiClient
from openapi_client.exceptions import (
    ApiTypeError,
    ApiValueError
)


class EnrollmentsApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def api_enrollments_my_enrollments_get(self, **kwargs):  # noqa: E501
        """api_enrollments_my_enrollments_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_enrollments_my_enrollments_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int limit_enrollments:
        :param bool include_sessions:
        :param bool include_session_participants:
        :param bool include_session_recordings:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: list[Enrollment]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.api_enrollments_my_enrollments_get_with_http_info(**kwargs)  # noqa: E501

    def api_enrollments_my_enrollments_get_with_http_info(self, **kwargs):  # noqa: E501
        """api_enrollments_my_enrollments_get  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_enrollments_my_enrollments_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param int limit_enrollments:
        :param bool include_sessions:
        :param bool include_session_participants:
        :param bool include_session_recordings:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: tuple(list[Enrollment], status_code(int), headers(HTTPHeaderDict))
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['limit_enrollments', 'include_sessions', 'include_session_participants', 'include_session_recordings']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_enrollments_my_enrollments_get" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit_enrollments' in local_var_params:
            query_params.append(('limitEnrollments', local_var_params['limit_enrollments']))  # noqa: E501
        if 'include_sessions' in local_var_params:
            query_params.append(('includeSessions', local_var_params['include_sessions']))  # noqa: E501
        if 'include_session_participants' in local_var_params:
            query_params.append(('includeSessionParticipants', local_var_params['include_session_participants']))  # noqa: E501
        if 'include_session_recordings' in local_var_params:
            query_params.append(('includeSessionRecordings', local_var_params['include_session_recordings']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain', 'application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/Enrollments/MyEnrollments', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[Enrollment]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)

    def api_enrollments_post(self, **kwargs):  # noqa: E501
        """api_enrollments_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_enrollments_post(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param EnrollUserModel enroll_user_model:
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return self.api_enrollments_post_with_http_info(**kwargs)  # noqa: E501

    def api_enrollments_post_with_http_info(self, **kwargs):  # noqa: E501
        """api_enrollments_post  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.api_enrollments_post_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool: execute request asynchronously
        :param EnrollUserModel enroll_user_model:
        :param _return_http_data_only: response data without head status code
                                       and headers
        :param _preload_content: if False, the urllib3.HTTPResponse object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        local_var_params = locals()

        all_params = ['enroll_user_model']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        for key, val in six.iteritems(local_var_params['kwargs']):
            if key not in all_params:
                raise ApiTypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method api_enrollments_post" % key
                )
            local_var_params[key] = val
        del local_var_params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'enroll_user_model' in local_var_params:
            body_params = local_var_params['enroll_user_model']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/*+json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['bearer']  # noqa: E501

        return self.api_client.call_api(
            '/api/Enrollments', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async_req=local_var_params.get('async_req'),
            _return_http_data_only=local_var_params.get('_return_http_data_only'),  # noqa: E501
            _preload_content=local_var_params.get('_preload_content', True),
            _request_timeout=local_var_params.get('_request_timeout'),
            collection_formats=collection_formats)
