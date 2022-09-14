




duration = 36576.7

totalClips = int(duration//60)

clipStart = 0
clipEnd = 60


for i in range(totalClips):
    print("Clip Start: " + str(clipStart))
    print("Clip End: " + str(clipEnd))

    if i < totalClips:
        clipStart += 60
        clipEnd += 60




