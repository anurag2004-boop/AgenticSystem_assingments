import json
# Step 1: Store a JSON-formatted string representing an API response
api_response = {
  "request_id": "1234",
  "status": "success",
  "result": {
    "text": "Hello world",
    "confidence": 0.98
  }
}
api_response = json.dumps(api_response) 
# Step 2: Parse the JSON string into Python objects
parsed_response = json.loads(api_response)      
# Step 3: Extract and print the required information
request_id = parsed_response.get("request_id")
status = parsed_response.get("status")
text_result = parsed_response.get("result", {}).get("text") 
confidence_score = parsed_response.get("result", {}).get("confidence")
print(f"Request ID: {request_id}")
print(f"Status: {status}")
print(f"Text Result: {text_result}")
print(f"Confidence Score: {confidence_score}")
