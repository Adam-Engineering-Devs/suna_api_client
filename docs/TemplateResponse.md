# TemplateResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **str** |  | 
**creator_id** | **str** |  | 
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**system_prompt** | **str** |  | 
**mcp_requirements** | **List[Dict[str, object]]** |  | 
**agentpress_tools** | **Dict[str, object]** |  | 
**tags** | **List[str]** |  | 
**is_public** | **bool** |  | 
**is_kortix_team** | **bool** |  | [optional] 
**marketplace_published_at** | **str** |  | [optional] 
**download_count** | **int** |  | 
**created_at** | **str** |  | 
**updated_at** | **str** |  | 
**profile_image_url** | **str** |  | [optional] 
**icon_name** | **str** |  | [optional] 
**icon_color** | **str** |  | [optional] 
**icon_background** | **str** |  | [optional] 
**metadata** | **Dict[str, object]** |  | 
**creator_name** | **str** |  | [optional] 

## Example

```python
from suna_api_client.models.template_response import TemplateResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplateResponse from a JSON string
template_response_instance = TemplateResponse.from_json(json)
# print the JSON string representation of the object
print(TemplateResponse.to_json())

# convert the object into a dict
template_response_dict = template_response_instance.to_dict()
# create an instance of TemplateResponse from a dict
template_response_from_dict = TemplateResponse.from_dict(template_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


