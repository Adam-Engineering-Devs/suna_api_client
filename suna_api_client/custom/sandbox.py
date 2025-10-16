from suna_api_client.api_client import ApiClient
import requests

def get_sandbox_file_content(
    api_client: ApiClient,
    sandbox_id: str,
    path: str,
    timeout: int = 30
) -> bytes:
    """
    Get file content from a sandbox using direct HTTP requests.
    
    This function uses the ApiClient's configuration to automatically extract
    the API key and host URL for making requests to the sandbox file content endpoint.
    
    Args:
        api_client: The ApiClient instance with configuration
        sandbox_id: The sandbox ID to read the file from
        path: The file path within the sandbox
        timeout: Request timeout in seconds (default: 30)
    
    Returns:
        bytes: The file content as bytes
    
    Raises:
        requests.exceptions.RequestException: If the HTTP request fails
        ValueError: If the API key cannot be extracted from the configuration
    
    Example:
        content = get_sandbox_file_content(api_client, "sandbox_123", "/path/to/file.txt")
        print(content.decode('utf-8'))
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
    
    # Build the file content URL
    url = f"{host}/api/sandboxes/{sandbox_id}/files/content"
    
    # Prepare headers
    headers = {
        "x-api-key": api_key,
    }
    
    # Prepare query parameters
    params = {
        "path": path
    }
    
    response = requests.get(url, headers=headers, params=params, timeout=timeout)
    response.raise_for_status()
    
    return response.content