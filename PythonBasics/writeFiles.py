
#  if I use w it is overwrite the all text
employee_file = open("employee.txt","a")

employee_file.write("\nPihu- software")

employee_file.close()

htmlfile = open("index.html","w")
htmlfile.write("<p> Hello word</p>")
htmlfile.close()