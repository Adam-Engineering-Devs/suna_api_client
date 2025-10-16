# coding: utf-8

"""
Streaming utilities for suna_api_client

This module provides custom streaming functionality for the suna_api_client package.
"""

import time
from typing import Generator
import requests
from suna_api_client.api_client import ApiClient


def stream_agent_run(
    api_client: ApiClient,
    agent_run_id: str,
    timeout: int = 30,
    safety_timeout: int = 30 * 60  # 30 minutes
) -> Generator[str, None, None]:
    """
    Stream agent run using direct HTTP requests with SSE handling.
    
    This function uses the ApiClient's configuration to automatically extract
    the API key and host URL for making streaming requests.
    
    Args:
        api_client: The ApiClient instance with configuration
        agent_run_id: The agent run ID to stream
        timeout: Request timeout in seconds (default: 30)
        safety_timeout: Maximum time to stream in seconds (default: 30 minutes)
    
    Yields:
        str: Each line from the streaming response
    
    Raises:
        requests.exceptions.RequestException: If the HTTP request fails
        ValueError: If the API key cannot be extracted from the configuration
    
    Example:
        for line in stream_agent_run(api_client, agent_run_id):
            print(line)
    """
    # Extract configuration from ApiClient
    config = api_client.configuration
    host = config.host.rstrip('/')
    
    # Extract API key from the ApiClient's default headers
    api_key = None
    for header_name, header_value in api_client.default_headers.items():
        if header_name.lower() == 'x-api-key':
            api_key = header_value
            break
    
    if not api_key:
        raise ValueError(
            "API key not found in ApiClient configuration. "
            "Make sure to set the 'x-api-key' header when creating the ApiClient."
        )
    
    # Build the streaming URL
    url = f"{host}/api/agent-run/{agent_run_id}/stream"
    
    # Prepare headers
    headers = {
        "x-api-key": api_key,
        "Accept": "text/event-stream",
        "Cache-Control": "no-cache"
    }
    
    with requests.get(url, headers=headers, stream=True, timeout=timeout) as response:
        response.raise_for_status()
        
        # Track start time for safety timeout
        start_time = time.time()
        
        for line in response.iter_lines(decode_unicode=True):
            # Check safety timeout
            if time.time() - start_time > safety_timeout:
                break
            
            if not line or line.strip() == '':
                continue
            
            yield line
