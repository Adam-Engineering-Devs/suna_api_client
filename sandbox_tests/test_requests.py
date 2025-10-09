import requests
import json

# Configuration
BASE_URL = "http://localhost:8000"
API_KEYS = {
    'public_key': 'pk_TxQNMYBqwVEdi8i0LEDzM83jyZwQQe2L',
    'secret_key': 'sk_2bhxOJfPomUwalnTChj01CD3rKzDuT19'
}

# Endpoint URL
ENDPOINT_URL = f"{BASE_URL}/api/agent/initiate"

# Request parameters
prompt = "Hello! Who are you?"
model_name = "gpt-5-mini"
enable_thinking = True
reasoning_effort = "medium"
stream = True
enable_context_manager = True
enable_prompt_caching = True
agent_id = None
files = None

# Prepare the request data
data = {
    'prompt': prompt,
    'model_name': model_name,
    'enable_thinking': enable_thinking,
    'reasoning_effort': reasoning_effort,
    'stream': stream,
    'enable_context_manager': enable_context_manager,
    'enable_prompt_caching': enable_prompt_caching,
    'agent_id': agent_id
}

# Prepare headers
headers = {
    'Accept': 'application/json',
    "x-api-key": f"{API_KEYS['public_key']}:{API_KEYS['secret_key']}"
}

try:
    # Make the POST request
    response = requests.post(
        ENDPOINT_URL,
        data=data,
        headers=headers,
        files=files
    )
    
    # Check if the request was successful
    response.raise_for_status()
    
    # Parse the JSON response
    response_data = response.json()
    
    # Extract the response fields
    thread_id = response_data.get('thread_id')
    agent_run_id = response_data.get('agent_run_id')
    
    print(f"Thread ID: {thread_id}")
    print(f"Agent Run ID: {agent_run_id}")
    print(f"Full Response: {json.dumps(response_data, indent=2)}")
    
except requests.exceptions.HTTPError as e:
    print(f"HTTP Error when calling initiate_agent: {e}")
    print(f"Response status code: {response.status_code}")
    print(f"Response content: {response.text}")
    
except requests.exceptions.RequestException as e:
    print(f"Request Exception when calling initiate_agent: {e}")
    
except json.JSONDecodeError as e:
    print(f"JSON Decode Error: {e}")
    print(f"Response content: {response.text}")
    
except Exception as e:
    print(f"Unexpected error: {e}")
