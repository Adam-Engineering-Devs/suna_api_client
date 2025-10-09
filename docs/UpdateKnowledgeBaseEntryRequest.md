# UpdateKnowledgeBaseEntryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**content** | **str** |  | [optional] 
**usage_context** | **str** |  | [optional] 
**is_active** | **bool** |  | [optional] 

## Example

```python
from suna_api_client.models.update_knowledge_base_entry_request import UpdateKnowledgeBaseEntryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateKnowledgeBaseEntryRequest from a JSON string
update_knowledge_base_entry_request_instance = UpdateKnowledgeBaseEntryRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateKnowledgeBaseEntryRequest.to_json())

# convert the object into a dict
update_knowledge_base_entry_request_dict = update_knowledge_base_entry_request_instance.to_dict()
# create an instance of UpdateKnowledgeBaseEntryRequest from a dict
update_knowledge_base_entry_request_from_dict = UpdateKnowledgeBaseEntryRequest.from_dict(update_knowledge_base_entry_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


