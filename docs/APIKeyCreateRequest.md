# APIKeyCreateRequest

Request model for creating a new API key

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | Human-readable title for the API key | 
**description** | **str** |  | [optional] 
**expires_in_days** | **int** |  | [optional] 

## Example

```python
from suna_api_client.models.api_key_create_request import APIKeyCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeyCreateRequest from a JSON string
api_key_create_request_instance = APIKeyCreateRequest.from_json(json)
# print the JSON string representation of the object
print(APIKeyCreateRequest.to_json())

# convert the object into a dict
api_key_create_request_dict = api_key_create_request_instance.to_dict()
# create an instance of APIKeyCreateRequest from a dict
api_key_create_request_from_dict = APIKeyCreateRequest.from_dict(api_key_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


