x = input("入れたい文字を入力してね！")
# x = "a"
l = ""
for _ in range(len(x)):
    l += "＊"

print("    　　　　　　　　　　　　　　　　　　　　　　　　　　　　　 ,, -―-、")
print("　　　　　　　　　　　　　　　　　　　　　　　　　　　　／　　　　 ヽ　 ＊＊"+l+"＊")
print("　　　　　　　　　　　　　　　　　　　　　　／￣￣／　　／i⌒ヽ､|　　　 　＊ "+x.translate(str.maketrans({chr(0x0021 + i): chr(0xFF01 + i) for i in range(94)}))+"! ＊")
print("　　　　　　　　　　　　　　　　　　　　　/　　（゜）/　　 ／　/　　　 　　"+l+"＊＊＊")
print("　　　　　　　　　　　　　　　　　　　　/　　　　 ト､.,../　,ー-､")
print("　　　　　　　　　　　　　　　　　　=彳　　　　　 ＼＼‘ﾟ。､｀ ヽ。、ｏ")
print("　　　　　　　　　　　　　　　　　　/ 　 　　　　　　　＼＼ﾟ。､。、ｏ")
print("　　　　　　　　　　　　　　　　　/　　　　　　　　　/⌒ ヽ ヽU　　ｏ")
print("　　　 　 　 　 　 　 　 　 ,. -^^ 　　　　　　 　 　|　　　　U　：l")
print("　　　　　　　　　　　　／　　　　　　　　　　　　　 |　　　　　|：!")
print("　　　　　　　 　 　 ／　　　　　　　　　　　 　 　.:/　　　　　Ｕ")
print("　　　　 　　　/l｢}/　　　　　　　　　　　　　　::／")
print("　　　　　　 　| l/　_ -―　　　　／　　:､＿／:}")
print("　　　　　　　∠＿ー‐ ＿ -一' 　　 :::::::／::::/")
print("　　　　　　　 　 ＼￣　　 　 　::::::::::::／}:/::/")
print("　　　　　　　　　　 ＼　.:::::::::::::::::::／　/:／")
print("　　　　　　　　　 　　/7￣￣￣｢|")
print("　　　　　　　　　　　 }｜　　　　l !＿＿")
print("　　　　　　　　　　　 |　＼　　　＼　ｰ-{")
print("　　　　　　　　　　　 ヽ ＼_>　　 　｀¨´")
print("　　　　　　　　　　　　 ｀¨´")