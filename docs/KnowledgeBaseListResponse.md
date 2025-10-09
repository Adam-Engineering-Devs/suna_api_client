# KnowledgeBaseListResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[KnowledgeBaseEntryResponse]**](KnowledgeBaseEntryResponse.md) |  | 
**total_count** | **int** |  | 
**total_tokens** | **int** |  | 

## Example

```python
from suna_api_client.models.knowledge_base_list_response import KnowledgeBaseListResponse

# TODO update the JSON string below
json = "{}"
# create an instance of KnowledgeBaseListResponse from a JSON string
knowledge_base_list_response_instance = KnowledgeBaseListResponse.from_json(json)
# print the JSON string representation of the object
print(KnowledgeBaseListResponse.to_json())

# convert the object into a dict
knowledge_base_list_response_dict = knowledge_base_list_response_instance.to_dict()
# create an instance of KnowledgeBaseListResponse from a dict
knowledge_base_list_response_from_dict = KnowledgeBaseListResponse.from_dict(knowledge_base_list_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


