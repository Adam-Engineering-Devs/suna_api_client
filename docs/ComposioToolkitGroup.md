# ComposioToolkitGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**toolkit_slug** | **str** |  | 
**toolkit_name** | **str** |  | 
**icon_url** | **str** |  | [optional] 
**profiles** | [**List[ComposioProfileSummary]**](ComposioProfileSummary.md) |  | 

## Example

```python
from suna_api_client.models.composio_toolkit_group import ComposioToolkitGroup

# TODO update the JSON string below
json = "{}"
# create an instance of ComposioToolkitGroup from a JSON string
composio_toolkit_group_instance = ComposioToolkitGroup.from_json(json)
# print the JSON string representation of the object
print(ComposioToolkitGroup.to_json())

# convert the object into a dict
composio_toolkit_group_dict = composio_toolkit_group_instance.to_dict()
# create an instance of ComposioToolkitGroup from a dict
composio_toolkit_group_from_dict = ComposioToolkitGroup.from_dict(composio_toolkit_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


