# suna_api_client.WorkflowsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_post**](WorkflowsApi.md#create_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_post) | **POST** /api/triggers/workflows/agents/{agent_id}/workflows | Create Agent Workflow
[**delete_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_delete**](WorkflowsApi.md#delete_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_delete) | **DELETE** /api/triggers/workflows/agents/{agent_id}/workflows/{workflow_id} | Delete Agent Workflow
[**execute_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_execute_post**](WorkflowsApi.md#execute_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_execute_post) | **POST** /api/triggers/workflows/agents/{agent_id}/workflows/{workflow_id}/execute | Execute Agent Workflow
[**get_agent_workflows_api_triggers_workflows_agents_agent_id_workflows_get**](WorkflowsApi.md#get_agent_workflows_api_triggers_workflows_agents_agent_id_workflows_get) | **GET** /api/triggers/workflows/agents/{agent_id}/workflows | Get Agent Workflows
[**update_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_put**](WorkflowsApi.md#update_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_put) | **PUT** /api/triggers/workflows/agents/{agent_id}/workflows/{workflow_id} | Update Agent Workflow


# **create_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_post**
> object create_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_post(agent_id, workflow_create_request)

Create Agent Workflow

Create a new workflow for an agent

### Example


```python
import suna_api_client
from suna_api_client.models.workflow_create_request import WorkflowCreateRequest
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
    api_instance = suna_api_client.WorkflowsApi(api_client)
    agent_id = 'agent_id_example' # str | 
    workflow_create_request = suna_api_client.WorkflowCreateRequest() # WorkflowCreateRequest | 

    try:
        # Create Agent Workflow
        api_response = api_instance.create_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_post(agent_id, workflow_create_request)
        print("The response of WorkflowsApi->create_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->create_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **workflow_create_request** | [**WorkflowCreateRequest**](WorkflowCreateRequest.md)|  | 

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

# **delete_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_delete**
> object delete_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_delete(agent_id, workflow_id)

Delete Agent Workflow

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
    api_instance = suna_api_client.WorkflowsApi(api_client)
    agent_id = 'agent_id_example' # str | 
    workflow_id = 'workflow_id_example' # str | 

    try:
        # Delete Agent Workflow
        api_response = api_instance.delete_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_delete(agent_id, workflow_id)
        print("The response of WorkflowsApi->delete_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->delete_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **workflow_id** | **str**|  | 

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

# **execute_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_execute_post**
> object execute_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_execute_post(agent_id, workflow_id, workflow_execute_request)

Execute Agent Workflow

### Example


```python
import suna_api_client
from suna_api_client.models.workflow_execute_request import WorkflowExecuteRequest
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
    api_instance = suna_api_client.WorkflowsApi(api_client)
    agent_id = 'agent_id_example' # str | 
    workflow_id = 'workflow_id_example' # str | 
    workflow_execute_request = suna_api_client.WorkflowExecuteRequest() # WorkflowExecuteRequest | 

    try:
        # Execute Agent Workflow
        api_response = api_instance.execute_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_execute_post(agent_id, workflow_id, workflow_execute_request)
        print("The response of WorkflowsApi->execute_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_execute_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->execute_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_execute_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **workflow_id** | **str**|  | 
 **workflow_execute_request** | [**WorkflowExecuteRequest**](WorkflowExecuteRequest.md)|  | 

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

# **get_agent_workflows_api_triggers_workflows_agents_agent_id_workflows_get**
> object get_agent_workflows_api_triggers_workflows_agents_agent_id_workflows_get(agent_id)

Get Agent Workflows

Get workflows for an agent

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
    api_instance = suna_api_client.WorkflowsApi(api_client)
    agent_id = 'agent_id_example' # str | 

    try:
        # Get Agent Workflows
        api_response = api_instance.get_agent_workflows_api_triggers_workflows_agents_agent_id_workflows_get(agent_id)
        print("The response of WorkflowsApi->get_agent_workflows_api_triggers_workflows_agents_agent_id_workflows_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->get_agent_workflows_api_triggers_workflows_agents_agent_id_workflows_get: %s\n" % e)
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

# **update_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_put**
> object update_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_put(agent_id, workflow_id, workflow_update_request)

Update Agent Workflow

Update a workflow

### Example


```python
import suna_api_client
from suna_api_client.models.workflow_update_request import WorkflowUpdateRequest
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
    api_instance = suna_api_client.WorkflowsApi(api_client)
    agent_id = 'agent_id_example' # str | 
    workflow_id = 'workflow_id_example' # str | 
    workflow_update_request = suna_api_client.WorkflowUpdateRequest() # WorkflowUpdateRequest | 

    try:
        # Update Agent Workflow
        api_response = api_instance.update_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_put(agent_id, workflow_id, workflow_update_request)
        print("The response of WorkflowsApi->update_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WorkflowsApi->update_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **workflow_id** | **str**|  | 
 **workflow_update_request** | [**WorkflowUpdateRequest**](WorkflowUpdateRequest.md)|  | 

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

