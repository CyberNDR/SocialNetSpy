#!/bin/python3
import time
try:
	from googlesearch import search
except ImportError:
	print("Error during packets import. Try again in few minutes.")

print("\n")

print("-----------------------------")
print("        SOCIALNETSPY        |")
print("-----------------------------")

print("\n")

print(" $$$$$                    $$           $$   $$   $$           $$    $$$$$")
print("$$   $$                        $$$$$   $$   $$$  $$   $$$$    $$   $$   $$   $$$$   $$  $$")
print(" $$$      $$$$    $$$$$   $$       $$  $$   $$$$ $$  $$  $$  $$$$   $$$     $$  $$  $$  $$")
print("   $$$   $$  $$  $$       $$    $$$$$  $$   $$ $$$$  $$$$$$   $$      $$$   $$  $$   $$$$$")
print("$$   $$  $$  $$  $$       $$   $$  $$  $$   $$  $$$  $$       $$   $$   $$  $$$$$       $$")
print(" $$$$$    $$$$    $$$$$   $$    $$$$$   $$  $$   $$   $$$$$    $$   $$$$$   $$      $$$$$")

print("\n")

print("Version 1.0")

print("\n")

print("-----------------------------")
print("        SOCIALNETSPY        |")
print("-----------------------------")

print("\n")

print("------------------------------")

maininput = input("INPUT A USERNAME\n->")

print("\n")

print("---------------")
print("QUERY = " + maininput)
print("---------------")

print("Processing...")

query = "https://instagram.com/" + maininput
print("\n-----------")
print("Instagram:")
print("----------\n")
final_results = ""
for final_results in search(query, tld="co.in", num=4, stop=4, pause=2):
  print(final_results)
if final_results == "":
	print("Not found")

query0 = "https://youtube.com/" + maininput
print("\n-----------")
print("YouTube")
print("-----------\n")
final_requests0 = ""
for final_requests0 in search(query0, tld="co.in", num=4, stop=4, pause=2):
	print(final_requests0)
if final_requests0 == "":
	print("Not found")

query1 = "https://facebook.com/" + maininput
print("\n-----------")
print("Facebook")
print("-----------\n")
final_requests1 = ""
for final_requests1 in search(query1, tld="co.in", num=4, stop=4, pause=2):
	print(final_requests1)
if final_requests1 == "":
		print("Not found")

query2 = "https://tiktok.com/" + maininput
print("\n-----------")
print("TikTok")
print("-----------\n")
final_requests2 = ""
for final_requests2 in search(query2, tld="co.in", num=4, stop=4, pause=2):
	print(final_requests2)
if final_requests2 == "":
	print("Not found")

query3 = "https://snapchat.com/" + maininput
print("\n-----------")
print("Snapchat")
print("-----------\n")
final_requests3 = ""
for final_requests3 in search(query3, tld="co.in", num=4, stop=4, pause=2):
	print(final_requests3)
if final_requests3 == "":
	print("Not found")

query4 = "https://telegram.com/" + maininput
print("\n-----------")
print("Telegram")
print("-----------\n")
final_requests4 = ""
for final_requests4 in search(query4, tld="co.in", num=4, stop=4, pause=2):
	print(final_requests4)
if final_requests4 == "":
	print("Not found")

query5 = "https://linkedin.com/" + maininput
print("\n-----------")
print("LinkedIn")
print("-----------\n")
final_requests5 = ""
for final_requests5 in search(query5, tld="co.in", num=4, stop=4, pause=2):
	print(final_requests5)
if final_requests5 == "":
	print("Not found")

query6 = "https://tripadvisor.com/members/" + maininput
print("\n-----------")
print("Trip Advisor")
print("-----------\n")
final_requests6 = ""
for final_requests6 in search(query6, tld="co.in", num=4, stop=4, pause=2):
	print(final_requests6)
if final_requests6 == "":
	print("Not found")

query7 = "https://pinterest.com/" + maininput
print("\n-----------")
print("Pinterest")
print("-----------\n")
final_requests7 = ""
for final_requests7 in search(query7, tld="co.in", num=4, stop=4, pause=2):
	print(final_requests7)
if final_requests7 == "":
	print("Not found")

query8 = "https://twitter.com/" + maininput
print("\n-----------")
print("Twitter")
print("-----------\n")
final_requests8 = ""
for final_requests8 in search(query8, tld="co.in", num=4, stop=4, pause=2):
	print(final_requests8)
if final_requests8 == "":
	print("Not found")

query9 = "https://twitch.com/" + maininput
print("\n-----------")
print("Twitch")
print("-----------\n")
final_requests9 = ""
for final_requests9 in search(query9, tld="co.in", num=4, stop=4, pause=2):
	print(final_requests9)
if final_requests9 == "":
	print("Not found")

query10 = "https://reddit.com/user/" + maininput
print("\n-----------")
print("Reddit")
print("-----------\n")
final_requests10 = ""
for final_requests10 in search(query10, tld="co.in", num=4, stop=4, pause=2):
	print(final_requests10)
if final_requests10 == "":
	print("Not found")

query22 = "https://soundcloud.com/" + maininput
print("\n-----------")
print("SoundCloud")
print("-----------\n")
final_requests22 = ""
for final_requests22 in search(query22, tld="co.in", num=4, stop=4, pause=2):
	print(final_requests22)
if final_requests22 == "":
	print("Not found")

query23 = "https://open.spotify.com/user/" + maininput
print("\n-----------")
print("Spotify")
print("-----------\n")
final_requests23 = ""
for final_requests23 in search(query23, tld="co.in", num=4, stop=4, pause=2):
	print(final_requests23)
if final_requests23 == "":
	print("Not found")

query24 = "https://steamcommunity.com/id/" + maininput
print("\n-----------")
print("Steam")
print("-----------\n")
final_requests24 = ""
for final_requests24 in search(query24, tld="co.in", num=4, stop=4, pause=2):
	print(final_requests24)
if final_requests24 == "":
	print("Not found")

query25 = "https://gotinder.com/@" + maininput
print("\n-----------")
print("Tinder")
print("-----------\n")
final_requests25 = ""
for final_requests25 in search(query25, tld="co.in", num=4, stop=4, pause=2):
	print(final_requests25)
if final_requests25 == "":
	print("Not found")

query26 = "https://wikipedia.org/wiki/User:" + maininput
print("\n-----------")
print("Wikipedia")
print("-----------\n")
final_requests26 = ""
for final_requests26 in search(query26, tld="co.in", num=4, stop=4, pause=2):
	print(final_requests26)
if final_requests26 == "":
	print("Not found")

query27 = "https://" + maininput + "wordpress.com/"
print("\n-----------")
print("WordPress")
print("-----------\n")
final_requests27 = ""
for final_requests27 in search(query27, tld="co.in", num=4, stop=4, pause=2):
	print(final_requests27)
if final_requests27 == "":
	print("Not found")

query28 = "https://about.me/" + maininput
print("\n-----------")
print("AboutMe")
print("-----------\n")
final_requests28 = ""
for final_requests28 in search(query28, tld="co.in", num=4, stop=4, pause=2):
	print(final_requests28)
if final_requests28 == "":
	print("Not found")

query29 = "https://researchgate.net/profile/" + maininput
print("\n-----------")
print("ResearchGate")
print("-----------\n")
final_requests29 = ""
for final_requests29 in search(query29, tld="co.in", num=4, stop=4, pause=2):
	print(final_requests29)
if final_requests29 == "":
	print("Not found")

print("\n")

print("------------------------------------------------")
print("General Informations about " + maininput)
print("------------------------------------------------")

query17 = "source:" + maininput
print("\n-----------")
print("Find news results from a certain source in Google News about " + maininput)
print("-----------\n")

query11 = "site:" + maininput
print("\n-----------")
print("Websites named as " + maininput)
print("-----------\n")
final_requests11 = ""
for final_requests11 in search(query11, tld="co.in", num=4, stop=4, pause=2):
	print(final_requests11)
if final_requests11 == "":
	print("Not found")

query12 = "inurl:" + maininput
print("\n-----------")
print("URLs which contain " + maininput)
print("-----------\n")
final_requests12 = ""
for final_requests12 in search(query12, tld="co.in", num=4, stop=4, pause=2):
	print(final_requests12)
if final_requests12 == "":
	print("Not found")

query13 = "intitle:" + maininput
print("\n-----------")
print("Titles which contain " + maininput)
print("-----------\n")
final_requests13 = ""
for final_requests13 in search(query13, tld="co.in", num=4, stop=4, pause=2):
	print(final_requests13)
if final_requests13 == "":
	print("Not found")

query14 = "related:" + maininput
print("\n-----------")
print("Websites related to " + maininput)
print("-----------\n")
final_requests14 = ""
for final_requests14 in search(query14, tld="co.in", num=4, stop=4, pause=2):
	print(final_requests14)
if final_requests14 == "":
	print("Not found")

query15 = "intext:" + maininput
print("\n-----------")
print("Text of the links which contain " + maininput)
print("-----------\n")
final_requests15 = ""
for final_requests15 in search(query15, tld="co.in", num=4, stop=4, pause=2):
	print(final_requests15)
if final_requests15 == "":
	print("Not found")

query21 = "phonebook:" + maininput
print("\n-----------")
print("Find " + maininput + "'s phone number")
print("-----------\n")
final_requests21 = ""
for final_requests21 in search(query21, tld="co.in", num=4, stop=4, pause=2):
	print(final_requests21)
if final_requests21 == "":
	print("Not found")


query18 = "inpostauthor:" + maininput
print("\n-----------")
print("Find blog posts in Google Blog written by " + maininput)
print("-----------\n")
final_requests18 = ""
for final_requests18 in search(query18, tld="co.in", num=4, stop=4, pause=2):
	print(final_requests18)
if final_requests18 == "":
	print("Not found")

query19 = "link:" + maininput
print("\n-----------")
print("Find pages linking " + maininput + " to a domain or URL")
print("-----------\n")
final_requests19 = ""
for final_requests19 in search(query19, tld="co.in", num=4, stop=4, pause=2):
	print(final_requests19)
if final_requests19 == "":
	print("Not found")

query20 = "info:" + maininput
print("\n-----------")
print("Find information about " + maininput + "'s specific page, including the most recent cache, similar pages, etc")
print("-----------\n")
final_requests20 = ""
for final_requests20 in search(query20, tld="co.in", num=4, stop=4, pause=2):
	print(final_requests20)
if final_requests20 == "":
	print("Not found")

query16 = "map:" + maininput
print("\n-----------")
print("All locations related to " + maininput)
print("-----------\n")
final_requests16 = ""
for final_requests16 in search(query16, tld="co.in", num=4, stop=4, pause=2):
	print(final_requests16)
if final_requests16 == "":
	print("Not found")

print("\n")

print("-----------------------------")
print("        SOCIALNETSPY        |")
print("-----------------------------")


print("\n")

print(" $$$$$                    $$           $$   $$   $$           $$    $$$$$")
print("$$   $$                        $$$$$   $$   $$$  $$   $$$$    $$   $$   $$   $$$$   $$  $$")
print(" $$$      $$$$    $$$$$   $$       $$  $$   $$$$ $$  $$  $$  $$$$   $$$     $$  $$  $$  $$")
print("   $$$   $$  $$  $$       $$    $$$$$  $$   $$ $$$$  $$$$$$   $$      $$$   $$  $$   $$$$$")
print("$$   $$  $$  $$  $$       $$   $$  $$  $$   $$  $$$  $$       $$   $$   $$  $$$$$       $$")
print(" $$$$$    $$$$    $$$$$   $$   $$$$$   $$  $$   $$   $$$$$    $$   $$$$$   $$      $$$$$")

print("\n")

print("Version 1.0")

print("\n")

print("-----------------------------")
print("        SOCIALNETSPY        |")
print("-----------------------------")
