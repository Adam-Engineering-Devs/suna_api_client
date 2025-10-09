# ToolsListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**toolkit_slug** | **str** |  | 
**limit** | **int** |  | [optional] [default to 50]
**cursor** | **str** |  | [optional] 

## Example

```python
from suna_api_client.models.tools_list_request import ToolsListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ToolsListRequest from a JSON string
tools_list_request_instance = ToolsListRequest.from_json(json)
# print the JSON string representation of the object
print(ToolsListRequest.to_json())

# convert the object into a dict
tools_list_request_dict = tools_list_request_instance.to_dict()
# create an instance of ToolsListRequest from a dict
tools_list_request_from_dict = ToolsListRequest.from_dict(tools_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


