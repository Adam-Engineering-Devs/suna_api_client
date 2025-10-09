# IntegrateToolkitRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**toolkit_slug** | **str** |  | 
**profile_name** | **str** |  | [optional] 
**display_name** | **str** |  | [optional] 
**mcp_server_name** | **str** |  | [optional] 
**save_as_profile** | **bool** |  | [optional] [default to True]

## Example

```python
from suna_api_client.models.integrate_toolkit_request import IntegrateToolkitRequest

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrateToolkitRequest from a JSON string
integrate_toolkit_request_instance = IntegrateToolkitRequest.from_json(json)
# print the JSON string representation of the object
print(IntegrateToolkitRequest.to_json())

# convert the object into a dict
integrate_toolkit_request_dict = integrate_toolkit_request_instance.to_dict()
# create an instance of IntegrateToolkitRequest from a dict
integrate_toolkit_request_from_dict = IntegrateToolkitRequest.from_dict(integrate_toolkit_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


