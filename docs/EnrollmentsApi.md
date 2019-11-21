# openapi_client.EnrollmentsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_enrollments_my_enrollments_get**](EnrollmentsApi.md#api_enrollments_my_enrollments_get) | **GET** /api/Enrollments/MyEnrollments | 
[**api_enrollments_post**](EnrollmentsApi.md#api_enrollments_post) | **POST** /api/Enrollments | 


# **api_enrollments_my_enrollments_get**
> list[Enrollment] api_enrollments_my_enrollments_get(limit_enrollments=limit_enrollments, include_sessions=include_sessions, include_session_participants=include_session_participants, include_session_recordings=include_session_recordings)



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

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Create an instance of the API class
api_instance = openapi_client.EnrollmentsApi(openapi_client.ApiClient(configuration))
limit_enrollments = 56 # int |  (optional)
include_sessions = True # bool |  (optional)
include_session_participants = True # bool |  (optional)
include_session_recordings = True # bool |  (optional)

try:
    api_response = api_instance.api_enrollments_my_enrollments_get(limit_enrollments=limit_enrollments, include_sessions=include_sessions, include_session_participants=include_session_participants, include_session_recordings=include_session_recordings)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EnrollmentsApi->api_enrollments_my_enrollments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit_enrollments** | **int**|  | [optional] 
 **include_sessions** | **bool**|  | [optional] 
 **include_session_participants** | **bool**|  | [optional] 
 **include_session_recordings** | **bool**|  | [optional] 

### Return type

[**list[Enrollment]**](Enrollment.md)

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

# **api_enrollments_post**
> api_enrollments_post(enroll_user_model=enroll_user_model)



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

# Defining host is optional and default to http://localhost
configuration.host = "http://localhost"
# Create an instance of the API class
api_instance = openapi_client.EnrollmentsApi(openapi_client.ApiClient(configuration))
enroll_user_model = openapi_client.EnrollUserModel() # EnrollUserModel |  (optional)

try:
    api_instance.api_enrollments_post(enroll_user_model=enroll_user_model)
except ApiException as e:
    print("Exception when calling EnrollmentsApi->api_enrollments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **enroll_user_model** | [**EnrollUserModel**](EnrollUserModel.md)|  | [optional] 

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

