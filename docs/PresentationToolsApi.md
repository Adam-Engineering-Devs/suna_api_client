# suna_api_client.PresentationToolsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert_and_upload_to_google_slides_api_presentation_tools_convert_and_upload_to_slides_post**](PresentationToolsApi.md#convert_and_upload_to_google_slides_api_presentation_tools_convert_and_upload_to_slides_post) | **POST** /api/presentation-tools/convert-and-upload-to-slides | Convert And Upload To Google Slides


# **convert_and_upload_to_google_slides_api_presentation_tools_convert_and_upload_to_slides_post**
> ConvertToSlidesResponse convert_and_upload_to_google_slides_api_presentation_tools_convert_and_upload_to_slides_post(convert_to_slides_request)

Convert And Upload To Google Slides

Convert HTML presentation to PPTX and upload to Google Slides

Flow:
1. Call sandbox to convert HTML → PPTX
2. Download PPTX from sandbox  
3. Upload PPTX to Google Slides using authenticated user's credentials
4. Return both local and Google Slides URLs

### Example


```python
import suna_api_client
from suna_api_client.models.convert_to_slides_request import ConvertToSlidesRequest
from suna_api_client.models.convert_to_slides_response import ConvertToSlidesResponse
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
    api_instance = suna_api_client.PresentationToolsApi(api_client)
    convert_to_slides_request = suna_api_client.ConvertToSlidesRequest() # ConvertToSlidesRequest | 

    try:
        # Convert And Upload To Google Slides
        api_response = api_instance.convert_and_upload_to_google_slides_api_presentation_tools_convert_and_upload_to_slides_post(convert_to_slides_request)
        print("The response of PresentationToolsApi->convert_and_upload_to_google_slides_api_presentation_tools_convert_and_upload_to_slides_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PresentationToolsApi->convert_and_upload_to_google_slides_api_presentation_tools_convert_and_upload_to_slides_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **convert_to_slides_request** | [**ConvertToSlidesRequest**](ConvertToSlidesRequest.md)|  | 

### Return type

[**ConvertToSlidesResponse**](ConvertToSlidesResponse.md)

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

