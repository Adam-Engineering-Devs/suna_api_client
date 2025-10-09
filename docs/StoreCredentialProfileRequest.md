# StoreCredentialProfileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**mcp_qualified_name** | **str** |  | 
**profile_name** | **str** |  | 
**display_name** | **str** |  | 
**config** | **Dict[str, object]** |  | 
**is_default** | **bool** |  | [optional] [default to False]

## Example

```python
from suna_api_client.models.store_credential_profile_request import StoreCredentialProfileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StoreCredentialProfileRequest from a JSON string
store_credential_profile_request_instance = StoreCredentialProfileRequest.from_json(json)
# print the JSON string representation of the object
print(StoreCredentialProfileRequest.to_json())

# convert the object into a dict
store_credential_profile_request_dict = store_credential_profile_request_instance.to_dict()
# create an instance of StoreCredentialProfileRequest from a dict
store_credential_profile_request_from_dict = StoreCredentialProfileRequest.from_dict(store_credential_profile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


