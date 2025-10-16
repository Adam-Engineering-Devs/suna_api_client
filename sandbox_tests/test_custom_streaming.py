import suna_api_client
from suna_api_client.models.initiate_agent_response import InitiateAgentResponse
from suna_api_client.rest import ApiException
from suna_api_client.custom import stream_agent_run
import json

configuration = suna_api_client.Configuration(
    host="http://localhost:8000"
)

# Option 1: Set custom headers when creating the ApiClient
with suna_api_client.ApiClient(
    configuration,
    header_name="x-api-key",
    header_value="pk_TxQNMYBqwVEdi8i0LEDzM83jyZwQQe2L:sk_2bhxOJfPomUwalnTChj01CD3rKzDuT19"
) as api_client:
    
    api_instance = suna_api_client.DefaultApi(api_client)

    prompt = "Creami un sito web per un'impresa di quattro salti in padella"
    model_name = "gpt-5-mini"  # Optional
    enable_thinking = True  # Optional
    reasoning_effort = "medium"  # Optional
    stream = True  # Optional
    enable_context_manager = True  # Optional
    enable_prompt_caching = True  # Optional
    agent_id = None  # Optional
    files = None  # Optional - List of files to attach

    try:
        # Call the initiate endpoint
        response = api_instance.initiate_agent_with_files_api_agent_initiate_post(
            prompt=prompt,
            model_name=model_name,
            enable_thinking=enable_thinking,
            reasoning_effort=reasoning_effort,
            stream=stream,
            enable_context_manager=enable_context_manager,
            enable_prompt_caching=enable_prompt_caching,
            agent_id=agent_id,
            files=files
        )
        
        print(f"Thread ID: {response.thread_id}")
        print(f"Agent Run ID: {response.agent_run_id}") 
        
        # Now stream the response using the new custom module
        print("\n--- Starting Stream with Custom Module ---")
        
        # Use the new custom streaming function (generator pattern)
        for line in stream_agent_run(api_client, response.agent_run_id):
            print(line)
        
    except ApiException as e:
        print(f"Exception when calling initiate_agent: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
