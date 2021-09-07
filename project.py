import csv

# Create an empty insurances list 
insurances = []
with open("insurance.csv") as ins_file:
    insurances_obj = csv.DictReader(ins_file)
    i = 0
    for ins in insurances_obj:
        insurances.append(ins)

# Function for calculating an average of the given list
def get_average(data):
    total = 0
    for item in data:
        total += float(item)
    return total / len(data)

# Get the list of fiven field name
def full_list(field_name):
    return [float(item[field_name]) for item in insurances]

# Compare two given fields between each other. There are three parameters:
# The first field is taken as category. 
# The second field is for average calculating
# The third parameter for limit by given (field, key). Is optional
# So the function will print the condition (if given) and the average of the second field distributed by the first field
def compare_two_fields(field_1, field_2, field_condition = ('no', 'no')):
    field_1_unique = {}
    for item in insurances:
        if field_condition[0] != 'no': 
            if item[field_condition[0]] != field_condition[1]:
                continue
        if item[field_1] not in field_1_unique:
            field_1_unique.update({item[field_1]: []})
        field_1_unique[item[field_1]].append(item[field_2])
    field_1_avg = {}
    print("Average {} by {} is:".format(field_2, field_1))
    if field_condition[0] != 'no':
        print("Only for {} is {}".format(field_condition[0], field_condition[1]))
    for key, val in sorted(field_1_unique.items()):
        field_1_avg.update({key: get_average(val)})
        print(str(key) + '=>' + str(round(field_1_avg[key], 2)))

# Calc how many rows are in insurance list distributed by the given field. 
# The second parameter for limit by given (field, key). Is optional 
def compare_field_vs_count(field_1, field_condition = ('no', 'no')):
    field_1_unique = {}
    for item in insurances:
        if field_condition[0] != 'no':
            if item[field_condition[0]] != field_condition[1]:
                continue
        if item[field_1] not in field_1_unique:
            field_1_unique.update({item[field_1]: 0})
        field_1_unique[item[field_1]] += 1

    print("Number of people by {} is:".format(field_1))
    if field_condition[0] != 'no':
        print("Only for {} is {}".format(field_condition[0], field_condition[1]))
    for key, val in sorted(field_1_unique.items()):
        print(str(key) + '=>' + str(val))


# Let's test functions:
#
# print(get_average(full_list('age')))
# compare_two_fields('region', 'charges', ('smoker', 'no'))
# compare_two_fields('smoker', 'age')
# compare_field_vs_count('smoker')
compare_field_vs_count('smoker', ('region', 'northwest'))


# Further analysis of data like finding some correlations, linear regression functions, etc. makes sense with statistical modules. So it will be added after...