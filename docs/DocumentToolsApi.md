# suna_api_client.DocumentToolsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert_and_upload_to_google_docs_api_document_tools_convert_and_upload_to_docs_post**](DocumentToolsApi.md#convert_and_upload_to_google_docs_api_document_tools_convert_and_upload_to_docs_post) | **POST** /api/document-tools/convert-and-upload-to-docs | Convert And Upload To Google Docs
[**debug_endpoint_api_document_tools_debug_get**](DocumentToolsApi.md#debug_endpoint_api_document_tools_debug_get) | **GET** /api/document-tools/debug | Debug Endpoint


# **convert_and_upload_to_google_docs_api_document_tools_convert_and_upload_to_docs_post**
> ConvertToDocsResponse convert_and_upload_to_google_docs_api_document_tools_convert_and_upload_to_docs_post(convert_to_docs_request)

Convert And Upload To Google Docs

### Example


```python
import suna_api_client
from suna_api_client.models.convert_to_docs_request import ConvertToDocsRequest
from suna_api_client.models.convert_to_docs_response import ConvertToDocsResponse
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
    api_instance = suna_api_client.DocumentToolsApi(api_client)
    convert_to_docs_request = suna_api_client.ConvertToDocsRequest() # ConvertToDocsRequest | 

    try:
        # Convert And Upload To Google Docs
        api_response = api_instance.convert_and_upload_to_google_docs_api_document_tools_convert_and_upload_to_docs_post(convert_to_docs_request)
        print("The response of DocumentToolsApi->convert_and_upload_to_google_docs_api_document_tools_convert_and_upload_to_docs_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentToolsApi->convert_and_upload_to_google_docs_api_document_tools_convert_and_upload_to_docs_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **convert_to_docs_request** | [**ConvertToDocsRequest**](ConvertToDocsRequest.md)|  | 

### Return type

[**ConvertToDocsResponse**](ConvertToDocsResponse.md)

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

# **debug_endpoint_api_document_tools_debug_get**
> object debug_endpoint_api_document_tools_debug_get()

Debug Endpoint

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
    api_instance = suna_api_client.DocumentToolsApi(api_client)

    try:
        # Debug Endpoint
        api_response = api_instance.debug_endpoint_api_document_tools_debug_get()
        print("The response of DocumentToolsApi->debug_endpoint_api_document_tools_debug_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentToolsApi->debug_endpoint_api_document_tools_debug_get: %s\n" % e)
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

