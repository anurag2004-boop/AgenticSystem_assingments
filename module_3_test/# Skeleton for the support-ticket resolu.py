# Skeleton for the support-ticket resolution workflow.
# Fill in the TODOs below; keep the function signatures unchanged.

def classify_ticket(state):
    """Classifies the support ticket based on its description."""
    description = state.get("description", "").lower()
    
    # Defined keyword lists based on requirements
    billing_keywords = ["charged", "invoice", "payment", "refund", "subscription", "billed"]
    technical_keywords = ["connection", "error", "crash", "bug", "not working", "dropping", "slow", "freezing"]
    account_keywords = ["password", "login", "locked", "access", "sign in"]
    
    # Check in the required order: Billing -> Technical -> Account
    for keyword in billing_keywords:
        if keyword in description:
            return {"category": "Billing"}
            
    for keyword in technical_keywords:
        if keyword in description:
            return {"category": "Technical Issue"}
            
    for keyword in account_keywords:
        if keyword in description:
            return {"category": "Account Access"}
            
    # Fallback if no keywords match
    return {"category": "General Inquiry"}

def generate_resolution(state):
    """Generates a proposed resolution based on the ticket's category."""
    category = state.get("category", "")
    
    # Fixed lookup table for resolutions
    resolution_map = {
        "Technical Issue": "Our technical team will run a diagnostic on your connection within 24 hours.",
        "Billing": "We have flagged this charge for review and will issue a refund within 3-5 business days if applicable.",
        "Account Access": "Please reset your password using the link we just sent to your registered email.",
        "General Inquiry": "Thank you for reaching out; a support representative will respond within one business day."
    }
    
    # Get the matching resolution or default to General Inquiry if unexpected category
    resolution = resolution_map.get(category, resolution_map["General Inquiry"])
    
    return {"resolution": resolution}

def run_workflow(initial_state):
    """Runs classify_ticket -> generate_resolution in sequence, updating the shared state at each step (mirrors START -> node -> node -> END)."""
    # Create a copy of the state to avoid mutating the original input dict directly
    state = initial_state.copy()
    
    # Node 1: Classify Ticket
    category_update = classify_ticket(state)
    state.update(category_update)
    
    # Node 2: Generate Resolution
    resolution_update = generate_resolution(state)
    state.update(resolution_update)
    
    # Return the final modified state
    return state

if __name__ == "__main__":
    initial_state = {
        "ticket_id": "T1001",
        "description": "My internet connection keeps dropping every few minutes",
        "category": "",
        "resolution": "",
    }
    print(run_workflow(initial_state))