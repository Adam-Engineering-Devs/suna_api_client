# PaginatedResponseDictStrAny


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **List[Dict[str, object]]** |  | 
**pagination** | [**PaginationMeta**](PaginationMeta.md) |  | 

## Example

```python
from suna_api_client.models.paginated_response_dict_str_any import PaginatedResponseDictStrAny

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedResponseDictStrAny from a JSON string
paginated_response_dict_str_any_instance = PaginatedResponseDictStrAny.from_json(json)
# print the JSON string representation of the object
print(PaginatedResponseDictStrAny.to_json())

# convert the object into a dict
paginated_response_dict_str_any_dict = paginated_response_dict_str_any_instance.to_dict()
# create an instance of PaginatedResponseDictStrAny from a dict
paginated_response_dict_str_any_from_dict = PaginatedResponseDictStrAny.from_dict(paginated_response_dict_str_any_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


