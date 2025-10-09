# UserActivityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**days** | **int** |  | [optional] [default to 30]

## Example

```python
from suna_api_client.models.user_activity_request import UserActivityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UserActivityRequest from a JSON string
user_activity_request_instance = UserActivityRequest.from_json(json)
# print the JSON string representation of the object
print(UserActivityRequest.to_json())

# convert the object into a dict
user_activity_request_dict = user_activity_request_instance.to_dict()
# create an instance of UserActivityRequest from a dict
user_activity_request_from_dict = UserActivityRequest.from_dict(user_activity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


