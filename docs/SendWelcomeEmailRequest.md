# SendWelcomeEmailRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**name** | **str** |  | [optional] 

## Example

```python
from suna_api_client.models.send_welcome_email_request import SendWelcomeEmailRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SendWelcomeEmailRequest from a JSON string
send_welcome_email_request_instance = SendWelcomeEmailRequest.from_json(json)
# print the JSON string representation of the object
print(SendWelcomeEmailRequest.to_json())

# convert the object into a dict
send_welcome_email_request_dict = send_welcome_email_request_instance.to_dict()
# create an instance of SendWelcomeEmailRequest from a dict
send_welcome_email_request_from_dict = SendWelcomeEmailRequest.from_dict(send_welcome_email_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


