PRICING = {
    "Kimi K3": {"input_rate": 3, "output_rate": 15},
    "GPT": {"input_rate": 5, "output_rate": 30}
}

def route_model(query_type):
    if query_type == "simple":
        return "Kimi K3"
    elif query_type == "complex":
        return "GPT"
    else:
        raise ValueError(f"Invalid query type: {query_type}")

def calculate_cost(query_type, input_tokens, output_tokens):
    model = route_model(query_type)
    rates = PRICING[model]
    
    input_cost = (input_tokens / 1_000_000) * rates["input_rate"]
    output_cost = (output_tokens / 1_000_000) * rates["output_rate"]
    total_cost = input_cost + output_cost
    
    return model, round(total_cost, 4)

def process_requests(requests):
    results = []
    total_cost = 0.0
    
    for req in requests:
        model, cost = calculate_cost(req["query_type"], req["input_tokens"], req["output_tokens"])
        total_cost += cost
        
        # Formatting to match the expected output dictionary string
        results.append(f"{{'request_id': {req['request_id']}, 'model': '{model}', 'cost_usd': {cost}}}")
        
    results.append(f"TOTAL: {round(total_cost, 4)}")
    return " ".join(results)

if __name__ == "__main__":
    sample_requests = [
        {"request_id": 1, "query_type": "simple", "input_tokens": 500, "output_tokens": 150},
        {"request_id": 2, "query_type": "complex", "input_tokens": 2000, "output_tokens": 800},
        {"request_id": 3, "query_type": "simple", "input_tokens": 300, "output_tokens": 100},
        {"request_id": 4, "query_type": "complex", "input_tokens": 5000, "output_tokens": 1200},
        {"request_id": 5, "query_type": "simple", "input_tokens": 800, "output_tokens": 200},
        {"request_id": 6, "query_type": "complex", "input_tokens": 1200, "output_tokens": 400}
    ]
    output = process_requests(sample_requests)
    print(output)