'''
This file loads all the csv files generated by bookBarn spiders and using them,
it creates three files csv files:
1. Genre ID and generes
2. Author ID, authors name and author about [:50]
3. Publisher ID and publishers
'''

import os
import csv
import glob

#username is fetched and other path is same in all linux systems
username = os.environ.get('USERNAME')
#Moving to SpiderGenerated folder containg book*.csv files
dir = '/home/' + username + '/Documents/GitRepositories/bookbarn/ScrappedData/csvFiles/SpiderGenerated'
try:
    os.chdir(dir)
except:
    print('## Wrong directory!!')
    print('Note : Correct the directory path in generateCSV.py line no. 16')
    exit()


#get all csv files with the name book*.csv
files = sorted(glob.glob('book*.csv'))

#contains unique authors and their IDs
authorDict = {}
#contains unique genres and their IDs
genreDict = {}
#contains unique publishers and their IDs
publisherDict = {}

aid = 100000000   #starrting point of author ID and 'A' is prefixed
gid = 500000000   #starrting point of genre ID and 'G' is prefixed
pid = 700000000   #starrting point of publisher ID and 'P' is prefixed


for file in files:
    #loading each csv file as DictReader and
    #creating corresponding dictionaries of authors, genres and publishers
    with open(file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            akey = row['AuthorName'] + ' ' + row['AboutAuthor'][:50]
            if(akey not in authorDict):
                authorDict[akey] = 'A' + str(aid)
                aid += 1

            pkey = row['Publisher']
            if(pkey == ''):
                pkey = 'No Publisher'
            if(pkey not in publisherDict):
                publisherDict[pkey] = 'P' + str(pid)
                pid += 1

            genres = row['Genres'].split(',')
            for gkey in genres:
                gkey = gkey.strip()
                if(gkey == ''):
                    gkey = 'No Genre'
                if(gkey not in genreDict):
                    genreDict[gkey] = 'G' + str(gid)
                    gid += 1


#Moving to ScriptGenerated folder containing authorID etc csv files
dir = '/home/' + username + '/Documents/GitRepositories/bookbarn/ScrappedData/csvFiles/ScriptGenerated'
try:
    os.chdir(dir)
except:
    print('## Wrong directory!!')
    print('Note : Correct the directory path in generatedCSV.py line no. 70')
    exit()


#Writing authorIDs
with open('authorIDs.csv', 'w') as auth:
    fieldnames = ['AuthorID', 'Author_about']
    csv_writer = csv.DictWriter(auth, fieldnames=fieldnames)

    csv_writer.writeheader()

    for key in authorDict:
        csv_writer.writerow({'AuthorID' : authorDict[key], 'Author_about' : key})


#Writing genreIDs
with open('genreIDs.csv', 'w') as gen:
    fieldnames = ['GenreID', 'Genre']
    csv_writer = csv.DictWriter(gen, fieldnames=fieldnames)

    csv_writer.writeheader()

    for key in genreDict:
        csv_writer.writerow({'GenreID' : genreDict[key], 'Genre' : key})


#Writing publisherIDs
with open('publisherIDs.csv', 'w') as pub:
    fieldnames = ['PublisherID', 'Publisher']
    csv_writer = csv.DictWriter(pub, fieldnames=fieldnames)

    csv_writer.writeheader()

    for key in publisherDict:
        csv_writer.writerow({'PublisherID' : publisherDict[key], 'Publisher' : key})
