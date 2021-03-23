import re
file_object  = open(r'C:\Users\Owner\Desktop\RegularExpression.txt', 'r+',encoding='utf-8',errors='ignore')
file_object.seek(0)
a=file_object.read()
file_object.close()
ip = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",a)
email =  re.findall(r'[a-zA-Z0-9]+@[a-zA-Z]+\.[a-zA-Z\.]+\.[a-zA-Z\.]+[a-zA-Z]', a)
Call_ID = re.findall(r'Call-ID:(.*)',a)
From = re.findall(r'From:(.*)',a)
To = re.findall(r'To:(.*)',a)
f = open(r'C:\Users\Owner\Desktop\answer.txt', 'w+',encoding='utf-8',errors='ignore')
f.write("Email: \n")
for i in email:
	f.write(i)
	f.write("\n")
f.write("\nIP: \n")
for i in ip :
	f.write(i)
	f.write("\n")
f.write("\nCall ID: \n")
for i in Call_ID :
	f.write(i)
	f.write("\n")
f.write("\nFrom: \n")
for i in From :
	f.write(i)
	f.write("\n")
f.write("\nTo: \n")
for i in To :
	f.write(i)
	f.write("\n")
f.close()
print("\n Please see the answer.txt for the answer")
