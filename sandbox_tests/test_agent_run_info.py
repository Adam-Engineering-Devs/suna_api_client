import suna_api_client
from suna_api_client.rest import ApiException
import json


def test_get_agent_run_info(agent_run_id, api_key="pk_TxQNMYBqwVEdi8i0LEDzM83jyZwQQe2L:sk_2bhxOJfPomUwalnTChj01CD3rKzDuT19"):
    """Test function to fetch agent run information by agent_run_id"""
    print(f"--- Testing Get Agent Run Info for Agent Run: {agent_run_id} ---")
    
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
            # Call the get agent run endpoint
            agent_run_response = api_instance.get_agent_run_api_agent_run_agent_run_id_get(
                agent_run_id=agent_run_id
            )
            
            print(f"Agent run response type: {type(agent_run_response)}")
            print(f"Agent run response: {agent_run_response}")
            
            # Try to parse and display the response data
            if hasattr(agent_run_response, '__dict__'):
                print("\nAgent Run Information:")
                for key, value in agent_run_response.__dict__.items():
                    if isinstance(value, (dict, list)):
                        print(f"  {key}: {json.dumps(value, indent=4, default=str)}")
                    else:
                        print(f"  {key}: {value}")
            else:
                print(f"Agent run data: {agent_run_response}")
                
            return agent_run_response
                
        except ApiException as e:
            print(f"Exception when calling get_agent_run: {e}")
            if hasattr(e, 'body') and e.body:
                try:
                    error_data = json.loads(e.body)
                    print(f"Error details: {json.dumps(error_data, indent=2)}")
                except:
                    print(f"Error body: {e.body}")
            return None
        except Exception as e:
            print(f"Unexpected error in test_get_agent_run_info: {e}")
            return None


def test_get_agent_run_info_with_requests(agent_run_id, api_key="pk_TxQNMYBqwVEdi8i0LEDzM83jyZwQQe2L:sk_2bhxOJfPomUwalnTChj01CD3rKzDuT19"):
    """Alternative test function using direct HTTP requests"""
    print(f"--- Testing Get Agent Run Info (Direct HTTP) for Agent Run: {agent_run_id} ---")
    
    import requests
    
    url = f"http://localhost:8000/api/agent-run/{agent_run_id}"
    headers = {
        "x-api-key": api_key,
        "Accept": "application/json"
    }
    
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        
        agent_run_data = response.json()
        print(f"Agent run data: {json.dumps(agent_run_data, indent=2, default=str)}")
        
        return agent_run_data
        
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error when calling get agent run: {e}")
        print(f"Response status code: {response.status_code}")
        print(f"Response content: {response.text}")
        return None
        
    except requests.exceptions.RequestException as e:
        print(f"Request Exception when calling get agent run: {e}")
        return None
        
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
        print(f"Response content: {response.text}")
        return None
        
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None


def test_agent_run_status(agent_run_id, api_key="pk_TxQNMYBqwVEdi8i0LEDzM83jyZwQQe2L:sk_2bhxOJfPomUwalnTChj01CD3rKzDuT19"):
    """Test function to get detailed agent run status information"""
    print(f"--- Testing Agent Run Status for Agent Run: {agent_run_id} ---")
    
    # Get the agent run info first
    agent_run_info = test_get_agent_run_info(agent_run_id, api_key)
    
    if agent_run_info:
        print("\n" + "="*50)
        print("AGENT RUN STATUS SUMMARY")
        print("="*50)
        
        # Extract key status information
        if isinstance(agent_run_info, dict):
            status = agent_run_info.get('status', 'Unknown')
            started_at = agent_run_info.get('started_at', 'Unknown')
            completed_at = agent_run_info.get('completed_at', 'Not completed')
            error = agent_run_info.get('error', None)
            agent_id = agent_run_info.get('agent_id', 'None')
            agent_version_id = agent_run_info.get('agent_version_id', 'None')
            
            print(f"Status: {status}")
            print(f"Started at: {started_at}")
            print(f"Completed at: {completed_at}")
            print(f"Agent ID: {agent_id}")
            print(f"Agent Version ID: {agent_version_id}")
            
            if error:
                print(f"Error: {error}")
            else:
                print("Error: None")
                
            # Check if there are any responses or outputs
            if 'responses' in agent_run_info:
                responses = agent_run_info['responses']
                print(f"Number of responses: {len(responses) if isinstance(responses, list) else 'Unknown'}")
                
            if 'outputs' in agent_run_info:
                outputs = agent_run_info['outputs']
                print(f"Number of outputs: {len(outputs) if isinstance(outputs, list) else 'Unknown'}")
                
        return agent_run_info
    else:
        print("Failed to retrieve agent run information")
        return None


if __name__ == "__main__":
    # Test with a sample agent_run_id (you can replace this with an actual agent_run_id)
    # This agent_run_id was obtained from the thread info test
    agent_run_id = "c170f383-81b7-4843-bab1-9617930d244b"
    
    print("=" * 60)
    print("Testing Agent Run Information Retrieval")
    print("=" * 60)
    
    print("\n" + "=" * 60)
    print("Testing with Suna API Client")
    print("=" * 60)
    result1 = test_get_agent_run_info(agent_run_id)
    
    print("\n" + "=" * 60)
    print("Testing with Direct HTTP Requests")
    print("=" * 60)
    result2 = test_get_agent_run_info_with_requests(agent_run_id)
    
    print("\n" + "=" * 60)
    print("Testing Agent Run Status Summary")
    print("=" * 60)
    result3 = test_agent_run_status(agent_run_id)
    
    print("\n" + "=" * 60)
    print("Test Summary")
    print("=" * 60)
    print(f"API Client test result: {'SUCCESS' if result1 is not None else 'FAILED'}")
    print(f"Direct HTTP test result: {'SUCCESS' if result2 is not None else 'FAILED'}")
    print(f"Status summary test result: {'SUCCESS' if result3 is not None else 'FAILED'}")
