import numpy as np
import pandas as pd

def track_daily():
    week_devos = np.array([True, False, True, True, True, False, False])
    print(week_devos)
    missed_devos = []
    accomplished_devos = []

    for i, status in enumerate(week_devos):
        if status != 0:
            accomplished_devos = np.append(accomplished_devos, status)
            print(f"Day {i + 1}: Finished! Keep going!")
        else:
            missed_devos = np.append(missed_devos, status)
            print(f"Day {i + 1}: Didn't do devotional.")

            match len(missed_devos):
                case 1:
                    print("Don't forget to do your devotional!")
                    # note to return a value later on for extra checking
                case 2:
                    print("Doing your daily devotional strengthens the spirit!")
                case 3:
                    print("Your spirit is hungry!")
                case 4:
                    print("Spirit is in critical health!")

    print(f"Missed devos: {len(missed_devos)}") # number of missed devos
    print(f"Accomplished devos: {len(accomplished_devos)}") # number of accomplished devos

track_daily()