# openapi_client.VideostreamApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_videostream_post**](VideostreamApi.md#api_videostream_post) | **POST** /api/Videostream | 
[**api_videostream_ul_token_body_post**](VideostreamApi.md#api_videostream_ul_token_body_post) | **POST** /api/Videostream/{ulToken}/body | 
[**api_videostream_ul_token_post**](VideostreamApi.md#api_videostream_ul_token_post) | **POST** /api/Videostream/{ulToken} | 
[**api_videostream_video_id_get**](VideostreamApi.md#api_videostream_video_id_get) | **GET** /api/Videostream/{videoId} | 


# **api_videostream_post**
> UlTokenModel api_videostream_post(video=video)



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
api_instance = openapi_client.VideostreamApi(openapi_client.ApiClient(configuration))
video = openapi_client.Video() # Video |  (optional)

try:
    api_response = api_instance.api_videostream_post(video=video)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideostreamApi->api_videostream_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video** | [**Video**](Video.md)|  | [optional] 

### Return type

[**UlTokenModel**](UlTokenModel.md)

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

# **api_videostream_ul_token_body_post**
> Video api_videostream_ul_token_body_post(ul_token, body)



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
api_instance = openapi_client.VideostreamApi(openapi_client.ApiClient(configuration))
ul_token = 'ul_token_example' # str | 
body = '/path/to/file' # file | payload

try:
    api_response = api_instance.api_videostream_ul_token_body_post(ul_token, body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideostreamApi->api_videostream_ul_token_body_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ul_token** | **str**|  | 
 **body** | **file**| payload | 

### Return type

[**Video**](Video.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: application/octet-stream
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_videostream_ul_token_post**
> Video api_videostream_ul_token_post(ul_token, file=file)



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
api_instance = openapi_client.VideostreamApi(openapi_client.ApiClient(configuration))
ul_token = 'ul_token_example' # str | 
file = '/path/to/file' # list[file] |  (optional)

try:
    api_response = api_instance.api_videostream_ul_token_post(ul_token, file=file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideostreamApi->api_videostream_ul_token_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ul_token** | **str**|  | 
 **file** | **list[file]**|  | [optional] 

### Return type

[**Video**](Video.md)

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: text/plain, application/json, text/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_videostream_video_id_get**
> file api_videostream_video_id_get(video_id)



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
api_instance = openapi_client.VideostreamApi(openapi_client.ApiClient(configuration))
video_id = 56 # int | 

try:
    api_response = api_instance.api_videostream_video_id_get(video_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling VideostreamApi->api_videostream_video_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **video_id** | **int**|  | 

### Return type

**file**

### Authorization

[bearer](../README.md#bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

