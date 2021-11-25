from requests import get

print ("===== DEVASC PROJECT =====")
print ("This will display your local computer's information such as your public IP Address")
print ("")

#finds your own ip and information about your ip
print ('Your IP Address is ' + (get('https://ipapi.co/ip/').text))
print ('The city is ' +(get('https://ipapi.co/city/').text))
print ('The country is ' +(get('https://ipapi.co/country/').text))
print ('The currency of that country is ' +(get('https://ipapi.co/currency/').text))
print ('The languages that is being used are ' +(get('https://ipapi.co/languages/').text)) 
print ('The ASN is ' +(get('https://ipapi.co/asn/').text))
print("")

yn = input("Do you want to search the details of an IP Address? (wink wink) (Y/N)")
if (yn == "Y"):
    #enter an ip add
    ipad = input("Enter your ip address: ")
    print (get('https://ipapi.co/'+ipad+'/country/').text)
else:
    print("Thank you! :DD")


print("")
print("========================\nPrepared by:")
print("Ferrer, Vincent Russell \nMataga, Carl Jeric \nOlidana, Ma.Donna Rose\n4ITG")

# Backlog
# Develop GUI for this Python code using a toolkit to make the application more appealing to more common users
# Allow GUI to save information from past entries of IP addresses, both addresses detected by the API and user-inputted addresses