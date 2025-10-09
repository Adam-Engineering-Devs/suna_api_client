# AdvancedSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_contains** | **str** |  | [optional] 
**tier_in** | **List[str]** |  | [optional] 
**subscription_status_in** | **List[str]** |  | [optional] 
**trial_status_in** | **List[str]** |  | [optional] 
**balance_min** | **float** |  | [optional] 
**balance_max** | **float** |  | [optional] 
**created_after** | **datetime** |  | [optional] 
**created_before** | **datetime** |  | [optional] 
**has_activity_since** | **datetime** |  | [optional] 
**sort_by** | **str** |  | [optional] [default to 'created_at']
**sort_order** | **str** |  | [optional] [default to 'desc']

## Example

```python
from suna_api_client.models.advanced_search_request import AdvancedSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AdvancedSearchRequest from a JSON string
advanced_search_request_instance = AdvancedSearchRequest.from_json(json)
# print the JSON string representation of the object
print(AdvancedSearchRequest.to_json())

# convert the object into a dict
advanced_search_request_dict = advanced_search_request_instance.to_dict()
# create an instance of AdvancedSearchRequest from a dict
advanced_search_request_from_dict = AdvancedSearchRequest.from_dict(advanced_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


