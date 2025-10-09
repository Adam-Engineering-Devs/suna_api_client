# JsonAnalysisResponse

Response from JSON analysis.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**requires_setup** | **bool** |  | 
**missing_regular_credentials** | **List[Dict[str, object]]** |  | [optional] [default to []]
**missing_custom_configs** | **List[Dict[str, object]]** |  | [optional] [default to []]
**agent_info** | **Dict[str, object]** |  | [optional] 

## Example

```python
from suna_api_client.models.json_analysis_response import JsonAnalysisResponse

# TODO update the JSON string below
json = "{}"
# create an instance of JsonAnalysisResponse from a JSON string
json_analysis_response_instance = JsonAnalysisResponse.from_json(json)
# print the JSON string representation of the object
print(JsonAnalysisResponse.to_json())

# convert the object into a dict
json_analysis_response_dict = json_analysis_response_instance.to_dict()
# create an instance of JsonAnalysisResponse from a dict
json_analysis_response_from_dict = JsonAnalysisResponse.from_dict(json_analysis_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


