import hashlib


class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        """
        Initializes a new block in the blockchain.

        :param index: The index that identifies the block in the blockchain.
        :param timestamp: The date and time when the block was created.
        :param data: A dictionary containing a pair of secret text and password.
        :param previous_hash: The hash of the previous block in the blockchain.
        """
        self.index = index
        self.timestamp = timestamp
        self.data = data.copy()  # Copy the data (private) to prevent changes in the original input.
        self.previous_hash = previous_hash
        self.hash = self.calculate_md5_hash()

    def calculate_md5_hash(self):
        """
        Generates an MD5 hash for the block by combining the timestamp, block data and the previous hash.

        :return: The hash of the block.
        """
        concatenated_hash_data = f'{self.timestamp}_{self.concatenate_data()}{self.previous_hash}'
        md5_hash = hashlib.md5(concatenated_hash_data.encode())  # Create MD5 hash object.
        return md5_hash.hexdigest()

    def concatenate_data(self):
        """
        Concatenates the blocks data into a single string for an easier hash calculation.

        :return: The concatenated string of all the values in the data dictionary.
        """
        concatenated_data = ''
        for value in self.data.values():  # Loop through the data's dictionary values.
            concatenated_data += value + '_'  # Append each value with an underscore.
        return concatenated_data

    def check_hash(self):
        """
        Re-computes the block hash and compares it to the stored block hash.

        :return: True if the hashes are the same, False otherwise.
        """
        recomputed_hash = self.calculate_md5_hash()
        return self.hash == recomputed_hash
