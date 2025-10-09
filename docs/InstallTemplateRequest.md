# InstallTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**template_id** | **str** |  | 
**instance_name** | **str** |  | [optional] 
**custom_system_prompt** | **str** |  | [optional] 
**profile_mappings** | **Dict[str, str]** |  | [optional] 
**custom_mcp_configs** | **Dict[str, Dict[str, object]]** |  | [optional] 

## Example

```python
from suna_api_client.models.install_template_request import InstallTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of InstallTemplateRequest from a JSON string
install_template_request_instance = InstallTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(InstallTemplateRequest.to_json())

# convert the object into a dict
install_template_request_dict = install_template_request_instance.to_dict()
# create an instance of InstallTemplateRequest from a dict
install_template_request_from_dict = InstallTemplateRequest.from_dict(install_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


