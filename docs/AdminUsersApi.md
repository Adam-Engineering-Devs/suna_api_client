# suna_api_client.AdminUsersApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adjust_user_credits_api_admin_users_credits_adjust_post**](AdminUsersApi.md#adjust_user_credits_api_admin_users_credits_adjust_post) | **POST** /api/admin/users/credits/adjust | Adjust User Credits
[**advanced_user_search_api_admin_users_search_advanced_post**](AdminUsersApi.md#advanced_user_search_api_admin_users_search_advanced_post) | **POST** /api/admin/users/search/advanced | Advanced User Search
[**get_user_activity_summary_api_admin_users_activity_summary_post**](AdminUsersApi.md#get_user_activity_summary_api_admin_users_activity_summary_post) | **POST** /api/admin/users/activity/summary | Get User Activity Summary
[**get_user_details_api_admin_users_user_id_get**](AdminUsersApi.md#get_user_details_api_admin_users_user_id_get) | **GET** /api/admin/users/{user_id} | Get User Details
[**get_user_stats_overview_api_admin_users_stats_overview_get**](AdminUsersApi.md#get_user_stats_overview_api_admin_users_stats_overview_get) | **GET** /api/admin/users/stats/overview | Get User Stats Overview
[**list_users_api_admin_users_list_get**](AdminUsersApi.md#list_users_api_admin_users_list_get) | **GET** /api/admin/users/list | List Users
[**search_users_by_email_api_admin_users_search_email_get**](AdminUsersApi.md#search_users_by_email_api_admin_users_search_email_get) | **GET** /api/admin/users/search/email | Search Users By Email


# **adjust_user_credits_api_admin_users_credits_adjust_post**
> object adjust_user_credits_api_admin_users_credits_adjust_post(core_admin_users_admin_credit_adjustment_request)

Adjust User Credits

### Example

* Bearer Authentication (HTTPBearer):

```python
import suna_api_client
from suna_api_client.models.core_admin_users_admin_credit_adjustment_request import CoreAdminUsersAdminCreditAdjustmentRequest
from suna_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = suna_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = suna_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with suna_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suna_api_client.AdminUsersApi(api_client)
    core_admin_users_admin_credit_adjustment_request = suna_api_client.CoreAdminUsersAdminCreditAdjustmentRequest() # CoreAdminUsersAdminCreditAdjustmentRequest | 

    try:
        # Adjust User Credits
        api_response = api_instance.adjust_user_credits_api_admin_users_credits_adjust_post(core_admin_users_admin_credit_adjustment_request)
        print("The response of AdminUsersApi->adjust_user_credits_api_admin_users_credits_adjust_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminUsersApi->adjust_user_credits_api_admin_users_credits_adjust_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **core_admin_users_admin_credit_adjustment_request** | [**CoreAdminUsersAdminCreditAdjustmentRequest**](CoreAdminUsersAdminCreditAdjustmentRequest.md)|  | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **advanced_user_search_api_admin_users_search_advanced_post**
> PaginatedResponseUserSummary advanced_user_search_api_admin_users_search_advanced_post(advanced_search_request, page=page, page_size=page_size)

Advanced User Search

### Example

* Bearer Authentication (HTTPBearer):

```python
import suna_api_client
from suna_api_client.models.advanced_search_request import AdvancedSearchRequest
from suna_api_client.models.paginated_response_user_summary import PaginatedResponseUserSummary
from suna_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = suna_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = suna_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with suna_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suna_api_client.AdminUsersApi(api_client)
    advanced_search_request = suna_api_client.AdvancedSearchRequest() # AdvancedSearchRequest | 
    page = 1 # int | Page number (optional) (default to 1)
    page_size = 20 # int | Items per page (optional) (default to 20)

    try:
        # Advanced User Search
        api_response = api_instance.advanced_user_search_api_admin_users_search_advanced_post(advanced_search_request, page=page, page_size=page_size)
        print("The response of AdminUsersApi->advanced_user_search_api_admin_users_search_advanced_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminUsersApi->advanced_user_search_api_admin_users_search_advanced_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **advanced_search_request** | [**AdvancedSearchRequest**](AdvancedSearchRequest.md)|  | 
 **page** | **int**| Page number | [optional] [default to 1]
 **page_size** | **int**| Items per page | [optional] [default to 20]

### Return type

[**PaginatedResponseUserSummary**](PaginatedResponseUserSummary.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_activity_summary_api_admin_users_activity_summary_post**
> object get_user_activity_summary_api_admin_users_activity_summary_post(user_activity_request)

Get User Activity Summary

### Example

* Bearer Authentication (HTTPBearer):

```python
import suna_api_client
from suna_api_client.models.user_activity_request import UserActivityRequest
from suna_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = suna_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = suna_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with suna_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suna_api_client.AdminUsersApi(api_client)
    user_activity_request = suna_api_client.UserActivityRequest() # UserActivityRequest | 

    try:
        # Get User Activity Summary
        api_response = api_instance.get_user_activity_summary_api_admin_users_activity_summary_post(user_activity_request)
        print("The response of AdminUsersApi->get_user_activity_summary_api_admin_users_activity_summary_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminUsersApi->get_user_activity_summary_api_admin_users_activity_summary_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_activity_request** | [**UserActivityRequest**](UserActivityRequest.md)|  | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_details_api_admin_users_user_id_get**
> object get_user_details_api_admin_users_user_id_get(user_id)

Get User Details

### Example

* Bearer Authentication (HTTPBearer):

```python
import suna_api_client
from suna_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = suna_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = suna_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with suna_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suna_api_client.AdminUsersApi(api_client)
    user_id = 'user_id_example' # str | 

    try:
        # Get User Details
        api_response = api_instance.get_user_details_api_admin_users_user_id_get(user_id)
        print("The response of AdminUsersApi->get_user_details_api_admin_users_user_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminUsersApi->get_user_details_api_admin_users_user_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **str**|  | 

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_stats_overview_api_admin_users_stats_overview_get**
> object get_user_stats_overview_api_admin_users_stats_overview_get()

Get User Stats Overview

### Example

* Bearer Authentication (HTTPBearer):

```python
import suna_api_client
from suna_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = suna_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = suna_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with suna_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suna_api_client.AdminUsersApi(api_client)

    try:
        # Get User Stats Overview
        api_response = api_instance.get_user_stats_overview_api_admin_users_stats_overview_get()
        print("The response of AdminUsersApi->get_user_stats_overview_api_admin_users_stats_overview_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminUsersApi->get_user_stats_overview_api_admin_users_stats_overview_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_users_api_admin_users_list_get**
> PaginatedResponseUserSummary list_users_api_admin_users_list_get(page=page, page_size=page_size, search_email=search_email, search_name=search_name, tier_filter=tier_filter, sort_by=sort_by, sort_order=sort_order)

List Users

### Example

* Bearer Authentication (HTTPBearer):

```python
import suna_api_client
from suna_api_client.models.paginated_response_user_summary import PaginatedResponseUserSummary
from suna_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = suna_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = suna_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with suna_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suna_api_client.AdminUsersApi(api_client)
    page = 1 # int | Page number (optional) (default to 1)
    page_size = 20 # int | Items per page (optional) (default to 20)
    search_email = 'search_email_example' # str | Search by email (optional)
    search_name = 'search_name_example' # str | Search by name (optional)
    tier_filter = 'tier_filter_example' # str | Filter by tier (optional)
    sort_by = 'created_at' # str | Sort field (optional) (default to 'created_at')
    sort_order = 'desc' # str | Sort order: asc, desc (optional) (default to 'desc')

    try:
        # List Users
        api_response = api_instance.list_users_api_admin_users_list_get(page=page, page_size=page_size, search_email=search_email, search_name=search_name, tier_filter=tier_filter, sort_by=sort_by, sort_order=sort_order)
        print("The response of AdminUsersApi->list_users_api_admin_users_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminUsersApi->list_users_api_admin_users_list_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] [default to 1]
 **page_size** | **int**| Items per page | [optional] [default to 20]
 **search_email** | **str**| Search by email | [optional] 
 **search_name** | **str**| Search by name | [optional] 
 **tier_filter** | **str**| Filter by tier | [optional] 
 **sort_by** | **str**| Sort field | [optional] [default to &#39;created_at&#39;]
 **sort_order** | **str**| Sort order: asc, desc | [optional] [default to &#39;desc&#39;]

### Return type

[**PaginatedResponseUserSummary**](PaginatedResponseUserSummary.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_users_by_email_api_admin_users_search_email_get**
> PaginatedResponseDictStrAny search_users_by_email_api_admin_users_search_email_get(email, page=page, page_size=page_size)

Search Users By Email

### Example

* Bearer Authentication (HTTPBearer):

```python
import suna_api_client
from suna_api_client.models.paginated_response_dict_str_any import PaginatedResponseDictStrAny
from suna_api_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = suna_api_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization: HTTPBearer
configuration = suna_api_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with suna_api_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = suna_api_client.AdminUsersApi(api_client)
    email = 'email_example' # str | Email to search for
    page = 1 # int | Page number (optional) (default to 1)
    page_size = 10 # int | Items per page (optional) (default to 10)

    try:
        # Search Users By Email
        api_response = api_instance.search_users_by_email_api_admin_users_search_email_get(email, page=page, page_size=page_size)
        print("The response of AdminUsersApi->search_users_by_email_api_admin_users_search_email_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminUsersApi->search_users_by_email_api_admin_users_search_email_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email** | **str**| Email to search for | 
 **page** | **int**| Page number | [optional] [default to 1]
 **page_size** | **int**| Items per page | [optional] [default to 10]

### Return type

[**PaginatedResponseDictStrAny**](PaginatedResponseDictStrAny.md)

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

