#!/usr/bin/env python3
# You need a Hugging Face Token in your environment, an HF_TOKEN
# You need to install a virtual environment for python3 so you can use pip
#   $ python3 -m venv myenv
# You need to install openai
#   $ pip instal openai
import os
from openai import OpenAI

client = OpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.environ["HF_TOKEN"],
)

completion = client.chat.completions.create(
    model="moonshotai/Kimi-K2-Instruct-0905",
    messages=[
        {
            "role": "user",
            "content": "Write a dialogue between two characters meeting for the first time."
        }
    ],
)

print(completion.choices[0].message)
