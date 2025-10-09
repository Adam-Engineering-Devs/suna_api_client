# TrialStartRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success_url** | **str** |  | 
**cancel_url** | **str** |  | 

## Example

```python
from suna_api_client.models.trial_start_request import TrialStartRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TrialStartRequest from a JSON string
trial_start_request_instance = TrialStartRequest.from_json(json)
# print the JSON string representation of the object
print(TrialStartRequest.to_json())

# convert the object into a dict
trial_start_request_dict = trial_start_request_instance.to_dict()
# create an instance of TrialStartRequest from a dict
trial_start_request_from_dict = TrialStartRequest.from_dict(trial_start_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


