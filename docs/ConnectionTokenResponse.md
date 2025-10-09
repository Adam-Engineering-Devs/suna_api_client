# ConnectionTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**link** | **str** |  | [optional] 
**token** | **str** |  | [optional] 
**external_user_id** | **str** |  | [optional] [default to '']
**app** | **str** |  | [optional] 
**expires_at** | **str** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from suna_api_client.models.connection_token_response import ConnectionTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionTokenResponse from a JSON string
connection_token_response_instance = ConnectionTokenResponse.from_json(json)
# print the JSON string representation of the object
print(ConnectionTokenResponse.to_json())

# convert the object into a dict
connection_token_response_dict = connection_token_response_instance.to_dict()
# create an instance of ConnectionTokenResponse from a dict
connection_token_response_from_dict = ConnectionTokenResponse.from_dict(connection_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


