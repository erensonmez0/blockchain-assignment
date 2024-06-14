from blockchain_model.block import Block
from datetime import datetime


class Blockchain:
    INITIAL_INDEX = 0  # Index of the initial block
    INITIAL_PREV_HASH = '0'  # Previous hash value for the initial block
    TIMESTAMP_FORMAT = '%Y_%m_%d_%Hh_%Mm_%Ss'  # Timestamp format

    def __init__(self):
        """
        Initializes the blockchain with an initial block.
        """
        self.chain = []  # Initialize an empty array to hold the blocks of the blockchain.
        self.create_initial_block()

    def create_initial_block(self):
        """
        Creates the initial block in the blockchain.
        """
        timestamp = self.timestamp_calculate()  # Timestamp of the first block.
        data = {'secret': 'Genesis Block', 'password': 'none'}  # Data of the first block.
        initial_block = Block(Blockchain.INITIAL_INDEX, timestamp, data, Blockchain.INITIAL_PREV_HASH)
        self.chain.append(initial_block)

    @staticmethod
    def timestamp_calculate():
        """
        Calculates the current timestamp in a specific format.

        :return: The calculated timestamp.
        """
        now = datetime.now()
        timestamp = now.strftime(Blockchain.TIMESTAMP_FORMAT)
        return timestamp

    def add_block(self, data):
        """
        Adds a new block to the blockchain.

        :param data: The data to be included in the new block.
        """
        index = len(self.chain)  # Index of the new block.

        last_block = self.chain[-1]  # Determining the previous block's hash.
        previous_hash = last_block.hash

        timestamp = self.timestamp_calculate()  # Timestamp of the new block.
        new_block = Block(index, timestamp, data, previous_hash)
        self.chain.append(new_block)

    def print_chain(self):
        """
        Prints the index, timestamp, previous block's hash, and current hash for each block in the blockchain.
        """
        for block in self.chain:
            print(f'Block Index: {block.index}')
            print(f'Timestamp: {block.timestamp}')
            print(f'Previous Hash: {block.previous_hash}')
            print(f'Current Hash: {block.hash}')
            print('-' * 50)  # For an easier readability.

    def check_chain(self):
        """
        Checks if the hashes are correct for all the blocks in the blockchain.

        :return: True if the blocks are valid, False otherwise.
        """
        # Iterates over the blockchain starting from the second block .
        for block in self.chain[1:]:  # Skipping the initial block
            if not block.check_hash():
                return False
        return True
