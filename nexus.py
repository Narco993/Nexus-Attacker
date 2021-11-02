import os
import sys
import time
from os import system
from pathlib import Path

import colorama
import asyncio
import discord
import pyautogui
import requests as req
from discord.ext import commands, tasks

print("Don't worry! the gui isn't broken it takes some time.")

t_or_f = [True, False]

Test_Token = input ("[Required for some commands] Enter A Token: ")

CEND      = '\33[0m'
CGREEN2  = '\33[92m'
CBLUE   = '\33[34m'
CRED    = '\33[31m'
CYELLOW = '\33[33m'
 
def fivesectimer():
    num = ['5',
           '4',
           '3',
           '2',
           '1']
    
    for i in num:
        sys.stdout.write("\r\x1b[K" + "starting in " + i + " second")
        sys.stdout.flush()
        time.sleep(1)
 
    os.system("cls")
 
def tensectimer():
    num = ['10',
            '9',
            '8',
            '7',
            '6',
            '5',
            '4',
            '3',
            '2',
            '1']
    
    for i in num:
        sys.stdout.write("\r\x1b[K" + "Program is closing in " + i + " second")
        sys.stdout.flush()
        time.sleep(1)
    
    os.system("cls")
 
def normalspam():
 
    print("What do you want to spam ? ")
    word = input(CRED + ">>> " + CEND)
    print("How many time do you want to spam ? ")
    x = int(input(CRED + ">>> " + CEND))
 
    fivesectimer()
 
    for i in range(x):
      pyautogui.typewrite(word)
      pyautogui.press("enter")
 
 
def wordlistspam():
    print("Enter the .txt file name (without .txt)")
    filename = input(CRED + ">>> " + CEND)
    filenames = (filename+".txt")
 
    if Path(filenames).exists():
 
        print("Do you wish to start now ? [ Y / N ]")
        yn = input(CRED + ">>> " + CEND)
        yn = yn.lower()
 
        if yn == ("y"):
            fivesectimer()
 
            f = open(filenames, 'r')
            for i in f:
                pyautogui.typewrite(i)
                pyautogui.press("enter")
 
            fin = input("The task is finish press enter to close")
            exit()
 
        if yn == ("n"):
            tensectimer()
            exit()
        
        else:
            v = input("invalid choice press enter to close")
 
 
    
    if not Path(filenames).exists():
        print(filenames + ".txt do not exist do you want to create new .txt with that name ? [ Y / N ]")
        respond = input(CRED + ">>> " + CEND)
        respond = respond.lower()
 
        if respond == ("y"):
            file = open(filenames ,'w')
            w = input("Please write the wordlist in " + filenames + " and run the program again")
 
            tensectimer()
            exit()
        
        if respond == ("n"):
            c = input("Press enter to close.")
 
def discordwebhookspam():
    x = 0
    WEBHOOK_URL = str(input("Webhook URL : "))
    WEBHOOK_USERNAME = str(input("Name : "))
    WEBHOOK_AVATAR = str(input("Avatarurl : "))
    WEBHOOK_CONTENT = str(input("What to spam : "))
    SPAM = int(input("How many time to spam : "))
    while x < SPAM:
        try:
            payload = {"content":WEBHOOK_CONTENT,"username":WEBHOOK_USERNAME,"avatar_url":WEBHOOK_AVATAR}
            r = requests.post(WEBHOOK_URL,data=payload)
            x +=1
            print(WEBHOOK_CONTENT + "have been sent to webhook")
        except:
            print("Spam failed")
            pass
    os.system("cls")
    print("Spam finished")
 
def Bot_run():
    Token = input("DISCORD TOKEN : ")
    request_url = "https://canary.discordapp.com/api/v6/users/@me"
    
 
    req = requests.get(request_url, headers={'authorization': Token})
    if req.status_code == 401:
        print(f"The token : {Token} is invalid")
        inv = input("press enter to close")
        exit()
    if req.status_code == 200:
        print(f"The token : {Token} is valid")
    client = commands.Bot(command_prefix='h')
 
    @client.event
    async def on_ready():
        print('status : online')
 
    @client.command(name="dmall")
    async def dm_all(ctx, message):
        for member in ctx.guild.members:
            try:
                await member.create_dm()
                await member.dm_channel.send(message)
                print("Message has been sent to "+ member.name)
            except:
                print("Message failed to sent to "+ member.name)
 
    try:
        client.run(Token, bot=False, reconnect=True)
        print("Login success")
    except discord.errors.LoginFailure:
        print("Unable to connect")

def webhook_deleter():
   webhook = input ('Webhook URL: ')
   r = requests.delete(webhook)

def token_info():
    token = input("Token: ")
class MyClient(discord.Client):
    async def on_connect(self):
        print(f"""Getting information {client.user}
ID: {client.user.id}
Email: {client.user.email}
Created At: {client.user.created_at}
MFA: {client.user.mfa_enabled}
Nitro: {client.user.premium_type}
Flags: {client.user.public_flags}
Verified: {client.user.verified}""")

def server_leaver(Token):
    headers = {"authorization": Token, "user-agent": "Samsung Fridge/6.9"}
    leave_all_servers_request = requests.get(
        "https://canary.discord.com/api/v8/users/@me/guilds", headers=headers
    ).json()
    for guild in leave_all_servers_request:
        requests.delete(
            f"https://canary.discord.com/api/v8/users/@me/guilds/{guild['id']}",
            headers=headers,
        )
        print(f"Left Guild: {guild['id']}")

 
       
 
 
 
def credit():
    print("")
    print("               [*]=----------------------------------------------------------------------------------=[*]")
    print("                |                     Made with code not love                                          |")
    print("                |                 Discord : Landen III#9541                                            |")                     
    print("                |                 Github : https://github.com/Narco993                                 |")
    print("                |                 Youtube : https://www.youtube.com/channel/UCGXN_0kd_mEmMSSS3d-LhGA   |")
    print("                |                                                                                      |")
    print("                |                 Discord server invite link :                                         |")
    print("                |                 https://discord.com/invite/NajwTd7YCu                                |")
    print("                |                                                                                      |")
    print("               [*]=----------------------------------------------------------------------------------=[*]")
    print("")
    ic = input("")
 
def choice():
    print("                                \\\ ―――――――――――――――――― ///                            ")
    print("                                |||<NEXUS ATTACKER GUI>|||          ")
    print("                                /// ―――――――――――――――――― \\\ ")
    print("               [*]=--------------------------------------------------=[*]")
    print("                |                                                      |")
    print("                |                 1. Normal spambot                    |")                     
    print("                |                 2. Wordlist spambot                  |")
    print("                |                 3. Discord webhook spam              |")
    print("                |                 4. Discord self bot                  |")
    print("                |                 5. Credit                            |")
    print("                |                 6. Webhook deleter                   |")
    print("                |                 7  Leave All Servers                 |")
    print("                |                 8. Token Info                        |")
    print("                |                NEXUS THE BEST ATTACKER               |")
    print("               [*]=--------------------------------------------------=[*]")
    print("")
    spamchoice = input(CRED + ">>> " + CEND)
    
    if spamchoice == ("1"):
        os.system("cls")
        normalspam()
 
    if spamchoice == ("2"):
        os.system("cls")
        wordlistspam()
    
    if spamchoice == ("3"):
        os.system("cls")
        discordwebhookspam()
    
    if spamchoice == ("4"):
        os.system("cls")
        Bot_run()
    if spamchoice == ("5"):
        os.system("cls")
        credit()
    if spamchoice == ("6"):
        os.system("cls")
        webhook_deleter()
    if spamchoice == ("7"):
        os.system("cls")
        server_leaver()
    if spamchoice == ("8"):
        os.system("cls")
        token_info()
 
 
 
choice()