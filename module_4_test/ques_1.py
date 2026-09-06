from datetime import datetime
import json
import os

LOG_FILE = "trace_log.jsonl"

# Task 1: Log an event to the JSON Lines file
def log_event(trace_id, step_name, details):
    event = {
        "trace_id": trace_id,
        "step_name": step_name,
        "details": details,
        "timestamp": datetime.utcnow().isoformat() + "Z"
    }
    
    # Append the event as a single JSON line
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(event) + "\n")

# Task 2: Retrieve all events for a given trace_id
def get_trace(trace_id):
    if not os.path.exists(LOG_FILE):
        return []
        
    events = []
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                event = json.loads(line)
                if event.get("trace_id") == trace_id:
                    events.append(event)
            except json.JSONDecodeError:
                continue
                
    return events

# Task 3: List all unique trace IDs
def list_all_trace_ids():
    if not os.path.exists(LOG_FILE):
        return []
        
    unique_ids = []
    seen = set()
    
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                event = json.loads(line)
                t_id = event.get("trace_id")
                if t_id and t_id not in seen:
                    seen.add(t_id)
                    unique_ids.append(t_id)
            except json.JSONDecodeError:
                continue
                
    return unique_ids

# Task 4: Demonstrate the workflow
if __name__ == "__main__":
    # Clean up any existing file from previous runs to ensure clean demonstration
    if os.path.exists(LOG_FILE):
        os.remove(LOG_FILE)
        
    # Simulating two distinct parcels
    amazon_id = "AMZN-12345"
    myntra_id = "MYNT-67890"
    
    # Logging events for Amazon parcel (2 events)
    print("Logging events...")
    log_event(amazon_id, "Order Placed", {"vendor": "SellerA", "items_count": 2})
    log_event(amazon_id, "Dispatched", {"facility": "Mumbai_Hub", "carrier": "BlueDart"})
    
    # Logging events for Myntra parcel (2 events)
    log_event(myntra_id, "Order Confirmed", {"payment_mode": "UPI"})
    log_event(myntra_id, "In Transit", {"current_location": "Bengaluru_DC"})
    
    # Fetch and print trace for Amazon parcel
    print(f"\n--- Fetching trace for {amazon_id} ---")
    amazon_trace = get_trace(amazon_id)
    for event in amazon_trace:
        print(event)
        
    # List all distinct trace IDs logged
    print("\n--- Listing all distinct trace IDs ---")
    all_traces = list_all_trace_ids()
    print(all_traces)
