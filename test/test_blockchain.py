from blockchain_model.blockchain import Blockchain
import time


def setup_blockchain():
    blockchain = Blockchain()
    data_samples = [{'secret': 'First secret', 'password': 'pass1'},
                    {'secret': 'Second secret', 'password': 'pass2'},
                    {'secret': 'Third secret', 'password': 'pass3'}
                    ]
    for data in data_samples:
        time.sleep(1)  # Simulating one second delay
        blockchain.add_block(data)  # Adding the blocks
    return blockchain


# For the transition from the second test to the third test saving this attribute is crucial.

# First test
def first_test(blockchain):
    blockchain.print_chain()
    if blockchain.check_chain():
        print('First test: SUCCESSFUL')
    else:
        print('First test: FAILED')


# Second test
def second_test(blockchain):
    blockchain.chain[2].timestamp = blockchain.timestamp_calculate()  # Modifying the timestamp to the current date.
    blockchain.print_chain()
    if not blockchain.check_chain():
        print('Second test: SUCCESSFUL')
    else:
        print('Second test: FAILED')


# Third test
def third_test(blockchain, initial_timestamp):
    blockchain.chain[2].timestamp = initial_timestamp  # Using the original chain.

    # Chose the initial blocks hash as a Random MD5 Hash
    blockchain.chain[3].hash = blockchain.chain[0].calculate_md5_hash

    output_array = []
    for i in range(3, 0, -1):  # Iterates and adds the results of the check hash commands.
        output_array.append(blockchain.chain[i].check_hash())

    ref_array = [False, True, True]

    if output_array == ref_array:
        print('Third test: SUCCESSFUL')
    else:
        print('Third test: FAILED')


if __name__ == '__main__':
    blockchain_test = setup_blockchain()
    original_timestamp = blockchain_test.chain[2].timestamp  # Saving the original chain's information.

    first_test(blockchain_test)
    print("\n" * 3)  # For an easier readability.
    second_test(blockchain_test)
    print("\n" * 3)  # For an easier readability.
    third_test(blockchain_test, original_timestamp)
