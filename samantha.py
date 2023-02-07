import openai

# add api key here
openai.api_key = ""

COMPLETIONS_MODEL = "text-davinci-003"

conversation = []

# update prompt here
conversation.append(f"""Start with a greeting /e.'""")


while True:
  prompt = (f"{' '.join(conversation)}\n")

  response = openai.Completion.create(
    prompt=prompt,
    temperature=0.5,
    max_tokens=300,
    model=COMPLETIONS_MODEL
  )

  print(f"Samantha: {(response.choices[0].text).strip()}")
  conversation.append(f"{(response.choices[0].text)}. Me:")
  
  user_input = input("You: ")
  conversation.append(f"{user_input}\n")

  if user_input.lower() in ["exit", "quit"]:
    print("Exiting program...")
    break
