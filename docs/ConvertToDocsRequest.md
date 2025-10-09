# ConvertToDocsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**doc_path** | **str** | Path to the document file in sandbox | 
**sandbox_url** | **str** | URL of the sandbox service | 

## Example

```python
from suna_api_client.models.convert_to_docs_request import ConvertToDocsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertToDocsRequest from a JSON string
convert_to_docs_request_instance = ConvertToDocsRequest.from_json(json)
# print the JSON string representation of the object
print(ConvertToDocsRequest.to_json())

# convert the object into a dict
convert_to_docs_request_dict = convert_to_docs_request_instance.to_dict()
# create an instance of ConvertToDocsRequest from a dict
convert_to_docs_request_from_dict = ConvertToDocsRequest.from_dict(convert_to_docs_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


