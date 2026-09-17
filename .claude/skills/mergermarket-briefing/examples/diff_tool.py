import re, difflib

def load(p):
    d={}
    order=[]
    for line in open(p, encoding='utf-8'):
        line=line.rstrip('\n')
        if not line.strip(): continue
        m=re.search(r'/content/(\d+)', line)
        key=m.group(1) if m else line[:40]
        d[key]=line
        order.append(key)
    return d, order

fin, forder = load('final_robert.txt')
dra, dorder = load('draft_nico.txt')

print("Final entries:", len(fin), "Draft entries:", len(dra))
print("Nur im Final:", set(fin)-set(dra))
print("Nur im Draft:", set(dra)-set(fin))
print("Reihenfolge identisch:", forder==dorder)
print("="*80)

n=0
for k in forder:
    if k not in dra: continue
    f=fin[k]; d=dra[k]
    if f==d: continue
    n+=1
    fw=f.split(); dw=d.split()
    sm=difflib.SequenceMatcher(None, dw, fw)
    parts=[]
    for tag,i1,i2,j1,j2 in sm.get_opcodes():
        if tag=='equal': continue
        old=' '.join(dw[i1:i2]); new=' '.join(fw[j1:j2])
        if tag=='replace': parts.append(f'   DRAFT: «{old}»  ->  FINAL: «{new}»')
        elif tag=='delete': parts.append(f'   GESTRICHEN: «{old}»')
        elif tag=='insert': parts.append(f'   ERGAENZT: «{new}»')
    name=re.sub(r'^\* \d\d\.\d\d\.\d\d: ','',f)[:45]
    print(f'[{n:02d}] {name}')
    for p in parts: print(p)
    print()
print("="*80)
print("Geaenderte Eintraege:", n, "von", len(fin))
