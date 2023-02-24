import os
import csv


csvFile = os.path.join("resources", "election_data.csv")

count=0;
candidateVote = dict()
candidateVotePerc = dict()
winner=""
maxVote=0

with open(csvFile) as file :
    csvreader = csv.DictReader(file, delimiter=",")

    for row in csvreader:
        count = count+1
        candidateName = row["Candidate"]
        if(candidateVote.get(candidateName) == None):
            candidateVote[candidateName]=1
        else:
            candidateVote[candidateName] = candidateVote[candidateName] + 1
    
    for name in candidateVote.keys():
        candidateVotePerc[name] = "%.3f" %(candidateVote[name]/count*100)
        if(candidateVote[name]>maxVote):
            maxVote=candidateVote[name]
            winner=name
    

    #print(count)
    names=""
    for name in candidateVote.keys():
       if(names != ""):
          names = names+"\n    "     
       names =  names  + "{} : {}% ({})" .format(name, candidateVotePerc[name], candidateVote[name])
    

    outputStr = """
    Election Results
    -------------------------
    Total Votes: {}
    -------------------------
    {}
    -------------------------
    Winner: {}
    -------------------------
    """.format(str(count), names, winner)

    ### printing the output in terminal
    print(outputStr)

    ### writing the output in text file
    textFile = os.path.join("analysis", "output.txt")
    with open(textFile, "w") as f:
        f.write(outputStr)


