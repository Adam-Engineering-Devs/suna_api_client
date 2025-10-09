# MarketplaceTemplatesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**templates** | [**List[TemplateResponse]**](TemplateResponse.md) |  | 
**pagination** | [**MarketplacePaginationInfo**](MarketplacePaginationInfo.md) |  | 

## Example

```python
from suna_api_client.models.marketplace_templates_response import MarketplaceTemplatesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of MarketplaceTemplatesResponse from a JSON string
marketplace_templates_response_instance = MarketplaceTemplatesResponse.from_json(json)
# print the JSON string representation of the object
print(MarketplaceTemplatesResponse.to_json())

# convert the object into a dict
marketplace_templates_response_dict = marketplace_templates_response_instance.to_dict()
# create an instance of MarketplaceTemplatesResponse from a dict
marketplace_templates_response_from_dict = MarketplaceTemplatesResponse.from_dict(marketplace_templates_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


