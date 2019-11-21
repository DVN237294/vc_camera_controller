# openapi_client.VideosApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_videos_get**](VideosApi.md#api_videos_get) | **GET** /api/Videos | 
[**api_videos_id_delete**](VideosApi.md#api_videos_id_delete) | **DELETE** /api/Videos/{id} | 
[**api_videos_id_get**](VideosApi.md#api_videos_id_get) | **GET** /api/Videos/{id} | 
[**api_videos_id_put**](VideosApi.md#api_videos_id_put) | **PUT** /api/Videos/{id} | 
[**api_videos_post**](VideosApi.md#api_videos_post) | **POST** /api/Videos | 


# **api_videos_get**
> list[Video] api_videos_get(limit=limit)



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
api_instance = openapi_client.VideosApi(openapi_client.ApiClient(configuration))
limit = 56 # int |  (optional)

try:
    api_response = api_instance.api_videos_get(limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideosApi->api_videos_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] 

### Return type

[**list[Video]**](Video.md)

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

# **api_videos_id_delete**
> api_videos_id_delete(id)



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
api_instance = openapi_client.VideosApi(openapi_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_instance.api_videos_id_delete(id)
except ApiException as e:
    print("Exception when calling VideosApi->api_videos_id_delete: %s\n" % e)
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

# **api_videos_id_get**
> api_videos_id_get(id)



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
api_instance = openapi_client.VideosApi(openapi_client.ApiClient(configuration))
id = 56 # int | 

try:
    api_instance.api_videos_id_get(id)
except ApiException as e:
    print("Exception when calling VideosApi->api_videos_id_get: %s\n" % e)
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

# **api_videos_id_put**
> api_videos_id_put(id, video=video)



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
api_instance = openapi_client.VideosApi(openapi_client.ApiClient(configuration))
id = 56 # int | 
video = openapi_client.Video() # Video |  (optional)

try:
    api_instance.api_videos_id_put(id, video=video)
except ApiException as e:
    print("Exception when calling VideosApi->api_videos_id_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 
 **video** | [**Video**](Video.md)|  | [optional] 

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

# **api_videos_post**
> api_videos_post(video=video)



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
api_instance = openapi_client.VideosApi(openapi_client.ApiClient(configuration))
video = openapi_client.Video() # Video |  (optional)

try:
    api_instance.api_videos_post(video=video)
except ApiException as e:
    print("Exception when calling VideosApi->api_videos_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video** | [**Video**](Video.md)|  | [optional] 

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

