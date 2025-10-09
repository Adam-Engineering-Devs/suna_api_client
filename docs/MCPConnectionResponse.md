# MCPConnectionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**mcp_config** | **Dict[str, object]** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from suna_api_client.models.mcp_connection_response import MCPConnectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MCPConnectionResponse from a JSON string
mcp_connection_response_instance = MCPConnectionResponse.from_json(json)
# print the JSON string representation of the object
print(MCPConnectionResponse.to_json())

# convert the object into a dict
mcp_connection_response_dict = mcp_connection_response_instance.to_dict()
# create an instance of MCPConnectionResponse from a dict
mcp_connection_response_from_dict = MCPConnectionResponse.from_dict(mcp_connection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


