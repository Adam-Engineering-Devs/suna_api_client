# ConvertToSlidesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**presentation_path** | **str** | Path to the presentation in sandbox (e.g., /workspace/presentations/my-pres) | 
**sandbox_url** | **str** | Sandbox URL to fetch the PPTX from | 

## Example

```python
from suna_api_client.models.convert_to_slides_request import ConvertToSlidesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertToSlidesRequest from a JSON string
convert_to_slides_request_instance = ConvertToSlidesRequest.from_json(json)
# print the JSON string representation of the object
print(ConvertToSlidesRequest.to_json())

# convert the object into a dict
convert_to_slides_request_dict = convert_to_slides_request_instance.to_dict()
# create an instance of ConvertToSlidesRequest from a dict
convert_to_slides_request_from_dict = ConvertToSlidesRequest.from_dict(convert_to_slides_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


