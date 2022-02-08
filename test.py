import eel

eel.init("web")

@eel.expose
def txt_reader():
    file = open("info.txt", "r")
    text = file.read()
    return text

print(txt_reader())

eel.start("index.html", size = (1500, 900))