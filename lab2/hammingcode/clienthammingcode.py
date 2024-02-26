def hamming_encode(message):
    r = 0
    while 2**r < len(message) + r + 1:
        r += 1

    encoded_message = [0] * (len(message) + r)

    j = 0
    for i in range(1, len(encoded_message) + 1):
        if i & (i - 1) == 0:
            continue  
        encoded_message[i - 1] = int(message[j])
        j += 1

    for i in range(r):
        index = 2**i - 1
        parity_bit = 0
        for j in range(index, len(encoded_message), 2**(i + 1)):
            parity_bit ^= encoded_message[j]
        encoded_message[index] = parity_bit

    return ''.join(map(str, encoded_message))

def client():
    original_message = "1011"

    print(f"Original message from client: {original_message}")

    encoded_message = hamming_encode(original_message)
    print(f"Encoded message: {encoded_message}")

    server(received_message=encoded_message)

def server(received_message):
    print(f"Received encoded message from client: {received_message}")

    corrected_message = hamming_correct(received_message)
    print(f"Corrected message: {corrected_message}")

    original_message = hamming_extract(corrected_message)
    print(f"Original message: {original_message}")

def hamming_correct(encoded_message):

    return encoded_message

def hamming_extract(encoded_message):
    original_message = ""
    for i in range(len(encoded_message)):
        if i & (i + 1) != 0:  
            original_message += encoded_message[i]
    return original_message

if __name__ == "__main__":
    client()
