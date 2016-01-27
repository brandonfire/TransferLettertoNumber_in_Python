#!/usr/bin/python
# Author: Chengbin Hu
#

def transfer(str):
	leng = len(str)
	value = 0
	for item in str:
		leng = leng - 1
		value = value + (ord(item)-ord('A')+1)*(25 **leng)
	return value

def test():
        print('Transfer AA to')
        print(transfer('AA'))

        print('Transfer AX to')
        print(transfer('AX'))



if __name__ == "__main__":
        test()
