dictionary = {}

choice = raw_input("Search/Add Word?(s/a)")
if choice == 'a':
    word = raw_input("Please Input:")
    scripts = raw_input("Script:")
    dictionary[str(word)] = str(scripts)
    print "OK!"
    print dictionary
