# CoreComposioIntegrationApiProfileResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profile_id** | **str** |  | 
**profile_name** | **str** |  | 
**display_name** | **str** |  | 
**toolkit_slug** | **str** |  | 
**toolkit_name** | **str** |  | 
**mcp_url** | **str** |  | 
**redirect_url** | **str** |  | [optional] 
**connected_account_id** | **str** |  | [optional] 
**is_connected** | **bool** |  | 
**is_default** | **bool** |  | 
**created_at** | **str** |  | 

## Example

```python
from suna_api_client.models.core_composio_integration_api_profile_response import CoreComposioIntegrationApiProfileResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CoreComposioIntegrationApiProfileResponse from a JSON string
core_composio_integration_api_profile_response_instance = CoreComposioIntegrationApiProfileResponse.from_json(json)
# print the JSON string representation of the object
print(CoreComposioIntegrationApiProfileResponse.to_json())

# convert the object into a dict
core_composio_integration_api_profile_response_dict = core_composio_integration_api_profile_response_instance.to_dict()
# create an instance of CoreComposioIntegrationApiProfileResponse from a dict
core_composio_integration_api_profile_response_from_dict = CoreComposioIntegrationApiProfileResponse.from_dict(core_composio_integration_api_profile_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


