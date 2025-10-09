# TriggerUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config** | **Dict[str, object]** |  | [optional] 
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 

## Example

```python
from suna_api_client.models.trigger_update_request import TriggerUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerUpdateRequest from a JSON string
trigger_update_request_instance = TriggerUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(TriggerUpdateRequest.to_json())

# convert the object into a dict
trigger_update_request_dict = trigger_update_request_instance.to_dict()
# create an instance of TriggerUpdateRequest from a dict
trigger_update_request_from_dict = TriggerUpdateRequest.from_dict(trigger_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


