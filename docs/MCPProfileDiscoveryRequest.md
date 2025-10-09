# MCPProfileDiscoveryRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**external_user_id** | **str** |  | 
**app_slug** | **str** |  | [optional] 
**oauth_app_id** | **str** |  | [optional] 

## Example

```python
from suna_api_client.models.mcp_profile_discovery_request import MCPProfileDiscoveryRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MCPProfileDiscoveryRequest from a JSON string
mcp_profile_discovery_request_instance = MCPProfileDiscoveryRequest.from_json(json)
# print the JSON string representation of the object
print(MCPProfileDiscoveryRequest.to_json())

# convert the object into a dict
mcp_profile_discovery_request_dict = mcp_profile_discovery_request_instance.to_dict()
# create an instance of MCPProfileDiscoveryRequest from a dict
mcp_profile_discovery_request_from_dict = MCPProfileDiscoveryRequest.from_dict(mcp_profile_discovery_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


