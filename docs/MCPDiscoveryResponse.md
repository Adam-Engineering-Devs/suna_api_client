# MCPDiscoveryResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**mcp_servers** | **List[Dict[str, object]]** |  | 
**count** | **int** |  | 
**error** | **str** |  | [optional] 

## Example

```python
from suna_api_client.models.mcp_discovery_response import MCPDiscoveryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MCPDiscoveryResponse from a JSON string
mcp_discovery_response_instance = MCPDiscoveryResponse.from_json(json)
# print the JSON string representation of the object
print(MCPDiscoveryResponse.to_json())

# convert the object into a dict
mcp_discovery_response_dict = mcp_discovery_response_instance.to_dict()
# create an instance of MCPDiscoveryResponse from a dict
mcp_discovery_response_from_dict = MCPDiscoveryResponse.from_dict(mcp_discovery_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


