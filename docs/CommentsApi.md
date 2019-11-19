# openapi_client.CommentsApi

All URIs are relative to *http://localhost:58180*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_comments_id_delete**](CommentsApi.md#api_comments_id_delete) | **DELETE** /api/Comments/{id} | 
[**api_comments_post**](CommentsApi.md#api_comments_post) | **POST** /api/Comments | 
[**api_comments_video_id_get**](CommentsApi.md#api_comments_video_id_get) | **GET** /api/Comments/{videoId} | 


# **api_comments_id_delete**
> api_comments_id_delete(id)



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
api_instance = openapi_client.CommentsApi(openapi_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_instance.api_comments_id_delete(id)
except ApiException as e:
    print("Exception when calling CommentsApi->api_comments_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

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

# **api_comments_post**
> api_comments_post(message=message, video_id=video_id)



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
api_instance = openapi_client.CommentsApi(openapi_client.ApiClient(configuration))
message = 'message_example' # str |  (optional)
video_id = 56 # int |  (optional)

try:
    api_instance.api_comments_post(message=message, video_id=video_id)
except ApiException as e:
    print("Exception when calling CommentsApi->api_comments_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **message** | **str**|  | [optional] 
 **video_id** | **int**|  | [optional] 

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

# **api_comments_video_id_get**
> list[Comment] api_comments_video_id_get(video_id)



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
api_instance = openapi_client.CommentsApi(openapi_client.ApiClient(configuration))
video_id = 56 # int | 

try:
    api_response = api_instance.api_comments_video_id_get(video_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentsApi->api_comments_video_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**|  | 

### Return type

[**list[Comment]**](Comment.md)

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

