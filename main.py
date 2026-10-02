from http import HTTPStatus
import traceback
import requests
import sys
import os

def discord(url):
  webhooks = [
    "<[REQUIRED] Replace With Discord Webhook Here",
  ]
  body = {
    "content": url
  }
  for webhook in webhooks:
    requests.post(webhook, json=body)

def report(type, trace):
  webhooks = [
    # "<[OPTIONAL] Replace With Discord Webhook Here>",
  ]
  body = {
    "embeds": [
      {
        "title": type,
        "description": trace,
        "color": 3091758
      }
    ],
  }
  for webhook in webhooks:
    requests.post(webhook, json=body)

def get_last_sent():
  try:
    with open("last_sent.log", "x") as _:
      pass
  except:
    pass

  with open("last_sent.log") as infile:
    urls = infile.read().splitlines()
  return urls

def generate_last_sent(urls):
  with open("last_sent.log", "w") as outfile:
    outfile.write("\n".join(urls))

def send_it(sends):
  for send in sorted(sends):
    discord(send)

def main():
  page = requests.get("https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions")
  if page.status_code == 200:
    data = page.json()
    games = data["data"]["Catalog"]["searchStore"]["elements"]

    last_sent = get_last_sent()
    send = []
    sent = []

    for game in games:
      if game["price"]["totalPrice"]["discountPrice"] == 0:
        slug = game["offerMappings"][0]["pageSlug"]
        if slug is not None and slug != "[]":
          url = f"https://store.epicgames.com/p/{slug}"
          if url not in last_sent:
            send.append(url)
          sent.append(url)
        else:
          report("Slug Error", game["title"])
    send_it(send)
    generate_last_sent(sent)
  else:
    status_codes = {s.value: s.phrase for s in HTTPStatus}
    report("HTTP response status code", f"{page.status_code} {status_codes[page.status_code]}")

if __name__ == "__main__":
  try:
    try:
      os.chdir(os.path.sep.join(sys.argv[0].split(os.path.sep)[:-1]))
    except:
      pass
    main()
  except:
    report("Python Error", traceback.format_exc())
