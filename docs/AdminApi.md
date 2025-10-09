# suna_api_client.AdminApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**admin_install_suna_for_user_api_admin_suna_agents_install_user_account_id_post**](AdminApi.md#admin_install_suna_for_user_api_admin_suna_agents_install_user_account_id_post) | **POST** /api/admin/suna-agents/install-user/{account_id} | Admin Install Suna For User
[**get_env_vars_api_admin_env_vars_get**](AdminApi.md#get_env_vars_api_admin_env_vars_get) | **GET** /api/admin/env-vars | Get Env Vars
[**save_env_vars_api_admin_env_vars_post**](AdminApi.md#save_env_vars_api_admin_env_vars_post) | **POST** /api/admin/env-vars | Save Env Vars


# **admin_install_suna_for_user_api_admin_suna_agents_install_user_account_id_post**
> object admin_install_suna_for_user_api_admin_suna_agents_install_user_account_id_post(account_id, replace_existing=replace_existing, x_admin_api_key=x_admin_api_key)

Admin Install Suna For User

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
    api_instance = suna_api_client.AdminApi(api_client)
    account_id = 'account_id_example' # str | 
    replace_existing = False # bool |  (optional) (default to False)
    x_admin_api_key = 'x_admin_api_key_example' # str |  (optional)

    try:
        # Admin Install Suna For User
        api_response = api_instance.admin_install_suna_for_user_api_admin_suna_agents_install_user_account_id_post(account_id, replace_existing=replace_existing, x_admin_api_key=x_admin_api_key)
        print("The response of AdminApi->admin_install_suna_for_user_api_admin_suna_agents_install_user_account_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->admin_install_suna_for_user_api_admin_suna_agents_install_user_account_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **replace_existing** | **bool**|  | [optional] [default to False]
 **x_admin_api_key** | **str**|  | [optional] 

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

# **get_env_vars_api_admin_env_vars_get**
> Dict[str, str] get_env_vars_api_admin_env_vars_get()

Get Env Vars

Get environment variables (local mode only).

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
    api_instance = suna_api_client.AdminApi(api_client)

    try:
        # Get Env Vars
        api_response = api_instance.get_env_vars_api_admin_env_vars_get()
        print("The response of AdminApi->get_env_vars_api_admin_env_vars_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->get_env_vars_api_admin_env_vars_get: %s\n" % e)
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

# **save_env_vars_api_admin_env_vars_post**
> Dict[str, str] save_env_vars_api_admin_env_vars_post(request_body)

Save Env Vars

Save environment variables (local mode only).

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
    api_instance = suna_api_client.AdminApi(api_client)
    request_body = {'key': 'request_body_example'} # Dict[str, str] | 

    try:
        # Save Env Vars
        api_response = api_instance.save_env_vars_api_admin_env_vars_post(request_body)
        print("The response of AdminApi->save_env_vars_api_admin_env_vars_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminApi->save_env_vars_api_admin_env_vars_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_body** | [**Dict[str, str]**](str.md)|  | 

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

