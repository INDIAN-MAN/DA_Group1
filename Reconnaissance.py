#Reconnaissance
import requests #use the requests library
targeted_url = 'http://172.18.58.80/multi' #set the targeted url
webpage = requests.get(targeted_url) # this is the url
print(webpage.text) #this will get the full webpage in text
print("status code:") #get and print the status code
print("\t *", webpage.status_code)
h = requests.head(targeted_url) #gets the headers
print("Header:")
print("Header starts here")
for x in h.headers: #to print line by line
    print("\t ", x, ":", h.headers[x])
print("Header ends here")
headers = {'User-Agent' : 'Mobile'} #Modify the headers user-agent
targeted_url2 = 'http://httpbin.org/headers' #test it on an external site
requests_header = requests.get(targeted_url2, headers=headers)
print(requests_header.text)
