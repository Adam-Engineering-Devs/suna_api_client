# AgentVersionResponse

Response model for agent version information.

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
**created_at** | **str** |  | 
**updated_at** | **str** |  | 
**created_by** | **str** |  | [optional] 

## Example

```python
from suna_api_client.models.agent_version_response import AgentVersionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentVersionResponse from a JSON string
agent_version_response_instance = AgentVersionResponse.from_json(json)
# print the JSON string representation of the object
print(AgentVersionResponse.to_json())

# convert the object into a dict
agent_version_response_dict = agent_version_response_instance.to_dict()
# create an instance of AgentVersionResponse from a dict
agent_version_response_from_dict = AgentVersionResponse.from_dict(agent_version_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


