import suna_api_client
from suna_api_client.rest import ApiException
import json
import requests


def test_list_sandbox_files(sandbox_id, path="/", api_key="pk_TxQNMYBqwVEdi8i0LEDzM83jyZwQQe2L:sk_2bhxOJfPomUwalnTChj01CD3rKzDuT19"):
    """Test function to list files in a sandbox"""
    print(f"--- Testing List Sandbox Files for Sandbox: {sandbox_id}, Path: {path} ---")
    
    # Setup configuration and API client
    configuration = suna_api_client.Configuration(
        host="http://localhost:8000"
    )
    
    with suna_api_client.ApiClient(
        configuration,
        header_name="x-api-key",
        header_value=api_key
    ) as api_client:
        
        # Use SandboxApi instead of DefaultApi
        api_instance = suna_api_client.SandboxApi(api_client)
        
        try:
            # Call the list files endpoint
            files_response = api_instance.list_files_api_sandboxes_sandbox_id_files_get(
                sandbox_id=sandbox_id,
                path=path
            )
            
            print(f"Files response type: {type(files_response)}")
            print(f"Files response: {files_response}")
            
            # Try to parse and display the response data
            if hasattr(files_response, '__dict__'):
                print("\nFiles Information:")
                for key, value in files_response.__dict__.items():
                    if isinstance(value, (dict, list)):
                        print(f"  {key}: {json.dumps(value, indent=4, default=str)}")
                    else:
                        print(f"  {key}: {value}")
            else:
                print(f"Files data: {files_response}")
                
            return files_response
                
        except ApiException as e:
            print(f"Exception when calling list_files: {e}")
            if hasattr(e, 'body') and e.body:
                try:
                    error_data = json.loads(e.body)
                    print(f"Error details: {json.dumps(error_data, indent=2)}")
                except:
                    print(f"Error body: {e.body}")
            return None
        except Exception as e:
            print(f"Unexpected error in test_list_sandbox_files: {e}")
            return None


def test_read_sandbox_file(sandbox_id, file_path, api_key="pk_TxQNMYBqwVEdi8i0LEDzM83jyZwQQe2L:sk_2bhxOJfPomUwalnTChj01CD3rKzDuT19"):
    """Test function to read a specific file from a sandbox"""
    print(f"--- Testing Read Sandbox File: {file_path} from Sandbox: {sandbox_id} ---")
    
    # Setup configuration and API client
    configuration = suna_api_client.Configuration(
        host="http://localhost:8000"
    )
    
    with suna_api_client.ApiClient(
        configuration,
        header_name="x-api-key",
        header_value=api_key
    ) as api_client:
        
        # Use SandboxApi instead of DefaultApi
        api_instance = suna_api_client.SandboxApi(api_client)
        
        try:
            # Call the read file endpoint
            file_response = api_instance.read_file_api_sandboxes_sandbox_id_files_content_get(
                sandbox_id=sandbox_id,
                path=file_path
            )
            
            print(f"File response type: {type(file_response)}")
            print(f"File response: {file_response}")
            
            # Try to parse and display the response data
            if hasattr(file_response, '__dict__'):
                print("\nFile Content Information:")
                for key, value in file_response.__dict__.items():
                    if isinstance(value, (dict, list)):
                        print(f"  {key}: {json.dumps(value, indent=4, default=str)}")
                    else:
                        print(f"  {key}: {value}")
            else:
                print(f"File data: {file_response}")
                
            return file_response
                
        except ApiException as e:
            print(f"Exception when calling read_file: {e}")
            if hasattr(e, 'body') and e.body:
                try:
                    error_data = json.loads(e.body)
                    print(f"Error details: {json.dumps(error_data, indent=2)}")
                except:
                    print(f"Error body: {e.body}")
            return None
        except Exception as e:
            print(f"Unexpected error in test_read_sandbox_file: {e}")
            return None


def test_list_sandbox_files_with_requests(sandbox_id, path="/", api_key="pk_TxQNMYBqwVEdi8i0LEDzM83jyZwQQe2L:sk_2bhxOJfPomUwalnTChj01CD3rKzDuT19"):
    """Alternative test function using direct HTTP requests to list files"""
    print(f"--- Testing List Sandbox Files (Direct HTTP) for Sandbox: {sandbox_id}, Path: {path} ---")
    
    url = f"http://localhost:8000/api/sandboxes/{sandbox_id}/files"
    headers = {
        "x-api-key": api_key,
        "Accept": "application/json"
    }
    params = {"path": path}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        
        files_data = response.json()
        print(f"Files data: {json.dumps(files_data, indent=2, default=str)}")
        
        return files_data
        
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error when calling list files: {e}")
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.text}")
        return None
        
    except requests.exceptions.RequestException as e:
        print(f"Request Exception when calling list files: {e}")
        return None
        
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        print(f"Response content: {response.text}")
        return None
        
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


def test_read_sandbox_file_with_requests(sandbox_id, file_path, api_key="pk_TxQNMYBqwVEdi8i0LEDzM83jyZwQQe2L:sk_2bhxOJfPomUwalnTChj01CD3rKzDuT19"):
    """Alternative test function using direct HTTP requests to read a file"""
    print(f"--- Testing Read Sandbox File (Direct HTTP): {file_path} from Sandbox: {sandbox_id} ---")
    
    url = f"http://localhost:8000/api/sandboxes/{sandbox_id}/files/content"
    headers = {
        "x-api-key": api_key,
        "Accept": "application/json"
    }
    params = {"path": file_path}
    
    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        
        file_data = response.json()
        print(f"File data: {json.dumps(file_data, indent=2, default=str)}")
        
        return file_data
        
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error when calling read file: {e}")
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.text}")
        return None
        
    except requests.exceptions.RequestException as e:
        print(f"Request Exception when calling read file: {e}")
        return None
        
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        print(f"Response content: {response.text}")
        return None
        
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


def test_complete_sandbox_files_workflow(sandbox_id, api_key="pk_TxQNMYBqwVEdi8i0LEDzM83jyZwQQe2L:sk_2bhxOJfPomUwalnTChj01CD3rKzDuT19"):
    """
    Complete test workflow: List all files in sandbox, then read each file
    """
    print("=" * 80)
    print("COMPLETE SANDBOX FILES WORKFLOW TEST")
    print("=" * 80)
    
    # Step 1: List all files in the sandbox
    print("\n[STEP 1] Listing All Files in Sandbox")
    print("-" * 50)
    
    files_list = test_list_sandbox_files(sandbox_id, "/", api_key)
    
    if not files_list:
        print("[ERROR] Failed to list files in sandbox. Exiting.")
        return None
    
    # Step 2: Parse the files list and extract file paths
    print("\n[STEP 2] Parsing Files List")
    print("-" * 50)
    
    file_paths = []
    
    # Handle different response formats
    if isinstance(files_list, list):
        file_paths = files_list
    elif hasattr(files_list, '__dict__'):
        # Look for common file list fields
        for key, value in files_list.__dict__.items():
            if isinstance(value, list) and key.lower() in ['files', 'items', 'data']:
                file_paths = value
                break
    elif isinstance(files_list, dict):
        # Look for common file list fields in dict
        for key, value in files_list.items():
            if isinstance(value, list) and key.lower() in ['files', 'items', 'data']:
                file_paths = value
                break
    
    print(f"Found {len(file_paths)} files/directories")
    
    # Step 3: Read each file (skip directories)
    print("\n[STEP 3] Reading File Contents")
    print("-" * 50)
    
    file_contents = {}
    
    for i, file_info in enumerate(file_paths):
        # Extract file path from different possible formats
        file_path = None
        if isinstance(file_info, str):
            file_path = file_info
        elif isinstance(file_info, dict):
            # Look for common path fields
            for key in ['path', 'name', 'file_path', 'filename']:
                if key in file_info:
                    file_path = file_info[key]
                    break
        
        if not file_path:
            print(f"  File {i+1}: Could not extract path from {file_info}")
            continue
        
        print(f"\n  Reading file {i+1}/{len(file_paths)}: {file_path}")
        
        # Try to read the file
        file_content = test_read_sandbox_file(sandbox_id, file_path, api_key)
        
        if file_content:
            file_contents[file_path] = file_content
            print(f"    ✓ Successfully read {file_path}")
        else:
            print(f"    ✗ Failed to read {file_path}")
    
    print(f"\n{'='*80}")
    print("WORKFLOW TEST COMPLETED")
    print(f"{'='*80}")
    print(f"Total files found: {len(file_paths)}")
    print(f"Files successfully read: {len(file_contents)}")
    
    return {
        'sandbox_id': sandbox_id,
        'files_list': files_list,
        'file_paths': file_paths,
        'file_contents': file_contents
    }


def get_sandbox_id_from_thread(thread_id, api_key="pk_TxQNMYBqwVEdi8i0LEDzM83jyZwQQe2L:sk_2bhxOJfPomUwalnTChj01CD3rKzDuT19"):
    """
    Helper function to extract sandbox_id from thread data
    """
    print(f"--- Extracting Sandbox ID from Thread: {thread_id} ---")
    
    configuration = suna_api_client.Configuration(host="http://localhost:8000")
    
    with suna_api_client.ApiClient(
        configuration,
        header_name="x-api-key",
        header_value=api_key
    ) as api_client:
        
        api_instance = suna_api_client.DefaultApi(api_client)
        
        try:
            # Get thread with complete related data
            thread_data = api_instance.get_thread_api_threads_thread_id_get(thread_id=thread_id)
            
            print(f"Thread data type: {type(thread_data)}")
            
            # Look for sandbox_id in the response
            sandbox_id = None
            
            if hasattr(thread_data, '__dict__'):
                print("\nSearching for sandbox_id in thread data:")
                for key, value in thread_data.__dict__.items():
                    print(f"  {key}: {value}")
                    if 'sandbox' in key.lower() and value:
                        sandbox_id = value
                        break
            elif isinstance(thread_data, dict):
                print("\nSearching for sandbox_id in thread dict:")
                for key, value in thread_data.items():
                    print(f"  {key}: {value}")
                    if 'sandbox' in key.lower() and value:
                        sandbox_id = value
                        break
            
            if sandbox_id:
                print(f"\n✓ Found sandbox_id: {sandbox_id}")
            else:
                print(f"\n✗ No sandbox_id found in thread data")
                
            return sandbox_id
                
        except Exception as e:
            print(f"Error extracting sandbox_id from thread: {e}")
            return None


if __name__ == "__main__":
    # Test with a sample sandbox_id (you can replace this with an actual sandbox_id)
    sandbox_id = "d5a97505-9c33-4f90-8482-3d88f91a7271"
    
    print("=" * 60)
    print("Testing Sandbox Files with Suna API Client")
    print("=" * 60)
    
    # Test 1: List files using API client
    result1 = test_list_sandbox_files(sandbox_id)
    
    print("\n" + "=" * 60)
    print("Testing Sandbox Files with Direct HTTP Requests")
    print("=" * 60)
    
    # Test 2: List files using direct HTTP requests
    result2 = test_list_sandbox_files_with_requests(sandbox_id)
    
    print("\n" + "=" * 60)
    print("Testing Read Specific File")
    print("=" * 60)
    
    # Test 3: Read a specific file (if files were found)
    if result1 or result2:
        # Try to read a common file like index.html or main.py
        test_files = ["index.html", "main.py", "app.py", "README.md", "package.json"]
        for test_file in test_files:
            print(f"\nTrying to read: {test_file}")
            result3 = test_read_sandbox_file(sandbox_id, test_file)
            if result3:
                break
    
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    print(f"API Client list files result: {'SUCCESS' if result1 is not None else 'FAILED'}")
    print(f"Direct HTTP list files result: {'SUCCESS' if result2 is not None else 'FAILED'}")
    
    # Uncomment the following lines to test the complete workflow
    # print("\n" + "=" * 60)
    # print("Testing Complete Workflow")
    # print("=" * 60)
    # workflow_result = test_complete_sandbox_files_workflow(sandbox_id)
    # print(f"Complete workflow result: {'SUCCESS' if workflow_result is not None else 'FAILED'}")
