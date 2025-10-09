# StoreCredentialRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mcp_qualified_name** | **str** |  | 
**display_name** | **str** |  | 
**config** | **Dict[str, object]** |  | 

## Example

```python
from suna_api_client.models.store_credential_request import StoreCredentialRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StoreCredentialRequest from a JSON string
store_credential_request_instance = StoreCredentialRequest.from_json(json)
# print the JSON string representation of the object
print(StoreCredentialRequest.to_json())

# convert the object into a dict
store_credential_request_dict = store_credential_request_instance.to_dict()
# create an instance of StoreCredentialRequest from a dict
store_credential_request_from_dict = StoreCredentialRequest.from_dict(store_credential_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


