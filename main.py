import subprocess

#
#------TO DO-----------
#1. fix the fix headers method
#   a. fix the findLinks method
#   b. fix the replaceHref method
#
#2. fix the CLI interface ( inter() )
#   a. fix the interSub methods
#   



def pullSite(url):
    returnList = []
    pulledSite = subprocess.check_output(['curl','url'])
    returnList.append(url)
    returnList.append(sanitizer(pulledSite))
    return returnList

#This fixes the issues with python string manipulation and quotation marks and apostrophes
def sanitizer(unsatitizedCode):
    unsatitizedCode.replace('"','`')
    unsatitizedCode.replace("'",'`')
    return unsatitizedCode


def fixHeaders(urlInfo):
    startAt = urlInfo[1].find('<head>')
    endAt = urlInfo[1].find('</head>')
    theHeader = urlInfo[1][startAt:endAt+7]
    
    def findLinks(headerLink):
        #this will be a list of a list of link start and end positions aka a = [[1,4], [19,24]] thus [1,4] would denote the start of the link reference: '<link' and the end of the reference: '>'
        listOfLinks = []
        #this will iterate of the "<link" refernces and find the positions at which they start and stop for future reference
        while(headerLink[i].find('<link') != -1):


    def replaceHref(url, reference):
        theLength = len(reference)
        startAt = reference.find("href=`") + 6
        #This will fix the issue with finding the reference point(index) of the stoping point 
        fixPoint = 0
        endAt = reference[startAt:].find('`')
        endResult = reference[:startAt] + url + reference[startAt + endAt:]
        return endResult

def inter():
    ask = rawInput("Welcome to PullSite, a generic version of REDACTED.\n\nWe can pull a site and let you host the given site.\n\nSelect the options (the number) below:\n1. Pull Site and reconnect the header links.\n2. Give list of header links.\n3. Quit")
    if(ask == 1):
        interSub1()
    elif(ask == 2):
        interSub2()
    elif(ask == 3):
        quit()
    else:
        print("no such option available")
        inter()

    def interSub1():
    
    def interSub2():

def substituteLink(url, link):

    