# openapi_client.ScheduleApi

All URIs are relative to *http://localhost:58180*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_schedule_add_room_post**](ScheduleApi.md#api_schedule_add_room_post) | **POST** /api/Schedule/AddRoom | 
[**api_schedule_for_room_room_name_get**](ScheduleApi.md#api_schedule_for_room_room_name_get) | **GET** /api/Schedule/ForRoom/{roomName} | 
[**api_schedule_get_rooms_get**](ScheduleApi.md#api_schedule_get_rooms_get) | **GET** /api/Schedule/GetRooms | 
[**api_schedule_post**](ScheduleApi.md#api_schedule_post) | **POST** /api/Schedule | 


# **api_schedule_add_room_post**
> Room api_schedule_add_room_post(room=room)



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
api_instance = openapi_client.ScheduleApi(openapi_client.ApiClient(configuration))
room = openapi_client.Room() # Room |  (optional)

try:
    api_response = api_instance.api_schedule_add_room_post(room=room)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleApi->api_schedule_add_room_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room** | [**Room**](Room.md)|  | [optional] 

### Return type

[**Room**](Room.md)

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

# **api_schedule_for_room_room_name_get**
> RoomRecordingSchedule api_schedule_for_room_room_name_get(room_name, start_utc=start_utc, end_utc=end_utc)



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
api_instance = openapi_client.ScheduleApi(openapi_client.ApiClient(configuration))
room_name = 'room_name_example' # str | 
start_utc = '2013-10-20T19:20:30+01:00' # datetime |  (optional)
end_utc = '2013-10-20T19:20:30+01:00' # datetime |  (optional)

try:
    api_response = api_instance.api_schedule_for_room_room_name_get(room_name, start_utc=start_utc, end_utc=end_utc)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleApi->api_schedule_for_room_room_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **room_name** | **str**|  | 
 **start_utc** | **datetime**|  | [optional] 
 **end_utc** | **datetime**|  | [optional] 

### Return type

[**RoomRecordingSchedule**](RoomRecordingSchedule.md)

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

# **api_schedule_get_rooms_get**
> list[Room] api_schedule_get_rooms_get(limit=limit)



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
api_instance = openapi_client.ScheduleApi(openapi_client.ApiClient(configuration))
limit = 0 # int |  (optional) (default to 0)

try:
    api_response = api_instance.api_schedule_get_rooms_get(limit=limit)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ScheduleApi->api_schedule_get_rooms_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 0]

### Return type

[**list[Room]**](Room.md)

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

# **api_schedule_post**
> api_schedule_post(scheduled_session=scheduled_session)



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
api_instance = openapi_client.ScheduleApi(openapi_client.ApiClient(configuration))
scheduled_session = [openapi_client.ScheduledSession()] # list[ScheduledSession] |  (optional)

try:
    api_instance.api_schedule_post(scheduled_session=scheduled_session)
except ApiException as e:
    print("Exception when calling ScheduleApi->api_schedule_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **scheduled_session** | [**list[ScheduledSession]**](ScheduledSession.md)|  | [optional] 

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

