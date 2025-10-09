# MessageCreateRequest

Request model for creating a message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**content** | **str** |  | 
**is_llm_message** | **bool** |  | [optional] [default to True]

## Example

```python
from suna_api_client.models.message_create_request import MessageCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MessageCreateRequest from a JSON string
message_create_request_instance = MessageCreateRequest.from_json(json)
# print the JSON string representation of the object
print(MessageCreateRequest.to_json())

# convert the object into a dict
message_create_request_dict = message_create_request_instance.to_dict()
# create an instance of MessageCreateRequest from a dict
message_create_request_from_dict = MessageCreateRequest.from_dict(message_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


