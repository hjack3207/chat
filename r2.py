def read_file(filename):
	with open(filename, 'r', encoding='utf-8-sig') as f:
		lines = []
		for line in f:
			lines.append(line.strip())
	return lines	

def convert(lines):
	person = None
	new = []
	allen_word_count = 0
	allen_sticker_count = 0
	allen_image_count = 0
	viki_word_count = 0
	viki_sticker_count = 0
	viki_image_count = 0
	for line in lines:
		s = line.split(' ')
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count = allen_sticker_count + 1
			elif s[2] == '圖片':
				allen_image_count = allen_image_count + 1
			else:		
				for m in s[2:]:
					allen_word_count = allen_word_count + len(m)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count = viki_sticker_count + 1
			elif s[2] == '圖片':
				viki_image_count = viki_image_count + 1
			else:	
				for m in s[2:]:
					viki_word_count = viki_word_count + len(m)
	print('allen說了', allen_word_count, '個字')
	print('allen傳了', allen_sticker_count, '貼圖')
	print('allen傳了', allen_image_count, '圖片')
	print('viki說了', viki_word_count, '個字')
	print('viki傳了', viki_sticker_count, '貼圖')
	print('viki傳了', viki_image_count, '圖片')
	return new

def write_file(lines, filename):
	with open(filename, 'w', encoding='utf-8-sig') as f:
		for line in lines:
			f.write(line + '\n')


def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	#write_file(line, 'output.txt')

main()

