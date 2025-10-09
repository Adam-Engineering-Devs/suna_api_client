# CreateKnowledgeBaseEntryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**content** | **str** |  | 
**usage_context** | **str** |  | [optional] [default to 'always']

## Example

```python
from suna_api_client.models.create_knowledge_base_entry_request import CreateKnowledgeBaseEntryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateKnowledgeBaseEntryRequest from a JSON string
create_knowledge_base_entry_request_instance = CreateKnowledgeBaseEntryRequest.from_json(json)
# print the JSON string representation of the object
print(CreateKnowledgeBaseEntryRequest.to_json())

# convert the object into a dict
create_knowledge_base_entry_request_dict = create_knowledge_base_entry_request_instance.to_dict()
# create an instance of CreateKnowledgeBaseEntryRequest from a dict
create_knowledge_base_entry_request_from_dict = CreateKnowledgeBaseEntryRequest.from_dict(create_knowledge_base_entry_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


