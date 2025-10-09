# CoreAdminUsersAdminCreditAdjustmentRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** |  | 
**amount** | **float** |  | 
**reason** | **str** |  | 

## Example

```python
from suna_api_client.models.core_admin_users_admin_credit_adjustment_request import CoreAdminUsersAdminCreditAdjustmentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CoreAdminUsersAdminCreditAdjustmentRequest from a JSON string
core_admin_users_admin_credit_adjustment_request_instance = CoreAdminUsersAdminCreditAdjustmentRequest.from_json(json)
# print the JSON string representation of the object
print(CoreAdminUsersAdminCreditAdjustmentRequest.to_json())

# convert the object into a dict
core_admin_users_admin_credit_adjustment_request_dict = core_admin_users_admin_credit_adjustment_request_instance.to_dict()
# create an instance of CoreAdminUsersAdminCreditAdjustmentRequest from a dict
core_admin_users_admin_credit_adjustment_request_from_dict = CoreAdminUsersAdminCreditAdjustmentRequest.from_dict(core_admin_users_admin_credit_adjustment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


