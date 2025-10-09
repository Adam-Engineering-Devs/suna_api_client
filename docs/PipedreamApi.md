# suna_api_client.PipedreamApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**connect_credential_profile_api_pipedream_profiles_profile_id_connect_post**](PipedreamApi.md#connect_credential_profile_api_pipedream_profiles_profile_id_connect_post) | **POST** /api/pipedream/profiles/{profile_id}/connect | Connect Credential Profile
[**create_connection_token_api_pipedream_connection_token_post**](PipedreamApi.md#create_connection_token_api_pipedream_connection_token_post) | **POST** /api/pipedream/connection-token | Create Connection Token
[**create_credential_profile_api_pipedream_profiles_post**](PipedreamApi.md#create_credential_profile_api_pipedream_profiles_post) | **POST** /api/pipedream/profiles | Create Credential Profile
[**create_mcp_connection_api_pipedream_mcp_connect_post**](PipedreamApi.md#create_mcp_connection_api_pipedream_mcp_connect_post) | **POST** /api/pipedream/mcp/connect | Create Mcp Connection
[**delete_credential_profile_api_pipedream_profiles_profile_id_delete**](PipedreamApi.md#delete_credential_profile_api_pipedream_profiles_profile_id_delete) | **DELETE** /api/pipedream/profiles/{profile_id} | Delete Credential Profile
[**discover_mcp_servers_api_pipedream_mcp_discover_post**](PipedreamApi.md#discover_mcp_servers_api_pipedream_mcp_discover_post) | **POST** /api/pipedream/mcp/discover | Discover Mcp Servers
[**discover_mcp_servers_for_profile_api_pipedream_mcp_discover_profile_post**](PipedreamApi.md#discover_mcp_servers_for_profile_api_pipedream_mcp_discover_profile_post) | **POST** /api/pipedream/mcp/discover-profile | Discover Mcp Servers For Profile
[**get_app_icon_api_pipedream_apps_app_slug_icon_get**](PipedreamApi.md#get_app_icon_api_pipedream_apps_app_slug_icon_get) | **GET** /api/pipedream/apps/{app_slug}/icon | Get App Icon
[**get_app_tools_api_pipedream_apps_app_slug_tools_get**](PipedreamApi.md#get_app_tools_api_pipedream_apps_app_slug_tools_get) | **GET** /api/pipedream/apps/{app_slug}/tools | Get App Tools
[**get_credential_profile_api_pipedream_profiles_profile_id_get**](PipedreamApi.md#get_credential_profile_api_pipedream_profiles_profile_id_get) | **GET** /api/pipedream/profiles/{profile_id} | Get Credential Profile
[**get_credential_profiles_api_pipedream_profiles_get**](PipedreamApi.md#get_credential_profiles_api_pipedream_profiles_get) | **GET** /api/pipedream/profiles | Get Credential Profiles
[**get_pipedream_apps_api_pipedream_apps_get**](PipedreamApi.md#get_pipedream_apps_api_pipedream_apps_get) | **GET** /api/pipedream/apps | Get Pipedream Apps
[**get_popular_pipedream_apps_api_pipedream_apps_popular_get**](PipedreamApi.md#get_popular_pipedream_apps_api_pipedream_apps_popular_get) | **GET** /api/pipedream/apps/popular | Get Popular Pipedream Apps
[**get_profile_connections_api_pipedream_profiles_profile_id_connections_get**](PipedreamApi.md#get_profile_connections_api_pipedream_profiles_profile_id_connections_get) | **GET** /api/pipedream/profiles/{profile_id}/connections | Get Profile Connections
[**get_user_connections_api_pipedream_connections_get**](PipedreamApi.md#get_user_connections_api_pipedream_connections_get) | **GET** /api/pipedream/connections | Get User Connections
[**update_credential_profile_api_pipedream_profiles_profile_id_put**](PipedreamApi.md#update_credential_profile_api_pipedream_profiles_profile_id_put) | **PUT** /api/pipedream/profiles/{profile_id} | Update Credential Profile


# **connect_credential_profile_api_pipedream_profiles_profile_id_connect_post**
> object connect_credential_profile_api_pipedream_profiles_profile_id_connect_post(profile_id, app=app)

Connect Credential Profile

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
    api_instance = suna_api_client.PipedreamApi(api_client)
    profile_id = 'profile_id_example' # str | 
    app = 'app_example' # str |  (optional)

    try:
        # Connect Credential Profile
        api_response = api_instance.connect_credential_profile_api_pipedream_profiles_profile_id_connect_post(profile_id, app=app)
        print("The response of PipedreamApi->connect_credential_profile_api_pipedream_profiles_profile_id_connect_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipedreamApi->connect_credential_profile_api_pipedream_profiles_profile_id_connect_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**|  | 
 **app** | **str**|  | [optional] 

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

# **create_connection_token_api_pipedream_connection_token_post**
> ConnectionTokenResponse create_connection_token_api_pipedream_connection_token_post(create_connection_token_request)

Create Connection Token

### Example


```python
import suna_api_client
from suna_api_client.models.connection_token_response import ConnectionTokenResponse
from suna_api_client.models.create_connection_token_request import CreateConnectionTokenRequest
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
    api_instance = suna_api_client.PipedreamApi(api_client)
    create_connection_token_request = suna_api_client.CreateConnectionTokenRequest() # CreateConnectionTokenRequest | 

    try:
        # Create Connection Token
        api_response = api_instance.create_connection_token_api_pipedream_connection_token_post(create_connection_token_request)
        print("The response of PipedreamApi->create_connection_token_api_pipedream_connection_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipedreamApi->create_connection_token_api_pipedream_connection_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_connection_token_request** | [**CreateConnectionTokenRequest**](CreateConnectionTokenRequest.md)|  | 

### Return type

[**ConnectionTokenResponse**](ConnectionTokenResponse.md)

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

# **create_credential_profile_api_pipedream_profiles_post**
> CorePipedreamApiProfileResponse create_credential_profile_api_pipedream_profiles_post(profile_request)

Create Credential Profile

### Example


```python
import suna_api_client
from suna_api_client.models.core_pipedream_api_profile_response import CorePipedreamApiProfileResponse
from suna_api_client.models.profile_request import ProfileRequest
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
    api_instance = suna_api_client.PipedreamApi(api_client)
    profile_request = suna_api_client.ProfileRequest() # ProfileRequest | 

    try:
        # Create Credential Profile
        api_response = api_instance.create_credential_profile_api_pipedream_profiles_post(profile_request)
        print("The response of PipedreamApi->create_credential_profile_api_pipedream_profiles_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipedreamApi->create_credential_profile_api_pipedream_profiles_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_request** | [**ProfileRequest**](ProfileRequest.md)|  | 

### Return type

[**CorePipedreamApiProfileResponse**](CorePipedreamApiProfileResponse.md)

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

# **create_mcp_connection_api_pipedream_mcp_connect_post**
> MCPConnectionResponse create_mcp_connection_api_pipedream_mcp_connect_post(mcp_connection_request)

Create Mcp Connection

### Example


```python
import suna_api_client
from suna_api_client.models.mcp_connection_request import MCPConnectionRequest
from suna_api_client.models.mcp_connection_response import MCPConnectionResponse
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
    api_instance = suna_api_client.PipedreamApi(api_client)
    mcp_connection_request = suna_api_client.MCPConnectionRequest() # MCPConnectionRequest | 

    try:
        # Create Mcp Connection
        api_response = api_instance.create_mcp_connection_api_pipedream_mcp_connect_post(mcp_connection_request)
        print("The response of PipedreamApi->create_mcp_connection_api_pipedream_mcp_connect_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipedreamApi->create_mcp_connection_api_pipedream_mcp_connect_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mcp_connection_request** | [**MCPConnectionRequest**](MCPConnectionRequest.md)|  | 

### Return type

[**MCPConnectionResponse**](MCPConnectionResponse.md)

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

# **delete_credential_profile_api_pipedream_profiles_profile_id_delete**
> object delete_credential_profile_api_pipedream_profiles_profile_id_delete(profile_id)

Delete Credential Profile

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
    api_instance = suna_api_client.PipedreamApi(api_client)
    profile_id = 'profile_id_example' # str | 

    try:
        # Delete Credential Profile
        api_response = api_instance.delete_credential_profile_api_pipedream_profiles_profile_id_delete(profile_id)
        print("The response of PipedreamApi->delete_credential_profile_api_pipedream_profiles_profile_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipedreamApi->delete_credential_profile_api_pipedream_profiles_profile_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**|  | 

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

# **discover_mcp_servers_api_pipedream_mcp_discover_post**
> MCPDiscoveryResponse discover_mcp_servers_api_pipedream_mcp_discover_post(mcp_discovery_request)

Discover Mcp Servers

### Example


```python
import suna_api_client
from suna_api_client.models.mcp_discovery_request import MCPDiscoveryRequest
from suna_api_client.models.mcp_discovery_response import MCPDiscoveryResponse
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
    api_instance = suna_api_client.PipedreamApi(api_client)
    mcp_discovery_request = suna_api_client.MCPDiscoveryRequest() # MCPDiscoveryRequest | 

    try:
        # Discover Mcp Servers
        api_response = api_instance.discover_mcp_servers_api_pipedream_mcp_discover_post(mcp_discovery_request)
        print("The response of PipedreamApi->discover_mcp_servers_api_pipedream_mcp_discover_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipedreamApi->discover_mcp_servers_api_pipedream_mcp_discover_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mcp_discovery_request** | [**MCPDiscoveryRequest**](MCPDiscoveryRequest.md)|  | 

### Return type

[**MCPDiscoveryResponse**](MCPDiscoveryResponse.md)

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

# **discover_mcp_servers_for_profile_api_pipedream_mcp_discover_profile_post**
> MCPDiscoveryResponse discover_mcp_servers_for_profile_api_pipedream_mcp_discover_profile_post(mcp_profile_discovery_request)

Discover Mcp Servers For Profile

### Example


```python
import suna_api_client
from suna_api_client.models.mcp_discovery_response import MCPDiscoveryResponse
from suna_api_client.models.mcp_profile_discovery_request import MCPProfileDiscoveryRequest
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
    api_instance = suna_api_client.PipedreamApi(api_client)
    mcp_profile_discovery_request = suna_api_client.MCPProfileDiscoveryRequest() # MCPProfileDiscoveryRequest | 

    try:
        # Discover Mcp Servers For Profile
        api_response = api_instance.discover_mcp_servers_for_profile_api_pipedream_mcp_discover_profile_post(mcp_profile_discovery_request)
        print("The response of PipedreamApi->discover_mcp_servers_for_profile_api_pipedream_mcp_discover_profile_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipedreamApi->discover_mcp_servers_for_profile_api_pipedream_mcp_discover_profile_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mcp_profile_discovery_request** | [**MCPProfileDiscoveryRequest**](MCPProfileDiscoveryRequest.md)|  | 

### Return type

[**MCPDiscoveryResponse**](MCPDiscoveryResponse.md)

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

# **get_app_icon_api_pipedream_apps_app_slug_icon_get**
> object get_app_icon_api_pipedream_apps_app_slug_icon_get(app_slug)

Get App Icon

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
    api_instance = suna_api_client.PipedreamApi(api_client)
    app_slug = 'app_slug_example' # str | 

    try:
        # Get App Icon
        api_response = api_instance.get_app_icon_api_pipedream_apps_app_slug_icon_get(app_slug)
        print("The response of PipedreamApi->get_app_icon_api_pipedream_apps_app_slug_icon_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipedreamApi->get_app_icon_api_pipedream_apps_app_slug_icon_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_slug** | **str**|  | 

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

# **get_app_tools_api_pipedream_apps_app_slug_tools_get**
> object get_app_tools_api_pipedream_apps_app_slug_tools_get(app_slug)

Get App Tools

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
    api_instance = suna_api_client.PipedreamApi(api_client)
    app_slug = 'app_slug_example' # str | 

    try:
        # Get App Tools
        api_response = api_instance.get_app_tools_api_pipedream_apps_app_slug_tools_get(app_slug)
        print("The response of PipedreamApi->get_app_tools_api_pipedream_apps_app_slug_tools_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipedreamApi->get_app_tools_api_pipedream_apps_app_slug_tools_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_slug** | **str**|  | 

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

# **get_credential_profile_api_pipedream_profiles_profile_id_get**
> CorePipedreamApiProfileResponse get_credential_profile_api_pipedream_profiles_profile_id_get(profile_id)

Get Credential Profile

### Example


```python
import suna_api_client
from suna_api_client.models.core_pipedream_api_profile_response import CorePipedreamApiProfileResponse
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
    api_instance = suna_api_client.PipedreamApi(api_client)
    profile_id = 'profile_id_example' # str | 

    try:
        # Get Credential Profile
        api_response = api_instance.get_credential_profile_api_pipedream_profiles_profile_id_get(profile_id)
        print("The response of PipedreamApi->get_credential_profile_api_pipedream_profiles_profile_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipedreamApi->get_credential_profile_api_pipedream_profiles_profile_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**|  | 

### Return type

[**CorePipedreamApiProfileResponse**](CorePipedreamApiProfileResponse.md)

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

# **get_credential_profiles_api_pipedream_profiles_get**
> List[CorePipedreamApiProfileResponse] get_credential_profiles_api_pipedream_profiles_get(app_slug=app_slug, is_active=is_active)

Get Credential Profiles

### Example


```python
import suna_api_client
from suna_api_client.models.core_pipedream_api_profile_response import CorePipedreamApiProfileResponse
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
    api_instance = suna_api_client.PipedreamApi(api_client)
    app_slug = 'app_slug_example' # str |  (optional)
    is_active = True # bool |  (optional)

    try:
        # Get Credential Profiles
        api_response = api_instance.get_credential_profiles_api_pipedream_profiles_get(app_slug=app_slug, is_active=is_active)
        print("The response of PipedreamApi->get_credential_profiles_api_pipedream_profiles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipedreamApi->get_credential_profiles_api_pipedream_profiles_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_slug** | **str**|  | [optional] 
 **is_active** | **bool**|  | [optional] 

### Return type

[**List[CorePipedreamApiProfileResponse]**](CorePipedreamApiProfileResponse.md)

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

# **get_pipedream_apps_api_pipedream_apps_get**
> Dict[str, object] get_pipedream_apps_api_pipedream_apps_get(after=after, q=q, category=category)

Get Pipedream Apps

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
    api_instance = suna_api_client.PipedreamApi(api_client)
    after = 'after_example' # str | Cursor for pagination (optional)
    q = 'q_example' # str |  (optional)
    category = 'category_example' # str |  (optional)

    try:
        # Get Pipedream Apps
        api_response = api_instance.get_pipedream_apps_api_pipedream_apps_get(after=after, q=q, category=category)
        print("The response of PipedreamApi->get_pipedream_apps_api_pipedream_apps_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipedreamApi->get_pipedream_apps_api_pipedream_apps_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **after** | **str**| Cursor for pagination | [optional] 
 **q** | **str**|  | [optional] 
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

# **get_popular_pipedream_apps_api_pipedream_apps_popular_get**
> Dict[str, object] get_popular_pipedream_apps_api_pipedream_apps_popular_get()

Get Popular Pipedream Apps

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
    api_instance = suna_api_client.PipedreamApi(api_client)

    try:
        # Get Popular Pipedream Apps
        api_response = api_instance.get_popular_pipedream_apps_api_pipedream_apps_popular_get()
        print("The response of PipedreamApi->get_popular_pipedream_apps_api_pipedream_apps_popular_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipedreamApi->get_popular_pipedream_apps_api_pipedream_apps_popular_get: %s\n" % e)
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

# **get_profile_connections_api_pipedream_profiles_profile_id_connections_get**
> object get_profile_connections_api_pipedream_profiles_profile_id_connections_get(profile_id)

Get Profile Connections

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
    api_instance = suna_api_client.PipedreamApi(api_client)
    profile_id = 'profile_id_example' # str | 

    try:
        # Get Profile Connections
        api_response = api_instance.get_profile_connections_api_pipedream_profiles_profile_id_connections_get(profile_id)
        print("The response of PipedreamApi->get_profile_connections_api_pipedream_profiles_profile_id_connections_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipedreamApi->get_profile_connections_api_pipedream_profiles_profile_id_connections_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**|  | 

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

# **get_user_connections_api_pipedream_connections_get**
> ConnectionResponse get_user_connections_api_pipedream_connections_get()

Get User Connections

### Example


```python
import suna_api_client
from suna_api_client.models.connection_response import ConnectionResponse
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
    api_instance = suna_api_client.PipedreamApi(api_client)

    try:
        # Get User Connections
        api_response = api_instance.get_user_connections_api_pipedream_connections_get()
        print("The response of PipedreamApi->get_user_connections_api_pipedream_connections_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipedreamApi->get_user_connections_api_pipedream_connections_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ConnectionResponse**](ConnectionResponse.md)

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

# **update_credential_profile_api_pipedream_profiles_profile_id_put**
> CorePipedreamApiProfileResponse update_credential_profile_api_pipedream_profiles_profile_id_put(profile_id, update_profile_request)

Update Credential Profile

### Example


```python
import suna_api_client
from suna_api_client.models.core_pipedream_api_profile_response import CorePipedreamApiProfileResponse
from suna_api_client.models.update_profile_request import UpdateProfileRequest
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
    api_instance = suna_api_client.PipedreamApi(api_client)
    profile_id = 'profile_id_example' # str | 
    update_profile_request = suna_api_client.UpdateProfileRequest() # UpdateProfileRequest | 

    try:
        # Update Credential Profile
        api_response = api_instance.update_credential_profile_api_pipedream_profiles_profile_id_put(profile_id, update_profile_request)
        print("The response of PipedreamApi->update_credential_profile_api_pipedream_profiles_profile_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PipedreamApi->update_credential_profile_api_pipedream_profiles_profile_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**|  | 
 **update_profile_request** | [**UpdateProfileRequest**](UpdateProfileRequest.md)|  | 

### Return type

[**CorePipedreamApiProfileResponse**](CorePipedreamApiProfileResponse.md)

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

