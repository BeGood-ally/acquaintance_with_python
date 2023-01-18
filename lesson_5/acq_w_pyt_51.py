text = "джек бодро ходил рядом с белым обшарпанным зданием, тонущем в густых сумерках"
print(' '.join(list(filter(lambda x: not ('а' in x or 'б' in x or 'в' in x), text.split()))))