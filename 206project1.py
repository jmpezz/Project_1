import os
import csv

def getData(file):
	list_data = []
	fname = open(file, 'r')
	reader = csv.DictReader(fname)

	for row in reader:
		dict_data = dict(row)
		list_data.append(dict_data)
	return list_data


def mySort(data,col):
	sort_lst = sorted(data, key = lambda x: x[col])
	return sort_lst[0]['First'] + ' ' + sort_lst[0]['Last']


def classSizes(data):
	SrCount = 0
	JrCount = 0
	SophCount = 0
	FreshCount = 0

	lst_class = []

	for x in data:
		if x['Class'] == 'Senior':
			SrCount += 1
		elif x['Class'] == 'Junior':
			JrCount += 1
		elif x['Class'] == 'Sophomore':
			SophCount += 1
		elif x['Class'] == 'Freshman':
			FreshCount += 1
	lst_class.append(('Senior', SrCount))
	lst_class.append(('Junior', JrCount)) 
	lst_class.append(('Sophomore', SophCount)) 
	lst_class.append(('Freshman', FreshCount))

	return sorted(lst_class, key = lambda x: x[1], reverse = True)


def findDay(a):
	birthday_dict = {}
	for x in a:
		day = x['DOB'].split('/')[1]
		if day not in birthday_dict.keys():
			birthday_dict[day] = 1
		else:
			birthday_dict[day] += 1
	return int(sorted(birthday_dict, key = birthday_dict.get, reverse = True)[0])


# Find the average age (rounded) of the Students
def findAge(a):
# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	pass


#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
	csv = open(fileName, 'w')

	sort_list = sorted(a, key = lambda x: x[col])
	for x in sort_list:




################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),35)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

