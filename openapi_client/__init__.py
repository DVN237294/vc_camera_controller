# coding: utf-8

# flake8: noqa

"""
    vc_webapi

    Web API for the Virtual Classroom project  # noqa: E501

    The version of the OpenAPI document: v1
    Contact: 237294@via.dk
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

__version__ = "1.0.0"

# import apis into sdk package
from openapi_client.api.authentication_api import AuthenticationApi
from openapi_client.api.comments_api import CommentsApi
from openapi_client.api.courses_api import CoursesApi
from openapi_client.api.enrollments_api import EnrollmentsApi
from openapi_client.api.schedule_api import ScheduleApi
from openapi_client.api.search_api import SearchApi
from openapi_client.api.videos_api import VideosApi
from openapi_client.api.videostream_api import VideostreamApi

# import ApiClient
from openapi_client.api_client import ApiClient
from openapi_client.configuration import Configuration
from openapi_client.exceptions import OpenApiException
from openapi_client.exceptions import ApiTypeError
from openapi_client.exceptions import ApiValueError
from openapi_client.exceptions import ApiKeyError
from openapi_client.exceptions import ApiException
# import models into sdk package
from openapi_client.models.add_session_model import AddSessionModel
from openapi_client.models.authentication_response import AuthenticationResponse
from openapi_client.models.comment import Comment
from openapi_client.models.course import Course
from openapi_client.models.enroll_user_model import EnrollUserModel
from openapi_client.models.enrollment import Enrollment
from openapi_client.models.identity_error import IdentityError
from openapi_client.models.identity_result import IdentityResult
from openapi_client.models.inline_object import InlineObject
from openapi_client.models.login_model import LoginModel
from openapi_client.models.room import Room
from openapi_client.models.room_recording_schedule import RoomRecordingSchedule
from openapi_client.models.scheduled_session import ScheduledSession
from openapi_client.models.search_result import SearchResult
from openapi_client.models.session import Session
from openapi_client.models.ul_token_model import UlTokenModel
from openapi_client.models.user import User
from openapi_client.models.user_signup_model import UserSignupModel
from openapi_client.models.video import Video
from openapi_client.models.video_properties import VideoProperties

