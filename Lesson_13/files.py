import os

#data_file = open('data.txt', 'r')
#data_file.read()
#print('sdssdsd' + 1)
#data_file.close()

base_path = os.path.dirname(__file__)
#base_path = 'C:\\users\\username\\projects\\test-projects\\Lesson_13'
#file_path = f'{base_path}/data.txt'
file_path = os.path.join(base_path, 'data.txt')
new_file_path = os.path.join(base_path, 'data2.txt')
print(file_path)

def read_file():
    with open(file_path, 'r') as data_file:
        #print(data_file)
        for line in data_file.readlines():
            yield line

for data_line in read_file():
    with open(new_file_path, 'a') as new_file:
        data_line = data_line.replace('.', '').replace(',', '')
        new_file.write(data_line)

test_project_path = os.path.dirname(base_path)
viktor_file_path = os.path.join(test_project_path, 'test.txt')
print(viktor_file_path)

with open(viktor_file_path) as viktor_file:
    print(viktor_file.read())