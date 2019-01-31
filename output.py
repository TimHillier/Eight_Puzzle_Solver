
outputName = "HillierOutput.txt"
def initFile():
    file = open(outputName,"w+")
    file.write("Tim Hiller\n230108884\n\n")
    file.close()

def writeToFile(toWrite):
    file = open(outputName,"a+")
    file.write(toWrite+"\n")
    file.close()

