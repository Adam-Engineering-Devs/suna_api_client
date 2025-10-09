# WorkflowCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**trigger_phrase** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] [default to False]
**steps** | [**List[WorkflowStepRequest]**](WorkflowStepRequest.md) |  | [optional] [default to []]

## Example

```python
from suna_api_client.models.workflow_create_request import WorkflowCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowCreateRequest from a JSON string
workflow_create_request_instance = WorkflowCreateRequest.from_json(json)
# print the JSON string representation of the object
print(WorkflowCreateRequest.to_json())

# convert the object into a dict
workflow_create_request_dict = workflow_create_request_instance.to_dict()
# create an instance of WorkflowCreateRequest from a dict
workflow_create_request_from_dict = WorkflowCreateRequest.from_dict(workflow_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


