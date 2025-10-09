import suna_api_client
from suna_api_client.rest import ApiException


def test_list_messages(thread_id, api_key="pk_TxQNMYBqwVEdi8i0LEDzM83jyZwQQe2L:sk_2bhxOJfPomUwalnTChj01CD3rKzDuT19"):
    """Test function to list messages from a thread"""
    print(f"--- Testing List Messages for Thread: {thread_id} ---")
    
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
            # Call the get thread messages endpoint
            messages_response = api_instance.get_thread_messages_api_threads_thread_id_messages_get(
                thread_id=thread_id,
                order="desc"  # Get newest messages first
            )
            
            print(f"Messages response type: {type(messages_response)}")
            print(f"Messages response: {messages_response}")
            
            # If the response is a list or has a data attribute, try to process it
            if hasattr(messages_response, 'data'):
                messages_data = messages_response.data
            elif isinstance(messages_response, list):
                messages_data = messages_response
            else:
                messages_data = messages_response
                
            print(f"Number of messages: {len(messages_data) if hasattr(messages_data, '__len__') else 'Unknown'}")
            
            # Display messages if available
            if hasattr(messages_data, '__iter__') and not isinstance(messages_data, str):
                for i, message in enumerate(messages_data):
                    print(f"\nMessage {i + 1}:")
                    if hasattr(message, '__dict__'):
                        for key, value in message.__dict__.items():
                            print(f"  {key}: {value}")
                    else:
                        print(f"  {message}")
            else:
                print(f"Messages data: {messages_data}")
                
        except ApiException as e:
            print(f"Exception when calling get_thread_messages: {e}")
        except Exception as e:
            print(f"Unexpected error in test_list_messages: {e}")


if __name__ == "__main__":
    
    thread_id = "5a9df3b9-eb92-4b5b-bb64-f18c6ebb075b"
    test_list_messages(thread_id)