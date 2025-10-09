# EntryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_id** | **str** |  | 
**filename** | **str** |  | 
**summary** | **str** |  | 
**file_size** | **int** |  | 
**created_at** | **str** |  | 

## Example

```python
from suna_api_client.models.entry_response import EntryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EntryResponse from a JSON string
entry_response_instance = EntryResponse.from_json(json)
# print the JSON string representation of the object
print(EntryResponse.to_json())

# convert the object into a dict
entry_response_dict = entry_response_instance.to_dict()
# create an instance of EntryResponse from a dict
entry_response_from_dict = EntryResponse.from_dict(entry_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


