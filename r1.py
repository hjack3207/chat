def read_file(filename):
	with open(filename, 'r', encoding='utf-8-sig') as f:
		lines = []
		for line in f:
			lines.append(line.strip())
	return lines	

def convert(lines):
	person = None
	new = []
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		if person:	
			new.append(person + ': ' + line)
	return new

def write_file(new, filename):
	with open(filename, 'w', encoding='utf-8-sig') as f:
		for line in new:
			f.write(line + '\n')


def main():
	lines = read_file('input.txt')
	new = convert(lines)
	write_file(new, 'output.txt')

main()

