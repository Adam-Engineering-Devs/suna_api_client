# WorkflowUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**trigger_phrase** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**status** | **str** |  | [optional] 
**steps** | [**List[WorkflowStepRequest]**](WorkflowStepRequest.md) |  | [optional] 

## Example

```python
from suna_api_client.models.workflow_update_request import WorkflowUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowUpdateRequest from a JSON string
workflow_update_request_instance = WorkflowUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(WorkflowUpdateRequest.to_json())

# convert the object into a dict
workflow_update_request_dict = workflow_update_request_instance.to_dict()
# create an instance of WorkflowUpdateRequest from a dict
workflow_update_request_from_dict = WorkflowUpdateRequest.from_dict(workflow_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


