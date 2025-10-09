# WorkflowStepRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**config** | **Dict[str, object]** |  | [optional] 
**conditions** | **Dict[str, object]** |  | [optional] 
**order** | **int** |  | 
**parent_conditional_id** | **str** |  | [optional] 
**children** | [**List[WorkflowStepRequest]**](WorkflowStepRequest.md) |  | [optional] 

## Example

```python
from suna_api_client.models.workflow_step_request import WorkflowStepRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowStepRequest from a JSON string
workflow_step_request_instance = WorkflowStepRequest.from_json(json)
# print the JSON string representation of the object
print(WorkflowStepRequest.to_json())

# convert the object into a dict
workflow_step_request_dict = workflow_step_request_instance.to_dict()
# create an instance of WorkflowStepRequest from a dict
workflow_step_request_from_dict = WorkflowStepRequest.from_dict(workflow_step_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


