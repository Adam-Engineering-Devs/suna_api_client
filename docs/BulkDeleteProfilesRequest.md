# BulkDeleteProfilesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_ids** | **List[str]** |  | 

## Example

```python
from suna_api_client.models.bulk_delete_profiles_request import BulkDeleteProfilesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDeleteProfilesRequest from a JSON string
bulk_delete_profiles_request_instance = BulkDeleteProfilesRequest.from_json(json)
# print the JSON string representation of the object
print(BulkDeleteProfilesRequest.to_json())

# convert the object into a dict
bulk_delete_profiles_request_dict = bulk_delete_profiles_request_instance.to_dict()
# create an instance of BulkDeleteProfilesRequest from a dict
bulk_delete_profiles_request_from_dict = BulkDeleteProfilesRequest.from_dict(bulk_delete_profiles_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


