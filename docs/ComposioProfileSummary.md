# ComposioProfileSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_id** | **str** |  | 
**profile_name** | **str** |  | 
**display_name** | **str** |  | 
**toolkit_slug** | **str** |  | 
**toolkit_name** | **str** |  | 
**is_connected** | **bool** |  | 
**is_default** | **bool** |  | 
**created_at** | **str** |  | 
**has_mcp_url** | **bool** |  | 

## Example

```python
from suna_api_client.models.composio_profile_summary import ComposioProfileSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ComposioProfileSummary from a JSON string
composio_profile_summary_instance = ComposioProfileSummary.from_json(json)
# print the JSON string representation of the object
print(ComposioProfileSummary.to_json())

# convert the object into a dict
composio_profile_summary_dict = composio_profile_summary_instance.to_dict()
# create an instance of ComposioProfileSummary from a dict
composio_profile_summary_from_dict = ComposioProfileSummary.from_dict(composio_profile_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


