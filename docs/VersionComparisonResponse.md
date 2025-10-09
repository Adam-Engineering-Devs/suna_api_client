# VersionComparisonResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version1** | [**VersionResponse**](VersionResponse.md) |  | 
**version2** | [**VersionResponse**](VersionResponse.md) |  | 
**differences** | **List[Dict[str, object]]** |  | 

## Example

```python
from suna_api_client.models.version_comparison_response import VersionComparisonResponse

# TODO update the JSON string below
json = "{}"
# create an instance of VersionComparisonResponse from a JSON string
version_comparison_response_instance = VersionComparisonResponse.from_json(json)
# print the JSON string representation of the object
print(VersionComparisonResponse.to_json())

# convert the object into a dict
version_comparison_response_dict = version_comparison_response_instance.to_dict()
# create an instance of VersionComparisonResponse from a dict
version_comparison_response_from_dict = VersionComparisonResponse.from_dict(version_comparison_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


