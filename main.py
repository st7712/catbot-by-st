import discord, subprocess, sys, time, os, colorama, base64, codecs, datetime, io, random, numpy, datetime, smtplib, string, ctypes
import urllib.parse, urllib.request, re, json, requests, webbrowser, aiohttp, asyncio, functools, logging

from discord.ext import (
    commands,
    tasks
)
from bs4 import BeautifulSoup as bs4
from urllib.parse import urlencode
from pymongo import MongoClient
from selenium import webdriver
from threading import Thread
from subprocess import call
from itertools import cycle
from colorama import Fore
from sys import platform
from gtts import gTTS

bot = commands.Bot(command_prefix=".")

status = cycle(['st#1243 made this','Sending cat pics every 5 minutes','.gg/desc5qYvbR']) 

@bot.event
async def on_ready(): 
  change_status.start() 
  print("Your bot is ready") 
  
@tasks.loop(seconds=10)
async def change_status(): 
  await bot.change_presence(activity=discord.Game(next(status)))


@bot.command()
async def game(ctx, *, message): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Game]'''+Fore.RESET)
    game = discord.Game(
        name="JOIN .gg/desc5qYvbR"
    )
    await bot.change_presence(activity=game)

@bot.command(name="hello")
async def hello_world(ctx: commands.Context):
    await ctx.send("Hello, world!")

@bot.command() 
async def cat(ctx): # b'\xfc'
    await ctx.message.delete()
    print(f'''{Fore.BLUE}[LOG] {Fore.WHITE}Command ran [Cat]'''+Fore.RESET)
    while True:
      req = requests.get(f"https://api.thecatapi.com/v1/images/search?format=json&x-api-key=apikeyhere")
      r = req.json()
      em = discord.Embed(description="Heres a cute cat!")
      em.set_image(url=str(r[0]["url"]))
      await ctx.send(embed=em)
      print(f"{Fore.RED}[SENT]: {Fore.YELLOW}{req.text}"+Fore.RESET)
      time.sleep(300)

bot.run("tokenhere")
