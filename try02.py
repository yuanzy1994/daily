try:
    fh = open("test.txt", 'r')
    fh.write("try test file ...")

except IOError:
    print "IOerror!"

else:
    print "success!"
    fh.close()

finally:
    print "will out!"
