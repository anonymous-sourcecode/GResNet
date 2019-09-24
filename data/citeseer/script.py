

if 1:
	name_index_dict = {}
	index = 0
	f = open('node3', 'r')
	for line in f:
		name = line.split()[0]
		if name not in name_index_dict:
			name_index_dict[name] = index	
			index = index + 1
	f.close()

	f_read = open('node3', 'r')
	f_write = open('node', 'w')	
	for line in f_read:
		line = line.rstrip()
		entry_list = line.split()
		name = entry_list[0]
		index = name_index_dict[name]
		f_write.write(str(index) + '\t')
		for i in range(1, len(entry_list)-1):
			f_write.write(entry_list[i] + '\t')
		f_write.write(entry_list[len(entry_list)-1] + '\n')
		f_write.flush()
	f_write.close()
	f_read.close()

	f_read = open('link3', 'r')
	f_write = open('link', 'w')
	for line in f_read:
		line = line.rstrip()
		name1, name2 = line.split()
		if name1 not in name_index_dict or name2 not in name_index_dict:
			continue
		id1 = name_index_dict[name1]
		id2 = name_index_dict[name2]
		f_write.write(str(id1) + '\t' + str(id2) + '\n')
		f_write.flush()
	f_write.close()
	f_read.close()
