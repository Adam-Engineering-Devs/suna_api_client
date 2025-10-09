# ProfileRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_name** | **str** |  | 
**app_slug** | **str** |  | 
**app_name** | **str** |  | 
**description** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] [default to False]
**oauth_app_id** | **str** |  | [optional] 
**enabled_tools** | **List[str]** |  | [optional] [default to []]
**external_user_id** | **str** |  | [optional] 

## Example

```python
from suna_api_client.models.profile_request import ProfileRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ProfileRequest from a JSON string
profile_request_instance = ProfileRequest.from_json(json)
# print the JSON string representation of the object
print(ProfileRequest.to_json())

# convert the object into a dict
profile_request_dict = profile_request_instance.to_dict()
# create an instance of ProfileRequest from a dict
profile_request_from_dict = ProfileRequest.from_dict(profile_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


