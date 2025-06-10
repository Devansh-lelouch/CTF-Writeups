# La Casa Da Papel 

![image](https://github.com/user-attachments/assets/749c3d87-b5d6-4faf-8bbf-6ac514ea494c)


# Solution
The intial terminal looks like this : 

![image](https://github.com/user-attachments/assets/e7dec5c3-a26f-4e9c-8e7f-3b434142aa18)

So the challenge most prolly ask us to open the vault by fooling Alice 

![image](https://github.com/user-attachments/assets/dcb086b1-b97e-44d1-8939-74e839be4365)

Going through the python script , we figure out that the convo would move further only if its Bob and then it would ask for HMAC code from Bob. 
So we need to figure out a way to impersonate as Bob. 


"""
def practice_convo(secret):
    message = input("Send a message: ")
    hash = md5(secret, message.encode('latin-1'))
    print(f"Here is your encrypted message: {hash}")

def fool_alice(secret):
    print("\nBot: Okay, let's see if you're the real deal. What's your name?")
    user_name = input("Your name: ").encode('latin-1')
    user_name = user_name.decode('unicode_escape').encode('latin-1')
    print("\nBot: Please provide your HMAC")
    user_hmac = input("Your HMAC: ").encode('latin-1')
"""
Understanding the code further, the pratice convo would also hash the msg in md5 decoding and would also have secret as it is which we can use to get the hmac for Bob 

![image](https://github.com/user-attachments/assets/f44b4e4f-e0f4-4c9d-8ef2-cc410f84c8b1)

Since the encrpyted msg given by the bot in the pratice code isnt the real hmac , looking at the code again its a base64 decoder 

Putting the encrpyted msg returned in pratice convo in a base64 decoder 

![image](https://github.com/user-attachments/assets/7b90a9cf-cd95-4c97-b7b7-fc52d3607f33)

Putting this as the HMAC code reveals a vault code 

![image](https://github.com/user-attachments/assets/3fd62454-59cf-4d33-8f6f-d0c5ddd3b692)

Now just put the code in option 3 to crack the vault and get the flag 

![image](https://github.com/user-attachments/assets/bd83b0a7-55d0-4bf2-8a56-3374bfb053f7)

The flag is : nite{El_Pr0f3_0f_Prec1s10n_Pl4ns}

