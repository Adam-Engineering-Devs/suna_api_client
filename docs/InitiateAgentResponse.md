# InitiateAgentResponse

Response model for agent initiation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**thread_id** | **str** |  | 
**agent_run_id** | **str** |  | [optional] 

## Example

```python
from suna_api_client.models.initiate_agent_response import InitiateAgentResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InitiateAgentResponse from a JSON string
initiate_agent_response_instance = InitiateAgentResponse.from_json(json)
# print the JSON string representation of the object
print(InitiateAgentResponse.to_json())

# convert the object into a dict
initiate_agent_response_dict = initiate_agent_response_instance.to_dict()
# create an instance of InitiateAgentResponse from a dict
initiate_agent_response_from_dict = InitiateAgentResponse.from_dict(initiate_agent_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


