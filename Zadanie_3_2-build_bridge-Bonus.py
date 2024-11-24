def build_bridge(chunk, goal):
    if chunk <= 0 or goal <= 0:
        return False    
    segment_length = 1.5 * chunk
    rest_from_goal = goal % segment_length

    if goal % segment_length == 0:
        return True
    elif rest_from_goal % chunk == 0:
        return True
    else:
        return False

# Przykład interakcji z użytkownikiem
goal = int(input("Please enter the length of the bridge: "))
chunk = int(input("Please enter the length of the chunk: "))

if build_bridge(chunk, goal):
    print(f"You can build a bridge with {chunk} chunks and {goal} goal")
else:
    print(f"You can NOT build a bridge with {chunk} chunks and {goal} goal")


