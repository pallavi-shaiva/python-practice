import base64
def deocder(): 
    message = input("message to be encoded >>")
    message_in_bytes=bytes(message,"utf-8")
    message_in_bytes= base64.b64decoded(message_in_bytes)
    decoded_message =base64.b64decoded(message_in_bytes)
    print(f"Encoded:{decoded_message}")
def encoder():
    message = int(input("message to be encoded >>"))
    message-in_bytes =bytes(message,"utf-8")
    encoded_message =base64.b64encoded(message_in-bytes)
    print(f"Encoded: {encoded_message}")
print("python decoder and Encoder)
print("1.Encoder")
print("2.decoder")
option =input("select option (1/2 >>")
if option == "1"
  encoder()
elif option == "2"
  decoder()
else:
  print("Invalid option!!!!!")    
