import md5

counter = 1

pass_in = raw_input("Please enter the md5 Hash: ")
pwfile = raw_input("Please enter the password fie name: ")



try:
    pwfile=open(pwfile, "r")

except:
    print "\nFile NOT FOUND. ERROR 404."
    quit()

for paswword in pwfile:
    filemd5 = md5.new(paswword.strip()).hexdigest()
    print "Trying password number %d: %s" %(counter,paswword.strip())

    counter += 1

    if pass_in== filemd5:
        print ("\nMatch Found. \nPassword is : %s " % paswword)
        break
    
    else: print "\nPassword Not Found"