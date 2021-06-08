import tkinter as tk


class Application(tk.Frame):
    def __init__(self, master=None):
        # Windowの初期設定を行う。
        super().__init__(master)

        # Windowの画面サイズを設定する。
        # geometryについて : https://kuroro.blog/python/rozH3S2CYE0a0nB3s2QL/
        self.master.geometry("300x200")

        # labelframe Widgetを作成する。
        # text : テキスト情報
        # width : 幅の設定
        # height : 高さの設定
        labelframe = tk.LabelFrame(width=300, height=300, text="labelframe")

        # Windowを親要素とした場合に、labelframe Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        labelframe.pack()

        # labelframe Widget(Frame)を親要素として、label Widgetを作成する。
        # text : テキスト情報
        # width : 幅の設定
        # height : 高さの設定
        # bg : 背景色の設定
        # 色の設定を変更する場合 : http://www.tcl.tk/man/tcl/TkCmd/colors.htm
        # Labelについて : https://kuroro.blog/python/Pj4Z7JBNRvcHZvtFqiKD/
        label = tk.Label(labelframe, text="label",
                         width=30, height=15, bg="orchid4")

        # labelFrame Widget(Frame)を親要素とした場合に、label Widgetをどのように配置するのか?
        # packについて : https://kuroro.blog/python/UuvLfIBIEaw98BzBZ3FJ/
        label.pack()


# Tkinter初学者参考 : https://docs.python.org/ja/3/library/tkinter.html#a-simple-hello-world-program
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(master=root)
    # Windowをループさせて、継続的にWindow表示させる。
    # mainloopについて : https://kuroro.blog/python/DmJdUb50oAhmBteRa4fi/
    app.mainloop()
