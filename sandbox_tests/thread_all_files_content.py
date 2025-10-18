import suna_api_client
from suna_api_client.rest import ApiException
import requests
import zipfile
import os


def test_get_all_sandbox_files_content_with_thread(thread_id, api_key="pk_TxQNMYBqwVEdi8i0LEDzM83jyZwQQe2L:sk_2bhxOJfPomUwalnTChj01CD3rKzDuT19"):
    """Test function to get all files content using thread ID to find sandbox"""
    print(f"Getting all files content for thread: {thread_id}")
    
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
            # Step 1: Get thread info to extract sandbox ID
            thread_response = default_api.get_thread_api_threads_thread_id_get(thread_id=thread_id)
            sandbox_id = thread_response["project"]["sandbox"]["id"]
            print(f"Found sandbox ID: {sandbox_id}")
            
            # Step 2: Extract configuration for direct request
            config = api_client.configuration
            host = config.host.rstrip('/')
            
            # Extract API key
            api_key_from_client = None
            for header_name, header_value in api_client.default_headers.items():
                if header_name.lower() == 'x-api-key':
                    api_key_from_client = header_value
                    break
            
            # Step 3: Make request to get all files as zip
            url = f"{host}/api/sandboxes/{sandbox_id}/all_files/content"
            headers = {"x-api-key": api_key_from_client}
            
            response = requests.get(url, headers=headers, timeout=60)
            response.raise_for_status()
            
            # Step 4: Save zip file
            zip_filename = f"sandbox_{sandbox_id}_files.zip"
            with open(zip_filename, 'wb') as f:
                f.write(response.content)
            
            print(f"Zip file saved as: {zip_filename}")
            print(f"File size: {os.path.getsize(zip_filename)} bytes")
            
            # Verify it's a valid zip
            with zipfile.ZipFile(zip_filename, 'r') as zip_file:
                file_count = len(zip_file.namelist())
                print(f"Archive contains {file_count} files")
            
            return zip_filename
                
        except Exception as e:
            print(f"Error: {e}")
            import traceback
            traceback.print_exc()
            return None


if __name__ == "__main__":
    thread_id = "cbe1e075-75fa-4890-bd37-431d3e981bd0"
    test_get_all_sandbox_files_content_with_thread(thread_id)