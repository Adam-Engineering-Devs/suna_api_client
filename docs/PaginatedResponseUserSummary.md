# PaginatedResponseUserSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[UserSummary]**](UserSummary.md) |  | 
**pagination** | [**PaginationMeta**](PaginationMeta.md) |  | 

## Example

```python
from suna_api_client.models.paginated_response_user_summary import PaginatedResponseUserSummary

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponseUserSummary from a JSON string
paginated_response_user_summary_instance = PaginatedResponseUserSummary.from_json(json)
# print the JSON string representation of the object
print(PaginatedResponseUserSummary.to_json())

# convert the object into a dict
paginated_response_user_summary_dict = paginated_response_user_summary_instance.to_dict()
# create an instance of PaginatedResponseUserSummary from a dict
paginated_response_user_summary_from_dict = PaginatedResponseUserSummary.from_dict(paginated_response_user_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


