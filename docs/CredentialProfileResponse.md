# CredentialProfileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_id** | **str** |  | 
**mcp_qualified_name** | **str** |  | 
**profile_name** | **str** |  | 
**display_name** | **str** |  | 
**config_keys** | **List[str]** |  | 
**is_active** | **bool** |  | 
**is_default** | **bool** |  | 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from suna_api_client.models.credential_profile_response import CredentialProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialProfileResponse from a JSON string
credential_profile_response_instance = CredentialProfileResponse.from_json(json)
# print the JSON string representation of the object
print(CredentialProfileResponse.to_json())

# convert the object into a dict
credential_profile_response_dict = credential_profile_response_instance.to_dict()
# create an instance of CredentialProfileResponse from a dict
credential_profile_response_from_dict = CredentialProfileResponse.from_dict(credential_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


