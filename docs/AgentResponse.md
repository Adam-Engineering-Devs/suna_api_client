# AgentResponse

Response model for agent information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**system_prompt** | **str** |  | 
**configured_mcps** | **List[Dict[str, object]]** |  | 
**custom_mcps** | **List[Dict[str, object]]** |  | 
**agentpress_tools** | **Dict[str, object]** |  | 
**is_default** | **bool** |  | 
**profile_image_url** | **str** |  | [optional] 
**icon_name** | **str** |  | [optional] 
**icon_color** | **str** |  | [optional] 
**icon_background** | **str** |  | [optional] 
**created_at** | **str** |  | 
**updated_at** | **str** |  | [optional] 
**is_public** | **bool** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**current_version_id** | **str** |  | [optional] 
**version_count** | **int** |  | [optional] 
**current_version** | [**AgentVersionResponse**](AgentVersionResponse.md) |  | [optional] 
**metadata** | **Dict[str, object]** |  | [optional] 

## Example

```python
from suna_api_client.models.agent_response import AgentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentResponse from a JSON string
agent_response_instance = AgentResponse.from_json(json)
# print the JSON string representation of the object
print(AgentResponse.to_json())

# convert the object into a dict
agent_response_dict = agent_response_instance.to_dict()
# create an instance of AgentResponse from a dict
agent_response_from_dict = AgentResponse.from_dict(agent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


