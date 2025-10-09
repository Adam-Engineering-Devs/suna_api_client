# ProcessingJobResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **str** |  | 
**job_type** | **str** |  | 
**status** | **str** |  | 
**source_info** | **Dict[str, object]** |  | 
**result_info** | **Dict[str, object]** |  | 
**entries_created** | **int** |  | 
**total_files** | **int** |  | 
**created_at** | **str** |  | 
**completed_at** | **str** |  | 
**error_message** | **str** |  | 

## Example

```python
from suna_api_client.models.processing_job_response import ProcessingJobResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ProcessingJobResponse from a JSON string
processing_job_response_instance = ProcessingJobResponse.from_json(json)
# print the JSON string representation of the object
print(ProcessingJobResponse.to_json())

# convert the object into a dict
processing_job_response_dict = processing_job_response_instance.to_dict()
# create an instance of ProcessingJobResponse from a dict
processing_job_response_from_dict = ProcessingJobResponse.from_dict(processing_job_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


