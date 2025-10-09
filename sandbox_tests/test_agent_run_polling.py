import suna_api_client
from suna_api_client.rest import ApiException
import json
import time
import requests


def poll_agent_run_until_completion(agent_run_id, api_key="pk_TxQNMYBqwVEdi8i0LEDzM83jyZwQQe2L:sk_2bhxOJfPomUwalnTChj01CD3rKzDuT19", 
                                   poll_interval=2, max_poll_time=300):
    """
    Poll an agent run until it completes (completed_at != null)
    
    Args:
        agent_run_id: The ID of the agent run to poll
        api_key: API key for authentication
        poll_interval: Time in seconds between polls (default: 2 seconds)
        max_poll_time: Maximum time to poll in seconds (default: 5 minutes)
    
    Returns:
        dict: Agent run data when completed, None if failed or timed out
    """
    print(f"--- Polling Agent Run: {agent_run_id} ---")
    print(f"Poll interval: {poll_interval} seconds")
    print(f"Max poll time: {max_poll_time} seconds")
    
    start_time = time.time()
    poll_count = 0
    
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
        
        while True:
            poll_count += 1
            elapsed_time = time.time() - start_time
            
            print(f"\n[Poll #{poll_count}] Elapsed time: {elapsed_time:.1f}s")
            
            try:
                # Get current agent run status
                agent_run_response = api_instance.get_agent_run_api_agent_run_agent_run_id_get(
                    agent_run_id=agent_run_id
                )
                
                if isinstance(agent_run_response, dict):
                    status = agent_run_response.get('status', 'Unknown')
                    completed_at = agent_run_response.get('completedAt', None)
                    started_at = agent_run_response.get('startedAt', 'Unknown')
                    error = agent_run_response.get('error', None)
                    
                    print(f"  Status: {status}")
                    print(f"  Started at: {started_at}")
                    print(f"  Completed at: {completed_at}")
                    
                    if error:
                        print(f"  Error: {error}")
                    
                    # Check if completed
                    if completed_at is not None:
                        print(f"\n[SUCCESS] Agent run completed after {elapsed_time:.1f} seconds!")
                        print(f"   Final status: {status}")
                        print(f"   Completed at: {completed_at}")
                        return agent_run_response
                    
                    # Check for timeout
                    if elapsed_time >= max_poll_time:
                        print(f"\n[TIMEOUT] Polling timed out after {max_poll_time} seconds")
                        return None
                    
                    # Wait before next poll
                    print(f"  Waiting {poll_interval} seconds before next poll...")
                    time.sleep(poll_interval)
                    
                else:
                    print(f"  Unexpected response type: {type(agent_run_response)}")
                    time.sleep(poll_interval)
                    
            except ApiException as e:
                print(f"  API Exception: {e}")
                if hasattr(e, 'body') and e.body:
                    try:
                        error_data = json.loads(e.body)
                        print(f"  Error details: {json.dumps(error_data, indent=2)}")
                    except:
                        print(f"  Error body: {e.body}")
                time.sleep(poll_interval)
                
            except Exception as e:
                print(f"  Unexpected error: {e}")
                time.sleep(poll_interval)


def get_thread_messages(thread_id, api_key="pk_TxQNMYBqwVEdi8i0LEDzM83jyZwQQe2L:sk_2bhxOJfPomUwalnTChj01CD3rKzDuT19"):
    """
    Get all messages from a thread
    
    Args:
        thread_id: The ID of the thread to get messages from
        api_key: API key for authentication
    
    Returns:
        list: List of messages from the thread
    """
    print(f"\n--- Retrieving Messages from Thread: {thread_id} ---")
    
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
            # Get thread messages (newest first)
            messages_response = api_instance.get_thread_messages_api_threads_thread_id_messages_get(
                thread_id=thread_id,
                order="desc"  # Get newest messages first
            )
            
            # Process the response
            if hasattr(messages_response, 'data'):
                messages_data = messages_response.data
            elif isinstance(messages_response, list):
                messages_data = messages_response
            else:
                messages_data = messages_response
                
            print(f"Retrieved {len(messages_data) if hasattr(messages_data, '__len__') else 'Unknown'} messages")
            return messages_data
                
        except ApiException as e:
            print(f"Exception when calling get_thread_messages: {e}")
            if hasattr(e, 'body') and e.body:
                try:
                    error_data = json.loads(e.body)
                    print(f"Error details: {json.dumps(error_data, indent=2)}")
                except:
                    print(f"Error body: {e.body}")
            return None
        except Exception as e:
            print(f"Unexpected error in get_thread_messages: {e}")
            return None


def print_messages(messages_data):
    """
    Print messages in a formatted way
    
    Args:
        messages_data: List of messages to print
    """
    if not messages_data:
        print("No messages to display")
        return

    messages_data = [x for x in messages_data['messages'] if x["is_llm_message"]]
    messages_data = [x for x in messages_data if x.get("content") and isinstance(x["content"], dict) and x["content"].get("role") == "assistant"]
    messages_data = sorted(messages_data, key=lambda x: x["created_at"])

    print(f"\n{'='*80}")
    print("THREAD MESSAGES")
    print(f"{'='*80}")
    
    for i, message in enumerate(messages_data):
        print(f"\n--- Message {i + 1} ---")        
        print(f"\n{message['content']['content']}")


def test_agent_run_polling_and_messages(agent_run_id, api_key="pk_TxQNMYBqwVEdi8i0LEDzM83jyZwQQe2L:sk_2bhxOJfPomUwalnTChj01CD3rKzDuT19"):
    """
    Complete test: Poll agent run until completion, then get and display all messages
    
    Args:
        agent_run_id: The ID of the agent run to poll
        api_key: API key for authentication
    """
    print("=" * 80)
    print("AGENT RUN POLLING AND MESSAGE RETRIEVAL TEST")
    print("=" * 80)
    
    # Step 1: Poll agent run until completion
    print("\n[STEP 1] Polling Agent Run Until Completion")
    print("-" * 50)
    
    completed_agent_run = poll_agent_run_until_completion(agent_run_id, api_key)
    
    if not completed_agent_run:
        print("[ERROR] Failed to get completed agent run. Exiting.")
        return None
    
    # Step 2: Extract thread_id from the completed agent run
    print("\n[STEP 2] Extracting Thread ID")
    print("-" * 50)
    
    if isinstance(completed_agent_run, dict):
        thread_id = completed_agent_run.get('threadId', None)
        if not thread_id:
            print("[ERROR] No thread_id found in agent run response")
            return None
        print(f"Thread ID: {thread_id}")
    else:
        print("[ERROR] Unexpected agent run response format")
        return None
    
    # Step 3: Get all messages from the thread
    print("\n[STEP 3] Retrieving Thread Messages")
    print("-" * 50)
    
    messages = get_thread_messages(thread_id, api_key)
    
    if not messages:
        print("[ERROR] Failed to retrieve messages from thread")
        return None
    
    # Step 4: Display all messages
    print("\n[STEP 4] Displaying Messages")
    print("-" * 50)
    
    print_messages(messages)
    
    print(f"\n{'='*80}")
    print("TEST COMPLETED SUCCESSFULLY")
    print(f"{'='*80}")
    
    return {
        'agent_run': completed_agent_run,
        'thread_id': thread_id,
        'messages': messages
    }


def test_with_direct_requests(agent_run_id, api_key="pk_TxQNMYBqwVEdi8i0LEDzM83jyZwQQe2L:sk_2bhxOJfPomUwalnTChj01CD3rKzDuT19"):
    """
    Alternative implementation using direct HTTP requests
    """
    print("\n" + "=" * 80)
    print("DIRECT HTTP REQUESTS IMPLEMENTATION")
    print("=" * 80)
    
    # Poll agent run using direct requests
    print(f"\n--- Polling Agent Run (Direct HTTP): {agent_run_id} ---")
    
    start_time = time.time()
    poll_count = 0
    poll_interval = 2
    max_poll_time = 300
    
    while True:
        poll_count += 1
        elapsed_time = time.time() - start_time
        
        print(f"\n[Poll #{poll_count}] Elapsed time: {elapsed_time:.1f}s")
        
        try:
            url = f"http://localhost:8000/api/agent-run/{agent_run_id}"
            headers = {
                "x-api-key": api_key,
                "Accept": "application/json"
            }
            
            response = requests.get(url, headers=headers)
            response.raise_for_status()
            
            agent_run_data = response.json()
            
            status = agent_run_data.get('status', 'Unknown')
            completed_at = agent_run_data.get('completedAt', None)
            thread_id = agent_run_data.get('threadId', None)
            
            print(f"  Status: {status}")
            print(f"  Completed at: {completed_at}")
            print(f"  Thread ID: {thread_id}")
            
            if completed_at is not None:
                print(f"\n[SUCCESS] Agent run completed after {elapsed_time:.1f} seconds!")
                
                # Get messages using direct requests
                if thread_id:
                    print(f"\n--- Getting Messages from Thread: {thread_id} ---")
                    
                    messages_url = f"http://localhost:8000/api/threads/{thread_id}/messages"
                    messages_response = requests.get(messages_url, headers=headers)
                    messages_response.raise_for_status()
                    
                    messages_data = messages_response.json()
                    print(f"Retrieved {len(messages_data) if isinstance(messages_data, list) else 'Unknown'} messages")
                    
                    print_messages(messages_data)
                
                return agent_run_data
            
            if elapsed_time >= max_poll_time:
                print(f"\n[TIMEOUT] Polling timed out after {max_poll_time} seconds")
                return None
            
            time.sleep(poll_interval)
            
        except requests.exceptions.RequestException as e:
            print(f"  Request error: {e}")
            time.sleep(poll_interval)
        except Exception as e:
            print(f"  Unexpected error: {e}")
            time.sleep(poll_interval)


if __name__ == "__main__":
    # Test with a sample agent_run_id
    # You can replace this with an actual agent_run_id
    agent_run_id = "e11e933a-635f-415b-a4c3-db40bceb2f08"
    
    print("Starting Agent Run Polling and Message Retrieval Test")
    print(f"Agent Run ID: {agent_run_id}")
    
    # Test with API client
    result1 = test_agent_run_polling_and_messages(agent_run_id)
    
    # Test with direct HTTP requests
    result2 = test_with_direct_requests(agent_run_id)
    
    print("\n" + "=" * 80)
    print("FINAL TEST SUMMARY")
    print("=" * 80)
    print(f"API Client test result: {'SUCCESS' if result1 is not None else 'FAILED'}")
    print(f"Direct HTTP test result: {'SUCCESS' if result2 is not None else 'FAILED'}")
