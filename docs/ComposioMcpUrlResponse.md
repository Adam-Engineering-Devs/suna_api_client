# ComposioMcpUrlResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**mcp_url** | **str** |  | 
**profile_name** | **str** |  | 
**toolkit_name** | **str** |  | 
**warning** | **str** |  | 

## Example

```python
from suna_api_client.models.composio_mcp_url_response import ComposioMcpUrlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ComposioMcpUrlResponse from a JSON string
composio_mcp_url_response_instance = ComposioMcpUrlResponse.from_json(json)
# print the JSON string representation of the object
print(ComposioMcpUrlResponse.to_json())

# convert the object into a dict
composio_mcp_url_response_dict = composio_mcp_url_response_instance.to_dict()
# create an instance of ComposioMcpUrlResponse from a dict
composio_mcp_url_response_from_dict = ComposioMcpUrlResponse.from_dict(composio_mcp_url_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


