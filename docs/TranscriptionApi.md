# suna_api_client.TranscriptionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**transcribe_audio_api_transcription_post**](TranscriptionApi.md#transcribe_audio_api_transcription_post) | **POST** /api/transcription | Transcribe Audio
[**transcribe_audio_transcription_post**](TranscriptionApi.md#transcribe_audio_transcription_post) | **POST** /transcription | Transcribe Audio


# **transcribe_audio_api_transcription_post**
> TranscriptionResponse transcribe_audio_api_transcription_post(audio_file)

Transcribe Audio

Transcribe audio file to text using OpenAI Whisper.

### Example


```python
import suna_api_client
from suna_api_client.models.transcription_response import TranscriptionResponse
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
    api_instance = suna_api_client.TranscriptionApi(api_client)
    audio_file = None # bytearray | 

    try:
        # Transcribe Audio
        api_response = api_instance.transcribe_audio_api_transcription_post(audio_file)
        print("The response of TranscriptionApi->transcribe_audio_api_transcription_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranscriptionApi->transcribe_audio_api_transcription_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audio_file** | **bytearray**|  | 

### Return type

[**TranscriptionResponse**](TranscriptionResponse.md)

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

# **transcribe_audio_transcription_post**
> TranscriptionResponse transcribe_audio_transcription_post(audio_file)

Transcribe Audio

Transcribe audio file to text using OpenAI Whisper.

### Example


```python
import suna_api_client
from suna_api_client.models.transcription_response import TranscriptionResponse
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
    api_instance = suna_api_client.TranscriptionApi(api_client)
    audio_file = None # bytearray | 

    try:
        # Transcribe Audio
        api_response = api_instance.transcribe_audio_transcription_post(audio_file)
        print("The response of TranscriptionApi->transcribe_audio_transcription_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TranscriptionApi->transcribe_audio_transcription_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **audio_file** | **bytearray**|  | 

### Return type

[**TranscriptionResponse**](TranscriptionResponse.md)

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

