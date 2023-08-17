import streamlit as st
import hashlib
import time

class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash

def calculate_hash(index, previous_hash, timestamp, data):
    value = str(index) + str(previous_hash) + str(timestamp) + str(data)
    return hashlib.sha256(value.encode()).hexdigest()

def create_genesis_block():
    return Block(0, "0", int(time.time()), "Genesis Block", calculate_hash(0, "0", int(time.time()), "Genesis Block"))

def create_new_block(previous_block, data):
    index = previous_block.index + 1
    timestamp = int(time.time())
    hash = calculate_hash(index, previous_block.hash, timestamp, data)
    return Block(index, previous_block.hash, timestamp, data, hash)

# Streamlit app
def main():
    st.title("Basic Blockchain Visualization")

    blockchain = [create_genesis_block()]
    previous_block = blockchain[0]

    num_blocks_to_add = st.number_input("Number of Blocks to Add", min_value=1, value=1)
    add_blocks_button = st.button("Add Blocks")

    if add_blocks_button:
        for _ in range(num_blocks_to_add):
            new_data = f"This is block #{previous_block.index + 1}"
            new_block = create_new_block(previous_block, new_data)
            blockchain.append(new_block)
            previous_block = new_block
            st.write(f"Block #{new_block.index} has been added to the blockchain!")
            st.write(f"Hash: {new_block.hash}\n")

    st.write("Blockchain:")
    for block in blockchain:
        st.write(f"Block #{block.index}")
        st.write(f"Previous Hash: {block.previous_hash}")
        st.write(f"Timestamp: {block.timestamp}")
        st.write(f"Data: {block.data}")
        st.write(f"Hash: {block.hash}\n")
        st.write("---")

if __name__ == "__main__":
    main()
