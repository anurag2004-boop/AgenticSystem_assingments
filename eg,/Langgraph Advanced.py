import sqlite3
import json
import os

DB_PATH = "checkpoints.sqlite"

def get_connection():
    # open a sqlite3 connection to DB_PATH and
    # CREATE TABLE IF NOT EXISTS for `checkpoints` and `writes`
    conn = sqlite3.connect(DB_PATH)
    conn.execute('''
        CREATE TABLE IF NOT EXISTS checkpoints (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            thread_id TEXT,
            node_name TEXT,
            state_json TEXT
        )
    ''')
    conn.execute('''
        CREATE TABLE IF NOT EXISTS writes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            thread_id TEXT,
            node_name TEXT,
            key TEXT,
            value TEXT
        )
    ''')
    conn.commit()
    return conn

class SqliteCheckpointer:
    def __init__(self, conn):
        self.conn = conn

    def save(self, thread_id, node_name, state):
        # insert one row into checkpoints (full state_json)
        # and one row into writes per key in state
        state_json = json.dumps(state)
        cursor = self.conn.cursor()
        
        cursor.execute(
            "INSERT INTO checkpoints (thread_id, node_name, state_json) VALUES (?, ?, ?)",
            (thread_id, node_name, state_json)
        )
        
        for key, value in state.items():
            cursor.execute(
                "INSERT INTO writes (thread_id, node_name, key, value) VALUES (?, ?, ?, ?)",
                (thread_id, node_name, key, str(value))
            )
            
        self.conn.commit()

    def load_latest(self, thread_id):
        # return the most recently saved state dict for thread_id,
        # or {} if nothing has been saved yet
        cursor = self.conn.cursor()
        cursor.execute(
            "SELECT state_json FROM checkpoints WHERE thread_id = ? ORDER BY id DESC LIMIT 1",
            (thread_id,)
        )
        row = cursor.fetchone()
        if row:
            return json.loads(row[0])
        return {}

def generate_advertisement(state):
    # implement per the required output table above
    topic = state.get("topic", "")
    state["advertisement"] = f"Buy the best {topic} today!"
    return state

def generate_review(state):
    # implement per the required output table above
    topic = state.get("topic", "")
    state["review"] = f"This {topic} review is highly positive."
    return state

def generate_tagline(state):
    # implement per the required output table above
    topic = state.get("topic", "")
    state["tagline"] = f"{topic.title()} — Ride the Future."
    return state

def combine_outputs(state):
    # concatenate advertisement + review + tagline
    state["combined_output"] = state.get("advertisement", "") + state.get("review", "") + state.get("tagline", "")
    return state

def run_pipeline(thread_id, topic, checkpointer, nodes_to_run=None):
    # reload state, then run only the nodes that still need to
    # produce output, checkpointing after each one
    state = checkpointer.load_latest(thread_id)
    if not state:
        state = {"topic": topic}

    output_keys = {
        "generate_advertisement": "advertisement",
        "generate_review": "review",
        "generate_tagline": "tagline",
        "combine_outputs": "combined_output"
    }

    all_nodes = [generate_advertisement, generate_review, generate_tagline, combine_outputs]
    nodes = nodes_to_run if nodes_to_run else all_nodes

    for node in nodes:
        node_name = node.__name__
        out_key = output_keys[node_name]
        
        # skip node if its output key is already present in the reloaded state
        if out_key not in state:
            state = node(state)
            checkpointer.save(thread_id, node_name, state)

    return state

if __name__ == "__main__":
    # Clean up previous runs if the file exists for a fresh start
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)

    conn = get_connection()
    checkpointer = SqliteCheckpointer(conn)
    
    thread_id = "session-201"
    topic = "electric bicycles"

    # simulate a partial run (crash)
    partial_nodes = [generate_advertisement, generate_review]
    run_pipeline(thread_id, topic, checkpointer, nodes_to_run=partial_nodes)

    # reload the thread after the simulated crash
    reloaded_state = checkpointer.load_latest(thread_id)
    print(f"Reloaded state after simulated crash: {reloaded_state}")

    # resume and print the final combined_output plus checkpoint count
    final_state = run_pipeline(thread_id, topic, checkpointer)
    print(f"Final combined_output: {final_state['combined_output']}")

    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM checkpoints WHERE thread_id = ?", (thread_id,))
    checkpoint_count = cursor.fetchone()[0]
    print(f"Total checkpoint rows for thread: {checkpoint_count}")