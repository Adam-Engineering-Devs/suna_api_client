# suna_api_client.SandboxApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_file_api_sandboxes_sandbox_id_files_post**](SandboxApi.md#create_file_api_sandboxes_sandbox_id_files_post) | **POST** /api/sandboxes/{sandbox_id}/files | Create File
[**delete_file_api_sandboxes_sandbox_id_files_delete**](SandboxApi.md#delete_file_api_sandboxes_sandbox_id_files_delete) | **DELETE** /api/sandboxes/{sandbox_id}/files | Delete File
[**delete_sandbox_route_api_sandboxes_sandbox_id_delete**](SandboxApi.md#delete_sandbox_route_api_sandboxes_sandbox_id_delete) | **DELETE** /api/sandboxes/{sandbox_id} | Delete Sandbox Route
[**ensure_project_sandbox_active_api_project_project_id_sandbox_ensure_active_post**](SandboxApi.md#ensure_project_sandbox_active_api_project_project_id_sandbox_ensure_active_post) | **POST** /api/project/{project_id}/sandbox/ensure-active | Ensure Project Sandbox Active
[**get_sandbox_status_api_sandbox_status_get**](SandboxApi.md#get_sandbox_status_api_sandbox_status_get) | **GET** /api/sandbox/status | Get Sandbox Status
[**list_files_api_sandboxes_sandbox_id_files_get**](SandboxApi.md#list_files_api_sandboxes_sandbox_id_files_get) | **GET** /api/sandboxes/{sandbox_id}/files | List Files
[**read_file_api_sandboxes_sandbox_id_files_content_get**](SandboxApi.md#read_file_api_sandboxes_sandbox_id_files_content_get) | **GET** /api/sandboxes/{sandbox_id}/files/content | Read File
[**read_files_api_sandboxes_sandbox_id_all_files_content_get**](SandboxApi.md#read_files_api_sandboxes_sandbox_id_all_files_content_get) | **GET** /api/sandboxes/{sandbox_id}/all_files/content | Read Files
[**update_file_api_sandboxes_sandbox_id_files_put**](SandboxApi.md#update_file_api_sandboxes_sandbox_id_files_put) | **PUT** /api/sandboxes/{sandbox_id}/files | Update File


# **create_file_api_sandboxes_sandbox_id_files_post**
> object create_file_api_sandboxes_sandbox_id_files_post(sandbox_id, path, file)

Create File

Create a file in the sandbox using direct file upload

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
    api_instance = suna_api_client.SandboxApi(api_client)
    sandbox_id = 'sandbox_id_example' # str | 
    path = 'path_example' # str | 
    file = None # bytearray | 

    try:
        # Create File
        api_response = api_instance.create_file_api_sandboxes_sandbox_id_files_post(sandbox_id, path, file)
        print("The response of SandboxApi->create_file_api_sandboxes_sandbox_id_files_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SandboxApi->create_file_api_sandboxes_sandbox_id_files_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox_id** | **str**|  | 
 **path** | **str**|  | 
 **file** | **bytearray**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_file_api_sandboxes_sandbox_id_files_delete**
> object delete_file_api_sandboxes_sandbox_id_files_delete(sandbox_id, path)

Delete File

Delete a file from the sandbox

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
    api_instance = suna_api_client.SandboxApi(api_client)
    sandbox_id = 'sandbox_id_example' # str | 
    path = 'path_example' # str | 

    try:
        # Delete File
        api_response = api_instance.delete_file_api_sandboxes_sandbox_id_files_delete(sandbox_id, path)
        print("The response of SandboxApi->delete_file_api_sandboxes_sandbox_id_files_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SandboxApi->delete_file_api_sandboxes_sandbox_id_files_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox_id** | **str**|  | 
 **path** | **str**|  | 

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

# **delete_sandbox_route_api_sandboxes_sandbox_id_delete**
> object delete_sandbox_route_api_sandboxes_sandbox_id_delete(sandbox_id)

Delete Sandbox Route

Delete an entire sandbox

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
    api_instance = suna_api_client.SandboxApi(api_client)
    sandbox_id = 'sandbox_id_example' # str | 

    try:
        # Delete Sandbox Route
        api_response = api_instance.delete_sandbox_route_api_sandboxes_sandbox_id_delete(sandbox_id)
        print("The response of SandboxApi->delete_sandbox_route_api_sandboxes_sandbox_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SandboxApi->delete_sandbox_route_api_sandboxes_sandbox_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox_id** | **str**|  | 

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

# **ensure_project_sandbox_active_api_project_project_id_sandbox_ensure_active_post**
> object ensure_project_sandbox_active_api_project_project_id_sandbox_ensure_active_post(project_id)

Ensure Project Sandbox Active

Ensure that a project's sandbox is active and running.
Checks the sandbox status and starts it if it's not running.

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
    api_instance = suna_api_client.SandboxApi(api_client)
    project_id = 'project_id_example' # str | 

    try:
        # Ensure Project Sandbox Active
        api_response = api_instance.ensure_project_sandbox_active_api_project_project_id_sandbox_ensure_active_post(project_id)
        print("The response of SandboxApi->ensure_project_sandbox_active_api_project_project_id_sandbox_ensure_active_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SandboxApi->ensure_project_sandbox_active_api_project_project_id_sandbox_ensure_active_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_id** | **str**|  | 

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

# **get_sandbox_status_api_sandbox_status_get**
> object get_sandbox_status_api_sandbox_status_get()

Get Sandbox Status

Get current sandbox provider status and configuration

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
    api_instance = suna_api_client.SandboxApi(api_client)

    try:
        # Get Sandbox Status
        api_response = api_instance.get_sandbox_status_api_sandbox_status_get()
        print("The response of SandboxApi->get_sandbox_status_api_sandbox_status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SandboxApi->get_sandbox_status_api_sandbox_status_get: %s\n" % e)
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

# **list_files_api_sandboxes_sandbox_id_files_get**
> object list_files_api_sandboxes_sandbox_id_files_get(sandbox_id, path)

List Files

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
    api_instance = suna_api_client.SandboxApi(api_client)
    sandbox_id = 'sandbox_id_example' # str | 
    path = 'path_example' # str | 

    try:
        # List Files
        api_response = api_instance.list_files_api_sandboxes_sandbox_id_files_get(sandbox_id, path)
        print("The response of SandboxApi->list_files_api_sandboxes_sandbox_id_files_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SandboxApi->list_files_api_sandboxes_sandbox_id_files_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox_id** | **str**|  | 
 **path** | **str**|  | 

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

# **read_file_api_sandboxes_sandbox_id_files_content_get**
> object read_file_api_sandboxes_sandbox_id_files_content_get(sandbox_id, path)

Read File

Read a file from the sandbox

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
    api_instance = suna_api_client.SandboxApi(api_client)
    sandbox_id = 'sandbox_id_example' # str | 
    path = 'path_example' # str | 

    try:
        # Read File
        api_response = api_instance.read_file_api_sandboxes_sandbox_id_files_content_get(sandbox_id, path)
        print("The response of SandboxApi->read_file_api_sandboxes_sandbox_id_files_content_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SandboxApi->read_file_api_sandboxes_sandbox_id_files_content_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox_id** | **str**|  | 
 **path** | **str**|  | 

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

# **read_files_api_sandboxes_sandbox_id_all_files_content_get**
> object read_files_api_sandboxes_sandbox_id_all_files_content_get(sandbox_id)

Read Files

Read all files from the sandbox and return them as a zip archive

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
    api_instance = suna_api_client.SandboxApi(api_client)
    sandbox_id = 'sandbox_id_example' # str | 

    try:
        # Read Files
        api_response = api_instance.read_files_api_sandboxes_sandbox_id_all_files_content_get(sandbox_id)
        print("The response of SandboxApi->read_files_api_sandboxes_sandbox_id_all_files_content_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SandboxApi->read_files_api_sandboxes_sandbox_id_all_files_content_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox_id** | **str**|  | 

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

# **update_file_api_sandboxes_sandbox_id_files_put**
> object update_file_api_sandboxes_sandbox_id_files_put(sandbox_id)

Update File

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
    api_instance = suna_api_client.SandboxApi(api_client)
    sandbox_id = 'sandbox_id_example' # str | 

    try:
        # Update File
        api_response = api_instance.update_file_api_sandboxes_sandbox_id_files_put(sandbox_id)
        print("The response of SandboxApi->update_file_api_sandboxes_sandbox_id_files_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SandboxApi->update_file_api_sandboxes_sandbox_id_files_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sandbox_id** | **str**|  | 

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

