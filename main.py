from meta_ai_api import MetaAI
import random
import json


ai = MetaAI()
with open("email_samples.json","r") as json_file:
    scripts = json.load(json_file)

# given a website, youtube video, social media page the bot will return a ready to send message
# you have the option to add a fun "p.s" message to make your pitches that much better
# for testing: https://www.youtube.com/watch?v=nFx0kpQikRs, graphic design services, asha

print("Welcome Asha's cold emailer! This bot will help you generate messages for your outreach.")

data = input("Enter a website, YouTube video, social media, etc. This will be used to generate personalization: ")

you = input("Tell me about yourself. What are you pitching? What is your name?: ")

pitches = scripts["pitches"]
chosen_key = random.choice(list(pitches.keys())) # takes the keys makes it a list and randomly selects one
script = pitches[chosen_key]

prompt = f"Personalize {script} based on {data} and {you}"
response = ai.prompt(message=prompt)
print(response)






