# VersionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version_id** | **str** |  | 
**agent_id** | **str** |  | 
**version_number** | **int** |  | 
**version_name** | **str** |  | 
**system_prompt** | **str** |  | 
**model** | **str** |  | [optional] 
**configured_mcps** | **List[Dict[str, object]]** |  | 
**custom_mcps** | **List[Dict[str, object]]** |  | 
**agentpress_tools** | **Dict[str, object]** |  | 
**is_active** | **bool** |  | 
**status** | **str** |  | 
**created_at** | **str** |  | 
**updated_at** | **str** |  | 
**created_by** | **str** |  | 
**change_description** | **str** |  | [optional] 
**previous_version_id** | **str** |  | [optional] 

## Example

```python
from suna_api_client.models.version_response import VersionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VersionResponse from a JSON string
version_response_instance = VersionResponse.from_json(json)
# print the JSON string representation of the object
print(VersionResponse.to_json())

# convert the object into a dict
version_response_dict = version_response_instance.to_dict()
# create an instance of VersionResponse from a dict
version_response_from_dict = VersionResponse.from_dict(version_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


