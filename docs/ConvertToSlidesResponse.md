# ConvertToSlidesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 
**pptx_url** | **str** |  | [optional] 
**google_slides_url** | **str** |  | [optional] 
**google_slides_file_id** | **str** |  | [optional] 
**is_api_enabled** | **bool** |  | [optional] 

## Example

```python
from suna_api_client.models.convert_to_slides_response import ConvertToSlidesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConvertToSlidesResponse from a JSON string
convert_to_slides_response_instance = ConvertToSlidesResponse.from_json(json)
# print the JSON string representation of the object
print(ConvertToSlidesResponse.to_json())

# convert the object into a dict
convert_to_slides_response_dict = convert_to_slides_response_instance.to_dict()
# create an instance of ConvertToSlidesResponse from a dict
convert_to_slides_response_from_dict = ConvertToSlidesResponse.from_dict(convert_to_slides_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


