# EmailResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**message** | **str** |  | 

## Example

```python
from suna_api_client.models.email_response import EmailResponse

# TODO update the JSON string below
json = "{}"
# create an instance of EmailResponse from a JSON string
email_response_instance = EmailResponse.from_json(json)
# print the JSON string representation of the object
print(EmailResponse.to_json())

# convert the object into a dict
email_response_dict = email_response_instance.to_dict()
# create an instance of EmailResponse from a dict
email_response_from_dict = EmailResponse.from_dict(email_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


