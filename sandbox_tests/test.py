import suna_api_client
from suna_api_client.models.initiate_agent_response import InitiateAgentResponse
from suna_api_client.rest import ApiException
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
        
        # Now stream the response using the agent_run_id
        print("\n--- Starting Stream ---")
        
        # Use requests directly to handle SSE properly
        import requests
        
        def stream_agent_run(agent_run_id, api_key):
            """Stream agent run using direct HTTP requests with SSE handling"""
            url = f"http://localhost:8000/api/agent-run/{agent_run_id}/stream"
            headers = {
                "x-api-key": api_key,
                "Accept": "text/event-stream",
                "Cache-Control": "no-cache"
            }
            
            try:
                print(f"[STREAM] Starting EventSource-like connection to {url}")
                
                with requests.get(url, headers=headers, stream=True, timeout=30) as response:
                    response.raise_for_status()
                    
                    print(f"[STREAM] Connection opened, status: {response.status_code}")
                    
                    # Safety timeout (30 minutes like frontend)
                    import time
                    start_time = time.time()
                    safety_timeout = 30 * 60  # 30 minutes
                    
                    for line in response.iter_lines(decode_unicode=True):
                        # Check safety timeout
                        if time.time() - start_time > safety_timeout:
                            print("[STREAM] Safety timeout reached, cleaning up")
                            break
                        
                        if not line or line.strip() == '':
                            continue
                            
                        print(line)
                            
            except requests.exceptions.RequestException as e:
                print(f"[STREAM] Request error: {e}")
            except Exception as e:
                print(f"[STREAM] Unexpected error: {e}")
        
        # Start streaming
        stream_agent_run(response.agent_run_id, "pk_TxQNMYBqwVEdi8i0LEDzM83jyZwQQe2L:sk_2bhxOJfPomUwalnTChj01CD3rKzDuT19")
        
    except ApiException as e:
        print(f"Exception when calling initiate_agent: {e}")