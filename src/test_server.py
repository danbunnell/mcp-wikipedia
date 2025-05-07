import requests
import json

def test_mcp_server():
    # Test with a simple topic
    payload = {
        'topic': 'Python_(programming_language)'
    }
    
    response = requests.post(
        'http://localhost:5000/mcp',
        json=payload
    )
    
    print("Status Code:", response.status_code)
    print("Response:", json.dumps(response.json(), indent=2))

if __name__ == '__main__':
    test_mcp_server() 