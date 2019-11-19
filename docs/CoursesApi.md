# openapi_client.CoursesApi

All URIs are relative to *http://localhost:58180*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_courses_add_post**](CoursesApi.md#api_courses_add_post) | **POST** /api/Courses/Add | 
[**api_courses_add_range_post**](CoursesApi.md#api_courses_add_range_post) | **POST** /api/Courses/AddRange | 
[**api_courses_course_id_add_session_post**](CoursesApi.md#api_courses_course_id_add_session_post) | **POST** /api/Courses/{courseId}/AddSession | 
[**api_courses_get**](CoursesApi.md#api_courses_get) | **GET** /api/Courses | 
[**api_courses_id_get**](CoursesApi.md#api_courses_id_get) | **GET** /api/Courses/{id} | 


# **api_courses_add_post**
> api_courses_add_post(course=course)



### Example

* Bearer (JWT) Authentication (bearer):
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
api_instance = openapi_client.CoursesApi(openapi_client.ApiClient(configuration))
course = openapi_client.Course() # Course |  (optional)

try:
    api_instance.api_courses_add_post(course=course)
except ApiException as e:
    print("Exception when calling CoursesApi->api_courses_add_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course** | [**Course**](Course.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_courses_add_range_post**
> int api_courses_add_range_post(course=course)



### Example

* Bearer (JWT) Authentication (bearer):
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
api_instance = openapi_client.CoursesApi(openapi_client.ApiClient(configuration))
course = [openapi_client.Course()] # list[Course] |  (optional)

try:
    api_response = api_instance.api_courses_add_range_post(course=course)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoursesApi->api_courses_add_range_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course** | [**list[Course]**](Course.md)|  | [optional] 

### Return type

**int**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_courses_course_id_add_session_post**
> api_courses_course_id_add_session_post(course_id, add_session_model=add_session_model)



### Example

* Bearer (JWT) Authentication (bearer):
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
api_instance = openapi_client.CoursesApi(openapi_client.ApiClient(configuration))
course_id = 56 # int | 
add_session_model = openapi_client.AddSessionModel() # AddSessionModel |  (optional)

try:
    api_instance.api_courses_course_id_add_session_post(course_id, add_session_model=add_session_model)
except ApiException as e:
    print("Exception when calling CoursesApi->api_courses_course_id_add_session_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **course_id** | **int**|  | 
 **add_session_model** | [**AddSessionModel**](AddSessionModel.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_courses_get**
> list[Course] api_courses_get(limit_courses=limit_courses, include_sessions=include_sessions, include_session_recordings=include_session_recordings, include_session_participants=include_session_participants)



### Example

* Bearer (JWT) Authentication (bearer):
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
api_instance = openapi_client.CoursesApi(openapi_client.ApiClient(configuration))
limit_courses = 2147483647 # int |  (optional) (default to 2147483647)
include_sessions = False # bool |  (optional) (default to False)
include_session_recordings = False # bool |  (optional) (default to False)
include_session_participants = False # bool |  (optional) (default to False)

try:
    api_response = api_instance.api_courses_get(limit_courses=limit_courses, include_sessions=include_sessions, include_session_recordings=include_session_recordings, include_session_participants=include_session_participants)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CoursesApi->api_courses_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit_courses** | **int**|  | [optional] [default to 2147483647]
 **include_sessions** | **bool**|  | [optional] [default to False]
 **include_session_recordings** | **bool**|  | [optional] [default to False]
 **include_session_participants** | **bool**|  | [optional] [default to False]

### Return type

[**list[Course]**](Course.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_courses_id_get**
> api_courses_id_get(id, include_sessions=include_sessions, include_session_recordings=include_session_recordings, include_session_participants=include_session_participants)



### Example

* Bearer (JWT) Authentication (bearer):
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
api_instance = openapi_client.CoursesApi(openapi_client.ApiClient(configuration))
id = 56 # int | 
include_sessions = False # bool |  (optional) (default to False)
include_session_recordings = False # bool |  (optional) (default to False)
include_session_participants = False # bool |  (optional) (default to False)

try:
    api_instance.api_courses_id_get(id, include_sessions=include_sessions, include_session_recordings=include_session_recordings, include_session_participants=include_session_participants)
except ApiException as e:
    print("Exception when calling CoursesApi->api_courses_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **include_sessions** | **bool**|  | [optional] [default to False]
 **include_session_recordings** | **bool**|  | [optional] [default to False]
 **include_session_participants** | **bool**|  | [optional] [default to False]

### Return type

void (empty response body)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

