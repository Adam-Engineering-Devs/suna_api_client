# CustomMCPDiscoverRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | 
**config** | **Dict[str, object]** |  | 

## Example

```python
from suna_api_client.models.custom_mcp_discover_request import CustomMCPDiscoverRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CustomMCPDiscoverRequest from a JSON string
custom_mcp_discover_request_instance = CustomMCPDiscoverRequest.from_json(json)
# print the JSON string representation of the object
print(CustomMCPDiscoverRequest.to_json())

# convert the object into a dict
custom_mcp_discover_request_dict = custom_mcp_discover_request_instance.to_dict()
# create an instance of CustomMCPDiscoverRequest from a dict
custom_mcp_discover_request_from_dict = CustomMCPDiscoverRequest.from_dict(custom_mcp_discover_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


