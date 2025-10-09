# ConnectionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**connections** | **List[Dict[str, object]]** |  | 
**count** | **int** |  | 
**error** | **str** |  | [optional] 

## Example

```python
from suna_api_client.models.connection_response import ConnectionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectionResponse from a JSON string
connection_response_instance = ConnectionResponse.from_json(json)
# print the JSON string representation of the object
print(ConnectionResponse.to_json())

# convert the object into a dict
connection_response_dict = connection_response_instance.to_dict()
# create an instance of ConnectionResponse from a dict
connection_response_from_dict = ConnectionResponse.from_dict(connection_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


