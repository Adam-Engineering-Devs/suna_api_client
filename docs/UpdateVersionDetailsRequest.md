# UpdateVersionDetailsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version_name** | **str** |  | [optional] 
**change_description** | **str** |  | [optional] 

## Example

```python
from suna_api_client.models.update_version_details_request import UpdateVersionDetailsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateVersionDetailsRequest from a JSON string
update_version_details_request_instance = UpdateVersionDetailsRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateVersionDetailsRequest.to_json())

# convert the object into a dict
update_version_details_request_dict = update_version_details_request_instance.to_dict()
# create an instance of UpdateVersionDetailsRequest from a dict
update_version_details_request_from_dict = UpdateVersionDetailsRequest.from_dict(update_version_details_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


