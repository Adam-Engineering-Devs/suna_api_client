# UserSearchRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**account_id** | **str** |  | [optional] 

## Example

```python
from suna_api_client.models.user_search_request import UserSearchRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserSearchRequest from a JSON string
user_search_request_instance = UserSearchRequest.from_json(json)
# print the JSON string representation of the object
print(UserSearchRequest.to_json())

# convert the object into a dict
user_search_request_dict = user_search_request_instance.to_dict()
# create an instance of UserSearchRequest from a dict
user_search_request_from_dict = UserSearchRequest.from_dict(user_search_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


