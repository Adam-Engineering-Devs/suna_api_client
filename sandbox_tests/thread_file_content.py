import suna_api_client
from suna_api_client.rest import ApiException
from suna_api_client.custom import get_sandbox_file_content
import json


def test_get_sandbox_file_content(sandbox_id, file_path, api_key="pk_TxQNMYBqwVEdi8i0LEDzM83jyZwQQe2L:sk_2bhxOJfPomUwalnTChj01CD3rKzDuT19"):
    """Test function to get file content from a sandbox"""
    print(f"--- Testing Get Sandbox File Content for Sandbox: {sandbox_id}, Path: {file_path} ---")
    
    # Setup configuration and API client
    configuration = suna_api_client.Configuration(
        host="http://localhost:8000"
    )
    
    with suna_api_client.ApiClient(
        configuration,
        header_name="x-api-key",
        header_value=api_key
    ) as api_client:
        
        try:
            # Use the custom function to get file content
            print(f"Fetching file content using custom get_sandbox_file_content function...")
            
            content = get_sandbox_file_content(
                api_client=api_client,
                sandbox_id=sandbox_id,
                path=file_path
            )
            
            print(f"Successfully retrieved file content!")
            print(f"Content type: {type(content)}")
            print(f"Content length: {len(content)} bytes")
            
            # Try to decode as UTF-8 text if it's a text file
            try:
                text_content = content.decode('utf-8')
                print(f"\n=== File Content (as text) ===")
                print(text_content)
            except UnicodeDecodeError:
                print(f"\n=== File Content (binary) ===")
                print(f"Binary content (first 100 bytes): {content[:100]}")
                print("Note: This appears to be a binary file and cannot be displayed as text.")
            
            return content
                
        except Exception as e:
            print(f"Exception when getting file content: {e}")
            import traceback
            traceback.print_exc()
            return None


def test_get_sandbox_file_content_with_thread(thread_id, file_path, api_key="pk_TxQNMYBqwVEdi8i0LEDzM83jyZwQQe2L:sk_2bhxOJfPomUwalnTChj01CD3rKzDuT19"):
    """Test function to get file content using thread ID to find sandbox"""
    print(f"--- Testing Get Sandbox File Content via Thread: {thread_id}, Path: {file_path} ---")
    
    # Setup configuration and API client
    configuration = suna_api_client.Configuration(
        host="http://localhost:8000"
    )
    
    with suna_api_client.ApiClient(
        configuration,
        header_name="x-api-key",
        header_value=api_key
    ) as api_client:
        
        # Use DefaultApi for thread info
        default_api = suna_api_client.DefaultApi(api_client)
        
        try:
            print(f"Getting thread info for thread_id: {thread_id}")
            
            # Step 1: Get thread info to extract sandbox ID
            thread_response = default_api.get_thread_api_threads_thread_id_get(thread_id=thread_id)
            
            # Step 2: Extract sandbox ID
            sandbox_id = thread_response["project"]["sandbox"]["id"]
            
            if not sandbox_id:
                print("No sandbox ID found in thread response!")
                return None
            
            print(f"Found sandbox ID: {sandbox_id}")
            
            # Step 3: Get file content using the custom function
            content = get_sandbox_file_content(
                api_client=api_client,
                sandbox_id=sandbox_id,
                path=file_path
            )
            
            print(f"Successfully retrieved file content!")
            print(f"Content type: {type(content)}")
            print(f"Content length: {len(content)} bytes")
            
            # Try to decode as UTF-8 text if it's a text file
            try:
                text_content = content.decode('utf-8')
                print(f"\n=== File Content (as text) ===")
                print(text_content)
            except UnicodeDecodeError:
                print(f"\n=== File Content (binary) ===")
                print(f"Binary content (first 100 bytes): {content[:100]}")
                print("Note: This appears to be a binary file and cannot be displayed as text.")
            
            return content
                
        except ApiException as e:
            print(f"API Exception: {e}")
            print(f"Status: {e.status}")
            print(f"Reason: {e.reason}")
            print(f"Body: {e.body}")
            return None
        except Exception as e:
            print(f"Exception when getting file content: {e}")
            import traceback
            traceback.print_exc()
            return None


def test_file_content_error_handling(sandbox_id, invalid_path, api_key="pk_TxQNMYBqwVEdi8i0LEDzM83jyZwQQe2L:sk_2bhxOJfPomUwalnTChj01CD3rKzDuT19"):
    """Test error handling for invalid file paths"""
    print(f"--- Testing Error Handling for Invalid Path: {invalid_path} ---")
    
    # Setup configuration and API client
    configuration = suna_api_client.Configuration(
        host="http://localhost:8000"
    )
    
    with suna_api_client.ApiClient(
        configuration,
        header_name="x-api-key",
        header_value=api_key
    ) as api_client:
        
        try:
            # Try to get content from invalid path
            content = get_sandbox_file_content(
                api_client=api_client,
                sandbox_id=sandbox_id,
                path=invalid_path
            )
            
            print(f"Unexpectedly succeeded with invalid path!")
            return content
                
        except Exception as e:
            print(f"Expected exception for invalid path: {e}")
            print(f"Exception type: {type(e)}")
            return None


if __name__ == "__main__":
    # Test with a known thread ID and file path
    thread_id = "df6ea70c-02f5-459d-9bdd-8778cafb329b"
    test_file_path = "/script.js"  # Adjust this path as needed
    
    print("=== Testing get_sandbox_file_content function ===\n")
    
    # Test 1: Get file content via thread ID
    print("Test 1: Get file content via thread ID")
    content1 = test_get_sandbox_file_content_with_thread(thread_id, test_file_path)
    
    print("\n" + "="*60 + "\n")
    
    # Test 2: Test error handling with invalid path
    if content1 is not None:
        # Extract sandbox_id from the successful call for error testing
        configuration = suna_api_client.Configuration(host="http://localhost:8000")
        with suna_api_client.ApiClient(
            configuration,
            header_name="x-api-key",
            header_value="pk_TxQNMYBqwVEdi8i0LEDzM83jyZwQQe2L:sk_2bhxOJfPomUwalnTChj01CD3rKzDuT19"
        ) as api_client:
            default_api = suna_api_client.DefaultApi(api_client)
            try:
                thread_response = default_api.get_thread_api_threads_thread_id_get(thread_id=thread_id)
                sandbox_id = thread_response["project"]["sandbox"]["id"]
                
                print("Test 2: Error handling with invalid path")
                test_file_content_error_handling(sandbox_id, "/nonexistent/file.txt")
            except Exception as e:
                print(f"Could not get sandbox_id for error testing: {e}")
    
    print("\n=== Test completed ===")
