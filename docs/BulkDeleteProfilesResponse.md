# BulkDeleteProfilesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**deleted_count** | **int** |  | 
**failed_profiles** | **List[str]** |  | [optional] [default to []]
**message** | **str** |  | 

## Example

```python
from suna_api_client.models.bulk_delete_profiles_response import BulkDeleteProfilesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of BulkDeleteProfilesResponse from a JSON string
bulk_delete_profiles_response_instance = BulkDeleteProfilesResponse.from_json(json)
# print the JSON string representation of the object
print(BulkDeleteProfilesResponse.to_json())

# convert the object into a dict
bulk_delete_profiles_response_dict = bulk_delete_profiles_response_instance.to_dict()
# create an instance of BulkDeleteProfilesResponse from a dict
bulk_delete_profiles_response_from_dict = BulkDeleteProfilesResponse.from_dict(bulk_delete_profiles_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


