# UpdateProfileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**enabled_tools** | **List[str]** |  | [optional] 

## Example

```python
from suna_api_client.models.update_profile_request import UpdateProfileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateProfileRequest from a JSON string
update_profile_request_instance = UpdateProfileRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateProfileRequest.to_json())

# convert the object into a dict
update_profile_request_dict = update_profile_request_instance.to_dict()
# create an instance of UpdateProfileRequest from a dict
update_profile_request_from_dict = UpdateProfileRequest.from_dict(update_profile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


