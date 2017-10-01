import os
import filecmp
import csv
import datetime

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
	Grade = {'Senior': 0, 'Junior': 0, 'Sophomore': 0, 'Freshman': 0}
	for x in data:
		if x['Class'] == 'Senior':
			Grade['Senior'] += 1
		elif x['Class'] == 'Junior':
			Grade['Junior'] += 1
		elif x['Class'] == 'Sophomore':
			Grade['Sophomore'] += 1
		elif x['Class'] == 'Freshman':
			Grade['Freshman'] += 1
	sorted_grade = sorted(Grade, key = lambda x: Grade[x], reverse = True)
	Grade_Total = []
	for x in sorted_grade:
		Grade_Total.append((x, Grade[x]))
	return Grade_Total


def findDay(a):
	birthday_dict = {}
	for x in a:
		day = x['DOB'].split('/')[1]
		if day not in birthday_dict.keys():
			birthday_dict[day] = 1
		else:
			birthday_dict[day] += 1
	return int(sorted(birthday_dict, key = birthday_dict.get, reverse = True)[0])


def findAge(a):
	age = []
	year_now = int(datetime.date.today().year)
	month_now = int(datetime.date.today().month)
	day_now = int(datetime.date.today().day)
	for x in a[1:]:
		birthmonth, birthday, birthyear = x['DOB'].split('/')
		if ((day_now >= int(birthday)) and (month_now >= int(birthmonth))):
			age.append(year_now - int(birthyear))
		else:
			age.append(year_now - int(birthyear) + 1)
	return int((sum(age) / len(age)))


def mySortPrint(a,col,fileName):
	csv_file = open(fileName, 'w')
	sort_lst = sorted(a, key = lambda x: x[col])
	for x in sort_lst:
		first = x['First']
		last = x['Last']
		email = x['Email']
		row = (first + ',' + last + ',' + email)
		csv_file.write(row + '\n')
	csv_file.close()
	return None 



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
	total += test(type(data),type([]),40)
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

