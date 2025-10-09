# CredentialResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential_id** | **str** |  | 
**mcp_qualified_name** | **str** |  | 
**display_name** | **str** |  | 
**config_keys** | **List[str]** |  | 
**is_active** | **bool** |  | 
**created_at** | **str** |  | [optional] 
**updated_at** | **str** |  | [optional] 

## Example

```python
from suna_api_client.models.credential_response import CredentialResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CredentialResponse from a JSON string
credential_response_instance = CredentialResponse.from_json(json)
# print the JSON string representation of the object
print(CredentialResponse.to_json())

# convert the object into a dict
credential_response_dict = credential_response_instance.to_dict()
# create an instance of CredentialResponse from a dict
credential_response_from_dict = CredentialResponse.from_dict(credential_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


