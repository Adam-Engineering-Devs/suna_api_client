# UpcomingRunsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**upcoming_runs** | [**List[UpcomingRun]**](UpcomingRun.md) |  | 
**total_count** | **int** |  | 

## Example

```python
from suna_api_client.models.upcoming_runs_response import UpcomingRunsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpcomingRunsResponse from a JSON string
upcoming_runs_response_instance = UpcomingRunsResponse.from_json(json)
# print the JSON string representation of the object
print(UpcomingRunsResponse.to_json())

# convert the object into a dict
upcoming_runs_response_dict = upcoming_runs_response_instance.to_dict()
# create an instance of UpcomingRunsResponse from a dict
upcoming_runs_response_from_dict = UpcomingRunsResponse.from_dict(upcoming_runs_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


