# KnowledgeBaseApiUpdateFolderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from suna_api_client.models.knowledge_base_api_update_folder_request import KnowledgeBaseApiUpdateFolderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeBaseApiUpdateFolderRequest from a JSON string
knowledge_base_api_update_folder_request_instance = KnowledgeBaseApiUpdateFolderRequest.from_json(json)
# print the JSON string representation of the object
print(KnowledgeBaseApiUpdateFolderRequest.to_json())

# convert the object into a dict
knowledge_base_api_update_folder_request_dict = knowledge_base_api_update_folder_request_instance.to_dict()
# create an instance of KnowledgeBaseApiUpdateFolderRequest from a dict
knowledge_base_api_update_folder_request_from_dict = KnowledgeBaseApiUpdateFolderRequest.from_dict(knowledge_base_api_update_folder_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


