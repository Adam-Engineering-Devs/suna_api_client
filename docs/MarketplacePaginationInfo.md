# MarketplacePaginationInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_page** | **int** |  | 
**page_size** | **int** |  | 
**total_items** | **int** |  | 
**total_pages** | **int** |  | 
**has_next** | **bool** |  | 
**has_previous** | **bool** |  | 

## Example

```python
from suna_api_client.models.marketplace_pagination_info import MarketplacePaginationInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplacePaginationInfo from a JSON string
marketplace_pagination_info_instance = MarketplacePaginationInfo.from_json(json)
# print the JSON string representation of the object
print(MarketplacePaginationInfo.to_json())

# convert the object into a dict
marketplace_pagination_info_dict = marketplace_pagination_info_instance.to_dict()
# create an instance of MarketplacePaginationInfo from a dict
marketplace_pagination_info_from_dict = MarketplacePaginationInfo.from_dict(marketplace_pagination_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


