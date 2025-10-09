# WorkflowExecuteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_data** | **Dict[str, object]** |  | [optional] 
**model_name** | **str** |  | [optional] 

## Example

```python
from suna_api_client.models.workflow_execute_request import WorkflowExecuteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WorkflowExecuteRequest from a JSON string
workflow_execute_request_instance = WorkflowExecuteRequest.from_json(json)
# print the JSON string representation of the object
print(WorkflowExecuteRequest.to_json())

# convert the object into a dict
workflow_execute_request_dict = workflow_execute_request_instance.to_dict()
# create an instance of WorkflowExecuteRequest from a dict
workflow_execute_request_from_dict = WorkflowExecuteRequest.from_dict(workflow_execute_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


