# AgentCreateRequest

Request model for creating a new agent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
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

## Example

```python
from suna_api_client.models.agent_create_request import AgentCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentCreateRequest from a JSON string
agent_create_request_instance = AgentCreateRequest.from_json(json)
# print the JSON string representation of the object
print(AgentCreateRequest.to_json())

# convert the object into a dict
agent_create_request_dict = agent_create_request_instance.to_dict()
# create an instance of AgentCreateRequest from a dict
agent_create_request_from_dict = AgentCreateRequest.from_dict(agent_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


