# suna_api_client.DefaultApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activate_version_api_agents_agent_id_versions_version_id_activate_put**](DefaultApi.md#activate_version_api_agents_agent_id_versions_version_id_activate_put) | **PUT** /api/agents/{agent_id}/versions/{version_id}/activate | Activate Version
[**add_message_to_thread_api_threads_thread_id_messages_add_post**](DefaultApi.md#add_message_to_thread_api_threads_thread_id_messages_add_post) | **POST** /api/threads/{thread_id}/messages/add | Add Message To Thread
[**analyze_json_for_import_api_agents_json_analyze_post**](DefaultApi.md#analyze_json_for_import_api_agents_json_analyze_post) | **POST** /api/agents/json/analyze | Analyze Json For Import
[**bulk_delete_credential_profiles_api_secure_mcp_credential_profiles_bulk_delete_post**](DefaultApi.md#bulk_delete_credential_profiles_api_secure_mcp_credential_profiles_bulk_delete_post) | **POST** /api/secure-mcp/credential-profiles/bulk-delete | Bulk Delete Credential Profiles
[**compare_versions_api_agents_agent_id_versions_version1_id_compare_version2_id_get**](DefaultApi.md#compare_versions_api_agents_agent_id_versions_version1_id_compare_version2_id_get) | **GET** /api/agents/{agent_id}/versions/{version1_id}/compare/{version2_id} | Compare Versions
[**create_agent_api_agents_post**](DefaultApi.md#create_agent_api_agents_post) | **POST** /api/agents | Create Agent
[**create_api_key_api_api_keys_post**](DefaultApi.md#create_api_key_api_api_keys_post) | **POST** /api/api-keys | Create Api Key
[**create_message_api_threads_thread_id_messages_post**](DefaultApi.md#create_message_api_threads_thread_id_messages_post) | **POST** /api/threads/{thread_id}/messages | Create Message
[**create_template_from_agent_api_templates_post**](DefaultApi.md#create_template_from_agent_api_templates_post) | **POST** /api/templates | Create Template From Agent
[**create_thread_api_threads_post**](DefaultApi.md#create_thread_api_threads_post) | **POST** /api/threads | Create Thread
[**create_version_api_agents_agent_id_versions_post**](DefaultApi.md#create_version_api_agents_agent_id_versions_post) | **POST** /api/agents/{agent_id}/versions | Create Version
[**delete_agent_api_agents_agent_id_delete**](DefaultApi.md#delete_agent_api_agents_agent_id_delete) | **DELETE** /api/agents/{agent_id} | Delete Agent
[**delete_api_key_api_api_keys_key_id_delete**](DefaultApi.md#delete_api_key_api_api_keys_key_id_delete) | **DELETE** /api/api-keys/{key_id} | Delete Api Key
[**delete_credential_api_secure_mcp_credentials_mcp_qualified_name_delete**](DefaultApi.md#delete_credential_api_secure_mcp_credentials_mcp_qualified_name_delete) | **DELETE** /api/secure-mcp/credentials/{mcp_qualified_name} | Delete Credential
[**delete_credential_profile_api_secure_mcp_credential_profiles_profile_id_delete**](DefaultApi.md#delete_credential_profile_api_secure_mcp_credential_profiles_profile_id_delete) | **DELETE** /api/secure-mcp/credential-profiles/{profile_id} | Delete Credential Profile
[**delete_message_api_threads_thread_id_messages_message_id_delete**](DefaultApi.md#delete_message_api_threads_thread_id_messages_message_id_delete) | **DELETE** /api/threads/{thread_id}/messages/{message_id} | Delete Message
[**delete_template_api_templates_template_id_delete**](DefaultApi.md#delete_template_api_templates_template_id_delete) | **DELETE** /api/templates/{template_id} | Delete Template
[**discover_custom_mcp_tools_api_mcp_discover_custom_tools_post**](DefaultApi.md#discover_custom_mcp_tools_api_mcp_discover_custom_tools_post) | **POST** /api/mcp/discover-custom-tools | Discover Custom Mcp Tools
[**export_agent_api_agents_agent_id_export_get**](DefaultApi.md#export_agent_api_agents_agent_id_export_get) | **GET** /api/agents/{agent_id}/export | Export Agent
[**generate_agent_icon_api_agents_generate_icon_post**](DefaultApi.md#generate_agent_icon_api_agents_generate_icon_post) | **POST** /api/agents/generate-icon | Generate Agent Icon
[**get_agent_api_agents_agent_id_get**](DefaultApi.md#get_agent_api_agents_agent_id_get) | **GET** /api/agents/{agent_id} | Get Agent
[**get_agent_run_api_agent_run_agent_run_id_get**](DefaultApi.md#get_agent_run_api_agent_run_agent_run_id_get) | **GET** /api/agent-run/{agent_run_id} | Get Agent Run
[**get_agent_run_api_agent_runs_agent_run_id_get**](DefaultApi.md#get_agent_run_api_agent_runs_agent_run_id_get) | **GET** /api/agent-runs/{agent_run_id} | Get Agent Run
[**get_agent_runs_api_thread_thread_id_agent_runs_get**](DefaultApi.md#get_agent_runs_api_thread_thread_id_agent_runs_get) | **GET** /api/thread/{thread_id}/agent-runs | Get Agent Runs
[**get_agent_tools_api_agents_agent_id_tools_get**](DefaultApi.md#get_agent_tools_api_agents_agent_id_tools_get) | **GET** /api/agents/{agent_id}/tools | Get Agent Tools
[**get_agents_api_agents_get**](DefaultApi.md#get_agents_api_agents_get) | **GET** /api/agents | Get Agents
[**get_composio_mcp_url_api_secure_mcp_composio_profiles_profile_id_mcp_url_get**](DefaultApi.md#get_composio_mcp_url_api_secure_mcp_composio_profiles_profile_id_mcp_url_get) | **GET** /api/secure-mcp/composio-profiles/{profile_id}/mcp-url | Get Composio Mcp Url
[**get_composio_profiles_api_secure_mcp_composio_profiles_get**](DefaultApi.md#get_composio_profiles_api_secure_mcp_composio_profiles_get) | **GET** /api/secure-mcp/composio-profiles | Get Composio Profiles
[**get_credential_profile_api_secure_mcp_credential_profiles_profile_profile_id_get**](DefaultApi.md#get_credential_profile_api_secure_mcp_credential_profiles_profile_profile_id_get) | **GET** /api/secure-mcp/credential-profiles/profile/{profile_id} | Get Credential Profile
[**get_credential_profiles_for_mcp_api_secure_mcp_credential_profiles_mcp_qualified_name_get**](DefaultApi.md#get_credential_profiles_for_mcp_api_secure_mcp_credential_profiles_mcp_qualified_name_get) | **GET** /api/secure-mcp/credential-profiles/{mcp_qualified_name} | Get Credential Profiles For Mcp
[**get_custom_mcp_tools_for_agent_api_agents_agent_id_custom_mcp_tools_get**](DefaultApi.md#get_custom_mcp_tools_for_agent_api_agents_agent_id_custom_mcp_tools_get) | **GET** /api/agents/{agent_id}/custom-mcp-tools | Get Custom Mcp Tools For Agent
[**get_marketplace_templates_api_templates_marketplace_get**](DefaultApi.md#get_marketplace_templates_api_templates_marketplace_get) | **GET** /api/templates/marketplace | Get Marketplace Templates
[**get_my_templates_api_templates_my_get**](DefaultApi.md#get_my_templates_api_templates_my_get) | **GET** /api/templates/my | Get My Templates
[**get_public_template_api_templates_public_template_id_get**](DefaultApi.md#get_public_template_api_templates_public_template_id_get) | **GET** /api/templates/public/{template_id} | Get Public Template
[**get_template_api_templates_template_id_get**](DefaultApi.md#get_template_api_templates_template_id_get) | **GET** /api/templates/{template_id} | Get Template
[**get_thread_agent_api_thread_thread_id_agent_get**](DefaultApi.md#get_thread_agent_api_thread_thread_id_agent_get) | **GET** /api/thread/{thread_id}/agent | Get Thread Agent
[**get_thread_api_threads_thread_id_get**](DefaultApi.md#get_thread_api_threads_thread_id_get) | **GET** /api/threads/{thread_id} | Get Thread
[**get_thread_messages_api_threads_thread_id_messages_get**](DefaultApi.md#get_thread_messages_api_threads_thread_id_messages_get) | **GET** /api/threads/{thread_id}/messages | Get Thread Messages
[**get_user_credential_profiles_api_secure_mcp_credential_profiles_get**](DefaultApi.md#get_user_credential_profiles_api_secure_mcp_credential_profiles_get) | **GET** /api/secure-mcp/credential-profiles | Get User Credential Profiles
[**get_user_credentials_api_secure_mcp_credentials_get**](DefaultApi.md#get_user_credentials_api_secure_mcp_credentials_get) | **GET** /api/secure-mcp/credentials | Get User Credentials
[**get_user_threads_api_threads_get**](DefaultApi.md#get_user_threads_api_threads_get) | **GET** /api/threads | Get User Threads
[**get_version_api_agents_agent_id_versions_version_id_get**](DefaultApi.md#get_version_api_agents_agent_id_versions_version_id_get) | **GET** /api/agents/{agent_id}/versions/{version_id} | Get Version
[**get_versions_api_agents_agent_id_versions_get**](DefaultApi.md#get_versions_api_agents_agent_id_versions_get) | **GET** /api/agents/{agent_id}/versions | Get Versions
[**health_check_api_health_docker_get**](DefaultApi.md#health_check_api_health_docker_get) | **GET** /api/health-docker | Health Check
[**health_check_api_health_get**](DefaultApi.md#health_check_api_health_get) | **GET** /api/health | Health Check
[**import_agent_from_json_api_agents_json_import_post**](DefaultApi.md#import_agent_from_json_api_agents_json_import_post) | **POST** /api/agents/json/import | Import Agent From Json
[**initiate_agent_with_files_api_agent_initiate_post**](DefaultApi.md#initiate_agent_with_files_api_agent_initiate_post) | **POST** /api/agent/initiate | Initiate Agent With Files
[**install_template_api_templates_install_post**](DefaultApi.md#install_template_api_templates_install_post) | **POST** /api/templates/install | Install Template
[**list_api_keys_api_api_keys_get**](DefaultApi.md#list_api_keys_api_api_keys_get) | **GET** /api/api-keys | List Api Keys
[**publish_template_api_templates_template_id_publish_post**](DefaultApi.md#publish_template_api_templates_template_id_publish_post) | **POST** /api/templates/{template_id}/publish | Publish Template
[**revoke_api_key_api_api_keys_key_id_revoke_patch**](DefaultApi.md#revoke_api_key_api_api_keys_key_id_revoke_patch) | **PATCH** /api/api-keys/{key_id}/revoke | Revoke Api Key
[**rollback_to_version_api_agents_agent_id_versions_version_id_rollback_post**](DefaultApi.md#rollback_to_version_api_agents_agent_id_versions_version_id_rollback_post) | **POST** /api/agents/{agent_id}/versions/{version_id}/rollback | Rollback To Version
[**send_welcome_email_api_send_welcome_email_post**](DefaultApi.md#send_welcome_email_api_send_welcome_email_post) | **POST** /api/send-welcome-email | Send Welcome Email
[**set_default_credential_profile_api_secure_mcp_credential_profiles_profile_id_set_default_put**](DefaultApi.md#set_default_credential_profile_api_secure_mcp_credential_profiles_profile_id_set_default_put) | **PUT** /api/secure-mcp/credential-profiles/{profile_id}/set-default | Set Default Credential Profile
[**start_agent_api_thread_thread_id_agent_start_post**](DefaultApi.md#start_agent_api_thread_thread_id_agent_start_post) | **POST** /api/thread/{thread_id}/agent/start | Start Agent
[**stop_agent_api_agent_run_agent_run_id_stop_post**](DefaultApi.md#stop_agent_api_agent_run_agent_run_id_stop_post) | **POST** /api/agent-run/{agent_run_id}/stop | Stop Agent
[**store_credential_api_secure_mcp_credentials_post**](DefaultApi.md#store_credential_api_secure_mcp_credentials_post) | **POST** /api/secure-mcp/credentials | Store Credential
[**store_credential_profile_api_secure_mcp_credential_profiles_post**](DefaultApi.md#store_credential_profile_api_secure_mcp_credential_profiles_post) | **POST** /api/secure-mcp/credential-profiles | Store Credential Profile
[**stream_agent_run_api_agent_run_agent_run_id_stream_get**](DefaultApi.md#stream_agent_run_api_agent_run_agent_run_id_stream_get) | **GET** /api/agent-run/{agent_run_id}/stream | Stream Agent Run
[**unpublish_template_api_templates_template_id_unpublish_post**](DefaultApi.md#unpublish_template_api_templates_template_id_unpublish_post) | **POST** /api/templates/{template_id}/unpublish | Unpublish Template
[**update_agent_api_agents_agent_id_put**](DefaultApi.md#update_agent_api_agents_agent_id_put) | **PUT** /api/agents/{agent_id} | Update Agent
[**update_agent_custom_mcps_api_agents_agent_id_custom_mcp_tools_put**](DefaultApi.md#update_agent_custom_mcps_api_agents_agent_id_custom_mcp_tools_put) | **PUT** /api/agents/{agent_id}/custom-mcp-tools | Update Agent Custom Mcps
[**update_custom_mcp_tools_for_agent_api_agents_agent_id_custom_mcp_tools_post**](DefaultApi.md#update_custom_mcp_tools_for_agent_api_agents_agent_id_custom_mcp_tools_post) | **POST** /api/agents/{agent_id}/custom-mcp-tools | Update Custom Mcp Tools For Agent
[**update_version_details_api_agents_agent_id_versions_version_id_details_put**](DefaultApi.md#update_version_details_api_agents_agent_id_versions_version_id_details_put) | **PUT** /api/agents/{agent_id}/versions/{version_id}/details | Update Version Details


# **activate_version_api_agents_agent_id_versions_version_id_activate_put**
> object activate_version_api_agents_agent_id_versions_version_id_activate_put(agent_id, version_id)

Activate Version

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
    api_instance = suna_api_client.DefaultApi(api_client)
    agent_id = 'agent_id_example' # str | 
    version_id = 'version_id_example' # str | 

    try:
        # Activate Version
        api_response = api_instance.activate_version_api_agents_agent_id_versions_version_id_activate_put(agent_id, version_id)
        print("The response of DefaultApi->activate_version_api_agents_agent_id_versions_version_id_activate_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->activate_version_api_agents_agent_id_versions_version_id_activate_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **version_id** | **str**|  | 

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

# **add_message_to_thread_api_threads_thread_id_messages_add_post**
> object add_message_to_thread_api_threads_thread_id_messages_add_post(thread_id, message)

Add Message To Thread

Add a message to a thread

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
    api_instance = suna_api_client.DefaultApi(api_client)
    thread_id = 'thread_id_example' # str | 
    message = 'message_example' # str | 

    try:
        # Add Message To Thread
        api_response = api_instance.add_message_to_thread_api_threads_thread_id_messages_add_post(thread_id, message)
        print("The response of DefaultApi->add_message_to_thread_api_threads_thread_id_messages_add_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->add_message_to_thread_api_threads_thread_id_messages_add_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**|  | 
 **message** | **str**|  | 

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

# **analyze_json_for_import_api_agents_json_analyze_post**
> JsonAnalysisResponse analyze_json_for_import_api_agents_json_analyze_post(json_analysis_request)

Analyze Json For Import

Analyze imported JSON to determine required credentials and configurations

### Example


```python
import suna_api_client
from suna_api_client.models.json_analysis_request import JsonAnalysisRequest
from suna_api_client.models.json_analysis_response import JsonAnalysisResponse
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
    api_instance = suna_api_client.DefaultApi(api_client)
    json_analysis_request = suna_api_client.JsonAnalysisRequest() # JsonAnalysisRequest | 

    try:
        # Analyze Json For Import
        api_response = api_instance.analyze_json_for_import_api_agents_json_analyze_post(json_analysis_request)
        print("The response of DefaultApi->analyze_json_for_import_api_agents_json_analyze_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->analyze_json_for_import_api_agents_json_analyze_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_analysis_request** | [**JsonAnalysisRequest**](JsonAnalysisRequest.md)|  | 

### Return type

[**JsonAnalysisResponse**](JsonAnalysisResponse.md)

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

# **bulk_delete_credential_profiles_api_secure_mcp_credential_profiles_bulk_delete_post**
> BulkDeleteProfilesResponse bulk_delete_credential_profiles_api_secure_mcp_credential_profiles_bulk_delete_post(bulk_delete_profiles_request)

Bulk Delete Credential Profiles

### Example


```python
import suna_api_client
from suna_api_client.models.bulk_delete_profiles_request import BulkDeleteProfilesRequest
from suna_api_client.models.bulk_delete_profiles_response import BulkDeleteProfilesResponse
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
    api_instance = suna_api_client.DefaultApi(api_client)
    bulk_delete_profiles_request = suna_api_client.BulkDeleteProfilesRequest() # BulkDeleteProfilesRequest | 

    try:
        # Bulk Delete Credential Profiles
        api_response = api_instance.bulk_delete_credential_profiles_api_secure_mcp_credential_profiles_bulk_delete_post(bulk_delete_profiles_request)
        print("The response of DefaultApi->bulk_delete_credential_profiles_api_secure_mcp_credential_profiles_bulk_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->bulk_delete_credential_profiles_api_secure_mcp_credential_profiles_bulk_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **bulk_delete_profiles_request** | [**BulkDeleteProfilesRequest**](BulkDeleteProfilesRequest.md)|  | 

### Return type

[**BulkDeleteProfilesResponse**](BulkDeleteProfilesResponse.md)

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

# **compare_versions_api_agents_agent_id_versions_version1_id_compare_version2_id_get**
> VersionComparisonResponse compare_versions_api_agents_agent_id_versions_version1_id_compare_version2_id_get(agent_id, version1_id, version2_id)

Compare Versions

### Example


```python
import suna_api_client
from suna_api_client.models.version_comparison_response import VersionComparisonResponse
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
    api_instance = suna_api_client.DefaultApi(api_client)
    agent_id = 'agent_id_example' # str | 
    version1_id = 'version1_id_example' # str | 
    version2_id = 'version2_id_example' # str | 

    try:
        # Compare Versions
        api_response = api_instance.compare_versions_api_agents_agent_id_versions_version1_id_compare_version2_id_get(agent_id, version1_id, version2_id)
        print("The response of DefaultApi->compare_versions_api_agents_agent_id_versions_version1_id_compare_version2_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->compare_versions_api_agents_agent_id_versions_version1_id_compare_version2_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **version1_id** | **str**|  | 
 **version2_id** | **str**|  | 

### Return type

[**VersionComparisonResponse**](VersionComparisonResponse.md)

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

# **create_agent_api_agents_post**
> AgentResponse create_agent_api_agents_post(agent_create_request)

Create Agent

### Example


```python
import suna_api_client
from suna_api_client.models.agent_create_request import AgentCreateRequest
from suna_api_client.models.agent_response import AgentResponse
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
    api_instance = suna_api_client.DefaultApi(api_client)
    agent_create_request = suna_api_client.AgentCreateRequest() # AgentCreateRequest | 

    try:
        # Create Agent
        api_response = api_instance.create_agent_api_agents_post(agent_create_request)
        print("The response of DefaultApi->create_agent_api_agents_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_agent_api_agents_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_create_request** | [**AgentCreateRequest**](AgentCreateRequest.md)|  | 

### Return type

[**AgentResponse**](AgentResponse.md)

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

# **create_api_key_api_api_keys_post**
> APIKeyCreateResponse create_api_key_api_api_keys_post(api_key_create_request)

Create Api Key

Create a new API key for the authenticated user

Args:
    request: API key creation request with title, description, and expiration
    user_id: Authenticated user ID from JWT or API key
    api_key_service: API key service instance

Returns:
    APIKeyCreateResponse: The newly created API key details including the key value

### Example


```python
import suna_api_client
from suna_api_client.models.api_key_create_request import APIKeyCreateRequest
from suna_api_client.models.api_key_create_response import APIKeyCreateResponse
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
    api_instance = suna_api_client.DefaultApi(api_client)
    api_key_create_request = suna_api_client.APIKeyCreateRequest() # APIKeyCreateRequest | 

    try:
        # Create Api Key
        api_response = api_instance.create_api_key_api_api_keys_post(api_key_create_request)
        print("The response of DefaultApi->create_api_key_api_api_keys_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_api_key_api_api_keys_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **api_key_create_request** | [**APIKeyCreateRequest**](APIKeyCreateRequest.md)|  | 

### Return type

[**APIKeyCreateResponse**](APIKeyCreateResponse.md)

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

# **create_message_api_threads_thread_id_messages_post**
> object create_message_api_threads_thread_id_messages_post(thread_id, message_create_request)

Create Message

Create a new message in a thread.

### Example


```python
import suna_api_client
from suna_api_client.models.message_create_request import MessageCreateRequest
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
    api_instance = suna_api_client.DefaultApi(api_client)
    thread_id = 'thread_id_example' # str | 
    message_create_request = suna_api_client.MessageCreateRequest() # MessageCreateRequest | 

    try:
        # Create Message
        api_response = api_instance.create_message_api_threads_thread_id_messages_post(thread_id, message_create_request)
        print("The response of DefaultApi->create_message_api_threads_thread_id_messages_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_message_api_threads_thread_id_messages_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**|  | 
 **message_create_request** | [**MessageCreateRequest**](MessageCreateRequest.md)|  | 

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

# **create_template_from_agent_api_templates_post**
> Dict[str, str] create_template_from_agent_api_templates_post(create_template_request)

Create Template From Agent

### Example


```python
import suna_api_client
from suna_api_client.models.create_template_request import CreateTemplateRequest
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
    api_instance = suna_api_client.DefaultApi(api_client)
    create_template_request = suna_api_client.CreateTemplateRequest() # CreateTemplateRequest | 

    try:
        # Create Template From Agent
        api_response = api_instance.create_template_from_agent_api_templates_post(create_template_request)
        print("The response of DefaultApi->create_template_from_agent_api_templates_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_template_from_agent_api_templates_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_template_request** | [**CreateTemplateRequest**](CreateTemplateRequest.md)|  | 

### Return type

**Dict[str, str]**

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

# **create_thread_api_threads_post**
> CreateThreadResponse create_thread_api_threads_post(name=name)

Create Thread

Create a new thread without starting an agent run.

[WARNING] Keep in sync with initiate endpoint.

### Example


```python
import suna_api_client
from suna_api_client.models.create_thread_response import CreateThreadResponse
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
    api_instance = suna_api_client.DefaultApi(api_client)
    name = 'name_example' # str |  (optional)

    try:
        # Create Thread
        api_response = api_instance.create_thread_api_threads_post(name=name)
        print("The response of DefaultApi->create_thread_api_threads_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_thread_api_threads_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**|  | [optional] 

### Return type

[**CreateThreadResponse**](CreateThreadResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/x-www-form-urlencoded
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_version_api_agents_agent_id_versions_post**
> VersionResponse create_version_api_agents_agent_id_versions_post(agent_id, create_version_request)

Create Version

### Example


```python
import suna_api_client
from suna_api_client.models.create_version_request import CreateVersionRequest
from suna_api_client.models.version_response import VersionResponse
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
    api_instance = suna_api_client.DefaultApi(api_client)
    agent_id = 'agent_id_example' # str | 
    create_version_request = suna_api_client.CreateVersionRequest() # CreateVersionRequest | 

    try:
        # Create Version
        api_response = api_instance.create_version_api_agents_agent_id_versions_post(agent_id, create_version_request)
        print("The response of DefaultApi->create_version_api_agents_agent_id_versions_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->create_version_api_agents_agent_id_versions_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **create_version_request** | [**CreateVersionRequest**](CreateVersionRequest.md)|  | 

### Return type

[**VersionResponse**](VersionResponse.md)

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

# **delete_agent_api_agents_agent_id_delete**
> object delete_agent_api_agents_agent_id_delete(agent_id)

Delete Agent

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
    api_instance = suna_api_client.DefaultApi(api_client)
    agent_id = 'agent_id_example' # str | 

    try:
        # Delete Agent
        api_response = api_instance.delete_agent_api_agents_agent_id_delete(agent_id)
        print("The response of DefaultApi->delete_agent_api_agents_agent_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_agent_api_agents_agent_id_delete: %s\n" % e)
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

# **delete_api_key_api_api_keys_key_id_delete**
> object delete_api_key_api_api_keys_key_id_delete(key_id)

Delete Api Key

Permanently delete an API key

Args:
    key_id: The ID of the API key to delete
    user_id: Authenticated user ID from JWT or API key
    api_key_service: API key service instance

Returns:
    dict: Success message

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
    api_instance = suna_api_client.DefaultApi(api_client)
    key_id = 'key_id_example' # str | 

    try:
        # Delete Api Key
        api_response = api_instance.delete_api_key_api_api_keys_key_id_delete(key_id)
        print("The response of DefaultApi->delete_api_key_api_api_keys_key_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_api_key_api_api_keys_key_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**|  | 

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

# **delete_credential_api_secure_mcp_credentials_mcp_qualified_name_delete**
> object delete_credential_api_secure_mcp_credentials_mcp_qualified_name_delete(mcp_qualified_name)

Delete Credential

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
    api_instance = suna_api_client.DefaultApi(api_client)
    mcp_qualified_name = 'mcp_qualified_name_example' # str | 

    try:
        # Delete Credential
        api_response = api_instance.delete_credential_api_secure_mcp_credentials_mcp_qualified_name_delete(mcp_qualified_name)
        print("The response of DefaultApi->delete_credential_api_secure_mcp_credentials_mcp_qualified_name_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_credential_api_secure_mcp_credentials_mcp_qualified_name_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mcp_qualified_name** | **str**|  | 

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

# **delete_credential_profile_api_secure_mcp_credential_profiles_profile_id_delete**
> object delete_credential_profile_api_secure_mcp_credential_profiles_profile_id_delete(profile_id)

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
    api_instance = suna_api_client.DefaultApi(api_client)
    profile_id = 'profile_id_example' # str | 

    try:
        # Delete Credential Profile
        api_response = api_instance.delete_credential_profile_api_secure_mcp_credential_profiles_profile_id_delete(profile_id)
        print("The response of DefaultApi->delete_credential_profile_api_secure_mcp_credential_profiles_profile_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_credential_profile_api_secure_mcp_credential_profiles_profile_id_delete: %s\n" % e)
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

# **delete_message_api_threads_thread_id_messages_message_id_delete**
> object delete_message_api_threads_thread_id_messages_message_id_delete(thread_id, message_id)

Delete Message

Delete a message from a thread.

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
    api_instance = suna_api_client.DefaultApi(api_client)
    thread_id = 'thread_id_example' # str | 
    message_id = 'message_id_example' # str | 

    try:
        # Delete Message
        api_response = api_instance.delete_message_api_threads_thread_id_messages_message_id_delete(thread_id, message_id)
        print("The response of DefaultApi->delete_message_api_threads_thread_id_messages_message_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_message_api_threads_thread_id_messages_message_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**|  | 
 **message_id** | **str**|  | 

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

# **delete_template_api_templates_template_id_delete**
> object delete_template_api_templates_template_id_delete(template_id)

Delete Template

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
    api_instance = suna_api_client.DefaultApi(api_client)
    template_id = 'template_id_example' # str | 

    try:
        # Delete Template
        api_response = api_instance.delete_template_api_templates_template_id_delete(template_id)
        print("The response of DefaultApi->delete_template_api_templates_template_id_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->delete_template_api_templates_template_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

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

# **discover_custom_mcp_tools_api_mcp_discover_custom_tools_post**
> object discover_custom_mcp_tools_api_mcp_discover_custom_tools_post(custom_mcp_discover_request)

Discover Custom Mcp Tools

### Example


```python
import suna_api_client
from suna_api_client.models.custom_mcp_discover_request import CustomMCPDiscoverRequest
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
    api_instance = suna_api_client.DefaultApi(api_client)
    custom_mcp_discover_request = suna_api_client.CustomMCPDiscoverRequest() # CustomMCPDiscoverRequest | 

    try:
        # Discover Custom Mcp Tools
        api_response = api_instance.discover_custom_mcp_tools_api_mcp_discover_custom_tools_post(custom_mcp_discover_request)
        print("The response of DefaultApi->discover_custom_mcp_tools_api_mcp_discover_custom_tools_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->discover_custom_mcp_tools_api_mcp_discover_custom_tools_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **custom_mcp_discover_request** | [**CustomMCPDiscoverRequest**](CustomMCPDiscoverRequest.md)|  | 

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

# **export_agent_api_agents_agent_id_export_get**
> object export_agent_api_agents_agent_id_export_get(agent_id)

Export Agent

Export an agent configuration as JSON

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
    api_instance = suna_api_client.DefaultApi(api_client)
    agent_id = 'agent_id_example' # str | 

    try:
        # Export Agent
        api_response = api_instance.export_agent_api_agents_agent_id_export_get(agent_id)
        print("The response of DefaultApi->export_agent_api_agents_agent_id_export_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->export_agent_api_agents_agent_id_export_get: %s\n" % e)
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

# **generate_agent_icon_api_agents_generate_icon_post**
> AgentIconGenerationResponse generate_agent_icon_api_agents_generate_icon_post(agent_icon_generation_request)

Generate Agent Icon

Generate an appropriate icon and colors for an agent based on its name and description.

### Example


```python
import suna_api_client
from suna_api_client.models.agent_icon_generation_request import AgentIconGenerationRequest
from suna_api_client.models.agent_icon_generation_response import AgentIconGenerationResponse
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
    api_instance = suna_api_client.DefaultApi(api_client)
    agent_icon_generation_request = suna_api_client.AgentIconGenerationRequest() # AgentIconGenerationRequest | 

    try:
        # Generate Agent Icon
        api_response = api_instance.generate_agent_icon_api_agents_generate_icon_post(agent_icon_generation_request)
        print("The response of DefaultApi->generate_agent_icon_api_agents_generate_icon_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->generate_agent_icon_api_agents_generate_icon_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_icon_generation_request** | [**AgentIconGenerationRequest**](AgentIconGenerationRequest.md)|  | 

### Return type

[**AgentIconGenerationResponse**](AgentIconGenerationResponse.md)

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

# **get_agent_api_agents_agent_id_get**
> AgentResponse get_agent_api_agents_agent_id_get(agent_id)

Get Agent

### Example


```python
import suna_api_client
from suna_api_client.models.agent_response import AgentResponse
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
    api_instance = suna_api_client.DefaultApi(api_client)
    agent_id = 'agent_id_example' # str | 

    try:
        # Get Agent
        api_response = api_instance.get_agent_api_agents_agent_id_get(agent_id)
        print("The response of DefaultApi->get_agent_api_agents_agent_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_agent_api_agents_agent_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 

### Return type

[**AgentResponse**](AgentResponse.md)

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

# **get_agent_run_api_agent_run_agent_run_id_get**
> object get_agent_run_api_agent_run_agent_run_id_get(agent_run_id)

Get Agent Run

Get agent run status and responses.

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
    api_instance = suna_api_client.DefaultApi(api_client)
    agent_run_id = 'agent_run_id_example' # str | 

    try:
        # Get Agent Run
        api_response = api_instance.get_agent_run_api_agent_run_agent_run_id_get(agent_run_id)
        print("The response of DefaultApi->get_agent_run_api_agent_run_agent_run_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_agent_run_api_agent_run_agent_run_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_run_id** | **str**|  | 

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

# **get_agent_run_api_agent_runs_agent_run_id_get**
> object get_agent_run_api_agent_runs_agent_run_id_get(agent_run_id)

Get Agent Run

[DEPRECATED] Get an agent run by ID.

This endpoint is deprecated and may be removed in future versions.

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
    api_instance = suna_api_client.DefaultApi(api_client)
    agent_run_id = 'agent_run_id_example' # str | 

    try:
        # Get Agent Run
        api_response = api_instance.get_agent_run_api_agent_runs_agent_run_id_get(agent_run_id)
        print("The response of DefaultApi->get_agent_run_api_agent_runs_agent_run_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_agent_run_api_agent_runs_agent_run_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_run_id** | **str**|  | 

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

# **get_agent_runs_api_thread_thread_id_agent_runs_get**
> object get_agent_runs_api_thread_thread_id_agent_runs_get(thread_id)

Get Agent Runs

Get all agent runs for a thread.

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
    api_instance = suna_api_client.DefaultApi(api_client)
    thread_id = 'thread_id_example' # str | 

    try:
        # Get Agent Runs
        api_response = api_instance.get_agent_runs_api_thread_thread_id_agent_runs_get(thread_id)
        print("The response of DefaultApi->get_agent_runs_api_thread_thread_id_agent_runs_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_agent_runs_api_thread_thread_id_agent_runs_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**|  | 

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

# **get_agent_tools_api_agents_agent_id_tools_get**
> object get_agent_tools_api_agents_agent_id_tools_get(agent_id)

Get Agent Tools

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
    api_instance = suna_api_client.DefaultApi(api_client)
    agent_id = 'agent_id_example' # str | 

    try:
        # Get Agent Tools
        api_response = api_instance.get_agent_tools_api_agents_agent_id_tools_get(agent_id)
        print("The response of DefaultApi->get_agent_tools_api_agents_agent_id_tools_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_agent_tools_api_agents_agent_id_tools_get: %s\n" % e)
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

# **get_agents_api_agents_get**
> AgentsResponse get_agents_api_agents_get(page=page, limit=limit, search=search, sort_by=sort_by, sort_order=sort_order, has_default=has_default, has_mcp_tools=has_mcp_tools, has_agentpress_tools=has_agentpress_tools, tools=tools, content_type=content_type)

Get Agents

### Example


```python
import suna_api_client
from suna_api_client.models.agents_response import AgentsResponse
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
    api_instance = suna_api_client.DefaultApi(api_client)
    page = 56 # int | Page number (1-based) (optional)
    limit = 56 # int | Number of items per page (optional)
    search = 'search_example' # str | Search in name and description (optional)
    sort_by = 'sort_by_example' # str | Sort field: name, created_at, updated_at, tools_count (optional)
    sort_order = 'sort_order_example' # str | Sort order: asc, desc (optional)
    has_default = True # bool | Filter by default agents (optional)
    has_mcp_tools = True # bool | Filter by agents with MCP tools (optional)
    has_agentpress_tools = True # bool | Filter by agents with AgentPress tools (optional)
    tools = 'tools_example' # str | Comma-separated list of tools to filter by (optional)
    content_type = 'content_type_example' # str | Content type filter: 'agents', 'templates', or None for agents only (optional)

    try:
        # Get Agents
        api_response = api_instance.get_agents_api_agents_get(page=page, limit=limit, search=search, sort_by=sort_by, sort_order=sort_order, has_default=has_default, has_mcp_tools=has_mcp_tools, has_agentpress_tools=has_agentpress_tools, tools=tools, content_type=content_type)
        print("The response of DefaultApi->get_agents_api_agents_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_agents_api_agents_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number (1-based) | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **search** | **str**| Search in name and description | [optional] 
 **sort_by** | **str**| Sort field: name, created_at, updated_at, tools_count | [optional] 
 **sort_order** | **str**| Sort order: asc, desc | [optional] 
 **has_default** | **bool**| Filter by default agents | [optional] 
 **has_mcp_tools** | **bool**| Filter by agents with MCP tools | [optional] 
 **has_agentpress_tools** | **bool**| Filter by agents with AgentPress tools | [optional] 
 **tools** | **str**| Comma-separated list of tools to filter by | [optional] 
 **content_type** | **str**| Content type filter: &#39;agents&#39;, &#39;templates&#39;, or None for agents only | [optional] 

### Return type

[**AgentsResponse**](AgentsResponse.md)

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

# **get_composio_mcp_url_api_secure_mcp_composio_profiles_profile_id_mcp_url_get**
> ComposioMcpUrlResponse get_composio_mcp_url_api_secure_mcp_composio_profiles_profile_id_mcp_url_get(profile_id)

Get Composio Mcp Url

### Example


```python
import suna_api_client
from suna_api_client.models.composio_mcp_url_response import ComposioMcpUrlResponse
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
    api_instance = suna_api_client.DefaultApi(api_client)
    profile_id = 'profile_id_example' # str | 

    try:
        # Get Composio Mcp Url
        api_response = api_instance.get_composio_mcp_url_api_secure_mcp_composio_profiles_profile_id_mcp_url_get(profile_id)
        print("The response of DefaultApi->get_composio_mcp_url_api_secure_mcp_composio_profiles_profile_id_mcp_url_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_composio_mcp_url_api_secure_mcp_composio_profiles_profile_id_mcp_url_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**|  | 

### Return type

[**ComposioMcpUrlResponse**](ComposioMcpUrlResponse.md)

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

# **get_composio_profiles_api_secure_mcp_composio_profiles_get**
> ComposioCredentialsResponse get_composio_profiles_api_secure_mcp_composio_profiles_get()

Get Composio Profiles

### Example


```python
import suna_api_client
from suna_api_client.models.composio_credentials_response import ComposioCredentialsResponse
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
    api_instance = suna_api_client.DefaultApi(api_client)

    try:
        # Get Composio Profiles
        api_response = api_instance.get_composio_profiles_api_secure_mcp_composio_profiles_get()
        print("The response of DefaultApi->get_composio_profiles_api_secure_mcp_composio_profiles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_composio_profiles_api_secure_mcp_composio_profiles_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ComposioCredentialsResponse**](ComposioCredentialsResponse.md)

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

# **get_credential_profile_api_secure_mcp_credential_profiles_profile_profile_id_get**
> CredentialProfileResponse get_credential_profile_api_secure_mcp_credential_profiles_profile_profile_id_get(profile_id)

Get Credential Profile

### Example


```python
import suna_api_client
from suna_api_client.models.credential_profile_response import CredentialProfileResponse
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
    api_instance = suna_api_client.DefaultApi(api_client)
    profile_id = 'profile_id_example' # str | 

    try:
        # Get Credential Profile
        api_response = api_instance.get_credential_profile_api_secure_mcp_credential_profiles_profile_profile_id_get(profile_id)
        print("The response of DefaultApi->get_credential_profile_api_secure_mcp_credential_profiles_profile_profile_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_credential_profile_api_secure_mcp_credential_profiles_profile_profile_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **profile_id** | **str**|  | 

### Return type

[**CredentialProfileResponse**](CredentialProfileResponse.md)

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

# **get_credential_profiles_for_mcp_api_secure_mcp_credential_profiles_mcp_qualified_name_get**
> List[CredentialProfileResponse] get_credential_profiles_for_mcp_api_secure_mcp_credential_profiles_mcp_qualified_name_get(mcp_qualified_name)

Get Credential Profiles For Mcp

### Example


```python
import suna_api_client
from suna_api_client.models.credential_profile_response import CredentialProfileResponse
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
    api_instance = suna_api_client.DefaultApi(api_client)
    mcp_qualified_name = 'mcp_qualified_name_example' # str | 

    try:
        # Get Credential Profiles For Mcp
        api_response = api_instance.get_credential_profiles_for_mcp_api_secure_mcp_credential_profiles_mcp_qualified_name_get(mcp_qualified_name)
        print("The response of DefaultApi->get_credential_profiles_for_mcp_api_secure_mcp_credential_profiles_mcp_qualified_name_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_credential_profiles_for_mcp_api_secure_mcp_credential_profiles_mcp_qualified_name_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **mcp_qualified_name** | **str**|  | 

### Return type

[**List[CredentialProfileResponse]**](CredentialProfileResponse.md)

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

# **get_custom_mcp_tools_for_agent_api_agents_agent_id_custom_mcp_tools_get**
> object get_custom_mcp_tools_for_agent_api_agents_agent_id_custom_mcp_tools_get(agent_id)

Get Custom Mcp Tools For Agent

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
    api_instance = suna_api_client.DefaultApi(api_client)
    agent_id = 'agent_id_example' # str | 

    try:
        # Get Custom Mcp Tools For Agent
        api_response = api_instance.get_custom_mcp_tools_for_agent_api_agents_agent_id_custom_mcp_tools_get(agent_id)
        print("The response of DefaultApi->get_custom_mcp_tools_for_agent_api_agents_agent_id_custom_mcp_tools_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_custom_mcp_tools_for_agent_api_agents_agent_id_custom_mcp_tools_get: %s\n" % e)
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

# **get_marketplace_templates_api_templates_marketplace_get**
> MarketplaceTemplatesResponse get_marketplace_templates_api_templates_marketplace_get(page=page, limit=limit, search=search, tags=tags, is_kortix_team=is_kortix_team, mine=mine, sort_by=sort_by, sort_order=sort_order)

Get Marketplace Templates

### Example


```python
import suna_api_client
from suna_api_client.models.marketplace_templates_response import MarketplaceTemplatesResponse
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
    api_instance = suna_api_client.DefaultApi(api_client)
    page = 56 # int | Page number (1-based) (optional)
    limit = 56 # int | Number of items per page (optional)
    search = 'search_example' # str | Search term for name and description (optional)
    tags = 'tags_example' # str | Comma-separated list of tags to filter by (optional)
    is_kortix_team = True # bool | Filter for Kortix team templates (optional)
    mine = True # bool | Filter to show only user's own templates (optional)
    sort_by = 'sort_by_example' # str | Sort field: download_count, newest, name (optional)
    sort_order = 'sort_order_example' # str | Sort order: asc, desc (optional)

    try:
        # Get Marketplace Templates
        api_response = api_instance.get_marketplace_templates_api_templates_marketplace_get(page=page, limit=limit, search=search, tags=tags, is_kortix_team=is_kortix_team, mine=mine, sort_by=sort_by, sort_order=sort_order)
        print("The response of DefaultApi->get_marketplace_templates_api_templates_marketplace_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_marketplace_templates_api_templates_marketplace_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number (1-based) | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **search** | **str**| Search term for name and description | [optional] 
 **tags** | **str**| Comma-separated list of tags to filter by | [optional] 
 **is_kortix_team** | **bool**| Filter for Kortix team templates | [optional] 
 **mine** | **bool**| Filter to show only user&#39;s own templates | [optional] 
 **sort_by** | **str**| Sort field: download_count, newest, name | [optional] 
 **sort_order** | **str**| Sort order: asc, desc | [optional] 

### Return type

[**MarketplaceTemplatesResponse**](MarketplaceTemplatesResponse.md)

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

# **get_my_templates_api_templates_my_get**
> MarketplaceTemplatesResponse get_my_templates_api_templates_my_get(page=page, limit=limit, search=search, sort_by=sort_by, sort_order=sort_order)

Get My Templates

### Example


```python
import suna_api_client
from suna_api_client.models.marketplace_templates_response import MarketplaceTemplatesResponse
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
    api_instance = suna_api_client.DefaultApi(api_client)
    page = 56 # int | Page number (1-based) (optional)
    limit = 56 # int | Number of items per page (optional)
    search = 'search_example' # str | Search term for name and description (optional)
    sort_by = 'sort_by_example' # str | Sort field: created_at, name, download_count (optional)
    sort_order = 'sort_order_example' # str | Sort order: asc, desc (optional)

    try:
        # Get My Templates
        api_response = api_instance.get_my_templates_api_templates_my_get(page=page, limit=limit, search=search, sort_by=sort_by, sort_order=sort_order)
        print("The response of DefaultApi->get_my_templates_api_templates_my_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_my_templates_api_templates_my_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number (1-based) | [optional] 
 **limit** | **int**| Number of items per page | [optional] 
 **search** | **str**| Search term for name and description | [optional] 
 **sort_by** | **str**| Sort field: created_at, name, download_count | [optional] 
 **sort_order** | **str**| Sort order: asc, desc | [optional] 

### Return type

[**MarketplaceTemplatesResponse**](MarketplaceTemplatesResponse.md)

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

# **get_public_template_api_templates_public_template_id_get**
> TemplateResponse get_public_template_api_templates_public_template_id_get(template_id)

Get Public Template

Get a public template by ID without authentication

### Example


```python
import suna_api_client
from suna_api_client.models.template_response import TemplateResponse
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
    api_instance = suna_api_client.DefaultApi(api_client)
    template_id = 'template_id_example' # str | 

    try:
        # Get Public Template
        api_response = api_instance.get_public_template_api_templates_public_template_id_get(template_id)
        print("The response of DefaultApi->get_public_template_api_templates_public_template_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_public_template_api_templates_public_template_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

### Return type

[**TemplateResponse**](TemplateResponse.md)

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

# **get_template_api_templates_template_id_get**
> TemplateResponse get_template_api_templates_template_id_get(template_id)

Get Template

### Example


```python
import suna_api_client
from suna_api_client.models.template_response import TemplateResponse
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
    api_instance = suna_api_client.DefaultApi(api_client)
    template_id = 'template_id_example' # str | 

    try:
        # Get Template
        api_response = api_instance.get_template_api_templates_template_id_get(template_id)
        print("The response of DefaultApi->get_template_api_templates_template_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_template_api_templates_template_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

### Return type

[**TemplateResponse**](TemplateResponse.md)

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

# **get_thread_agent_api_thread_thread_id_agent_get**
> ThreadAgentResponse get_thread_agent_api_thread_thread_id_agent_get(thread_id)

Get Thread Agent

Get the agent details for a specific thread. Since threads are fully agent-agnostic, 
this returns the most recently used agent from agent_runs only.

### Example


```python
import suna_api_client
from suna_api_client.models.thread_agent_response import ThreadAgentResponse
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
    api_instance = suna_api_client.DefaultApi(api_client)
    thread_id = 'thread_id_example' # str | 

    try:
        # Get Thread Agent
        api_response = api_instance.get_thread_agent_api_thread_thread_id_agent_get(thread_id)
        print("The response of DefaultApi->get_thread_agent_api_thread_thread_id_agent_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_thread_agent_api_thread_thread_id_agent_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**|  | 

### Return type

[**ThreadAgentResponse**](ThreadAgentResponse.md)

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

# **get_thread_api_threads_thread_id_get**
> object get_thread_api_threads_thread_id_get(thread_id)

Get Thread

Get a specific thread by ID with complete related data.

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
    api_instance = suna_api_client.DefaultApi(api_client)
    thread_id = 'thread_id_example' # str | 

    try:
        # Get Thread
        api_response = api_instance.get_thread_api_threads_thread_id_get(thread_id)
        print("The response of DefaultApi->get_thread_api_threads_thread_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_thread_api_threads_thread_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**|  | 

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

# **get_thread_messages_api_threads_thread_id_messages_get**
> object get_thread_messages_api_threads_thread_id_messages_get(thread_id, order=order)

Get Thread Messages

Get all messages for a thread, fetching in batches of 1000 from the DB to avoid large queries.

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
    api_instance = suna_api_client.DefaultApi(api_client)
    thread_id = 'thread_id_example' # str | 
    order = 'desc' # str | Order by created_at: 'asc' or 'desc' (optional) (default to 'desc')

    try:
        # Get Thread Messages
        api_response = api_instance.get_thread_messages_api_threads_thread_id_messages_get(thread_id, order=order)
        print("The response of DefaultApi->get_thread_messages_api_threads_thread_id_messages_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_thread_messages_api_threads_thread_id_messages_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**|  | 
 **order** | **str**| Order by created_at: &#39;asc&#39; or &#39;desc&#39; | [optional] [default to &#39;desc&#39;]

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

# **get_user_credential_profiles_api_secure_mcp_credential_profiles_get**
> List[CredentialProfileResponse] get_user_credential_profiles_api_secure_mcp_credential_profiles_get()

Get User Credential Profiles

### Example


```python
import suna_api_client
from suna_api_client.models.credential_profile_response import CredentialProfileResponse
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
    api_instance = suna_api_client.DefaultApi(api_client)

    try:
        # Get User Credential Profiles
        api_response = api_instance.get_user_credential_profiles_api_secure_mcp_credential_profiles_get()
        print("The response of DefaultApi->get_user_credential_profiles_api_secure_mcp_credential_profiles_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_user_credential_profiles_api_secure_mcp_credential_profiles_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CredentialProfileResponse]**](CredentialProfileResponse.md)

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

# **get_user_credentials_api_secure_mcp_credentials_get**
> List[CredentialResponse] get_user_credentials_api_secure_mcp_credentials_get()

Get User Credentials

### Example


```python
import suna_api_client
from suna_api_client.models.credential_response import CredentialResponse
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
    api_instance = suna_api_client.DefaultApi(api_client)

    try:
        # Get User Credentials
        api_response = api_instance.get_user_credentials_api_secure_mcp_credentials_get()
        print("The response of DefaultApi->get_user_credentials_api_secure_mcp_credentials_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_user_credentials_api_secure_mcp_credentials_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[CredentialResponse]**](CredentialResponse.md)

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

# **get_user_threads_api_threads_get**
> object get_user_threads_api_threads_get(page=page, limit=limit)

Get User Threads

Get all threads for the current user with associated project data.

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
    api_instance = suna_api_client.DefaultApi(api_client)
    page = 56 # int | Page number (1-based) (optional)
    limit = 56 # int | Number of items per page (max 1000) (optional)

    try:
        # Get User Threads
        api_response = api_instance.get_user_threads_api_threads_get(page=page, limit=limit)
        print("The response of DefaultApi->get_user_threads_api_threads_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_user_threads_api_threads_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number (1-based) | [optional] 
 **limit** | **int**| Number of items per page (max 1000) | [optional] 

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

# **get_version_api_agents_agent_id_versions_version_id_get**
> VersionResponse get_version_api_agents_agent_id_versions_version_id_get(agent_id, version_id)

Get Version

### Example


```python
import suna_api_client
from suna_api_client.models.version_response import VersionResponse
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
    api_instance = suna_api_client.DefaultApi(api_client)
    agent_id = 'agent_id_example' # str | 
    version_id = 'version_id_example' # str | 

    try:
        # Get Version
        api_response = api_instance.get_version_api_agents_agent_id_versions_version_id_get(agent_id, version_id)
        print("The response of DefaultApi->get_version_api_agents_agent_id_versions_version_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_version_api_agents_agent_id_versions_version_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **version_id** | **str**|  | 

### Return type

[**VersionResponse**](VersionResponse.md)

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

# **get_versions_api_agents_agent_id_versions_get**
> List[VersionResponse] get_versions_api_agents_agent_id_versions_get(agent_id)

Get Versions

### Example


```python
import suna_api_client
from suna_api_client.models.version_response import VersionResponse
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
    api_instance = suna_api_client.DefaultApi(api_client)
    agent_id = 'agent_id_example' # str | 

    try:
        # Get Versions
        api_response = api_instance.get_versions_api_agents_agent_id_versions_get(agent_id)
        print("The response of DefaultApi->get_versions_api_agents_agent_id_versions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->get_versions_api_agents_agent_id_versions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 

### Return type

[**List[VersionResponse]**](VersionResponse.md)

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

# **health_check_api_health_docker_get**
> object health_check_api_health_docker_get()

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
    api_instance = suna_api_client.DefaultApi(api_client)

    try:
        # Health Check
        api_response = api_instance.health_check_api_health_docker_get()
        print("The response of DefaultApi->health_check_api_health_docker_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->health_check_api_health_docker_get: %s\n" % e)
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

# **health_check_api_health_get**
> object health_check_api_health_get()

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
    api_instance = suna_api_client.DefaultApi(api_client)

    try:
        # Health Check
        api_response = api_instance.health_check_api_health_get()
        print("The response of DefaultApi->health_check_api_health_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->health_check_api_health_get: %s\n" % e)
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

# **import_agent_from_json_api_agents_json_import_post**
> JsonImportResponse import_agent_from_json_api_agents_json_import_post(json_import_request_model)

Import Agent From Json

### Example


```python
import suna_api_client
from suna_api_client.models.json_import_request_model import JsonImportRequestModel
from suna_api_client.models.json_import_response import JsonImportResponse
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
    api_instance = suna_api_client.DefaultApi(api_client)
    json_import_request_model = suna_api_client.JsonImportRequestModel() # JsonImportRequestModel | 

    try:
        # Import Agent From Json
        api_response = api_instance.import_agent_from_json_api_agents_json_import_post(json_import_request_model)
        print("The response of DefaultApi->import_agent_from_json_api_agents_json_import_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->import_agent_from_json_api_agents_json_import_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **json_import_request_model** | [**JsonImportRequestModel**](JsonImportRequestModel.md)|  | 

### Return type

[**JsonImportResponse**](JsonImportResponse.md)

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

# **initiate_agent_with_files_api_agent_initiate_post**
> InitiateAgentResponse initiate_agent_with_files_api_agent_initiate_post(prompt, model_name=model_name, enable_thinking=enable_thinking, reasoning_effort=reasoning_effort, stream=stream, enable_context_manager=enable_context_manager, enable_prompt_caching=enable_prompt_caching, agent_id=agent_id, files=files)

Initiate Agent With Files

Initiate a new agent session with optional file attachments.

[WARNING] Keep in sync with create thread endpoint.

### Example


```python
import suna_api_client
from suna_api_client.models.initiate_agent_response import InitiateAgentResponse
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
    api_instance = suna_api_client.DefaultApi(api_client)
    prompt = 'prompt_example' # str | 
    model_name = 'model_name_example' # str |  (optional)
    enable_thinking = True # bool |  (optional)
    reasoning_effort = 'reasoning_effort_example' # str |  (optional)
    stream = True # bool |  (optional)
    enable_context_manager = True # bool |  (optional)
    enable_prompt_caching = True # bool |  (optional)
    agent_id = 'agent_id_example' # str |  (optional)
    files = None # List[bytearray] |  (optional)

    try:
        # Initiate Agent With Files
        api_response = api_instance.initiate_agent_with_files_api_agent_initiate_post(prompt, model_name=model_name, enable_thinking=enable_thinking, reasoning_effort=reasoning_effort, stream=stream, enable_context_manager=enable_context_manager, enable_prompt_caching=enable_prompt_caching, agent_id=agent_id, files=files)
        print("The response of DefaultApi->initiate_agent_with_files_api_agent_initiate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->initiate_agent_with_files_api_agent_initiate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prompt** | **str**|  | 
 **model_name** | **str**|  | [optional] 
 **enable_thinking** | **bool**|  | [optional] 
 **reasoning_effort** | **str**|  | [optional] 
 **stream** | **bool**|  | [optional] 
 **enable_context_manager** | **bool**|  | [optional] 
 **enable_prompt_caching** | **bool**|  | [optional] 
 **agent_id** | **str**|  | [optional] 
 **files** | **List[bytearray]**|  | [optional] 

### Return type

[**InitiateAgentResponse**](InitiateAgentResponse.md)

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

# **install_template_api_templates_install_post**
> InstallationResponse install_template_api_templates_install_post(install_template_request)

Install Template

### Example


```python
import suna_api_client
from suna_api_client.models.install_template_request import InstallTemplateRequest
from suna_api_client.models.installation_response import InstallationResponse
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
    api_instance = suna_api_client.DefaultApi(api_client)
    install_template_request = suna_api_client.InstallTemplateRequest() # InstallTemplateRequest | 

    try:
        # Install Template
        api_response = api_instance.install_template_api_templates_install_post(install_template_request)
        print("The response of DefaultApi->install_template_api_templates_install_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->install_template_api_templates_install_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **install_template_request** | [**InstallTemplateRequest**](InstallTemplateRequest.md)|  | 

### Return type

[**InstallationResponse**](InstallationResponse.md)

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

# **list_api_keys_api_api_keys_get**
> List[APIKeyResponse] list_api_keys_api_api_keys_get()

List Api Keys

List all API keys for the authenticated user

Args:
    user_id: Authenticated user ID from JWT or API key
    api_key_service: API key service instance

Returns:
    List[APIKeyResponse]: List of API keys (without the actual key values)

### Example


```python
import suna_api_client
from suna_api_client.models.api_key_response import APIKeyResponse
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
    api_instance = suna_api_client.DefaultApi(api_client)

    try:
        # List Api Keys
        api_response = api_instance.list_api_keys_api_api_keys_get()
        print("The response of DefaultApi->list_api_keys_api_api_keys_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->list_api_keys_api_api_keys_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**List[APIKeyResponse]**](APIKeyResponse.md)

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

# **publish_template_api_templates_template_id_publish_post**
> object publish_template_api_templates_template_id_publish_post(template_id, publish_template_request)

Publish Template

### Example


```python
import suna_api_client
from suna_api_client.models.publish_template_request import PublishTemplateRequest
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
    api_instance = suna_api_client.DefaultApi(api_client)
    template_id = 'template_id_example' # str | 
    publish_template_request = suna_api_client.PublishTemplateRequest() # PublishTemplateRequest | 

    try:
        # Publish Template
        api_response = api_instance.publish_template_api_templates_template_id_publish_post(template_id, publish_template_request)
        print("The response of DefaultApi->publish_template_api_templates_template_id_publish_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->publish_template_api_templates_template_id_publish_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 
 **publish_template_request** | [**PublishTemplateRequest**](PublishTemplateRequest.md)|  | 

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

# **revoke_api_key_api_api_keys_key_id_revoke_patch**
> object revoke_api_key_api_api_keys_key_id_revoke_patch(key_id)

Revoke Api Key

Revoke an API key

Args:
    key_id: The ID of the API key to revoke
    user_id: Authenticated user ID from JWT or API key
    api_key_service: API key service instance

Returns:
    dict: Success message

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
    api_instance = suna_api_client.DefaultApi(api_client)
    key_id = 'key_id_example' # str | 

    try:
        # Revoke Api Key
        api_response = api_instance.revoke_api_key_api_api_keys_key_id_revoke_patch(key_id)
        print("The response of DefaultApi->revoke_api_key_api_api_keys_key_id_revoke_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->revoke_api_key_api_api_keys_key_id_revoke_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **key_id** | **str**|  | 

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

# **rollback_to_version_api_agents_agent_id_versions_version_id_rollback_post**
> VersionResponse rollback_to_version_api_agents_agent_id_versions_version_id_rollback_post(agent_id, version_id)

Rollback To Version

### Example


```python
import suna_api_client
from suna_api_client.models.version_response import VersionResponse
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
    api_instance = suna_api_client.DefaultApi(api_client)
    agent_id = 'agent_id_example' # str | 
    version_id = 'version_id_example' # str | 

    try:
        # Rollback To Version
        api_response = api_instance.rollback_to_version_api_agents_agent_id_versions_version_id_rollback_post(agent_id, version_id)
        print("The response of DefaultApi->rollback_to_version_api_agents_agent_id_versions_version_id_rollback_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->rollback_to_version_api_agents_agent_id_versions_version_id_rollback_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **version_id** | **str**|  | 

### Return type

[**VersionResponse**](VersionResponse.md)

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

# **send_welcome_email_api_send_welcome_email_post**
> EmailResponse send_welcome_email_api_send_welcome_email_post(send_welcome_email_request, x_admin_api_key=x_admin_api_key)

Send Welcome Email

### Example


```python
import suna_api_client
from suna_api_client.models.email_response import EmailResponse
from suna_api_client.models.send_welcome_email_request import SendWelcomeEmailRequest
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
    api_instance = suna_api_client.DefaultApi(api_client)
    send_welcome_email_request = suna_api_client.SendWelcomeEmailRequest() # SendWelcomeEmailRequest | 
    x_admin_api_key = 'x_admin_api_key_example' # str |  (optional)

    try:
        # Send Welcome Email
        api_response = api_instance.send_welcome_email_api_send_welcome_email_post(send_welcome_email_request, x_admin_api_key=x_admin_api_key)
        print("The response of DefaultApi->send_welcome_email_api_send_welcome_email_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->send_welcome_email_api_send_welcome_email_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **send_welcome_email_request** | [**SendWelcomeEmailRequest**](SendWelcomeEmailRequest.md)|  | 
 **x_admin_api_key** | **str**|  | [optional] 

### Return type

[**EmailResponse**](EmailResponse.md)

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

# **set_default_credential_profile_api_secure_mcp_credential_profiles_profile_id_set_default_put**
> object set_default_credential_profile_api_secure_mcp_credential_profiles_profile_id_set_default_put(profile_id)

Set Default Credential Profile

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
    api_instance = suna_api_client.DefaultApi(api_client)
    profile_id = 'profile_id_example' # str | 

    try:
        # Set Default Credential Profile
        api_response = api_instance.set_default_credential_profile_api_secure_mcp_credential_profiles_profile_id_set_default_put(profile_id)
        print("The response of DefaultApi->set_default_credential_profile_api_secure_mcp_credential_profiles_profile_id_set_default_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->set_default_credential_profile_api_secure_mcp_credential_profiles_profile_id_set_default_put: %s\n" % e)
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

# **start_agent_api_thread_thread_id_agent_start_post**
> object start_agent_api_thread_thread_id_agent_start_post(thread_id, agent_start_request)

Start Agent

Start an agent for a specific thread in the background

### Example


```python
import suna_api_client
from suna_api_client.models.agent_start_request import AgentStartRequest
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
    api_instance = suna_api_client.DefaultApi(api_client)
    thread_id = 'thread_id_example' # str | 
    agent_start_request = suna_api_client.AgentStartRequest() # AgentStartRequest | 

    try:
        # Start Agent
        api_response = api_instance.start_agent_api_thread_thread_id_agent_start_post(thread_id, agent_start_request)
        print("The response of DefaultApi->start_agent_api_thread_thread_id_agent_start_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->start_agent_api_thread_thread_id_agent_start_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **thread_id** | **str**|  | 
 **agent_start_request** | [**AgentStartRequest**](AgentStartRequest.md)|  | 

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

# **stop_agent_api_agent_run_agent_run_id_stop_post**
> object stop_agent_api_agent_run_agent_run_id_stop_post(agent_run_id)

Stop Agent

Stop a running agent.

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
    api_instance = suna_api_client.DefaultApi(api_client)
    agent_run_id = 'agent_run_id_example' # str | 

    try:
        # Stop Agent
        api_response = api_instance.stop_agent_api_agent_run_agent_run_id_stop_post(agent_run_id)
        print("The response of DefaultApi->stop_agent_api_agent_run_agent_run_id_stop_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->stop_agent_api_agent_run_agent_run_id_stop_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_run_id** | **str**|  | 

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

# **store_credential_api_secure_mcp_credentials_post**
> CredentialResponse store_credential_api_secure_mcp_credentials_post(store_credential_request)

Store Credential

### Example


```python
import suna_api_client
from suna_api_client.models.credential_response import CredentialResponse
from suna_api_client.models.store_credential_request import StoreCredentialRequest
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
    api_instance = suna_api_client.DefaultApi(api_client)
    store_credential_request = suna_api_client.StoreCredentialRequest() # StoreCredentialRequest | 

    try:
        # Store Credential
        api_response = api_instance.store_credential_api_secure_mcp_credentials_post(store_credential_request)
        print("The response of DefaultApi->store_credential_api_secure_mcp_credentials_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->store_credential_api_secure_mcp_credentials_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_credential_request** | [**StoreCredentialRequest**](StoreCredentialRequest.md)|  | 

### Return type

[**CredentialResponse**](CredentialResponse.md)

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

# **store_credential_profile_api_secure_mcp_credential_profiles_post**
> CredentialProfileResponse store_credential_profile_api_secure_mcp_credential_profiles_post(store_credential_profile_request)

Store Credential Profile

### Example


```python
import suna_api_client
from suna_api_client.models.credential_profile_response import CredentialProfileResponse
from suna_api_client.models.store_credential_profile_request import StoreCredentialProfileRequest
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
    api_instance = suna_api_client.DefaultApi(api_client)
    store_credential_profile_request = suna_api_client.StoreCredentialProfileRequest() # StoreCredentialProfileRequest | 

    try:
        # Store Credential Profile
        api_response = api_instance.store_credential_profile_api_secure_mcp_credential_profiles_post(store_credential_profile_request)
        print("The response of DefaultApi->store_credential_profile_api_secure_mcp_credential_profiles_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->store_credential_profile_api_secure_mcp_credential_profiles_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **store_credential_profile_request** | [**StoreCredentialProfileRequest**](StoreCredentialProfileRequest.md)|  | 

### Return type

[**CredentialProfileResponse**](CredentialProfileResponse.md)

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

# **stream_agent_run_api_agent_run_agent_run_id_stream_get**
> object stream_agent_run_api_agent_run_agent_run_id_stream_get(agent_run_id, token=token)

Stream Agent Run

Stream the responses of an agent run using Redis Lists and Pub/Sub.

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
    api_instance = suna_api_client.DefaultApi(api_client)
    agent_run_id = 'agent_run_id_example' # str | 
    token = 'token_example' # str |  (optional)

    try:
        # Stream Agent Run
        api_response = api_instance.stream_agent_run_api_agent_run_agent_run_id_stream_get(agent_run_id, token=token)
        print("The response of DefaultApi->stream_agent_run_api_agent_run_agent_run_id_stream_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->stream_agent_run_api_agent_run_agent_run_id_stream_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_run_id** | **str**|  | 
 **token** | **str**|  | [optional] 

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

# **unpublish_template_api_templates_template_id_unpublish_post**
> object unpublish_template_api_templates_template_id_unpublish_post(template_id)

Unpublish Template

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
    api_instance = suna_api_client.DefaultApi(api_client)
    template_id = 'template_id_example' # str | 

    try:
        # Unpublish Template
        api_response = api_instance.unpublish_template_api_templates_template_id_unpublish_post(template_id)
        print("The response of DefaultApi->unpublish_template_api_templates_template_id_unpublish_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->unpublish_template_api_templates_template_id_unpublish_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **template_id** | **str**|  | 

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

# **update_agent_api_agents_agent_id_put**
> AgentResponse update_agent_api_agents_agent_id_put(agent_id, agent_update_request)

Update Agent

### Example


```python
import suna_api_client
from suna_api_client.models.agent_response import AgentResponse
from suna_api_client.models.agent_update_request import AgentUpdateRequest
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
    api_instance = suna_api_client.DefaultApi(api_client)
    agent_id = 'agent_id_example' # str | 
    agent_update_request = suna_api_client.AgentUpdateRequest() # AgentUpdateRequest | 

    try:
        # Update Agent
        api_response = api_instance.update_agent_api_agents_agent_id_put(agent_id, agent_update_request)
        print("The response of DefaultApi->update_agent_api_agents_agent_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_agent_api_agents_agent_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **agent_update_request** | [**AgentUpdateRequest**](AgentUpdateRequest.md)|  | 

### Return type

[**AgentResponse**](AgentResponse.md)

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

# **update_agent_custom_mcps_api_agents_agent_id_custom_mcp_tools_put**
> object update_agent_custom_mcps_api_agents_agent_id_custom_mcp_tools_put(agent_id, request_body)

Update Agent Custom Mcps

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
    api_instance = suna_api_client.DefaultApi(api_client)
    agent_id = 'agent_id_example' # str | 
    request_body = None # Dict[str, object] | 

    try:
        # Update Agent Custom Mcps
        api_response = api_instance.update_agent_custom_mcps_api_agents_agent_id_custom_mcp_tools_put(agent_id, request_body)
        print("The response of DefaultApi->update_agent_custom_mcps_api_agents_agent_id_custom_mcp_tools_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_agent_custom_mcps_api_agents_agent_id_custom_mcp_tools_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | 

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

# **update_custom_mcp_tools_for_agent_api_agents_agent_id_custom_mcp_tools_post**
> object update_custom_mcp_tools_for_agent_api_agents_agent_id_custom_mcp_tools_post(agent_id, request_body)

Update Custom Mcp Tools For Agent

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
    api_instance = suna_api_client.DefaultApi(api_client)
    agent_id = 'agent_id_example' # str | 
    request_body = None # Dict[str, object] | 

    try:
        # Update Custom Mcp Tools For Agent
        api_response = api_instance.update_custom_mcp_tools_for_agent_api_agents_agent_id_custom_mcp_tools_post(agent_id, request_body)
        print("The response of DefaultApi->update_custom_mcp_tools_for_agent_api_agents_agent_id_custom_mcp_tools_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_custom_mcp_tools_for_agent_api_agents_agent_id_custom_mcp_tools_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **request_body** | [**Dict[str, object]**](object.md)|  | 

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

# **update_version_details_api_agents_agent_id_versions_version_id_details_put**
> VersionResponse update_version_details_api_agents_agent_id_versions_version_id_details_put(agent_id, version_id, update_version_details_request)

Update Version Details

### Example


```python
import suna_api_client
from suna_api_client.models.update_version_details_request import UpdateVersionDetailsRequest
from suna_api_client.models.version_response import VersionResponse
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
    api_instance = suna_api_client.DefaultApi(api_client)
    agent_id = 'agent_id_example' # str | 
    version_id = 'version_id_example' # str | 
    update_version_details_request = suna_api_client.UpdateVersionDetailsRequest() # UpdateVersionDetailsRequest | 

    try:
        # Update Version Details
        api_response = api_instance.update_version_details_api_agents_agent_id_versions_version_id_details_put(agent_id, version_id, update_version_details_request)
        print("The response of DefaultApi->update_version_details_api_agents_agent_id_versions_version_id_details_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DefaultApi->update_version_details_api_agents_agent_id_versions_version_id_details_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **agent_id** | **str**|  | 
 **version_id** | **str**|  | 
 **update_version_details_request** | [**UpdateVersionDetailsRequest**](UpdateVersionDetailsRequest.md)|  | 

### Return type

[**VersionResponse**](VersionResponse.md)

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

