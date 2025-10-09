# ConvertToDocsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** | Whether the conversion was successful | 
**message** | **str** | Status message | 
**docx_url** | **str** |  | [optional] 
**google_docs_url** | **str** |  | [optional] 
**google_docs_file_id** | **str** |  | [optional] 
**is_api_enabled** | **bool** | Whether Google API is enabled | [optional] [default to True]

## Example

```python
from suna_api_client.models.convert_to_docs_response import ConvertToDocsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertToDocsResponse from a JSON string
convert_to_docs_response_instance = ConvertToDocsResponse.from_json(json)
# print the JSON string representation of the object
print(ConvertToDocsResponse.to_json())

# convert the object into a dict
convert_to_docs_response_dict = convert_to_docs_response_instance.to_dict()
# create an instance of ConvertToDocsResponse from a dict
convert_to_docs_response_from_dict = ConvertToDocsResponse.from_dict(convert_to_docs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


