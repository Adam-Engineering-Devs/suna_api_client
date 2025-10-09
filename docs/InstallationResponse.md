# InstallationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** |  | 
**instance_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**missing_regular_credentials** | **List[Dict[str, object]]** |  | [optional] [default to []]
**missing_custom_configs** | **List[Dict[str, object]]** |  | [optional] [default to []]
**template_info** | **Dict[str, object]** |  | [optional] 

## Example

```python
from suna_api_client.models.installation_response import InstallationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of InstallationResponse from a JSON string
installation_response_instance = InstallationResponse.from_json(json)
# print the JSON string representation of the object
print(InstallationResponse.to_json())

# convert the object into a dict
installation_response_dict = installation_response_instance.to_dict()
# create an instance of InstallationResponse from a dict
installation_response_from_dict = InstallationResponse.from_dict(installation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


