# APIKeyCreateResponse

Response model for newly created API key (includes both keys)

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**key_id** | **str** |  | 
**public_key** | **str** |  | 
**secret_key** | **str** |  | 
**title** | **str** |  | 
**description** | **str** |  | 
**status** | **str** |  | 
**expires_at** | **datetime** |  | 
**created_at** | **datetime** |  | 

## Example

```python
from suna_api_client.models.api_key_create_response import APIKeyCreateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of APIKeyCreateResponse from a JSON string
api_key_create_response_instance = APIKeyCreateResponse.from_json(json)
# print the JSON string representation of the object
print(APIKeyCreateResponse.to_json())

# convert the object into a dict
api_key_create_response_dict = api_key_create_response_instance.to_dict()
# create an instance of APIKeyCreateResponse from a dict
api_key_create_response_from_dict = APIKeyCreateResponse.from_dict(api_key_create_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


