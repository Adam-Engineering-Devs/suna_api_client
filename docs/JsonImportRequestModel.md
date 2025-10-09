# JsonImportRequestModel

Request to import agent from JSON.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_data** | **Dict[str, object]** |  | 
**instance_name** | **str** |  | [optional] 
**custom_system_prompt** | **str** |  | [optional] 
**profile_mappings** | **Dict[str, str]** |  | [optional] 
**custom_mcp_configs** | **Dict[str, Dict[str, object]]** |  | [optional] 

## Example

```python
from suna_api_client.models.json_import_request_model import JsonImportRequestModel

# TODO update the JSON string below
json = "{}"
# create an instance of JsonImportRequestModel from a JSON string
json_import_request_model_instance = JsonImportRequestModel.from_json(json)
# print the JSON string representation of the object
print(JsonImportRequestModel.to_json())

# convert the object into a dict
json_import_request_model_dict = json_import_request_model_instance.to_dict()
# create an instance of JsonImportRequestModel from a dict
json_import_request_model_from_dict = JsonImportRequestModel.from_dict(json_import_request_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


