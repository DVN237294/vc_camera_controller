# openapi_client.SearchApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_search_get**](SearchApi.md#api_search_get) | **GET** /api/Search | 


# **api_search_get**
> SearchResult api_search_get(query=query, limit=limit)



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
api_instance = openapi_client.SearchApi(openapi_client.ApiClient(configuration))
query = 'query_example' # str |  (optional)
limit = 0 # int |  (optional) (default to 0)

try:
    api_response = api_instance.api_search_get(query=query, limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SearchApi->api_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | [optional] 
 **limit** | **int**|  | [optional] [default to 0]

### Return type

[**SearchResult**](SearchResult.md)

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

