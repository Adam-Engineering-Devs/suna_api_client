# suna_api_client.ComposioApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**check_profile_name_availability_api_composio_profiles_check_name_availability_get**](ComposioApi.md#check_profile_name_availability_api_composio_profiles_check_name_availability_get) | **GET** /api/composio/profiles/check-name-availability | Check Profile Name Availability
[**composio_webhook_api_composio_webhook_post**](ComposioApi.md#composio_webhook_api_composio_webhook_post) | **POST** /api/composio/webhook | Composio Webhook
[**create_composio_trigger_api_composio_triggers_create_post**](ComposioApi.md#create_composio_trigger_api_composio_triggers_create_post) | **POST** /api/composio/triggers/create | Create Composio Trigger
[**create_profile_api_composio_profiles_post**](ComposioApi.md#create_profile_api_composio_profiles_post) | **POST** /api/composio/profiles | Create Profile
[**discover_composio_tools_api_composio_profiles_profile_id_discover_tools_post**](ComposioApi.md#discover_composio_tools_api_composio_profiles_profile_id_discover_tools_post) | **POST** /api/composio/profiles/{profile_id}/discover-tools | Discover Composio Tools
[**discover_tools_post_api_composio_discover_tools_profile_id_post**](ComposioApi.md#discover_tools_post_api_composio_discover_tools_profile_id_post) | **POST** /api/composio/discover-tools/{profile_id} | Discover Tools Post
[**get_integration_status_api_composio_integration_connected_account_id_status_get**](ComposioApi.md#get_integration_status_api_composio_integration_connected_account_id_status_get) | **GET** /api/composio/integration/{connected_account_id}/status | Get Integration Status
[**get_profile_info_api_composio_profiles_profile_id_get**](ComposioApi.md#get_profile_info_api_composio_profiles_profile_id_get) | **GET** /api/composio/profiles/{profile_id} | Get Profile Info
[**get_profile_mcp_config_api_composio_profiles_profile_id_mcp_config_get**](ComposioApi.md#get_profile_mcp_config_api_composio_profiles_profile_id_mcp_config_get) | **GET** /api/composio/profiles/{profile_id}/mcp-config | Get Profile Mcp Config
[**get_profiles_api_composio_profiles_get**](ComposioApi.md#get_profiles_api_composio_profiles_get) | **GET** /api/composio/profiles | Get Profiles
[**get_toolkit_details_api_composio_toolkits_toolkit_slug_details_get**](ComposioApi.md#get_toolkit_details_api_composio_toolkits_toolkit_slug_details_get) | **GET** /api/composio/toolkits/{toolkit_slug}/details | Get Toolkit Details
[**get_toolkit_icon_api_composio_toolkits_toolkit_slug_icon_get**](ComposioApi.md#get_toolkit_icon_api_composio_toolkits_toolkit_slug_icon_get) | **GET** /api/composio/toolkits/{toolkit_slug}/icon | Get Toolkit Icon
[**health_check_api_composio_health_get**](ComposioApi.md#health_check_api_composio_health_get) | **GET** /api/composio/health | Health Check
[**integrate_toolkit_api_composio_integrate_post**](ComposioApi.md#integrate_toolkit_api_composio_integrate_post) | **POST** /api/composio/integrate | Integrate Toolkit
[**list_apps_with_triggers_api_composio_triggers_apps_get**](ComposioApi.md#list_apps_with_triggers_api_composio_triggers_apps_get) | **GET** /api/composio/triggers/apps | List Apps With Triggers
[**list_categories_api_composio_categories_get**](ComposioApi.md#list_categories_api_composio_categories_get) | **GET** /api/composio/categories | List Categories
[**list_toolkit_tools_api_composio_tools_list_post**](ComposioApi.md#list_toolkit_tools_api_composio_tools_list_post) | **POST** /api/composio/tools/list | List Toolkit Tools
[**list_toolkits_api_composio_toolkits_get**](ComposioApi.md#list_toolkits_api_composio_toolkits_get) | **GET** /api/composio/toolkits | List Toolkits
[**list_triggers_for_app_api_composio_triggers_apps_toolkit_slug_get**](ComposioApi.md#list_triggers_for_app_api_composio_triggers_apps_toolkit_slug_get) | **GET** /api/composio/triggers/apps/{toolkit_slug} | List Triggers For App


# **check_profile_name_availability_api_composio_profiles_check_name_availability_get**
> Dict[str, object] check_profile_name_availability_api_composio_profiles_check_name_availability_get(toolkit_slug, profile_name)

Check Profile Name Availability

### Example


```python
import suna_api_client
from suna_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = suna_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with suna_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suna_api_client.ComposioApi(api_client)
    toolkit_slug = 'toolkit_slug_example' # str | The toolkit slug to check against
    profile_name = 'profile_name_example' # str | The profile name to check

    try:
        # Check Profile Name Availability
        api_response = api_instance.check_profile_name_availability_api_composio_profiles_check_name_availability_get(toolkit_slug, profile_name)
        print("The response of ComposioApi->check_profile_name_availability_api_composio_profiles_check_name_availability_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposioApi->check_profile_name_availability_api_composio_profiles_check_name_availability_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toolkit_slug** | **str**| The toolkit slug to check against | 
 **profile_name** | **str**| The profile name to check | 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **composio_webhook_api_composio_webhook_post**
> object composio_webhook_api_composio_webhook_post()

Composio Webhook

Shared Composio webhook endpoint. Verifies secret, matches triggers, and enqueues execution.

### Example


```python
import suna_api_client
from suna_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = suna_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with suna_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suna_api_client.ComposioApi(api_client)

    try:
        # Composio Webhook
        api_response = api_instance.composio_webhook_api_composio_webhook_post()
        print("The response of ComposioApi->composio_webhook_api_composio_webhook_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposioApi->composio_webhook_api_composio_webhook_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_composio_trigger_api_composio_triggers_create_post**
> Dict[str, object] create_composio_trigger_api_composio_triggers_create_post(create_composio_trigger_request)

Create Composio Trigger

### Example


```python
import suna_api_client
from suna_api_client.models.create_composio_trigger_request import CreateComposioTriggerRequest
from suna_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = suna_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with suna_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suna_api_client.ComposioApi(api_client)
    create_composio_trigger_request = suna_api_client.CreateComposioTriggerRequest() # CreateComposioTriggerRequest | 

    try:
        # Create Composio Trigger
        api_response = api_instance.create_composio_trigger_api_composio_triggers_create_post(create_composio_trigger_request)
        print("The response of ComposioApi->create_composio_trigger_api_composio_triggers_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposioApi->create_composio_trigger_api_composio_triggers_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_composio_trigger_request** | [**CreateComposioTriggerRequest**](CreateComposioTriggerRequest.md)|  | 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_profile_api_composio_profiles_post**
> CoreComposioIntegrationApiProfileResponse create_profile_api_composio_profiles_post(create_profile_request)

Create Profile

### Example


```python
import suna_api_client
from suna_api_client.models.core_composio_integration_api_profile_response import CoreComposioIntegrationApiProfileResponse
from suna_api_client.models.create_profile_request import CreateProfileRequest
from suna_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = suna_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with suna_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suna_api_client.ComposioApi(api_client)
    create_profile_request = suna_api_client.CreateProfileRequest() # CreateProfileRequest | 

    try:
        # Create Profile
        api_response = api_instance.create_profile_api_composio_profiles_post(create_profile_request)
        print("The response of ComposioApi->create_profile_api_composio_profiles_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposioApi->create_profile_api_composio_profiles_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_profile_request** | [**CreateProfileRequest**](CreateProfileRequest.md)|  | 

### Return type

[**CoreComposioIntegrationApiProfileResponse**](CoreComposioIntegrationApiProfileResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discover_composio_tools_api_composio_profiles_profile_id_discover_tools_post**
> Dict[str, object] discover_composio_tools_api_composio_profiles_profile_id_discover_tools_post(profile_id)

Discover Composio Tools

### Example


```python
import suna_api_client
from suna_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = suna_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with suna_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suna_api_client.ComposioApi(api_client)
    profile_id = 'profile_id_example' # str | 

    try:
        # Discover Composio Tools
        api_response = api_instance.discover_composio_tools_api_composio_profiles_profile_id_discover_tools_post(profile_id)
        print("The response of ComposioApi->discover_composio_tools_api_composio_profiles_profile_id_discover_tools_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposioApi->discover_composio_tools_api_composio_profiles_profile_id_discover_tools_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**|  | 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **discover_tools_post_api_composio_discover_tools_profile_id_post**
> Dict[str, object] discover_tools_post_api_composio_discover_tools_profile_id_post(profile_id)

Discover Tools Post

### Example


```python
import suna_api_client
from suna_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = suna_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with suna_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suna_api_client.ComposioApi(api_client)
    profile_id = 'profile_id_example' # str | 

    try:
        # Discover Tools Post
        api_response = api_instance.discover_tools_post_api_composio_discover_tools_profile_id_post(profile_id)
        print("The response of ComposioApi->discover_tools_post_api_composio_discover_tools_profile_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposioApi->discover_tools_post_api_composio_discover_tools_profile_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**|  | 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_integration_status_api_composio_integration_connected_account_id_status_get**
> Dict[str, object] get_integration_status_api_composio_integration_connected_account_id_status_get(connected_account_id)

Get Integration Status

### Example


```python
import suna_api_client
from suna_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = suna_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with suna_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suna_api_client.ComposioApi(api_client)
    connected_account_id = 'connected_account_id_example' # str | 

    try:
        # Get Integration Status
        api_response = api_instance.get_integration_status_api_composio_integration_connected_account_id_status_get(connected_account_id)
        print("The response of ComposioApi->get_integration_status_api_composio_integration_connected_account_id_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposioApi->get_integration_status_api_composio_integration_connected_account_id_status_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **connected_account_id** | **str**|  | 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile_info_api_composio_profiles_profile_id_get**
> Dict[str, object] get_profile_info_api_composio_profiles_profile_id_get(profile_id)

Get Profile Info

### Example


```python
import suna_api_client
from suna_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = suna_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with suna_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suna_api_client.ComposioApi(api_client)
    profile_id = 'profile_id_example' # str | 

    try:
        # Get Profile Info
        api_response = api_instance.get_profile_info_api_composio_profiles_profile_id_get(profile_id)
        print("The response of ComposioApi->get_profile_info_api_composio_profiles_profile_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposioApi->get_profile_info_api_composio_profiles_profile_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**|  | 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profile_mcp_config_api_composio_profiles_profile_id_mcp_config_get**
> Dict[str, object] get_profile_mcp_config_api_composio_profiles_profile_id_mcp_config_get(profile_id)

Get Profile Mcp Config

### Example


```python
import suna_api_client
from suna_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = suna_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with suna_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suna_api_client.ComposioApi(api_client)
    profile_id = 'profile_id_example' # str | 

    try:
        # Get Profile Mcp Config
        api_response = api_instance.get_profile_mcp_config_api_composio_profiles_profile_id_mcp_config_get(profile_id)
        print("The response of ComposioApi->get_profile_mcp_config_api_composio_profiles_profile_id_mcp_config_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposioApi->get_profile_mcp_config_api_composio_profiles_profile_id_mcp_config_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**|  | 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_profiles_api_composio_profiles_get**
> Dict[str, object] get_profiles_api_composio_profiles_get(toolkit_slug=toolkit_slug)

Get Profiles

### Example


```python
import suna_api_client
from suna_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = suna_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with suna_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suna_api_client.ComposioApi(api_client)
    toolkit_slug = 'toolkit_slug_example' # str |  (optional)

    try:
        # Get Profiles
        api_response = api_instance.get_profiles_api_composio_profiles_get(toolkit_slug=toolkit_slug)
        print("The response of ComposioApi->get_profiles_api_composio_profiles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposioApi->get_profiles_api_composio_profiles_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toolkit_slug** | **str**|  | [optional] 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_toolkit_details_api_composio_toolkits_toolkit_slug_details_get**
> Dict[str, object] get_toolkit_details_api_composio_toolkits_toolkit_slug_details_get(toolkit_slug)

Get Toolkit Details

### Example


```python
import suna_api_client
from suna_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = suna_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with suna_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suna_api_client.ComposioApi(api_client)
    toolkit_slug = 'toolkit_slug_example' # str | 

    try:
        # Get Toolkit Details
        api_response = api_instance.get_toolkit_details_api_composio_toolkits_toolkit_slug_details_get(toolkit_slug)
        print("The response of ComposioApi->get_toolkit_details_api_composio_toolkits_toolkit_slug_details_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposioApi->get_toolkit_details_api_composio_toolkits_toolkit_slug_details_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toolkit_slug** | **str**|  | 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_toolkit_icon_api_composio_toolkits_toolkit_slug_icon_get**
> object get_toolkit_icon_api_composio_toolkits_toolkit_slug_icon_get(toolkit_slug)

Get Toolkit Icon

### Example


```python
import suna_api_client
from suna_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = suna_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with suna_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suna_api_client.ComposioApi(api_client)
    toolkit_slug = 'toolkit_slug_example' # str | 

    try:
        # Get Toolkit Icon
        api_response = api_instance.get_toolkit_icon_api_composio_toolkits_toolkit_slug_icon_get(toolkit_slug)
        print("The response of ComposioApi->get_toolkit_icon_api_composio_toolkits_toolkit_slug_icon_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposioApi->get_toolkit_icon_api_composio_toolkits_toolkit_slug_icon_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toolkit_slug** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **health_check_api_composio_health_get**
> Dict[str, str] health_check_api_composio_health_get()

Health Check

### Example


```python
import suna_api_client
from suna_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = suna_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with suna_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suna_api_client.ComposioApi(api_client)

    try:
        # Health Check
        api_response = api_instance.health_check_api_composio_health_get()
        print("The response of ComposioApi->health_check_api_composio_health_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposioApi->health_check_api_composio_health_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, str]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **integrate_toolkit_api_composio_integrate_post**
> IntegrationStatusResponse integrate_toolkit_api_composio_integrate_post(integrate_toolkit_request)

Integrate Toolkit

### Example


```python
import suna_api_client
from suna_api_client.models.integrate_toolkit_request import IntegrateToolkitRequest
from suna_api_client.models.integration_status_response import IntegrationStatusResponse
from suna_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = suna_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with suna_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suna_api_client.ComposioApi(api_client)
    integrate_toolkit_request = suna_api_client.IntegrateToolkitRequest() # IntegrateToolkitRequest | 

    try:
        # Integrate Toolkit
        api_response = api_instance.integrate_toolkit_api_composio_integrate_post(integrate_toolkit_request)
        print("The response of ComposioApi->integrate_toolkit_api_composio_integrate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposioApi->integrate_toolkit_api_composio_integrate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **integrate_toolkit_request** | [**IntegrateToolkitRequest**](IntegrateToolkitRequest.md)|  | 

### Return type

[**IntegrationStatusResponse**](IntegrationStatusResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_apps_with_triggers_api_composio_triggers_apps_get**
> Dict[str, object] list_apps_with_triggers_api_composio_triggers_apps_get()

List Apps With Triggers

### Example


```python
import suna_api_client
from suna_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = suna_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with suna_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suna_api_client.ComposioApi(api_client)

    try:
        # List Apps With Triggers
        api_response = api_instance.list_apps_with_triggers_api_composio_triggers_apps_get()
        print("The response of ComposioApi->list_apps_with_triggers_api_composio_triggers_apps_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposioApi->list_apps_with_triggers_api_composio_triggers_apps_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_categories_api_composio_categories_get**
> Dict[str, object] list_categories_api_composio_categories_get()

List Categories

### Example


```python
import suna_api_client
from suna_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = suna_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with suna_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suna_api_client.ComposioApi(api_client)

    try:
        # List Categories
        api_response = api_instance.list_categories_api_composio_categories_get()
        print("The response of ComposioApi->list_categories_api_composio_categories_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposioApi->list_categories_api_composio_categories_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_toolkit_tools_api_composio_tools_list_post**
> object list_toolkit_tools_api_composio_tools_list_post(tools_list_request)

List Toolkit Tools

### Example


```python
import suna_api_client
from suna_api_client.models.tools_list_request import ToolsListRequest
from suna_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = suna_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with suna_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suna_api_client.ComposioApi(api_client)
    tools_list_request = suna_api_client.ToolsListRequest() # ToolsListRequest | 

    try:
        # List Toolkit Tools
        api_response = api_instance.list_toolkit_tools_api_composio_tools_list_post(tools_list_request)
        print("The response of ComposioApi->list_toolkit_tools_api_composio_tools_list_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposioApi->list_toolkit_tools_api_composio_tools_list_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tools_list_request** | [**ToolsListRequest**](ToolsListRequest.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_toolkits_api_composio_toolkits_get**
> Dict[str, object] list_toolkits_api_composio_toolkits_get(limit=limit, cursor=cursor, search=search, category=category)

List Toolkits

### Example


```python
import suna_api_client
from suna_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = suna_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with suna_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suna_api_client.ComposioApi(api_client)
    limit = 100 # int |  (optional) (default to 100)
    cursor = 'cursor_example' # str |  (optional)
    search = 'search_example' # str |  (optional)
    category = 'category_example' # str |  (optional)

    try:
        # List Toolkits
        api_response = api_instance.list_toolkits_api_composio_toolkits_get(limit=limit, cursor=cursor, search=search, category=category)
        print("The response of ComposioApi->list_toolkits_api_composio_toolkits_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposioApi->list_toolkits_api_composio_toolkits_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional] [default to 100]
 **cursor** | **str**|  | [optional] 
 **search** | **str**|  | [optional] 
 **category** | **str**|  | [optional] 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_triggers_for_app_api_composio_triggers_apps_toolkit_slug_get**
> Dict[str, object] list_triggers_for_app_api_composio_triggers_apps_toolkit_slug_get(toolkit_slug)

List Triggers For App

### Example


```python
import suna_api_client
from suna_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = suna_api_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with suna_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suna_api_client.ComposioApi(api_client)
    toolkit_slug = 'toolkit_slug_example' # str | 

    try:
        # List Triggers For App
        api_response = api_instance.list_triggers_for_app_api_composio_triggers_apps_toolkit_slug_get(toolkit_slug)
        print("The response of ComposioApi->list_triggers_for_app_api_composio_triggers_apps_toolkit_slug_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ComposioApi->list_triggers_for_app_api_composio_triggers_apps_toolkit_slug_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **toolkit_slug** | **str**|  | 

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

