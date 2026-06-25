justice_league = ["Superman", "Batman", "Wonder Woman", "Flash", "Aquaman", "Green Lantern"]
print(f"1. Total members: {len(justice_league)}") # Print the total number of members in the justice league

justice_league.extend(["Batgirl", "Nightwing"]) # Add new members to the justice league
print(f"2. New team after recruitement{justice_league}") # Print the updated list of members in the justice league after recruitment

justice_league.remove("Wonder Woman") # Remove Wonder Woman from the list
justice_league.insert(0, "Wonder Woman") # Insert Wonder Woman at the beginning of the list
print(f"3. Moving new leader at front: {justice_league}") # Print the updated list with Wonder Woman as the new leader

justice_league.remove("Superman") # Remove Superman from the list
aquaman_idx = justice_league.index("Aquaman") # Find the index of Aquaman in the list
justice_league.insert(aquaman_idx, "Superman") # Insert Superman at the index of Aquaman
print(f"4. Seperate Flash and Aquaman: {justice_league}") # Print the updated list with Supermans and Aquamans separated

justice_league = ["Cyborg", "Shazam", "Hawkgirl", "Martian Manhunter", "Green Arrow"] # Add new members to the justice league
print(f"5. Crisis Team: {justice_league}") # Print the new crisis team members in the justice league

justice_league.sort() # Sort the list of members in the justice league in alphabetical order
new_leader = justice_league[0] # Assign the first member in the sorted list as the new leader
print(f"6. Sorted list: {justice_league}") # Print the sorted list of members in the justice league
print(f"The new leader is: {new_leader}") # Print the new leader of the justice league