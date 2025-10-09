# AgentIconGenerationRequest

Request model for generating agent icon and colors.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from suna_api_client.models.agent_icon_generation_request import AgentIconGenerationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentIconGenerationRequest from a JSON string
agent_icon_generation_request_instance = AgentIconGenerationRequest.from_json(json)
# print the JSON string representation of the object
print(AgentIconGenerationRequest.to_json())

# convert the object into a dict
agent_icon_generation_request_dict = agent_icon_generation_request_instance.to_dict()
# create an instance of AgentIconGenerationRequest from a dict
agent_icon_generation_request_from_dict = AgentIconGenerationRequest.from_dict(agent_icon_generation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


