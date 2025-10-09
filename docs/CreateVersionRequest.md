# CreateVersionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**system_prompt** | **str** |  | 
**model** | **str** |  | [optional] 
**configured_mcps** | **List[Dict[str, object]]** |  | [optional] [default to []]
**custom_mcps** | **List[Dict[str, object]]** |  | [optional] [default to []]
**agentpress_tools** | **Dict[str, object]** |  | [optional] 
**version_name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from suna_api_client.models.create_version_request import CreateVersionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateVersionRequest from a JSON string
create_version_request_instance = CreateVersionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateVersionRequest.to_json())

# convert the object into a dict
create_version_request_dict = create_version_request_instance.to_dict()
# create an instance of CreateVersionRequest from a dict
create_version_request_from_dict = CreateVersionRequest.from_dict(create_version_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


