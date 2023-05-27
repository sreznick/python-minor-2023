text = 'wdqdf ifwdfdw   ffqw fwfwq'
starts = {index: c2 for index, (c1, c2) in enumerate(zip(text, text[1:])) if c1 == ' ' and c2 != ' '}
print(starts)

