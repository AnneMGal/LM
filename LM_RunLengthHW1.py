import sys

def encode(input_string):
    count = 1
    prev = ''
    lst = []
    for character in input_string:
        if character != prev:
            if prev:
                entry = (prev,count)
                lst.append(entry)
                #print lst
            count = 1
            prev = character
        else:
            count += 1

    # last character
    entry = (character,count)
    lst.append(entry)
    
    return lst
  
def list2string(lst):
    encoded_string = ''
    for (letter, count) in lst:
        encoded_string += letter + str(count)

    return encoded_string

def decode(lst):
    q = ""
    for character, count in lst:
        q += character * count
    return q
 
input_string = sys.argv[1]
encoded_list = encode(input_string)
encoded_string = list2string(encoded_list)
decoded_string = decode(encoded_list)


print "input: " + input_string
print "encoded list: " + str(encoded_list)
print "encoded string: " + encoded_string
print "decoded string: " + decoded_string

compression_ratio = len(encoded_string) / float(len(input_string))
print "  compression ratio: %.2f %%" % (compression_ratio*100)

if compression_ratio > 1:
    print "     WARNING: len(RLE) > len(original): not many duplicates found, consider not using RLE"

if input_string == decoded_string:
    print "input == decoded: SUCCESS!"
else:
    print "input != decoded: FAIL!"

# warning: potential encoding collision, eg:
'''
As-MacBook-Pro:LearningMachines_HW1 AM_local$ python LM_RunLengthHW1.py 1111111111112
input: 1111111111112
encoded list: [('1', 12), ('2', 1)]
encoded string: 11221
decoded string: 1111111111112

As-MacBook-Pro:LearningMachines_HW1 AM_local$ python LM_RunLengthHW1.py 1222222222222222222222
input: 1222222222222222222222
encoded list: [('1', 1), ('2', 21)]
encoded string: 11221
decoded string: 1222222222222222222222
'''