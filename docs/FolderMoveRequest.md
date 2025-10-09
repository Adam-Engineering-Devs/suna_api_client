# FolderMoveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**folder_id** | **str** |  | 

## Example

```python
from suna_api_client.models.folder_move_request import FolderMoveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FolderMoveRequest from a JSON string
folder_move_request_instance = FolderMoveRequest.from_json(json)
# print the JSON string representation of the object
print(FolderMoveRequest.to_json())

# convert the object into a dict
folder_move_request_dict = folder_move_request_instance.to_dict()
# create an instance of FolderMoveRequest from a dict
folder_move_request_from_dict = FolderMoveRequest.from_dict(folder_move_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


