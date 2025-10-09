# CoreKnowledgeBaseApiUpdateFolderRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 

## Example

```python
from suna_api_client.models.core_knowledge_base_api_update_folder_request import CoreKnowledgeBaseApiUpdateFolderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CoreKnowledgeBaseApiUpdateFolderRequest from a JSON string
core_knowledge_base_api_update_folder_request_instance = CoreKnowledgeBaseApiUpdateFolderRequest.from_json(json)
# print the JSON string representation of the object
print(CoreKnowledgeBaseApiUpdateFolderRequest.to_json())

# convert the object into a dict
core_knowledge_base_api_update_folder_request_dict = core_knowledge_base_api_update_folder_request_instance.to_dict()
# create an instance of CoreKnowledgeBaseApiUpdateFolderRequest from a dict
core_knowledge_base_api_update_folder_request_from_dict = CoreKnowledgeBaseApiUpdateFolderRequest.from_dict(core_knowledge_base_api_update_folder_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


