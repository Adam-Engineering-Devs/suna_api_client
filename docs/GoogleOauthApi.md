# suna_api_client.GoogleOauthApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_google_auth_url_api_google_auth_url_get**](GoogleOauthApi.md#get_google_auth_url_api_google_auth_url_get) | **GET** /api/google/auth-url | Get Google Auth Url
[**google_oauth_callback_api_google_callback_get**](GoogleOauthApi.md#google_oauth_callback_api_google_callback_get) | **GET** /api/google/callback | Google Oauth Callback


# **get_google_auth_url_api_google_auth_url_get**
> AuthURLResponse get_google_auth_url_api_google_auth_url_get(return_url=return_url)

Get Google Auth Url

Generate Google OAuth consent URL for the authenticated user

Args:
    user_id: User identifier from JWT authentication
    return_url: Optional URL to redirect to after successful OAuth
    google_service: Injected Google Slides service

Returns:
    OAuth consent URL that user should visit

### Example


```python
import suna_api_client
from suna_api_client.models.auth_url_response import AuthURLResponse
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
    api_instance = suna_api_client.GoogleOauthApi(api_client)
    return_url = 'return_url_example' # str | URL to redirect to after OAuth (optional)

    try:
        # Get Google Auth Url
        api_response = api_instance.get_google_auth_url_api_google_auth_url_get(return_url=return_url)
        print("The response of GoogleOauthApi->get_google_auth_url_api_google_auth_url_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleOauthApi->get_google_auth_url_api_google_auth_url_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **return_url** | **str**| URL to redirect to after OAuth | [optional] 

### Return type

[**AuthURLResponse**](AuthURLResponse.md)

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

# **google_oauth_callback_api_google_callback_get**
> object google_oauth_callback_api_google_callback_get(code=code, state=state, error=error)

Google Oauth Callback

Handle Google OAuth callback

This endpoint receives the authorization code from Google and exchanges it for tokens.
Redirects to the frontend with success/error status.

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
    api_instance = suna_api_client.GoogleOauthApi(api_client)
    code = 'code_example' # str | Authorization code from Google (optional)
    state = 'state_example' # str | State parameter (contains user_id) (optional)
    error = 'error_example' # str | Error from Google OAuth (optional)

    try:
        # Google Oauth Callback
        api_response = api_instance.google_oauth_callback_api_google_callback_get(code=code, state=state, error=error)
        print("The response of GoogleOauthApi->google_oauth_callback_api_google_callback_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GoogleOauthApi->google_oauth_callback_api_google_callback_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **code** | **str**| Authorization code from Google | [optional] 
 **state** | **str**| State parameter (contains user_id) | [optional] 
 **error** | **str**| Error from Google OAuth | [optional] 

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

