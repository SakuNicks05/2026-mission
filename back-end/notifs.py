import numpy as np
import pandas as pd
import requests

def encourage_func():
    encouragement_array = np.array(["Well done for showing up today—faithfulness matters",
                                    "That time you set aside wasn’t small; it was meaningful",
                                    "You chose presence over pressure today. That counts",
                                    "One day at a time—today’s devotion is a win",
                                    "What you planted today will bear fruit in time",
                                    "You honored God with your time today—be encouraged",
                                    "Take this peace with you into the rest of your day",
                                    "Consistency is being built, even in quiet moments like this",
                                    "Let today’s devotion settle gently into your heart",
                                    "You did this—not out of obligation, but intention"])
    rand_num = np.random.default_rng()
    max = 10
    print("REPEAT ALLOWED:")
    for num in range(7): # allows repeats
        i = rand_num.integers(0, max)
        print(f"Day {num + 1}: {encouragement_array[i]}")

    print("\nREPEAT NOT ALLOWED:")
    for num in range(7): # does NOT repeats
        i = rand_num.integers(0, max)
        print(f"Day {num + 1}: {encouragement_array[i]}")
        np.delete(encouragement_array, i)
        max -= 1

# encourage_func()

def daily_verse():
    url = "https://beta.ourmanna.com/api/v1/get/?format=json"
    try:
        source = requests.get(url)
        source.raise_for_status() # jumps to except if return 404
        verse_data = source.json()
        verse = verse_data["verse"]["details"]["text"]
        reference = verse_data["verse"]["details"]["reference"]
        print(f"{verse} \n - {reference}")
    except requests.RequestException as e:
        print(f"Error fetching verse: {e}")

daily_verse()