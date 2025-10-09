# CorePipedreamApiProfileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_id** | **str** |  | 
**account_id** | **str** |  | 
**mcp_qualified_name** | **str** |  | 
**profile_name** | **str** |  | 
**display_name** | **str** |  | 
**app_slug** | **str** |  | 
**app_name** | **str** |  | 
**external_user_id** | **str** |  | 
**enabled_tools** | **List[str]** |  | 
**is_active** | **bool** |  | 
**is_default** | **bool** |  | 
**is_connected** | **bool** |  | 
**created_at** | **datetime** |  | 
**updated_at** | **datetime** |  | 
**last_used_at** | **datetime** |  | [optional] 

## Example

```python
from suna_api_client.models.core_pipedream_api_profile_response import CorePipedreamApiProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CorePipedreamApiProfileResponse from a JSON string
core_pipedream_api_profile_response_instance = CorePipedreamApiProfileResponse.from_json(json)
# print the JSON string representation of the object
print(CorePipedreamApiProfileResponse.to_json())

# convert the object into a dict
core_pipedream_api_profile_response_dict = core_pipedream_api_profile_response_instance.to_dict()
# create an instance of CorePipedreamApiProfileResponse from a dict
core_pipedream_api_profile_response_from_dict = CorePipedreamApiProfileResponse.from_dict(core_pipedream_api_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


