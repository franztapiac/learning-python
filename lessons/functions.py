# Favourite song on 12 Jan 2021
# Written by Franz A. Tapia Chaca
# on 13 Jan 2021

title = "Christ is Mine Forevermore"
artist = "City Alight"
releaseYear = "2016"
album = "Only a Holy God"
durationInSeconds = 5*60 + 28  # seconds
genre = "Christian worship"
CCLInum = 7036096  # reference number to song within licensed copyright library


def Artist():
    return artist


def ReleaseYear():
    return releaseYear


def Genre():
    return genre


def DoesFranzEnjoyTheSong():
    return True


print("My favourite song on 12 Jan 2021 was: ")
print(title)
print("by " + Artist() + ".")
print("It was released in " + ReleaseYear())
print("as part of their album " + album + ".")
print("The song is " + str(durationInSeconds) + " seconds, ")
print("and it's a " + Genre() + " song.")
print("Its reference number to the CCLI library is " + str(CCLInum) + ".")
print("Does Franz enjoy the song: " + str(DoesFranzEnjoyTheSong()))
