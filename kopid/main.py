
from typing import Tuple


list_input = []
data_input = ''
final_set = ()
list_dist = []
list_affect = []


def recursive_list(myList, index):
    # print(myList[index])
    if(index < len(myList)):
        list_final.append(myList[index])
        recursive_list(myList, index+1)
    # else:
        # find(myList, index-1, myList[index-1])


def find(myList, index, key):
    # print(key)
    for i in range(index):
        for j in range(len(myList[i])):
            # print("i", i, "j", j)
            # print(key)
            # print(updated_key)
            # print(myList[i][j], " ", key)
            if myList[i][0] == key:
                key = myList[i][j+1]
                recursive_list(myList[i], j)
    # find(myList, index-1, key)
    # if(myList[i][j])
    # if j >= len(myList[i])-1:
    # continue
    # print("j", j)
    # if j != 0:
    # recursive_list(myList[i], j)
    # else:
    # print(myList[i][j])
    # find(myList, index-1, key)
    # print(updated_key, " h ", i)
    # if len(myList[i])-1 >= 0:
    # find(myList, index-1, updated_key)


print('Masukkan rantai penyebaran:')
while 1:

    data_input = input()
    temp = data_input.split(' ')

    len_input = len(temp)

    list_input.append(temp)

    if temp[len_input-1] == 'selesai':
        break

    # list_affect.append(temp)

# print(len(list_input))
# print(list_input)
# print()

print('Perintah yang tersedia:')
print('1.  RANTAI PENYEBARAN ')
print('2.  CEK_PENULARAN ')
print('3.  EXIT ')

panjang_list = len(list_input)

while 1:
    list_final = []
    data_input = input('Masukkan perintah:')
    list_tujuan = []
    if data_input == 'EXIT':
        print("Goodbye~ Semoga virus KOPIT cepat berakhir.")
        break
    else:
        found = False
        temp = data_input.split(' ')
        # if temp[0] == 'r':
        if temp[0] == 'RANTAI_PENYEBARAN':
            # print("haha")
            for i in range(len(list_input)):
                if temp[1] == list_input[i][0]:
                    find(list_input, len(list_input), temp[1])
                    found = True
                elif i >= len(list_input)-1 and not found:
                    print("Maaf, nama ", temp[1],
                          " tidak ada dalam rantai penyebaran")
                    break
            final_set = set(list_final)
            print("Rantai penyebaran ", temp[1], ":")
            for e in final_set:
                print('- ', e)
            print()
        elif temp[0] == 'CEK_PENULARAN':
            for i in range(len(list_input)):
                # print(temp[2], list_input[i][0])
                if temp[2] == list_input[i][0]:
                    # print("dalam")
                    find(list_input, len(list_input), temp[2])
                    found = True

                elif i >= len(list_input)-1 and not found:
                    print(
                        "Maaf, nama ", temp[1], "dan ", temp[2], " tidak ada dalam rantai penyebaran")
                    break

                final_set = set(list_final)
                # print(final_set)
                for e in final_set:
                    # print(e)
                    if e == temp[1]:
                        print("Ya\n")
                        found = True
                        break
                    elif not found:
                        print("Tidak\n")
                        found = False
                        break
                # else:
                    # print("Tidak ")
                    # continue
        else:
            print("Maaf perintah tidak dikenali. Masukkan perintah yang valid.")
            continue
