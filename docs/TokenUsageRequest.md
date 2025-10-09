# TokenUsageRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**prompt_tokens** | **int** |  | 
**completion_tokens** | **int** |  | 
**model** | **str** |  | 
**thread_id** | **str** |  | [optional] 
**message_id** | **str** |  | [optional] 

## Example

```python
from suna_api_client.models.token_usage_request import TokenUsageRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TokenUsageRequest from a JSON string
token_usage_request_instance = TokenUsageRequest.from_json(json)
# print the JSON string representation of the object
print(TokenUsageRequest.to_json())

# convert the object into a dict
token_usage_request_dict = token_usage_request_instance.to_dict()
# create an instance of TokenUsageRequest from a dict
token_usage_request_from_dict = TokenUsageRequest.from_dict(token_usage_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


