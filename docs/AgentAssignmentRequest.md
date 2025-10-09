# AgentAssignmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**assignments** | **Dict[str, object]** | Dictionary of folder assignments | 

## Example

```python
from suna_api_client.models.agent_assignment_request import AgentAssignmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AgentAssignmentRequest from a JSON string
agent_assignment_request_instance = AgentAssignmentRequest.from_json(json)
# print the JSON string representation of the object
print(AgentAssignmentRequest.to_json())

# convert the object into a dict
agent_assignment_request_dict = agent_assignment_request_instance.to_dict()
# create an instance of AgentAssignmentRequest from a dict
agent_assignment_request_from_dict = AgentAssignmentRequest.from_dict(agent_assignment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


