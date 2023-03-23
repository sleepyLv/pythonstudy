def print_list(list):
    for song in list:
        print(f"I like {song}")


favourite_songs = ["7 rings", "SOS", "杀手"]

# print song in the list
print_list(favourite_songs)

# delete one song
delete_song = favourite_songs.pop()
print(f"delete {delete_song},the list is:")
print_list(favourite_songs)

# add one song
add_song = "半岛铁盒"
favourite_songs.append(add_song)
print(f"add {add_song},the list is:")
print_list(favourite_songs)

