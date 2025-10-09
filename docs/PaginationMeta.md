# PaginationMeta


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_page** | **int** |  | 
**page_size** | **int** |  | 
**total_items** | **int** |  | 
**total_pages** | **int** |  | 
**has_next** | **bool** |  | 
**has_previous** | **bool** |  | 
**next_cursor** | **str** |  | [optional] 
**previous_cursor** | **str** |  | [optional] 

## Example

```python
from suna_api_client.models.pagination_meta import PaginationMeta

# TODO update the JSON string below
json = "{}"
# create an instance of PaginationMeta from a JSON string
pagination_meta_instance = PaginationMeta.from_json(json)
# print the JSON string representation of the object
print(PaginationMeta.to_json())

# convert the object into a dict
pagination_meta_dict = pagination_meta_instance.to_dict()
# create an instance of PaginationMeta from a dict
pagination_meta_from_dict = PaginationMeta.from_dict(pagination_meta_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


