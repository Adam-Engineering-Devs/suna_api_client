# FolderResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**entry_count** | **int** |  | 
**created_at** | **str** |  | 

## Example

```python
from suna_api_client.models.folder_response import FolderResponse

# TODO update the JSON string below
json = "{}"
# create an instance of FolderResponse from a JSON string
folder_response_instance = FolderResponse.from_json(json)
# print the JSON string representation of the object
print(FolderResponse.to_json())

# convert the object into a dict
folder_response_dict = folder_response_instance.to_dict()
# create an instance of FolderResponse from a dict
folder_response_from_dict = FolderResponse.from_dict(folder_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


