# IntegrationStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**toolkit** | **str** |  | 
**auth_config_id** | **str** |  | 
**connected_account_id** | **str** |  | 
**mcp_server_id** | **str** |  | 
**final_mcp_url** | **str** |  | 
**profile_id** | **str** |  | [optional] 
**redirect_url** | **str** |  | [optional] 

## Example

```python
from suna_api_client.models.integration_status_response import IntegrationStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IntegrationStatusResponse from a JSON string
integration_status_response_instance = IntegrationStatusResponse.from_json(json)
# print the JSON string representation of the object
print(IntegrationStatusResponse.to_json())

# convert the object into a dict
integration_status_response_dict = integration_status_response_instance.to_dict()
# create an instance of IntegrationStatusResponse from a dict
integration_status_response_from_dict = IntegrationStatusResponse.from_dict(integration_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


