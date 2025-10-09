# PurchaseCreditsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | [**Amount**](Amount.md) |  | 
**success_url** | **str** |  | 
**cancel_url** | **str** |  | 

## Example

```python
from suna_api_client.models.purchase_credits_request import PurchaseCreditsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PurchaseCreditsRequest from a JSON string
purchase_credits_request_instance = PurchaseCreditsRequest.from_json(json)
# print the JSON string representation of the object
print(PurchaseCreditsRequest.to_json())

# convert the object into a dict
purchase_credits_request_dict = purchase_credits_request_instance.to_dict()
# create an instance of PurchaseCreditsRequest from a dict
purchase_credits_request_from_dict = PurchaseCreditsRequest.from_dict(purchase_credits_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


