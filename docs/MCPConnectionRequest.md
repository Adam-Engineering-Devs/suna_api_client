# MCPConnectionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_slug** | **str** |  | 
**oauth_app_id** | **str** |  | [optional] 

## Example

```python
from suna_api_client.models.mcp_connection_request import MCPConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of MCPConnectionRequest from a JSON string
mcp_connection_request_instance = MCPConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(MCPConnectionRequest.to_json())

# convert the object into a dict
mcp_connection_request_dict = mcp_connection_request_instance.to_dict()
# create an instance of MCPConnectionRequest from a dict
mcp_connection_request_from_dict = MCPConnectionRequest.from_dict(mcp_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


