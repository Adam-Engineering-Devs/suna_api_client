# UpcomingRun


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trigger_id** | **str** |  | 
**trigger_name** | **str** |  | 
**trigger_type** | **str** |  | 
**next_run_time** | **str** |  | 
**next_run_time_local** | **str** |  | 
**timezone** | **str** |  | 
**cron_expression** | **str** |  | 
**execution_type** | **str** |  | 
**agent_prompt** | **str** |  | [optional] 
**workflow_id** | **str** |  | [optional] 
**is_active** | **bool** |  | 
**human_readable** | **str** |  | 

## Example

```python
from suna_api_client.models.upcoming_run import UpcomingRun

# TODO update the JSON string below
json = "{}"
# create an instance of UpcomingRun from a JSON string
upcoming_run_instance = UpcomingRun.from_json(json)
# print the JSON string representation of the object
print(UpcomingRun.to_json())

# convert the object into a dict
upcoming_run_dict = upcoming_run_instance.to_dict()
# create an instance of UpcomingRun from a dict
upcoming_run_from_dict = UpcomingRun.from_dict(upcoming_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


