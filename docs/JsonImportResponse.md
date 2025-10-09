# JsonImportResponse

Response from JSON import.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**instance_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**missing_regular_credentials** | **List[Dict[str, object]]** |  | [optional] [default to []]
**missing_custom_configs** | **List[Dict[str, object]]** |  | [optional] [default to []]
**agent_info** | **Dict[str, object]** |  | [optional] 

## Example

```python
from suna_api_client.models.json_import_response import JsonImportResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JsonImportResponse from a JSON string
json_import_response_instance = JsonImportResponse.from_json(json)
# print the JSON string representation of the object
print(JsonImportResponse.to_json())

# convert the object into a dict
json_import_response_dict = json_import_response_instance.to_dict()
# create an instance of JsonImportResponse from a dict
json_import_response_from_dict = JsonImportResponse.from_dict(json_import_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


