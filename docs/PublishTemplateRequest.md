# PublishTemplateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tags** | **List[str]** |  | [optional] 

## Example

```python
from suna_api_client.models.publish_template_request import PublishTemplateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PublishTemplateRequest from a JSON string
publish_template_request_instance = PublishTemplateRequest.from_json(json)
# print the JSON string representation of the object
print(PublishTemplateRequest.to_json())

# convert the object into a dict
publish_template_request_dict = publish_template_request_instance.to_dict()
# create an instance of PublishTemplateRequest from a dict
publish_template_request_from_dict = PublishTemplateRequest.from_dict(publish_template_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


