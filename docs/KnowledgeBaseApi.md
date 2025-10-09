# suna_api_client.KnowledgeBaseApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_agent_knowledge_base_entry_api_knowledge_base_agents_agent_id_post**](KnowledgeBaseApi.md#create_agent_knowledge_base_entry_api_knowledge_base_agents_agent_id_post) | **POST** /api/knowledge-base/agents/{agent_id} | Create Agent Knowledge Base Entry
[**create_folder_api_knowledge_base_folders_post**](KnowledgeBaseApi.md#create_folder_api_knowledge_base_folders_post) | **POST** /api/knowledge-base/folders | Create Folder
[**delete_entry_api_knowledge_base_entries_entry_id_delete**](KnowledgeBaseApi.md#delete_entry_api_knowledge_base_entries_entry_id_delete) | **DELETE** /api/knowledge-base/entries/{entry_id} | Delete Entry
[**delete_folder_api_knowledge_base_folders_folder_id_delete**](KnowledgeBaseApi.md#delete_folder_api_knowledge_base_folders_folder_id_delete) | **DELETE** /api/knowledge-base/folders/{folder_id} | Delete Folder
[**delete_knowledge_base_entry_api_knowledge_base_entry_id_delete**](KnowledgeBaseApi.md#delete_knowledge_base_entry_api_knowledge_base_entry_id_delete) | **DELETE** /api/knowledge-base/{entry_id} | Delete Knowledge Base Entry
[**download_file_api_knowledge_base_entries_entry_id_download_get**](KnowledgeBaseApi.md#download_file_api_knowledge_base_entries_entry_id_download_get) | **GET** /api/knowledge-base/entries/{entry_id}/download | Download File
[**get_agent_assignments_api_knowledge_base_agents_agent_id_assignments_get**](KnowledgeBaseApi.md#get_agent_assignments_api_knowledge_base_agents_agent_id_assignments_get) | **GET** /api/knowledge-base/agents/{agent_id}/assignments | Get Agent Assignments
[**get_agent_knowledge_base_api_knowledge_base_agents_agent_id_get**](KnowledgeBaseApi.md#get_agent_knowledge_base_api_knowledge_base_agents_agent_id_get) | **GET** /api/knowledge-base/agents/{agent_id} | Get Agent Knowledge Base
[**get_agent_knowledge_base_context_api_knowledge_base_agents_agent_id_context_get**](KnowledgeBaseApi.md#get_agent_knowledge_base_context_api_knowledge_base_agents_agent_id_context_get) | **GET** /api/knowledge-base/agents/{agent_id}/context | Get Agent Knowledge Base Context
[**get_agent_processing_jobs_api_knowledge_base_agents_agent_id_processing_jobs_get**](KnowledgeBaseApi.md#get_agent_processing_jobs_api_knowledge_base_agents_agent_id_processing_jobs_get) | **GET** /api/knowledge-base/agents/{agent_id}/processing-jobs | Get Agent Processing Jobs
[**get_folder_entries_api_knowledge_base_folders_folder_id_entries_get**](KnowledgeBaseApi.md#get_folder_entries_api_knowledge_base_folders_folder_id_entries_get) | **GET** /api/knowledge-base/folders/{folder_id}/entries | Get Folder Entries
[**get_folders_api_knowledge_base_folders_get**](KnowledgeBaseApi.md#get_folders_api_knowledge_base_folders_get) | **GET** /api/knowledge-base/folders | Get Folders
[**get_knowledge_base_entry_api_knowledge_base_entry_id_get**](KnowledgeBaseApi.md#get_knowledge_base_entry_api_knowledge_base_entry_id_get) | **GET** /api/knowledge-base/{entry_id} | Get Knowledge Base Entry
[**move_file_api_knowledge_base_entries_entry_id_move_put**](KnowledgeBaseApi.md#move_file_api_knowledge_base_entries_entry_id_move_put) | **PUT** /api/knowledge-base/entries/{entry_id}/move | Move File
[**update_agent_assignments_api_knowledge_base_agents_agent_id_assignments_post**](KnowledgeBaseApi.md#update_agent_assignments_api_knowledge_base_agents_agent_id_assignments_post) | **POST** /api/knowledge-base/agents/{agent_id}/assignments | Update Agent Assignments
[**update_entry_api_knowledge_base_entries_entry_id_patch**](KnowledgeBaseApi.md#update_entry_api_knowledge_base_entries_entry_id_patch) | **PATCH** /api/knowledge-base/entries/{entry_id} | Update Entry
[**update_folder_api_knowledge_base_folders_folder_id_put**](KnowledgeBaseApi.md#update_folder_api_knowledge_base_folders_folder_id_put) | **PUT** /api/knowledge-base/folders/{folder_id} | Update Folder
[**update_knowledge_base_entry_api_knowledge_base_entry_id_put**](KnowledgeBaseApi.md#update_knowledge_base_entry_api_knowledge_base_entry_id_put) | **PUT** /api/knowledge-base/{entry_id} | Update Knowledge Base Entry
[**upload_file_api_knowledge_base_folders_folder_id_upload_post**](KnowledgeBaseApi.md#upload_file_api_knowledge_base_folders_folder_id_upload_post) | **POST** /api/knowledge-base/folders/{folder_id}/upload | Upload File
[**upload_file_to_agent_kb_api_knowledge_base_agents_agent_id_upload_file_post**](KnowledgeBaseApi.md#upload_file_to_agent_kb_api_knowledge_base_agents_agent_id_upload_file_post) | **POST** /api/knowledge-base/agents/{agent_id}/upload-file | Upload File To Agent Kb


# **create_agent_knowledge_base_entry_api_knowledge_base_agents_agent_id_post**
> KnowledgeBaseEntryResponse create_agent_knowledge_base_entry_api_knowledge_base_agents_agent_id_post(agent_id, create_knowledge_base_entry_request)

Create Agent Knowledge Base Entry

Create a new knowledge base entry for an agent

### Example


```python
import suna_api_client
from suna_api_client.models.create_knowledge_base_entry_request import CreateKnowledgeBaseEntryRequest
from suna_api_client.models.knowledge_base_entry_response import KnowledgeBaseEntryResponse
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
    api_instance = suna_api_client.KnowledgeBaseApi(api_client)
    agent_id = 'agent_id_example' # str | 
    create_knowledge_base_entry_request = suna_api_client.CreateKnowledgeBaseEntryRequest() # CreateKnowledgeBaseEntryRequest | 

    try:
        # Create Agent Knowledge Base Entry
        api_response = api_instance.create_agent_knowledge_base_entry_api_knowledge_base_agents_agent_id_post(agent_id, create_knowledge_base_entry_request)
        print("The response of KnowledgeBaseApi->create_agent_knowledge_base_entry_api_knowledge_base_agents_agent_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseApi->create_agent_knowledge_base_entry_api_knowledge_base_agents_agent_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **create_knowledge_base_entry_request** | [**CreateKnowledgeBaseEntryRequest**](CreateKnowledgeBaseEntryRequest.md)|  | 

### Return type

[**KnowledgeBaseEntryResponse**](KnowledgeBaseEntryResponse.md)

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

# **create_folder_api_knowledge_base_folders_post**
> FolderResponse create_folder_api_knowledge_base_folders_post(create_folder_request)

Create Folder

Create a new folder

### Example


```python
import suna_api_client
from suna_api_client.models.create_folder_request import CreateFolderRequest
from suna_api_client.models.folder_response import FolderResponse
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
    api_instance = suna_api_client.KnowledgeBaseApi(api_client)
    create_folder_request = suna_api_client.CreateFolderRequest() # CreateFolderRequest | 

    try:
        # Create Folder
        api_response = api_instance.create_folder_api_knowledge_base_folders_post(create_folder_request)
        print("The response of KnowledgeBaseApi->create_folder_api_knowledge_base_folders_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseApi->create_folder_api_knowledge_base_folders_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_folder_request** | [**CreateFolderRequest**](CreateFolderRequest.md)|  | 

### Return type

[**FolderResponse**](FolderResponse.md)

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

# **delete_entry_api_knowledge_base_entries_entry_id_delete**
> object delete_entry_api_knowledge_base_entries_entry_id_delete(entry_id)

Delete Entry

Delete a knowledge base entry.

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
    api_instance = suna_api_client.KnowledgeBaseApi(api_client)
    entry_id = 'entry_id_example' # str | 

    try:
        # Delete Entry
        api_response = api_instance.delete_entry_api_knowledge_base_entries_entry_id_delete(entry_id)
        print("The response of KnowledgeBaseApi->delete_entry_api_knowledge_base_entries_entry_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseApi->delete_entry_api_knowledge_base_entries_entry_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entry_id** | **str**|  | 

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

# **delete_folder_api_knowledge_base_folders_folder_id_delete**
> object delete_folder_api_knowledge_base_folders_folder_id_delete(folder_id)

Delete Folder

Delete a knowledge base folder and all its entries.

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
    api_instance = suna_api_client.KnowledgeBaseApi(api_client)
    folder_id = 'folder_id_example' # str | 

    try:
        # Delete Folder
        api_response = api_instance.delete_folder_api_knowledge_base_folders_folder_id_delete(folder_id)
        print("The response of KnowledgeBaseApi->delete_folder_api_knowledge_base_folders_folder_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseApi->delete_folder_api_knowledge_base_folders_folder_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  | 

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

# **delete_knowledge_base_entry_api_knowledge_base_entry_id_delete**
> object delete_knowledge_base_entry_api_knowledge_base_entry_id_delete(entry_id)

Delete Knowledge Base Entry

Delete an agent knowledge base entry

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
    api_instance = suna_api_client.KnowledgeBaseApi(api_client)
    entry_id = 'entry_id_example' # str | 

    try:
        # Delete Knowledge Base Entry
        api_response = api_instance.delete_knowledge_base_entry_api_knowledge_base_entry_id_delete(entry_id)
        print("The response of KnowledgeBaseApi->delete_knowledge_base_entry_api_knowledge_base_entry_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseApi->delete_knowledge_base_entry_api_knowledge_base_entry_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entry_id** | **str**|  | 

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

# **download_file_api_knowledge_base_entries_entry_id_download_get**
> object download_file_api_knowledge_base_entries_entry_id_download_get(entry_id)

Download File

Download the actual file content from S3

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
    api_instance = suna_api_client.KnowledgeBaseApi(api_client)
    entry_id = 'entry_id_example' # str | 

    try:
        # Download File
        api_response = api_instance.download_file_api_knowledge_base_entries_entry_id_download_get(entry_id)
        print("The response of KnowledgeBaseApi->download_file_api_knowledge_base_entries_entry_id_download_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseApi->download_file_api_knowledge_base_entries_entry_id_download_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entry_id** | **str**|  | 

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

# **get_agent_assignments_api_knowledge_base_agents_agent_id_assignments_get**
> object get_agent_assignments_api_knowledge_base_agents_agent_id_assignments_get(agent_id)

Get Agent Assignments

Get current knowledge base assignments for an agent

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
    api_instance = suna_api_client.KnowledgeBaseApi(api_client)
    agent_id = 'agent_id_example' # str | 

    try:
        # Get Agent Assignments
        api_response = api_instance.get_agent_assignments_api_knowledge_base_agents_agent_id_assignments_get(agent_id)
        print("The response of KnowledgeBaseApi->get_agent_assignments_api_knowledge_base_agents_agent_id_assignments_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseApi->get_agent_assignments_api_knowledge_base_agents_agent_id_assignments_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 

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

# **get_agent_knowledge_base_api_knowledge_base_agents_agent_id_get**
> KnowledgeBaseListResponse get_agent_knowledge_base_api_knowledge_base_agents_agent_id_get(agent_id, include_inactive=include_inactive)

Get Agent Knowledge Base

Get all knowledge base entries for an agent

### Example


```python
import suna_api_client
from suna_api_client.models.knowledge_base_list_response import KnowledgeBaseListResponse
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
    api_instance = suna_api_client.KnowledgeBaseApi(api_client)
    agent_id = 'agent_id_example' # str | 
    include_inactive = False # bool |  (optional) (default to False)

    try:
        # Get Agent Knowledge Base
        api_response = api_instance.get_agent_knowledge_base_api_knowledge_base_agents_agent_id_get(agent_id, include_inactive=include_inactive)
        print("The response of KnowledgeBaseApi->get_agent_knowledge_base_api_knowledge_base_agents_agent_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseApi->get_agent_knowledge_base_api_knowledge_base_agents_agent_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **include_inactive** | **bool**|  | [optional] [default to False]

### Return type

[**KnowledgeBaseListResponse**](KnowledgeBaseListResponse.md)

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

# **get_agent_knowledge_base_context_api_knowledge_base_agents_agent_id_context_get**
> object get_agent_knowledge_base_context_api_knowledge_base_agents_agent_id_context_get(agent_id, max_tokens=max_tokens)

Get Agent Knowledge Base Context

Get knowledge base context for agent prompts

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
    api_instance = suna_api_client.KnowledgeBaseApi(api_client)
    agent_id = 'agent_id_example' # str | 
    max_tokens = 4000 # int |  (optional) (default to 4000)

    try:
        # Get Agent Knowledge Base Context
        api_response = api_instance.get_agent_knowledge_base_context_api_knowledge_base_agents_agent_id_context_get(agent_id, max_tokens=max_tokens)
        print("The response of KnowledgeBaseApi->get_agent_knowledge_base_context_api_knowledge_base_agents_agent_id_context_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseApi->get_agent_knowledge_base_context_api_knowledge_base_agents_agent_id_context_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **max_tokens** | **int**|  | [optional] [default to 4000]

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

# **get_agent_processing_jobs_api_knowledge_base_agents_agent_id_processing_jobs_get**
> List[ProcessingJobResponse] get_agent_processing_jobs_api_knowledge_base_agents_agent_id_processing_jobs_get(agent_id, limit=limit)

Get Agent Processing Jobs

Get processing jobs for an agent

### Example


```python
import suna_api_client
from suna_api_client.models.processing_job_response import ProcessingJobResponse
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
    api_instance = suna_api_client.KnowledgeBaseApi(api_client)
    agent_id = 'agent_id_example' # str | 
    limit = 10 # int |  (optional) (default to 10)

    try:
        # Get Agent Processing Jobs
        api_response = api_instance.get_agent_processing_jobs_api_knowledge_base_agents_agent_id_processing_jobs_get(agent_id, limit=limit)
        print("The response of KnowledgeBaseApi->get_agent_processing_jobs_api_knowledge_base_agents_agent_id_processing_jobs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseApi->get_agent_processing_jobs_api_knowledge_base_agents_agent_id_processing_jobs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 10]

### Return type

[**List[ProcessingJobResponse]**](ProcessingJobResponse.md)

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

# **get_folder_entries_api_knowledge_base_folders_folder_id_entries_get**
> object get_folder_entries_api_knowledge_base_folders_folder_id_entries_get(folder_id)

Get Folder Entries

Get all entries in a folder

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
    api_instance = suna_api_client.KnowledgeBaseApi(api_client)
    folder_id = 'folder_id_example' # str | 

    try:
        # Get Folder Entries
        api_response = api_instance.get_folder_entries_api_knowledge_base_folders_folder_id_entries_get(folder_id)
        print("The response of KnowledgeBaseApi->get_folder_entries_api_knowledge_base_folders_folder_id_entries_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseApi->get_folder_entries_api_knowledge_base_folders_folder_id_entries_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  | 

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

# **get_folders_api_knowledge_base_folders_get**
> List[FolderResponse] get_folders_api_knowledge_base_folders_get()

Get Folders

Get all folders for the current user

### Example


```python
import suna_api_client
from suna_api_client.models.folder_response import FolderResponse
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
    api_instance = suna_api_client.KnowledgeBaseApi(api_client)

    try:
        # Get Folders
        api_response = api_instance.get_folders_api_knowledge_base_folders_get()
        print("The response of KnowledgeBaseApi->get_folders_api_knowledge_base_folders_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseApi->get_folders_api_knowledge_base_folders_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[FolderResponse]**](FolderResponse.md)

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

# **get_knowledge_base_entry_api_knowledge_base_entry_id_get**
> KnowledgeBaseEntryResponse get_knowledge_base_entry_api_knowledge_base_entry_id_get(entry_id)

Get Knowledge Base Entry

Get a specific agent knowledge base entry

### Example


```python
import suna_api_client
from suna_api_client.models.knowledge_base_entry_response import KnowledgeBaseEntryResponse
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
    api_instance = suna_api_client.KnowledgeBaseApi(api_client)
    entry_id = 'entry_id_example' # str | 

    try:
        # Get Knowledge Base Entry
        api_response = api_instance.get_knowledge_base_entry_api_knowledge_base_entry_id_get(entry_id)
        print("The response of KnowledgeBaseApi->get_knowledge_base_entry_api_knowledge_base_entry_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseApi->get_knowledge_base_entry_api_knowledge_base_entry_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entry_id** | **str**|  | 

### Return type

[**KnowledgeBaseEntryResponse**](KnowledgeBaseEntryResponse.md)

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

# **move_file_api_knowledge_base_entries_entry_id_move_put**
> object move_file_api_knowledge_base_entries_entry_id_move_put(entry_id, folder_move_request)

Move File

Move a file to a different folder.

### Example


```python
import suna_api_client
from suna_api_client.models.folder_move_request import FolderMoveRequest
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
    api_instance = suna_api_client.KnowledgeBaseApi(api_client)
    entry_id = 'entry_id_example' # str | 
    folder_move_request = suna_api_client.FolderMoveRequest() # FolderMoveRequest | 

    try:
        # Move File
        api_response = api_instance.move_file_api_knowledge_base_entries_entry_id_move_put(entry_id, folder_move_request)
        print("The response of KnowledgeBaseApi->move_file_api_knowledge_base_entries_entry_id_move_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseApi->move_file_api_knowledge_base_entries_entry_id_move_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entry_id** | **str**|  | 
 **folder_move_request** | [**FolderMoveRequest**](FolderMoveRequest.md)|  | 

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

# **update_agent_assignments_api_knowledge_base_agents_agent_id_assignments_post**
> object update_agent_assignments_api_knowledge_base_agents_agent_id_assignments_post(agent_id, agent_assignment_request)

Update Agent Assignments

Update knowledge base assignments for an agent

### Example


```python
import suna_api_client
from suna_api_client.models.agent_assignment_request import AgentAssignmentRequest
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
    api_instance = suna_api_client.KnowledgeBaseApi(api_client)
    agent_id = 'agent_id_example' # str | 
    agent_assignment_request = suna_api_client.AgentAssignmentRequest() # AgentAssignmentRequest | 

    try:
        # Update Agent Assignments
        api_response = api_instance.update_agent_assignments_api_knowledge_base_agents_agent_id_assignments_post(agent_id, agent_assignment_request)
        print("The response of KnowledgeBaseApi->update_agent_assignments_api_knowledge_base_agents_agent_id_assignments_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseApi->update_agent_assignments_api_knowledge_base_agents_agent_id_assignments_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **agent_assignment_request** | [**AgentAssignmentRequest**](AgentAssignmentRequest.md)|  | 

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

# **update_entry_api_knowledge_base_entries_entry_id_patch**
> EntryResponse update_entry_api_knowledge_base_entries_entry_id_patch(entry_id, update_entry_request)

Update Entry

Update a knowledge base entry summary.

### Example


```python
import suna_api_client
from suna_api_client.models.entry_response import EntryResponse
from suna_api_client.models.update_entry_request import UpdateEntryRequest
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
    api_instance = suna_api_client.KnowledgeBaseApi(api_client)
    entry_id = 'entry_id_example' # str | 
    update_entry_request = suna_api_client.UpdateEntryRequest() # UpdateEntryRequest | 

    try:
        # Update Entry
        api_response = api_instance.update_entry_api_knowledge_base_entries_entry_id_patch(entry_id, update_entry_request)
        print("The response of KnowledgeBaseApi->update_entry_api_knowledge_base_entries_entry_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseApi->update_entry_api_knowledge_base_entries_entry_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entry_id** | **str**|  | 
 **update_entry_request** | [**UpdateEntryRequest**](UpdateEntryRequest.md)|  | 

### Return type

[**EntryResponse**](EntryResponse.md)

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

# **update_folder_api_knowledge_base_folders_folder_id_put**
> FolderResponse update_folder_api_knowledge_base_folders_folder_id_put(folder_id, core_knowledge_base_api_update_folder_request)

Update Folder

Update/rename a folder

### Example


```python
import suna_api_client
from suna_api_client.models.core_knowledge_base_api_update_folder_request import CoreKnowledgeBaseApiUpdateFolderRequest
from suna_api_client.models.folder_response import FolderResponse
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
    api_instance = suna_api_client.KnowledgeBaseApi(api_client)
    folder_id = 'folder_id_example' # str | 
    core_knowledge_base_api_update_folder_request = suna_api_client.CoreKnowledgeBaseApiUpdateFolderRequest() # CoreKnowledgeBaseApiUpdateFolderRequest | 

    try:
        # Update Folder
        api_response = api_instance.update_folder_api_knowledge_base_folders_folder_id_put(folder_id, core_knowledge_base_api_update_folder_request)
        print("The response of KnowledgeBaseApi->update_folder_api_knowledge_base_folders_folder_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseApi->update_folder_api_knowledge_base_folders_folder_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  | 
 **core_knowledge_base_api_update_folder_request** | [**CoreKnowledgeBaseApiUpdateFolderRequest**](CoreKnowledgeBaseApiUpdateFolderRequest.md)|  | 

### Return type

[**FolderResponse**](FolderResponse.md)

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

# **update_knowledge_base_entry_api_knowledge_base_entry_id_put**
> KnowledgeBaseEntryResponse update_knowledge_base_entry_api_knowledge_base_entry_id_put(entry_id, update_knowledge_base_entry_request)

Update Knowledge Base Entry

Update an agent knowledge base entry

### Example


```python
import suna_api_client
from suna_api_client.models.knowledge_base_entry_response import KnowledgeBaseEntryResponse
from suna_api_client.models.update_knowledge_base_entry_request import UpdateKnowledgeBaseEntryRequest
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
    api_instance = suna_api_client.KnowledgeBaseApi(api_client)
    entry_id = 'entry_id_example' # str | 
    update_knowledge_base_entry_request = suna_api_client.UpdateKnowledgeBaseEntryRequest() # UpdateKnowledgeBaseEntryRequest | 

    try:
        # Update Knowledge Base Entry
        api_response = api_instance.update_knowledge_base_entry_api_knowledge_base_entry_id_put(entry_id, update_knowledge_base_entry_request)
        print("The response of KnowledgeBaseApi->update_knowledge_base_entry_api_knowledge_base_entry_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseApi->update_knowledge_base_entry_api_knowledge_base_entry_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **entry_id** | **str**|  | 
 **update_knowledge_base_entry_request** | [**UpdateKnowledgeBaseEntryRequest**](UpdateKnowledgeBaseEntryRequest.md)|  | 

### Return type

[**KnowledgeBaseEntryResponse**](KnowledgeBaseEntryResponse.md)

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

# **upload_file_api_knowledge_base_folders_folder_id_upload_post**
> object upload_file_api_knowledge_base_folders_folder_id_upload_post(folder_id, file)

Upload File

Upload a file to a knowledge base folder.

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
    api_instance = suna_api_client.KnowledgeBaseApi(api_client)
    folder_id = 'folder_id_example' # str | 
    file = None # bytearray | 

    try:
        # Upload File
        api_response = api_instance.upload_file_api_knowledge_base_folders_folder_id_upload_post(folder_id, file)
        print("The response of KnowledgeBaseApi->upload_file_api_knowledge_base_folders_folder_id_upload_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseApi->upload_file_api_knowledge_base_folders_folder_id_upload_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **folder_id** | **str**|  | 
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

# **upload_file_to_agent_kb_api_knowledge_base_agents_agent_id_upload_file_post**
> object upload_file_to_agent_kb_api_knowledge_base_agents_agent_id_upload_file_post(agent_id, file)

Upload File To Agent Kb

Upload and process a file for agent knowledge base

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
    api_instance = suna_api_client.KnowledgeBaseApi(api_client)
    agent_id = 'agent_id_example' # str | 
    file = None # bytearray | 

    try:
        # Upload File To Agent Kb
        api_response = api_instance.upload_file_to_agent_kb_api_knowledge_base_agents_agent_id_upload_file_post(agent_id, file)
        print("The response of KnowledgeBaseApi->upload_file_to_agent_kb_api_knowledge_base_agents_agent_id_upload_file_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling KnowledgeBaseApi->upload_file_to_agent_kb_api_knowledge_base_agents_agent_id_upload_file_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
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

