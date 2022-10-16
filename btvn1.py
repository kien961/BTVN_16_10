d = dict(orange='cam', banana='chuoi', durian="sau rieng",kiwi="trai kiwi",tomato="ca chua",potato="khoai tay",coconut="qua dua",wattermelon="dua hau",tenten="qua1",huhuh="qua2")
print(d)
d.update({'orange':"qua cam"})
print(d)
d2 = {"sinh to 1":"bo","sinh to 2":"mang cau","sinh to 2":"xoai"}
d.update(d2)
for x in d:
    print("key: ", x)
print(len(d))