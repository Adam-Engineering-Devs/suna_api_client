# suna_api_client.TriggersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_agent_trigger_api_triggers_agents_agent_id_triggers_post**](TriggersApi.md#create_agent_trigger_api_triggers_agents_agent_id_triggers_post) | **POST** /api/triggers/agents/{agent_id}/triggers | Create Agent Trigger
[**create_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_post**](TriggersApi.md#create_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_post) | **POST** /api/triggers/workflows/agents/{agent_id}/workflows | Create Agent Workflow
[**delete_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_delete**](TriggersApi.md#delete_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_delete) | **DELETE** /api/triggers/workflows/agents/{agent_id}/workflows/{workflow_id} | Delete Agent Workflow
[**delete_trigger_api_triggers_trigger_id_delete**](TriggersApi.md#delete_trigger_api_triggers_trigger_id_delete) | **DELETE** /api/triggers/{trigger_id} | Delete Trigger
[**execute_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_execute_post**](TriggersApi.md#execute_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_execute_post) | **POST** /api/triggers/workflows/agents/{agent_id}/workflows/{workflow_id}/execute | Execute Agent Workflow
[**get_agent_triggers_api_triggers_agents_agent_id_triggers_get**](TriggersApi.md#get_agent_triggers_api_triggers_agents_agent_id_triggers_get) | **GET** /api/triggers/agents/{agent_id}/triggers | Get Agent Triggers
[**get_agent_upcoming_runs_api_triggers_agents_agent_id_upcoming_runs_get**](TriggersApi.md#get_agent_upcoming_runs_api_triggers_agents_agent_id_upcoming_runs_get) | **GET** /api/triggers/agents/{agent_id}/upcoming-runs | Get Agent Upcoming Runs
[**get_agent_workflows_api_triggers_workflows_agents_agent_id_workflows_get**](TriggersApi.md#get_agent_workflows_api_triggers_workflows_agents_agent_id_workflows_get) | **GET** /api/triggers/workflows/agents/{agent_id}/workflows | Get Agent Workflows
[**get_all_user_triggers_api_triggers_all_get**](TriggersApi.md#get_all_user_triggers_api_triggers_all_get) | **GET** /api/triggers/all | Get All User Triggers
[**get_providers_api_triggers_providers_get**](TriggersApi.md#get_providers_api_triggers_providers_get) | **GET** /api/triggers/providers | Get Providers
[**get_trigger_api_triggers_trigger_id_get**](TriggersApi.md#get_trigger_api_triggers_trigger_id_get) | **GET** /api/triggers/{trigger_id} | Get Trigger
[**trigger_webhook_api_triggers_trigger_id_webhook_post**](TriggersApi.md#trigger_webhook_api_triggers_trigger_id_webhook_post) | **POST** /api/triggers/{trigger_id}/webhook | Trigger Webhook
[**update_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_put**](TriggersApi.md#update_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_put) | **PUT** /api/triggers/workflows/agents/{agent_id}/workflows/{workflow_id} | Update Agent Workflow
[**update_trigger_api_triggers_trigger_id_put**](TriggersApi.md#update_trigger_api_triggers_trigger_id_put) | **PUT** /api/triggers/{trigger_id} | Update Trigger


# **create_agent_trigger_api_triggers_agents_agent_id_triggers_post**
> TriggerResponse create_agent_trigger_api_triggers_agents_agent_id_triggers_post(agent_id, trigger_create_request)

Create Agent Trigger

Create a new trigger for an agent

### Example


```python
import suna_api_client
from suna_api_client.models.trigger_create_request import TriggerCreateRequest
from suna_api_client.models.trigger_response import TriggerResponse
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
    api_instance = suna_api_client.TriggersApi(api_client)
    agent_id = 'agent_id_example' # str | 
    trigger_create_request = suna_api_client.TriggerCreateRequest() # TriggerCreateRequest | 

    try:
        # Create Agent Trigger
        api_response = api_instance.create_agent_trigger_api_triggers_agents_agent_id_triggers_post(agent_id, trigger_create_request)
        print("The response of TriggersApi->create_agent_trigger_api_triggers_agents_agent_id_triggers_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TriggersApi->create_agent_trigger_api_triggers_agents_agent_id_triggers_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **trigger_create_request** | [**TriggerCreateRequest**](TriggerCreateRequest.md)|  | 

### Return type

[**TriggerResponse**](TriggerResponse.md)

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
    api_instance = suna_api_client.TriggersApi(api_client)
    agent_id = 'agent_id_example' # str | 
    workflow_create_request = suna_api_client.WorkflowCreateRequest() # WorkflowCreateRequest | 

    try:
        # Create Agent Workflow
        api_response = api_instance.create_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_post(agent_id, workflow_create_request)
        print("The response of TriggersApi->create_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TriggersApi->create_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_post: %s\n" % e)
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
    api_instance = suna_api_client.TriggersApi(api_client)
    agent_id = 'agent_id_example' # str | 
    workflow_id = 'workflow_id_example' # str | 

    try:
        # Delete Agent Workflow
        api_response = api_instance.delete_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_delete(agent_id, workflow_id)
        print("The response of TriggersApi->delete_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TriggersApi->delete_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_delete: %s\n" % e)
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

# **delete_trigger_api_triggers_trigger_id_delete**
> object delete_trigger_api_triggers_trigger_id_delete(trigger_id)

Delete Trigger

Delete a trigger

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
    api_instance = suna_api_client.TriggersApi(api_client)
    trigger_id = 'trigger_id_example' # str | 

    try:
        # Delete Trigger
        api_response = api_instance.delete_trigger_api_triggers_trigger_id_delete(trigger_id)
        print("The response of TriggersApi->delete_trigger_api_triggers_trigger_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TriggersApi->delete_trigger_api_triggers_trigger_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_id** | **str**|  | 

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
    api_instance = suna_api_client.TriggersApi(api_client)
    agent_id = 'agent_id_example' # str | 
    workflow_id = 'workflow_id_example' # str | 
    workflow_execute_request = suna_api_client.WorkflowExecuteRequest() # WorkflowExecuteRequest | 

    try:
        # Execute Agent Workflow
        api_response = api_instance.execute_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_execute_post(agent_id, workflow_id, workflow_execute_request)
        print("The response of TriggersApi->execute_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_execute_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TriggersApi->execute_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_execute_post: %s\n" % e)
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

# **get_agent_triggers_api_triggers_agents_agent_id_triggers_get**
> List[TriggerResponse] get_agent_triggers_api_triggers_agents_agent_id_triggers_get(agent_id)

Get Agent Triggers

### Example


```python
import suna_api_client
from suna_api_client.models.trigger_response import TriggerResponse
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
    api_instance = suna_api_client.TriggersApi(api_client)
    agent_id = 'agent_id_example' # str | 

    try:
        # Get Agent Triggers
        api_response = api_instance.get_agent_triggers_api_triggers_agents_agent_id_triggers_get(agent_id)
        print("The response of TriggersApi->get_agent_triggers_api_triggers_agents_agent_id_triggers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TriggersApi->get_agent_triggers_api_triggers_agents_agent_id_triggers_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 

### Return type

[**List[TriggerResponse]**](TriggerResponse.md)

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

# **get_agent_upcoming_runs_api_triggers_agents_agent_id_upcoming_runs_get**
> UpcomingRunsResponse get_agent_upcoming_runs_api_triggers_agents_agent_id_upcoming_runs_get(agent_id, limit=limit)

Get Agent Upcoming Runs

Get upcoming scheduled runs for agent triggers

### Example


```python
import suna_api_client
from suna_api_client.models.upcoming_runs_response import UpcomingRunsResponse
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
    api_instance = suna_api_client.TriggersApi(api_client)
    agent_id = 'agent_id_example' # str | 
    limit = 10 # int |  (optional) (default to 10)

    try:
        # Get Agent Upcoming Runs
        api_response = api_instance.get_agent_upcoming_runs_api_triggers_agents_agent_id_upcoming_runs_get(agent_id, limit=limit)
        print("The response of TriggersApi->get_agent_upcoming_runs_api_triggers_agents_agent_id_upcoming_runs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TriggersApi->get_agent_upcoming_runs_api_triggers_agents_agent_id_upcoming_runs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 10]

### Return type

[**UpcomingRunsResponse**](UpcomingRunsResponse.md)

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
    api_instance = suna_api_client.TriggersApi(api_client)
    agent_id = 'agent_id_example' # str | 

    try:
        # Get Agent Workflows
        api_response = api_instance.get_agent_workflows_api_triggers_workflows_agents_agent_id_workflows_get(agent_id)
        print("The response of TriggersApi->get_agent_workflows_api_triggers_workflows_agents_agent_id_workflows_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TriggersApi->get_agent_workflows_api_triggers_workflows_agents_agent_id_workflows_get: %s\n" % e)
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

# **get_all_user_triggers_api_triggers_all_get**
> List[Dict[str, object]] get_all_user_triggers_api_triggers_all_get()

Get All User Triggers

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
    api_instance = suna_api_client.TriggersApi(api_client)

    try:
        # Get All User Triggers
        api_response = api_instance.get_all_user_triggers_api_triggers_all_get()
        print("The response of TriggersApi->get_all_user_triggers_api_triggers_all_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TriggersApi->get_all_user_triggers_api_triggers_all_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**List[Dict[str, object]]**

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

# **get_providers_api_triggers_providers_get**
> object get_providers_api_triggers_providers_get()

Get Providers

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
    api_instance = suna_api_client.TriggersApi(api_client)

    try:
        # Get Providers
        api_response = api_instance.get_providers_api_triggers_providers_get()
        print("The response of TriggersApi->get_providers_api_triggers_providers_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TriggersApi->get_providers_api_triggers_providers_get: %s\n" % e)
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

# **get_trigger_api_triggers_trigger_id_get**
> TriggerResponse get_trigger_api_triggers_trigger_id_get(trigger_id)

Get Trigger

Get a trigger by ID

### Example


```python
import suna_api_client
from suna_api_client.models.trigger_response import TriggerResponse
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
    api_instance = suna_api_client.TriggersApi(api_client)
    trigger_id = 'trigger_id_example' # str | 

    try:
        # Get Trigger
        api_response = api_instance.get_trigger_api_triggers_trigger_id_get(trigger_id)
        print("The response of TriggersApi->get_trigger_api_triggers_trigger_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TriggersApi->get_trigger_api_triggers_trigger_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_id** | **str**|  | 

### Return type

[**TriggerResponse**](TriggerResponse.md)

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

# **trigger_webhook_api_triggers_trigger_id_webhook_post**
> object trigger_webhook_api_triggers_trigger_id_webhook_post(trigger_id)

Trigger Webhook

Handle incoming webhook for a trigger

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
    api_instance = suna_api_client.TriggersApi(api_client)
    trigger_id = 'trigger_id_example' # str | 

    try:
        # Trigger Webhook
        api_response = api_instance.trigger_webhook_api_triggers_trigger_id_webhook_post(trigger_id)
        print("The response of TriggersApi->trigger_webhook_api_triggers_trigger_id_webhook_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TriggersApi->trigger_webhook_api_triggers_trigger_id_webhook_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_id** | **str**|  | 

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
    api_instance = suna_api_client.TriggersApi(api_client)
    agent_id = 'agent_id_example' # str | 
    workflow_id = 'workflow_id_example' # str | 
    workflow_update_request = suna_api_client.WorkflowUpdateRequest() # WorkflowUpdateRequest | 

    try:
        # Update Agent Workflow
        api_response = api_instance.update_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_put(agent_id, workflow_id, workflow_update_request)
        print("The response of TriggersApi->update_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TriggersApi->update_agent_workflow_api_triggers_workflows_agents_agent_id_workflows_workflow_id_put: %s\n" % e)
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

# **update_trigger_api_triggers_trigger_id_put**
> TriggerResponse update_trigger_api_triggers_trigger_id_put(trigger_id, trigger_update_request)

Update Trigger

Update a trigger

### Example


```python
import suna_api_client
from suna_api_client.models.trigger_response import TriggerResponse
from suna_api_client.models.trigger_update_request import TriggerUpdateRequest
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
    api_instance = suna_api_client.TriggersApi(api_client)
    trigger_id = 'trigger_id_example' # str | 
    trigger_update_request = suna_api_client.TriggerUpdateRequest() # TriggerUpdateRequest | 

    try:
        # Update Trigger
        api_response = api_instance.update_trigger_api_triggers_trigger_id_put(trigger_id, trigger_update_request)
        print("The response of TriggersApi->update_trigger_api_triggers_trigger_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TriggersApi->update_trigger_api_triggers_trigger_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trigger_id** | **str**|  | 
 **trigger_update_request** | [**TriggerUpdateRequest**](TriggerUpdateRequest.md)|  | 

### Return type

[**TriggerResponse**](TriggerResponse.md)

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

