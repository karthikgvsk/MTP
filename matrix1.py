no_of_parts = 16
no_of_dirs = 3
input_file = open("operations.txt", "r")
output_file = open("new", "w")
matrix = []
for i in range(no_of_parts):
	l = []
	for j in range(no_of_parts * no_of_dirs):
		l.append(0)
	matrix.append(l)
print matrix

for op in input_file:
	op = op.split()
	print op

	part_1 = int(op[0])
	part_2 = int(op[1])
	dir_ = int(op[2])

	row = (part_1 - 1)
	col = (part_2 - 1) * no_of_dirs + (dir_ - 1)
	matrix[row][col] = 1

print matrix
output_file.write(str(matrix))