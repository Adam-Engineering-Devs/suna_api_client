# ComposioCredentialsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**toolkits** | [**List[ComposioToolkitGroup]**](ComposioToolkitGroup.md) |  | 
**total_profiles** | **int** |  | 

## Example

```python
from suna_api_client.models.composio_credentials_response import ComposioCredentialsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ComposioCredentialsResponse from a JSON string
composio_credentials_response_instance = ComposioCredentialsResponse.from_json(json)
# print the JSON string representation of the object
print(ComposioCredentialsResponse.to_json())

# convert the object into a dict
composio_credentials_response_dict = composio_credentials_response_instance.to_dict()
# create an instance of ComposioCredentialsResponse from a dict
composio_credentials_response_from_dict = ComposioCredentialsResponse.from_dict(composio_credentials_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


