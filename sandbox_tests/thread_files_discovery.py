import suna_api_client
from suna_api_client.rest import ApiException
import json

configuration = suna_api_client.Configuration(
    host="http://localhost:8000"
)

# Given thread ID
thread_id = "df6ea70c-02f5-459d-9bdd-8778cafb329b"

# Option 1: Set custom headers when creating the ApiClient
with suna_api_client.ApiClient(
    configuration,
    header_name="x-api-key",
    header_value="pk_TxQNMYBqwVEdi8i0LEDzM83jyZwQQe2L:sk_2bhxOJfPomUwalnTChj01CD3rKzDuT19"
) as api_client:
    
    # Use DefaultApi for thread info and SandboxApi for file operations
    default_api = suna_api_client.DefaultApi(api_client)
    sandbox_api = suna_api_client.SandboxApi(api_client)

    try:
        print(f"Getting thread info for thread_id: {thread_id}")
        
        # Step 1: Get thread info using the API
        thread_response = default_api.get_thread_api_threads_thread_id_get(thread_id=thread_id)
        
        # Step 2: Extract sandbox ID
        sandbox_id = thread_response["project"]["sandbox"]["id"]
        
        if not sandbox_id:
            print("No sandbox ID found in thread response!")
            exit(1)
        
        print(f"\nUsing sandbox ID: {sandbox_id}")
        
        # Step 3: List files in the sandbox using the API-generated method
        print(f"Fetching files using SandboxApi...")
        
        files_response = sandbox_api.list_files_api_sandboxes_sandbox_id_files_get(
            sandbox_id=sandbox_id,
            path="/"  # List files from root directory
        )
        
        print(f"\n=== Sandbox Files ===")
        print(f"Files response type: {type(files_response)}")
        
        # Display the files response
        if hasattr(files_response, '__dict__'):
            print("\nFiles Information:")
            for key, value in files_response.__dict__.items():
                if isinstance(value, (dict, list)):
                    print(f"  {key}: {json.dumps(value, indent=4, default=str)}")
                else:
                    print(f"  {key}: {value}")
        else:
            print(f"Files data: {files_response}")
        
    except ApiException as e:
        print(f"API Exception: {e}")
        print(f"Status: {e.status}")
        print(f"Reason: {e.reason}")
        print(f"Body: {e.body}")
    except Exception as e:
        print(f"Unexpected error: {e}")
        import traceback
        traceback.print_exc()
