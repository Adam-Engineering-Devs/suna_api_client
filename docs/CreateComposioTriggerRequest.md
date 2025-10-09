# CreateComposioTriggerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_id** | **str** |  | 
**profile_id** | **str** |  | 
**slug** | **str** |  | 
**trigger_config** | **Dict[str, object]** |  | 
**route** | **str** |  | 
**name** | **str** |  | [optional] 
**agent_prompt** | **str** |  | [optional] 
**workflow_id** | **str** |  | [optional] 
**workflow_input** | **Dict[str, object]** |  | [optional] 
**connected_account_id** | **str** |  | [optional] 
**webhook_url** | **str** |  | [optional] 
**toolkit_slug** | **str** |  | [optional] 

## Example

```python
from suna_api_client.models.create_composio_trigger_request import CreateComposioTriggerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateComposioTriggerRequest from a JSON string
create_composio_trigger_request_instance = CreateComposioTriggerRequest.from_json(json)
# print the JSON string representation of the object
print(CreateComposioTriggerRequest.to_json())

# convert the object into a dict
create_composio_trigger_request_dict = create_composio_trigger_request_instance.to_dict()
# create an instance of CreateComposioTriggerRequest from a dict
create_composio_trigger_request_from_dict = CreateComposioTriggerRequest.from_dict(create_composio_trigger_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


