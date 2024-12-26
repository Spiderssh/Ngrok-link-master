import requests
import argparse
from termcolor import colored

def display_banner():
    """Displays the tool's banner."""
    banner = r"""
       _______   __       ___       ________   _______      
      /  ___  | |  |     /   \     |       /  |   ____|     
     |  |   | | |  |    /  ^  \    `---/  /   |  |__        
     |  |   | | |  |   /  /_\  \      /  /    |   __|       
     |  `---' | |  `--./  _____  \    /  /----.|  |____     
      \______/  |_____/__/     \__\  /________||_______|    
       Ninja and Ngrok Master
    """
    print(colored(banner, "red", attrs=["bold"]))
    print("-" * 50)

def mask_url(public_url, mask_url, port):
    """Masks the Ngrok URL based on user input."""
    masked_url = f"{mask_url}:{port}"
    print(colored(f"Ngrok URL: {public_url}", "green"))
    print(colored(f"Masked URL: {masked_url}", "green"))
    return masked_url

if __name__ == "__main__":
    display_banner()
    
    # User inputs
    public_url = input(colored("Enter your Ngrok public URL (e.g., http://abcd1234.ngrok.io): ", "green"))
    mask_url_input = input(colored("Enter your preferred masking URL (e.g., http://yourdomain.com): ", "green"))
    port = input(colored("Enter the port number (e.g., 8080): ", "green"))

    # Process and display masked URL
    masked_url = mask_url(public_url, mask_url_input, port)
    print("-" * 50)
    print(colored("Masked URL successfully generated!", "green"))
    print(colored(f"Access your masked link here: {masked_url}", "green"))
    print("-" * 50)
