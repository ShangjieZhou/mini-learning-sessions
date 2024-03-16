with open('sample.json', 'rb') as file:
    # Read the entire file content into a bytes object
    byte_content = file.read()

    decoded_content = byte_content.decode("utf-8")
    print(decoded_content)

    # Convert each byte to its hexadecimal representation and print
    hex_content = ' '.join(f'{byte:02x}' for byte in byte_content)
    print(hex_content)