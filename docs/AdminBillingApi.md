# suna_api_client.AdminBillingApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**adjust_user_credits_api_admin_billing_credits_adjust_post**](AdminBillingApi.md#adjust_user_credits_api_admin_billing_credits_adjust_post) | **POST** /api/admin/billing/credits/adjust | Adjust User Credits
[**get_user_billing_summary_api_admin_billing_user_account_id_summary_get**](AdminBillingApi.md#get_user_billing_summary_api_admin_billing_user_account_id_summary_get) | **GET** /api/admin/billing/user/{account_id}/summary | Get User Billing Summary
[**get_user_transactions_api_admin_billing_user_account_id_transactions_get**](AdminBillingApi.md#get_user_transactions_api_admin_billing_user_account_id_transactions_get) | **GET** /api/admin/billing/user/{account_id}/transactions | Get User Transactions
[**grant_credits_to_users_api_admin_billing_credits_grant_post**](AdminBillingApi.md#grant_credits_to_users_api_admin_billing_credits_grant_post) | **POST** /api/admin/billing/credits/grant | Grant Credits To Users
[**migrate_user_to_credits_api_admin_billing_migrate_user_account_id_post**](AdminBillingApi.md#migrate_user_to_credits_api_admin_billing_migrate_user_account_id_post) | **POST** /api/admin/billing/migrate-user/{account_id} | Migrate User To Credits
[**process_refund_api_admin_billing_refund_post**](AdminBillingApi.md#process_refund_api_admin_billing_refund_post) | **POST** /api/admin/billing/refund | Process Refund
[**search_user_api_admin_billing_user_search_post**](AdminBillingApi.md#search_user_api_admin_billing_user_search_post) | **POST** /api/admin/billing/user/search | Search User


# **adjust_user_credits_api_admin_billing_credits_adjust_post**
> object adjust_user_credits_api_admin_billing_credits_adjust_post(core_billing_admin_credit_adjustment_request)

Adjust User Credits

### Example

* Bearer Authentication (HTTPBearer):

```python
import suna_api_client
from suna_api_client.models.core_billing_admin_credit_adjustment_request import CoreBillingAdminCreditAdjustmentRequest
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
    api_instance = suna_api_client.AdminBillingApi(api_client)
    core_billing_admin_credit_adjustment_request = suna_api_client.CoreBillingAdminCreditAdjustmentRequest() # CoreBillingAdminCreditAdjustmentRequest | 

    try:
        # Adjust User Credits
        api_response = api_instance.adjust_user_credits_api_admin_billing_credits_adjust_post(core_billing_admin_credit_adjustment_request)
        print("The response of AdminBillingApi->adjust_user_credits_api_admin_billing_credits_adjust_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminBillingApi->adjust_user_credits_api_admin_billing_credits_adjust_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **core_billing_admin_credit_adjustment_request** | [**CoreBillingAdminCreditAdjustmentRequest**](CoreBillingAdminCreditAdjustmentRequest.md)|  | 

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

# **get_user_billing_summary_api_admin_billing_user_account_id_summary_get**
> object get_user_billing_summary_api_admin_billing_user_account_id_summary_get(account_id)

Get User Billing Summary

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
    api_instance = suna_api_client.AdminBillingApi(api_client)
    account_id = 'account_id_example' # str | 

    try:
        # Get User Billing Summary
        api_response = api_instance.get_user_billing_summary_api_admin_billing_user_account_id_summary_get(account_id)
        print("The response of AdminBillingApi->get_user_billing_summary_api_admin_billing_user_account_id_summary_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminBillingApi->get_user_billing_summary_api_admin_billing_user_account_id_summary_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 

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

# **get_user_transactions_api_admin_billing_user_account_id_transactions_get**
> object get_user_transactions_api_admin_billing_user_account_id_transactions_get(account_id, limit=limit, offset=offset, type_filter=type_filter)

Get User Transactions

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
    api_instance = suna_api_client.AdminBillingApi(api_client)
    account_id = 'account_id_example' # str | 
    limit = 100 # int |  (optional) (default to 100)
    offset = 0 # int |  (optional) (default to 0)
    type_filter = 'type_filter_example' # str |  (optional)

    try:
        # Get User Transactions
        api_response = api_instance.get_user_transactions_api_admin_billing_user_account_id_transactions_get(account_id, limit=limit, offset=offset, type_filter=type_filter)
        print("The response of AdminBillingApi->get_user_transactions_api_admin_billing_user_account_id_transactions_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminBillingApi->get_user_transactions_api_admin_billing_user_account_id_transactions_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 
 **limit** | **int**|  | [optional] [default to 100]
 **offset** | **int**|  | [optional] [default to 0]
 **type_filter** | **str**|  | [optional] 

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

# **grant_credits_to_users_api_admin_billing_credits_grant_post**
> object grant_credits_to_users_api_admin_billing_credits_grant_post(grant_credits_request)

Grant Credits To Users

### Example

* Bearer Authentication (HTTPBearer):

```python
import suna_api_client
from suna_api_client.models.grant_credits_request import GrantCreditsRequest
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
    api_instance = suna_api_client.AdminBillingApi(api_client)
    grant_credits_request = suna_api_client.GrantCreditsRequest() # GrantCreditsRequest | 

    try:
        # Grant Credits To Users
        api_response = api_instance.grant_credits_to_users_api_admin_billing_credits_grant_post(grant_credits_request)
        print("The response of AdminBillingApi->grant_credits_to_users_api_admin_billing_credits_grant_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminBillingApi->grant_credits_to_users_api_admin_billing_credits_grant_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **grant_credits_request** | [**GrantCreditsRequest**](GrantCreditsRequest.md)|  | 

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

# **migrate_user_to_credits_api_admin_billing_migrate_user_account_id_post**
> object migrate_user_to_credits_api_admin_billing_migrate_user_account_id_post(account_id)

Migrate User To Credits

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
    api_instance = suna_api_client.AdminBillingApi(api_client)
    account_id = 'account_id_example' # str | 

    try:
        # Migrate User To Credits
        api_response = api_instance.migrate_user_to_credits_api_admin_billing_migrate_user_account_id_post(account_id)
        print("The response of AdminBillingApi->migrate_user_to_credits_api_admin_billing_migrate_user_account_id_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminBillingApi->migrate_user_to_credits_api_admin_billing_migrate_user_account_id_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **account_id** | **str**|  | 

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

# **process_refund_api_admin_billing_refund_post**
> object process_refund_api_admin_billing_refund_post(refund_request)

Process Refund

### Example

* Bearer Authentication (HTTPBearer):

```python
import suna_api_client
from suna_api_client.models.refund_request import RefundRequest
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
    api_instance = suna_api_client.AdminBillingApi(api_client)
    refund_request = suna_api_client.RefundRequest() # RefundRequest | 

    try:
        # Process Refund
        api_response = api_instance.process_refund_api_admin_billing_refund_post(refund_request)
        print("The response of AdminBillingApi->process_refund_api_admin_billing_refund_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminBillingApi->process_refund_api_admin_billing_refund_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **refund_request** | [**RefundRequest**](RefundRequest.md)|  | 

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

# **search_user_api_admin_billing_user_search_post**
> object search_user_api_admin_billing_user_search_post(user_search_request)

Search User

### Example

* Bearer Authentication (HTTPBearer):

```python
import suna_api_client
from suna_api_client.models.user_search_request import UserSearchRequest
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
    api_instance = suna_api_client.AdminBillingApi(api_client)
    user_search_request = suna_api_client.UserSearchRequest() # UserSearchRequest | 

    try:
        # Search User
        api_response = api_instance.search_user_api_admin_billing_user_search_post(user_search_request)
        print("The response of AdminBillingApi->search_user_api_admin_billing_user_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AdminBillingApi->search_user_api_admin_billing_user_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_search_request** | [**UserSearchRequest**](UserSearchRequest.md)|  | 

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

