import os
import time

def print_logo():
    logo = r"""
    \033[32m
 


██████  ███████ ██    ██ ██ ██      ██   ██ ██████  
██   ██ ██      ██    ██ ██ ██       ██ ██  ██   ██ 
██   ██ █████   ██    ██ ██ ██        ███   ██   ██ 
██   ██ ██       ██  ██  ██ ██       ██ ██  ██   ██ 
██████  ███████   ████   ██ ███████ ██   ██ ██████                                             
    \033[0mWelcome to the Facebook Loader Script
    """
    print(logo)

def generate_token():
    print("\033[32mGenerating token and cookies...\033[0m")
    email = input("Enter your Email: ")
    password = input("Enter your Password: ")
    
    # Simulated token generation (replace with actual token retrieval logic)
    if email and password:
        print("\033[32mToken: YOUR_GENERATED_TOKEN_HERE\033[0m")
        print("\033[32mCookies: YOUR_GENERATED_COOKIES_HERE\033[0m")
    else:
        print("\033[31mInvalid Email or Password!\033[0m")

def messenger_loader():
    thread_count = int(input("Enter the number of Threads to use: "))
    for i in range(thread_count):
        group_id = input(f"Enter group thread ID {i + 1}: ")
        token_limit = int(input("Enter number of tokens to use for this group: "))
        for j in range(token_limit):
            token = input(f"Enter Token {j + 1}: ")
        hater_name = input("Enter Hater's Name: ")
        msg_file = input("Enter Your Msg File Path: ")
        delay_seconds = int(input("Enter Delay Seconds: "))
        
        # Simulated sending messages logic
        print(f"\033[32mSending messages to group {group_id} with {token_limit} tokens...\033[0m")
        time.sleep(delay_seconds)

def facebook_comment_loader():
    thread_count = int(input("Enter the number of Threads to use: "))
    for i in range(thread_count):
        post_id = input(f"Enter Facebook Post ID {i + 1}: ")
        token_limit = int(input("Enter number of tokens to use for this post: "))
        for j in range(token_limit):
            token = input(f"Enter Token {j + 1}: ")
        hater_name = input("Enter Hater's Name: ")
        msg_file = input("Enter Your Msg File Path: ")
        delay_seconds = int(input("Enter Delay Seconds: "))
        
        # Simulated posting comments logic
        print(f"\033[32mPosting comments to post {post_id} with {token_limit} tokens...\033[0m")
        time.sleep(delay_seconds)

def token_checker():
    token = input("Enter the token to check: ")
    if token:
        print(f"\033[32mChecking validity for token: {token}...\033[0m")
        print("\033[32mToken is valid.\033[0m")
    else:
        print("\033[31mInvalid token provided!\033[0m")

def post_comment_with_cookies():
    cookie_count = int(input("Enter the number of Cookies: "))
    for i in range(cookie_count):
        cookie = input(f"Enter Cookie {i + 1}: ")
    post_id = input("Enter the Facebook Post ID: ")
    hater_name = input("Enter Hater's Name: ")
    msg_file = input("Enter Your Msg File Path: ")
    
    # Simulated posting comments logic
    print("\033[32mPosting comments to post {} using cookies...\033[0m".format(post_id))

def cookies_to_json():
    cookies = input("Enter the cookies to convert (comma separated): ")
    print("\033[32mConverting cookies to JSON...\033[0m")
    if cookies:
        print("\033[32mConverted JSON: {\"cookies\": \"" + cookies + "\"}\033[0m")
    else:
        print("\033[31mNo cookies provided!\033[0m")

def send_from_web():
    print("\033[32mSending message, sticker, gift, emoji from web...\033[0m")

def main():
    print_logo()
    while True:
        print("\033[32mSelect an option:\033[0m")
        print("\033[32m1) Generate Your ID Token\033[0m")
        print("\033[32m2) Messenger Convo Loader\033[0m")
        print("\033[32m3) Facebook Post Comment Loader\033[0m")
        print("\033[32m4) Token Checker\033[0m")
        print("\033[32m5) Facebook Post Comment Send Using Cookies\033[0m")
        print("\033[32m6) Cookies to JSON Extract\033[0m")
        print("\033[32m7) Send From Web (MSG, Sticker, Gift, Emoji)\033[0m")
        print("\033[32m8) Exit\033[0m")

        choice = input("Choose an option: ")

        if choice == "1":
            generate_token()
        elif choice == "2":
            messenger_loader()
        elif choice == "3":
            facebook_comment_loader()
        elif choice == "4":
            token_checker()
        elif choice == "5":
            post_comment_with_cookies()
        elif choice == "6":
            cookies_to_json()
        elif choice == "7":
            send_from_web()
        elif choice == "8":
            exit()
        else:
            print("\033[31mInvalid choice! Please try again.\033[0m")

if __name__ == "__main__":
    main()
