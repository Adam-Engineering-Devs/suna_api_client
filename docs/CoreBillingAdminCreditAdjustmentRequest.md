# CoreBillingAdminCreditAdjustmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** |  | 
**amount** | [**Amount1**](Amount1.md) |  | 
**reason** | **str** |  | 
**is_expiring** | **bool** | Whether credits expire at end of billing cycle | [optional] [default to True]
**notify_user** | **bool** |  | [optional] [default to True]

## Example

```python
from suna_api_client.models.core_billing_admin_credit_adjustment_request import CoreBillingAdminCreditAdjustmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CoreBillingAdminCreditAdjustmentRequest from a JSON string
core_billing_admin_credit_adjustment_request_instance = CoreBillingAdminCreditAdjustmentRequest.from_json(json)
# print the JSON string representation of the object
print(CoreBillingAdminCreditAdjustmentRequest.to_json())

# convert the object into a dict
core_billing_admin_credit_adjustment_request_dict = core_billing_admin_credit_adjustment_request_instance.to_dict()
# create an instance of CoreBillingAdminCreditAdjustmentRequest from a dict
core_billing_admin_credit_adjustment_request_from_dict = CoreBillingAdminCreditAdjustmentRequest.from_dict(core_billing_admin_credit_adjustment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


