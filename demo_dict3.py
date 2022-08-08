import json

fl_st = open('stu.json')
js_stu = json.load(fl_st)
for a in js_stu['stu']:
    print(a)
