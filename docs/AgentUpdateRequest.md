# AgentUpdateRequest

Request model for updating an existing agent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**system_prompt** | **str** |  | [optional] 
**configured_mcps** | **List[Dict[str, object]]** |  | [optional] 
**custom_mcps** | **List[Dict[str, object]]** |  | [optional] 
**agentpress_tools** | **Dict[str, object]** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**profile_image_url** | **str** |  | [optional] 
**icon_name** | **str** |  | [optional] 
**icon_color** | **str** |  | [optional] 
**icon_background** | **str** |  | [optional] 
**replace_mcps** | **bool** |  | [optional] 

## Example

```python
from suna_api_client.models.agent_update_request import AgentUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentUpdateRequest from a JSON string
agent_update_request_instance = AgentUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(AgentUpdateRequest.to_json())

# convert the object into a dict
agent_update_request_dict = agent_update_request_instance.to_dict()
# create an instance of AgentUpdateRequest from a dict
agent_update_request_from_dict = AgentUpdateRequest.from_dict(agent_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


