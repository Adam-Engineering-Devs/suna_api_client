import suna_api_client
from suna_api_client.models.initiate_agent_response import InitiateAgentResponse
from suna_api_client.rest import ApiException
from suna_api_client.custom import stream_agent_run
import json
import time

configuration = suna_api_client.Configuration(
    host="http://localhost:8000"
)

# Advanced processor that collects and processes data
class StreamProcessor:
    def __init__(self):
        self.messages = []
        self.start_time = time.time()
    
    def process_line(self, line: str):
        """Advanced processing that stores streaming data"""
        current_time = time.time() - self.start_time
        self.messages.append({
                'timestamp': current_time,
                'type': 'raw',
                'content': line
            })
        print(f"[{current_time:.2f}s] RAW: {line}")
    
    def get_summary(self):
        """Get a summary of the streamed data"""
        data_messages = [m for m in self.messages if m['type'] == 'data']
        return {
            'total_messages': len(self.messages),
            'data_messages': len(data_messages),
            'duration': time.time() - self.start_time,
            'messages': self.messages
        }

def test_advanced_streaming():
    """Test advanced streaming with custom processing"""
    print("\n=== Testing Advanced Streaming ===")
    
    with suna_api_client.ApiClient(
        configuration,
        header_name="x-api-key",
        header_value="pk_TxQNMYBqwVEdi8i0LEDzM83jyZwQQe2L:sk_2bhxOJfPomUwalnTChj01CD3rKzDuT19"
    ) as api_client:
        
        api_instance = suna_api_client.DefaultApi(api_client)
        processor = StreamProcessor()
        
        try:
            response = api_instance.initiate_agent_with_files_api_agent_initiate_post(
                prompt="Explain quantum computing in simple terms",
                model_name="claude-sonnet-4.5",
                enable_thinking=True,
                reasoning_effort="medium",
                stream=True,
                enable_context_manager=True,
                enable_prompt_caching=True,
                agent_id=None,
                files=None
            )
            
            print(f"Thread ID: {response.thread_id}")
            print(f"Agent Run ID: {response.agent_run_id}")
            
            # Advanced streaming with custom processor
            for line in stream_agent_run(api_client, response.agent_run_id, safety_timeout=300):
                processor.process_line(line)
            
            # Show summary
            summary = processor.get_summary()
            print(f"\n=== Stream Summary ===")
            print(f"Total messages: {summary['total_messages']}")
            print(f"Data messages: {summary['data_messages']}")
            print(f"Duration: {summary['duration']:.2f} seconds")
            
        except Exception as e:
            print(f"Error in advanced streaming: {e}")

if __name__ == "__main__":
    test_advanced_streaming()
    
    print("\n=== All tests completed ===")
