# AgentStartRequest

Request model for starting an agent.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**model_name** | **str** |  | [optional] 
**enable_thinking** | **bool** |  | [optional] 
**reasoning_effort** | **str** |  | [optional] 
**stream** | **bool** |  | [optional] 
**enable_context_manager** | **bool** |  | [optional] 
**enable_prompt_caching** | **bool** |  | [optional] 
**agent_id** | **str** |  | [optional] 

## Example

```python
from suna_api_client.models.agent_start_request import AgentStartRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentStartRequest from a JSON string
agent_start_request_instance = AgentStartRequest.from_json(json)
# print the JSON string representation of the object
print(AgentStartRequest.to_json())

# convert the object into a dict
agent_start_request_dict = agent_start_request_instance.to_dict()
# create an instance of AgentStartRequest from a dict
agent_start_request_from_dict = AgentStartRequest.from_dict(agent_start_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


