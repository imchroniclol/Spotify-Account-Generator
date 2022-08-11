import os, requests, random, json, threading
from datetime import datetime
from colorama import Fore





email = [
    "discord.com",
    "github.com",
    "spotify.com"
]

url = "https://spclient.wg.spotify.com/signup/public/v2/account/create"




def center(var: str, space: int = None):  # pycenter
    if not space:
        space = (
            os.get_terminal_size().columns
            - len(var.splitlines()[int(len(var.splitlines()) / 2)])
        ) / 2

    return "\n".join((" " * int(space)) + var for var in var.splitlines())




class AIO:
    def GetEmail():
        semail = str(random.randint(11111111, 99999999)) + "@" + random.choice(email)
        return semail

    def GetGender():
        genders = ["Female", "Male"]
        return random.choice(genders)

    def CreateAccount():
        with open("proxies.txt", encoding="utf-8") as f:
            proxies = [i.strip() for i in f]
        while True:
            proxy = random.choice(proxies)
            passw = "ChronicLmao155!"
            os.system(f"title Spotify v0.1")
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            emails = AIO.GetEmail()
            account = emails+":"+passw
            payload = json.dumps(
                {
                    "account_details": {
                        "birthdate": "1999-09-02",
                        "consent_flags": {
                            "eula_agreed": True,
                            "send_email": True,
                            "third_party_email": False,
                        },
                        "display_name": "chronic",
                        "email_and_password_identifier": {
                            "email": emails,
                            "password": passw,
                        },
                        "gender": 1,
                    },
                    "callback_uri": "https://www.spotify.com/signup/challenge?forward_url=https%3A%2F%2Fopen.spotify.com%2F&locale=uk",
                    "client_info": {
                        "api_key": "a1e486e2729f46d6bb368d6b2bcda326",
                        "app_version": "v2",
                        "capabilities": [1],
                        "installation_id": "",
                        "platform": "www",
                    },
                    "tracking": {
                        "creation_flow": "",
                        "creation_point": "https://www.spotify.com/uk/",
                        "referrer": "",
                    },
                }
            )
            xxx = requests.post(url, data=payload, proxies={"http": "http" + "://" + proxy})
            if xxx.status_code == 200:
                print(
                    center(
                        (f'{current_time} {Fore.GREEN} [!] - {Fore.CYAN}{account} | {Fore.GREEN}Proxy: {proxy}  {Fore.RESET}')
                    )
                )

                with open("accounts.txt", "a+") as h:
                    h.write(account+"\n")
                    h.close
            else:
                print(center(f'{current_time} {Fore.RED} [!] - {Fore.CYAN}{account} | {Fore.RED}Proxy: {proxy}  {Fore.RESET}'))




if __name__ == "__main__":
    print(
        center(
            f"""\n\n
        
╔═╗┌─┐┌─┐┌┬┐┬┌─┐┬ ┬
╚═╗├─┘│ │ │ │├┤ └┬┘
╚═╝┴  └─┘ ┴ ┴└   ┴ 
          

        
        """
        )
    )



a = int(input("How many threads would you like to use?: "))

for _ in range(a):
    threading.Thread(target=AIO.CreateAccount).start()

    
        
# https://github.com/imchroniclol/Spotify-Account-Generator
