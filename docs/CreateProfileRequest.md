# CreateProfileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**toolkit_slug** | **str** |  | 
**profile_name** | **str** |  | 
**display_name** | **str** |  | [optional] 
**mcp_server_name** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] [default to False]
**initiation_fields** | **Dict[str, str]** |  | [optional] 
**custom_auth_config** | **Dict[str, str]** |  | [optional] 
**use_custom_auth** | **bool** |  | [optional] [default to False]

## Example

```python
from suna_api_client.models.create_profile_request import CreateProfileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProfileRequest from a JSON string
create_profile_request_instance = CreateProfileRequest.from_json(json)
# print the JSON string representation of the object
print(CreateProfileRequest.to_json())

# convert the object into a dict
create_profile_request_dict = create_profile_request_instance.to_dict()
# create an instance of CreateProfileRequest from a dict
create_profile_request_from_dict = CreateProfileRequest.from_dict(create_profile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


