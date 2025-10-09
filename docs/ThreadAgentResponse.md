# ThreadAgentResponse

Response model for thread agent information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent** | [**AgentResponse**](AgentResponse.md) |  | 
**source** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from suna_api_client.models.thread_agent_response import ThreadAgentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ThreadAgentResponse from a JSON string
thread_agent_response_instance = ThreadAgentResponse.from_json(json)
# print the JSON string representation of the object
print(ThreadAgentResponse.to_json())

# convert the object into a dict
thread_agent_response_dict = thread_agent_response_instance.to_dict()
# create an instance of ThreadAgentResponse from a dict
thread_agent_response_from_dict = ThreadAgentResponse.from_dict(thread_agent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


