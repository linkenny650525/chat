def read_file(filename):
    with open (filename, 'r', encoding = 'utf-8-sig') as f:
        lines = []
        for line in f:
            lines.append(line.strip())
        return lines

def convert(lines):
    person = None
    allen_word_count = 0
    allen_sc = 0
    allen_image = 0
    viki_image = 0
    viki_sc = 0
    viki_word_count = 0
    for line in lines:
        s = line.split(' ')
        time = s[0]
        name = s[1]
        if name == 'Allen':
            if s[2] == '貼圖':
                allen_sc +=1
            elif s[2] == '圖片':
                allen_image += 1
            else:
                for m in s[2:]:
                    allen_word_count += len (m)
        elif name == 'Viki':
            if s[2] =='貼圖':
                viki_sc += 1
            elif s[2] == '圖片':
                viki_image += 1
            else:
                for m in s[2:]:
                    viki_word_count += len (m)
    print ('allen說了: ', allen_word_count, '個字 傳了', allen_sc ,'貼圖', allen_image, '圖片')
    print ('viki說了: ', viki_word_count, '個字 傳了', viki_sc ,'貼圖', viki_image, '圖片')
    
def write_file(filename,lines):
    with open (filename, 'w', encoding = 'utf-8-sig') as f:
        for line in lines:
            f.write(line + '\n')
        return lines
def main():
    lines = read_file('-LINE-Viki.txt')
    lines = convert(lines)
    #write_file('output.txt',lines)

main()

