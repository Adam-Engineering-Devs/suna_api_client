# JsonAnalysisRequest

Request to analyze JSON for import requirements.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_data** | **Dict[str, object]** |  | 

## Example

```python
from suna_api_client.models.json_analysis_request import JsonAnalysisRequest

# TODO update the JSON string below
json = "{}"
# create an instance of JsonAnalysisRequest from a JSON string
json_analysis_request_instance = JsonAnalysisRequest.from_json(json)
# print the JSON string representation of the object
print(JsonAnalysisRequest.to_json())

# convert the object into a dict
json_analysis_request_dict = json_analysis_request_instance.to_dict()
# create an instance of JsonAnalysisRequest from a dict
json_analysis_request_from_dict = JsonAnalysisRequest.from_dict(json_analysis_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


