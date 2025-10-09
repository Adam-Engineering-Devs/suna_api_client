# AgentIconGenerationResponse

Response model for generated agent icon and colors.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**icon_name** | **str** |  | 
**icon_color** | **str** |  | 
**icon_background** | **str** |  | 

## Example

```python
from suna_api_client.models.agent_icon_generation_response import AgentIconGenerationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AgentIconGenerationResponse from a JSON string
agent_icon_generation_response_instance = AgentIconGenerationResponse.from_json(json)
# print the JSON string representation of the object
print(AgentIconGenerationResponse.to_json())

# convert the object into a dict
agent_icon_generation_response_dict = agent_icon_generation_response_instance.to_dict()
# create an instance of AgentIconGenerationResponse from a dict
agent_icon_generation_response_from_dict = AgentIconGenerationResponse.from_dict(agent_icon_generation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


