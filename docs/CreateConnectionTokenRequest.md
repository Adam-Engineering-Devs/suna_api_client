# CreateConnectionTokenRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app** | **str** |  | [optional] 

## Example

```python
from suna_api_client.models.create_connection_token_request import CreateConnectionTokenRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateConnectionTokenRequest from a JSON string
create_connection_token_request_instance = CreateConnectionTokenRequest.from_json(json)
# print the JSON string representation of the object
print(CreateConnectionTokenRequest.to_json())

# convert the object into a dict
create_connection_token_request_dict = create_connection_token_request_instance.to_dict()
# create an instance of CreateConnectionTokenRequest from a dict
create_connection_token_request_from_dict = CreateConnectionTokenRequest.from_dict(create_connection_token_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


