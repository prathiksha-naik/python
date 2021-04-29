def string_1():
    message="welcome to Mysore"
    word=message[-7:]
    if(word=="mysore"):
        print("got it")
    else:
        message=message[3:14]
        print(message)
string_1()     

def strings_2():
    song="JINGLE Bells jingle Bells Jingle All The Way"
    song.upper()
    song_words=song.split()
    count=0
    for word in song_words:
        if(word.startswith("jingle")):
            count=count+1
            print(count)
strings_2()
