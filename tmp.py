import pickle


# list_count = [5,]
# output = open('data.pkl','wb')
# pickle.dump(list_count,output)
# output.close()
# list_count = []
# pkl_file = open('data.pkl', 'rb')
# count = 1
# count_list = pickle.load(pkl_file)
# count += count_list[0]
# print count
#
# list_count.append(count)
# print  list_count
# output = open('data.pkl','wb')
# pickle.dump(list_count,output)
# output.close()




load_file=open("data.pkl",'rb')
count=1
count_list=pickle.load(load_file)
print count_list[0]
count+=count_list[0]
count_list[0]=count
load_file.close()
dump_file=open("data.pkl",'wb')
pickle.dump(count_list,dump_file)
dump_file.close()

a = "hello".join("fsdfsfs")
print a