# strange message

strange_message = "C123o3213d325i747ng F677a76c87tor75678y567"

decrypted_message = ""

for char in strange_message:
    if not char.isnumeric():
        decrypted_message += char

print("Message:", decrypted_message)
