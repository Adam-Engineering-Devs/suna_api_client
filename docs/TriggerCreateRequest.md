# TriggerCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** |  | 
**name** | **str** |  | 
**config** | **Dict[str, object]** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from suna_api_client.models.trigger_create_request import TriggerCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerCreateRequest from a JSON string
trigger_create_request_instance = TriggerCreateRequest.from_json(json)
# print the JSON string representation of the object
print(TriggerCreateRequest.to_json())

# convert the object into a dict
trigger_create_request_dict = trigger_create_request_instance.to_dict()
# create an instance of TriggerCreateRequest from a dict
trigger_create_request_from_dict = TriggerCreateRequest.from_dict(trigger_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


