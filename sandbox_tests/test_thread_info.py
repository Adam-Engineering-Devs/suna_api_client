import suna_api_client
from suna_api_client.rest import ApiException
import json


def test_get_thread_info(thread_id, api_key="pk_TxQNMYBqwVEdi8i0LEDzM83jyZwQQe2L:sk_2bhxOJfPomUwalnTChj01CD3rKzDuT19"):
    """Test function to fetch thread information by thread_id"""
    print(f"--- Testing Get Thread Info for Thread: {thread_id} ---")
    
    # Setup configuration and API client
    configuration = suna_api_client.Configuration(
        host="http://localhost:8000"
    )
    
    with suna_api_client.ApiClient(
        configuration,
        header_name="x-api-key",
        header_value=api_key
    ) as api_client:
        
        api_instance = suna_api_client.DefaultApi(api_client)
        
        try:
            # Call the get thread endpoint
            thread_response = api_instance.get_thread_api_threads_thread_id_get(
                thread_id=thread_id
            )
            
            print(f"Thread response type: {type(thread_response)}")
            print(f"Thread response: {thread_response}")
            
            # Try to parse and display the response data
            if hasattr(thread_response, '__dict__'):
                print("\nThread Information:")
                for key, value in thread_response.__dict__.items():
                    if isinstance(value, (dict, list)):
                        print(f"  {key}: {json.dumps(value, indent=4, default=str)}")
                    else:
                        print(f"  {key}: {value}")
            else:
                print(f"Thread data: {thread_response}")
                
            return thread_response
                
        except ApiException as e:
            print(f"Exception when calling get_thread: {e}")
            if hasattr(e, 'body') and e.body:
                try:
                    error_data = json.loads(e.body)
                    print(f"Error details: {json.dumps(error_data, indent=2)}")
                except:
                    print(f"Error body: {e.body}")
            return None
        except Exception as e:
            print(f"Unexpected error in test_get_thread_info: {e}")
            return None


def test_get_thread_info_with_requests(thread_id, api_key="pk_TxQNMYBqwVEdi8i0LEDzM83jyZwQQe2L:sk_2bhxOJfPomUwalnTChj01CD3rKzDuT19"):
    """Alternative test function using direct HTTP requests"""
    print(f"--- Testing Get Thread Info (Direct HTTP) for Thread: {thread_id} ---")
    
    import requests
    
    url = f"http://localhost:8000/api/threads/{thread_id}"
    headers = {
        "x-api-key": api_key,
        "Accept": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        thread_data = response.json()
        print(f"Thread data: {json.dumps(thread_data, indent=2, default=str)}")
        
        return thread_data
        
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error when calling get thread: {e}")
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.text}")
        return None
        
    except requests.exceptions.RequestException as e:
        print(f"Request Exception when calling get thread: {e}")
        return None
        
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        print(f"Response content: {response.text}")
        return None
        
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


if __name__ == "__main__":
    # Test with a sample thread_id (you can replace this with an actual thread_id)
    thread_id = "df6ea70c-02f5-459d-9bdd-8778cafb329b"
    
    print("=" * 60)
    print("Testing with Suna API Client")
    print("=" * 60)
    result1 = test_get_thread_info(thread_id)
    
    print("\n" + "=" * 60)
    print("Testing with Direct HTTP Requests")
    print("=" * 60)
    result2 = test_get_thread_info_with_requests(thread_id)
    
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    print(f"API Client test result: {'SUCCESS' if result1 is not None else 'FAILED'}")
    print(f"Direct HTTP test result: {'SUCCESS' if result2 is not None else 'FAILED'}")
