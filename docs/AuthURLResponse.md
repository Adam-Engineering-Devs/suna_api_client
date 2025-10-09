# AuthURLResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_url** | **str** |  | 
**message** | **str** |  | 

## Example

```python
from suna_api_client.models.auth_url_response import AuthURLResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AuthURLResponse from a JSON string
auth_url_response_instance = AuthURLResponse.from_json(json)
# print the JSON string representation of the object
print(AuthURLResponse.to_json())

# convert the object into a dict
auth_url_response_dict = auth_url_response_instance.to_dict()
# create an instance of AuthURLResponse from a dict
auth_url_response_from_dict = AuthURLResponse.from_dict(auth_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


