# openapi-client
Web API for the Virtual Classroom project

This Python package is automatically generated by the [OpenAPI Generator](https://openapi-generator.tech) project:

- API version: v1
- Package version: 1.0.0
- Build package: org.openapitools.codegen.languages.PythonClientCodegen

## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on a repository, you can install directly using:

```sh
pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/GIT_USER_ID/GIT_REPO_ID.git`)

Then import the package:
```python
import openapi_client 
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import openapi_client
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

```python
from __future__ import print_function
import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint

configuration = openapi_client.Configuration()
# Configure Bearer authorization (JWT): bearer
configuration.access_token = 'YOUR_BEARER_TOKEN'

# Defining host is optional and default to http://localhost:58180
configuration.host = "http://localhost:58180"
# Create an instance of the API class
api_instance = openapi_client.AuthenticationApi(openapi_client.ApiClient(configuration))
login_model = openapi_client.LoginModel() # LoginModel |  (optional)

try:
    api_response = api_instance.api_authentication_post(login_model=login_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->api_authentication_post: %s\n" % e)

```

## Documentation for API Endpoints

All URIs are relative to *http://localhost:58180*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AuthenticationApi* | [**api_authentication_post**](docs/AuthenticationApi.md#api_authentication_post) | **POST** /api/Authentication | 
*AuthenticationApi* | [**api_authentication_register_post**](docs/AuthenticationApi.md#api_authentication_register_post) | **POST** /api/Authentication/Register | 
*CommentsApi* | [**api_comments_id_delete**](docs/CommentsApi.md#api_comments_id_delete) | **DELETE** /api/Comments/{id} | 
*CommentsApi* | [**api_comments_post**](docs/CommentsApi.md#api_comments_post) | **POST** /api/Comments | 
*CommentsApi* | [**api_comments_video_id_get**](docs/CommentsApi.md#api_comments_video_id_get) | **GET** /api/Comments/{videoId} | 
*CoursesApi* | [**api_courses_add_post**](docs/CoursesApi.md#api_courses_add_post) | **POST** /api/Courses/Add | 
*CoursesApi* | [**api_courses_add_range_post**](docs/CoursesApi.md#api_courses_add_range_post) | **POST** /api/Courses/AddRange | 
*CoursesApi* | [**api_courses_course_id_add_session_post**](docs/CoursesApi.md#api_courses_course_id_add_session_post) | **POST** /api/Courses/{courseId}/AddSession | 
*CoursesApi* | [**api_courses_get**](docs/CoursesApi.md#api_courses_get) | **GET** /api/Courses | 
*CoursesApi* | [**api_courses_id_get**](docs/CoursesApi.md#api_courses_id_get) | **GET** /api/Courses/{id} | 
*EnrollmentsApi* | [**api_enrollments_my_enrollments_get**](docs/EnrollmentsApi.md#api_enrollments_my_enrollments_get) | **GET** /api/Enrollments/MyEnrollments | 
*EnrollmentsApi* | [**api_enrollments_post**](docs/EnrollmentsApi.md#api_enrollments_post) | **POST** /api/Enrollments | 
*ScheduleApi* | [**api_schedule_add_room_post**](docs/ScheduleApi.md#api_schedule_add_room_post) | **POST** /api/Schedule/AddRoom | 
*ScheduleApi* | [**api_schedule_for_room_room_name_get**](docs/ScheduleApi.md#api_schedule_for_room_room_name_get) | **GET** /api/Schedule/ForRoom/{roomName} | 
*ScheduleApi* | [**api_schedule_get_rooms_get**](docs/ScheduleApi.md#api_schedule_get_rooms_get) | **GET** /api/Schedule/GetRooms | 
*ScheduleApi* | [**api_schedule_post**](docs/ScheduleApi.md#api_schedule_post) | **POST** /api/Schedule | 
*SearchApi* | [**api_search_get**](docs/SearchApi.md#api_search_get) | **GET** /api/Search | 
*VideosApi* | [**api_videos_get**](docs/VideosApi.md#api_videos_get) | **GET** /api/Videos | 
*VideosApi* | [**api_videos_id_delete**](docs/VideosApi.md#api_videos_id_delete) | **DELETE** /api/Videos/{id} | 
*VideosApi* | [**api_videos_id_get**](docs/VideosApi.md#api_videos_id_get) | **GET** /api/Videos/{id} | 
*VideosApi* | [**api_videos_id_put**](docs/VideosApi.md#api_videos_id_put) | **PUT** /api/Videos/{id} | 
*VideosApi* | [**api_videos_post**](docs/VideosApi.md#api_videos_post) | **POST** /api/Videos | 
*VideostreamApi* | [**api_videostream_post**](docs/VideostreamApi.md#api_videostream_post) | **POST** /api/Videostream | 
*VideostreamApi* | [**api_videostream_ul_token_body_post**](docs/VideostreamApi.md#api_videostream_ul_token_body_post) | **POST** /api/Videostream/{ulToken}/body | 
*VideostreamApi* | [**api_videostream_ul_token_post**](docs/VideostreamApi.md#api_videostream_ul_token_post) | **POST** /api/Videostream/{ulToken} | 
*VideostreamApi* | [**api_videostream_video_id_get**](docs/VideostreamApi.md#api_videostream_video_id_get) | **GET** /api/Videostream/{videoId} | 


## Documentation For Models

 - [AddSessionModel](docs/AddSessionModel.md)
 - [AuthenticationResponse](docs/AuthenticationResponse.md)
 - [Comment](docs/Comment.md)
 - [Course](docs/Course.md)
 - [EnrollUserModel](docs/EnrollUserModel.md)
 - [Enrollment](docs/Enrollment.md)
 - [IdentityError](docs/IdentityError.md)
 - [IdentityResult](docs/IdentityResult.md)
 - [InlineObject](docs/InlineObject.md)
 - [LoginModel](docs/LoginModel.md)
 - [Room](docs/Room.md)
 - [RoomRecordingSchedule](docs/RoomRecordingSchedule.md)
 - [ScheduledSession](docs/ScheduledSession.md)
 - [SearchResult](docs/SearchResult.md)
 - [Session](docs/Session.md)
 - [UlTokenModel](docs/UlTokenModel.md)
 - [User](docs/User.md)
 - [UserSignupModel](docs/UserSignupModel.md)
 - [Video](docs/Video.md)
 - [VideoProperties](docs/VideoProperties.md)


## Documentation For Authorization


## bearer

- **Type**: Bearer authentication (JWT)


## Author

237294@via.dk


