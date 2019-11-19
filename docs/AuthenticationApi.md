# openapi_client.AuthenticationApi

All URIs are relative to *http://localhost:58180*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_authentication_post**](AuthenticationApi.md#api_authentication_post) | **POST** /api/Authentication | 
[**api_authentication_register_post**](AuthenticationApi.md#api_authentication_register_post) | **POST** /api/Authentication/Register | 


# **api_authentication_post**
> AuthenticationResponse api_authentication_post(login_model=login_model)



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
api_instance = openapi_client.AuthenticationApi(openapi_client.ApiClient(configuration))
login_model = openapi_client.LoginModel() # LoginModel |  (optional)

try:
    api_response = api_instance.api_authentication_post(login_model=login_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->api_authentication_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_model** | [**LoginModel**](LoginModel.md)|  | [optional] 

### Return type

[**AuthenticationResponse**](AuthenticationResponse.md)

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

# **api_authentication_register_post**
> IdentityResult api_authentication_register_post(user_signup_model=user_signup_model)



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
api_instance = openapi_client.AuthenticationApi(openapi_client.ApiClient(configuration))
user_signup_model = openapi_client.UserSignupModel() # UserSignupModel |  (optional)

try:
    api_response = api_instance.api_authentication_register_post(user_signup_model=user_signup_model)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AuthenticationApi->api_authentication_register_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_signup_model** | [**UserSignupModel**](UserSignupModel.md)|  | [optional] 

### Return type

[**IdentityResult**](IdentityResult.md)

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

