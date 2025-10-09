# MCPDiscoveryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_slug** | **str** |  | [optional] 
**oauth_app_id** | **str** |  | [optional] 

## Example

```python
from suna_api_client.models.mcp_discovery_request import MCPDiscoveryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MCPDiscoveryRequest from a JSON string
mcp_discovery_request_instance = MCPDiscoveryRequest.from_json(json)
# print the JSON string representation of the object
print(MCPDiscoveryRequest.to_json())

# convert the object into a dict
mcp_discovery_request_dict = mcp_discovery_request_instance.to_dict()
# create an instance of MCPDiscoveryRequest from a dict
mcp_discovery_request_from_dict = MCPDiscoveryRequest.from_dict(mcp_discovery_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


