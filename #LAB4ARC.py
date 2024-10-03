#LAB4ARC

import csv

#open the CSV file
with open('budget_data.csv', 'r') as file :
    reader = csv.reader(file)
    data = list(reader)

#printing the first few records to show the original
print("Original Dataset:")
for row in data[:5]:
    print(row)

def selection_sort(data):
    for x in range(len(data)):
        #finding the smallest date in the unsorted portion of the list
        minimum = x
        for y in range(x+1, len(data)):
            if data[y][0] < data[minimum][0]:
                minimum = y

        #changing the smallest date with the current position
        data[x], data[minimum] = data[minimum], data[x]

    return data

def insertion_sort(data):
    for x in range(1, len(data)):
        key = data[x]
        y = x-1
        while y >= 0 and data[y][0] > key[0]:
            data[y+1] = data[y]
            y -= 1
        data[y+1] = key

    return data

#selection sort to the dataset and printing the first records of the sorted dataset
sorted_data_selection = selection_sort(data)

print("\nSorted Dataset (Selection Sort):")
for row in sorted_data_selection[:5]:
    print(row)

#insertion sort to the dataset and printing the first records of the sorted dataset
sorted_data_insertion = insertion_sort(data)

print("\nSorted Dataset (Insertion Sort):")
for row in sorted_data_insertion[:5]:
    print(row)