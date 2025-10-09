# KnowledgeBaseEntryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entry_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | 
**content** | **str** |  | 
**usage_context** | **str** |  | 
**is_active** | **bool** |  | 
**content_tokens** | **int** |  | 
**created_at** | **str** |  | 
**updated_at** | **str** |  | 
**source_type** | **str** |  | [optional] 
**source_metadata** | **Dict[str, object]** |  | [optional] 
**file_size** | **int** |  | [optional] 
**file_mime_type** | **str** |  | [optional] 

## Example

```python
from suna_api_client.models.knowledge_base_entry_response import KnowledgeBaseEntryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeBaseEntryResponse from a JSON string
knowledge_base_entry_response_instance = KnowledgeBaseEntryResponse.from_json(json)
# print the JSON string representation of the object
print(KnowledgeBaseEntryResponse.to_json())

# convert the object into a dict
knowledge_base_entry_response_dict = knowledge_base_entry_response_instance.to_dict()
# create an instance of KnowledgeBaseEntryResponse from a dict
knowledge_base_entry_response_from_dict = KnowledgeBaseEntryResponse.from_dict(knowledge_base_entry_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


