
Names=("John", "Fred", "Waldo", "Wally", "Waldorama", "Susan", "Nick", "Waldo",
       "Waldo", "Reese", "Haythem", "Kim", "Ned", "Ron")

search_term = "Waldo"
count=Names.count('Waldo')
if search_term in Names:
    print(search_term+" appears at least once in the tuple.")
print("Waldo comes out", count, "times.")

