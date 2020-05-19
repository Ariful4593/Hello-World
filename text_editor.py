from tkinter import *
from tkinter import filedialog
class text_editor:
    current_open_file = "no_file"

    #function for open_file...
    def open_file(self):
        open_return = filedialog.askopenfile(initialdir="/", title="Select file to open", filetypes=(("text files", "*.txt"), ("all files", "*.*")))
        if open_return != None:
            self.text_area.delete(1.0, END)
            for line in open_return:
                self.text_area.insert(END, line)
            self.current_open_file = open_return.name
            open_return.close()


    #function for save as file...
    def save_as_file(self):
        f = filedialog.asksaveasfile(mode='w', defaultextension=".txt")
        if f is None:
            return
        text_to_save = self.text_area.get(1.0, END)
        self.current_open_file=f.name
        f.write(text_to_save)
        f.close()


    #function for save file...
    def save_file(self):
        if self.current_open_file == "no_file":
            self.save_as_file()
        else:
            f = open(self.current_open_file, "w+")
            f.write(self.text_area.get(1.0,END))
            f.close()


    def new_file(self):
        self.text_area.delete(1.0,END)
        self.current_open_file="no_file"


    def copy_text(self):
        self.text_area.clipboard_clear()
        self.text_area.clipboard_append(self.text_area.selection_get())

    def cut_text(self):
        self.copy_text()
        self.text_area.delete("sel.first","sel.last")

    def paste_text(self):
        self.text_area.insert(INSERT, self.text_area.clipboard_get())


    def __init__(self,master):

        self.master = master
        master.title("Notepad++")
        self.text_area = Text(self.master, undo=True)
        self.text_area.pack(fill=BOTH, expand=1)
        self.main_menu = Menu()
        self.master.config(menu=self.main_menu)

        #Show a file menu
        self.file_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="File", menu=self.file_menu)

        self.file_menu.add_command(label="New", command=self.new_file)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_command(label="Open Containing Folder")
        self.file_menu.add_command(label="Open in Default Viewer")
        self.file_menu.add_command(label="Open folder As Workspace")
        self.file_menu.add_command(label="Reload from Disc")
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save As", command=self.save_as_file)
        self.file_menu.add_command(label="Save a Copy As")
        self.file_menu.add_command(label="Save All")
        self.file_menu.add_command(label="Rename")
        self.file_menu.add_command(label="Close")
        self.file_menu.add_command(label="Close All")
        self.file_menu.add_command(label="Close More")
        self.file_menu.add_command(label="Move to recycle Bin")
        self.file_menu.add_command(label="Exit", command=master.quit)

        #Show a Edit Menu
        self.edit_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="Edit", menu=self.edit_menu)

        self.edit_menu.add_command(label="Undo", command=self.text_area.edit_undo)
        self.edit_menu.add_command(label="Redo", command=self.text_area.edit_redo)
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Copy",command=self.copy_text)
        self.edit_menu.add_command(label="Cut",command=self.cut_text)
        self.edit_menu.add_command(label="Paste",command=self.paste_text)
        self.edit_menu.add_command(label="Delete")
        self.edit_menu.add_command(label="Select All")
        self.edit_menu.add_command(label="Begin/End Select")
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Copy to Clipboard")
        self.edit_menu.add_command(label="Indent")
        self.edit_menu.add_command(label="Convert Case To")
        self.edit_menu.add_command(label="Line Operations")
        self.edit_menu.add_command(label="Comment/Uncomment")
        self.edit_menu.add_command(label="Auto Completion")
        self.edit_menu.add_command(label="EOL Conversion")
        self.edit_menu.add_command(label="Blank Operations")

        #Show a Search Menu
        self.search_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="Search", menu=self.search_menu)

        self.search_menu.add_command(label="Find..")
        self.search_menu.add_command(label="Find in Files")
        self.search_menu.add_command(label="Find Next")
        self.search_menu.add_command(label="Find Previous")
        self.search_menu.add_command(label="Select and Find Next")
        self.search_menu.add_command(label="Find (Volatile) Next")
        self.search_menu.add_command(label="Find (Volatile) Previous")
        self.search_menu.add_command(label="Replace")
        self.search_menu.add_command(label="Incremental Scratch")
        self.search_menu.add_command(label="Search Result window")
        self.search_menu.add_command(label="Next Search Result")
        self.search_menu.add_command(label="Previous Search Result")
        self.search_menu.add_command(label="Go to..")

        #Edit View MENU
        self.view_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="View", menu=self.view_menu)

        self.view_menu.add_command(label="Always on Top")
        self.view_menu.add_command(label="Toggle Full Screen Model")
        self.view_menu.add_command(label="Post it")
        self.view_menu.add_separator()
        self.view_menu.add_command(label="View Current file in")
        self.view_menu.add_separator()
        self.view_menu.add_command(label="Show Symbol")
        self.view_menu.add_command(label="Zoom")
        self.view_menu.add_command(label="Move")
        self.view_menu.add_command(label="Tab")
        self.view_menu.add_command(label="Wordwrap")
        self.view_menu.add_command(label="Focus on another view")
        self.view_menu.add_command(label="Hide Lines")
        self.view_menu.add_separator()
        self.view_menu.add_command(label="Fold All")
        self.view_menu.add_command(label="Unfold All")
        self.view_menu.add_command(label="Collapse Current Label")
        self.view_menu.add_command(label="Uncollapse Current Label")
        self.view_menu.add_command(label="Collapse Label")
        self.view_menu.add_command(label="Uncollapse Label")
        self.view_menu.add_separator()
        self.view_menu.add_command(label="Summary")


        #Edit Encoding MENU
        self.Encoding_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="Encoding", menu=self.Encoding_menu)

        self.Encoding_menu.add_command(label="ANSI")
        self.Encoding_menu.add_command(label="UTF-8")
        self.Encoding_menu.add_command(label="UTF-8-BOM")
        self.Encoding_menu.add_command(label="UCS-2 BE BOM")
        self.Encoding_menu.add_command(label="UCS-2 LE BOM")
        self.Encoding_menu.add_command(label="Character Set")
        self.Encoding_menu.add_separator()
        self.Encoding_menu.add_command(label="Convert to ANSI")
        self.Encoding_menu.add_command(label="Convert to UTF-8")
        self.Encoding_menu.add_command(label="Convert to UTF-8-BOM")
        self.Encoding_menu.add_command(label="Convert to UCS-2 BE BOM")
        self.Encoding_menu.add_command(label="Convert to UCS-2 LE BOM")

        #Edit Language MENU
        self.Language_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="Language", menu=self.Language_menu)

        self.Language_menu.add_command(label="A")
        self.Language_menu.add_command(label="B")
        self.Language_menu.add_command(label="C")
        self.Language_menu.add_command(label="D")
        self.Language_menu.add_command(label="E")
        self.Language_menu.add_command(label="F")

        #Edit Settings MENU
        self.Settings_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="Settings", menu=self.Settings_menu)

        self.Settings_menu.add_command(label="Preference")
        self.Settings_menu.add_command(label="Style Configurator")
        self.Settings_menu.add_command(label="Shortcut Mapper")
        self.Settings_menu.add_command(label="Import")
        self.Settings_menu.add_command(label="Edit Pop Up ContexMenu")

        #Edit Tools MENU
        self.Tools_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="Tools", menu=self.Tools_menu)

        self.Tools_menu.add_command(label="MD5")
        self.Tools_menu.add_command(label="SHA 256")


        #Edit Macro MENU
        self.Macro_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="Macro", menu=self.Macro_menu)

        self.Macro_menu.add_command(label="Start Recording")
        self.Macro_menu.add_command(label="Stop Recording")
        self.Macro_menu.add_command(label="Playback")
        self.Macro_menu.add_command(label="Save current recorded micro")
        self.Macro_menu.add_command(label="Run a Micro Multiple Times")
        self.Macro_menu.add_separator()
        self.Macro_menu.add_command(label="Trim Trailing Space and Save")
        self.Macro_menu.add_separator()
        self.Macro_menu.add_command(label="Modify Shortcut")


        #Edit Run MENU
        self.Run_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="Run", menu=self.Run_menu)

        self.Run_menu.add_separator()
        self.Run_menu.add_command(label="Run")
        self.Run_menu.add_separator()
        self.Run_menu.add_command(label="Get PHP Help")
        self.Run_menu.add_command(label="Wikipedia Search")
        self.Run_menu.add_command(label="Open file in another instance")
        self.Run_menu.add_command(label="Mozilla Firefox")
        self.Run_menu.add_command(label="Google Chrome")


        #Edit Plugin MENU
        self.Plugin_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="Plugin", menu=self.Plugin_menu)


        self.Plugin_menu.add_command(label="MIME Tools")
        self.Plugin_menu.add_command(label="Converter")
        self.Plugin_menu.add_command(label="NppExport")
        self.Plugin_menu.add_separator()
        self.Plugin_menu.add_command(label="Plugin Admin")
        self.Plugin_menu.add_separator()
        self.Plugin_menu.add_command(label="Open Plugin Folder")
        self.Plugin_menu.add_separator()

        #Edit Window MENU
        self.Window_menu = Menu(self.main_menu, tearoff=False)
        self.main_menu.add_cascade(label="Window ?", menu=self.Window_menu)


        self.Window_menu.add_command(label="1: Index.html")
        self.Window_menu.add_command(label="2: Inside.html")
        self.Window_menu.add_command(label="3: Style.css")
        self.Window_menu.add_command(label="4: res.html")
        self.Window_menu.add_command(label="Windows")
        self.Window_menu.add_separator()
root =Tk()
te = text_editor(root)

root.mainloop()