#!/usr/bin/python3

# Swaps two values
def swap(x, y):
    return y, x

message_file = open("message.txt", "r")
message = list(message_file.read())

for i in range(0, len(message), 3):
    message[i], message[i+2] = swap(message[i], message[i+2])
    message[i+1], message[i+2] = swap(message[i+1], message[i+2])

print(message)
answer = "".join(message)
print(answer)

