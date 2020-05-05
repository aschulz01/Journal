import sublime
import sublime_plugin
import os
import time

def getPath(self):
        s = sublime.load_settings("Journal.sublime-settings")

        save_path_settings = s.get("save_path", "~/Documents/Journal")
        save_path = sublime.expand_variables(
            save_path_settings, 
            self.window.extract_variables())
        
        if ("$" in save_path_settings) and (save_path == ""):
            sublime.error_message("unknown token: " + save_path_settings)
            raise

        if save_path[0:1]=="~":
            return  os.path.expanduser(save_path)
        
        if ("\\" in save_path) or ("/" in save_path):
            return  save_path

        if "$" in save_path:
            sublime.error_message("Error: " +s.get("save_path", "") + " cannot be resolved. Did you open a folder instead of a .sublime-project? In this case you should configure $folder instead of $project_path in Journal.sublime-settings file.")
            raise
        return  os.path.expanduser('~/Documents/' + save_path)

def getExtension():
    s = sublime.load_settings("Journal.sublime-settings")
    save_extension = s.get("extension", ".md")
    return save_extension

class JournalCommand(sublime_plugin.WindowCommand):
    def run(self):
        save_path = getPath(self) +'\\' + time.strftime('%Y') + '\\' + time.strftime('%m')

        s = sublime.load_settings("Journal.sublime-settings")
        if s.get("use_dayfolder", "") == "true" :
            save_path = save_path + '\\' + time.strftime('%d')

        try:
            os.makedirs(save_path)
        except OSError:
            pass
            
        self.window.open_file(save_path + "/" + time.strftime('%Y%m%d') + getExtension())

class TimestampCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        timestamp = "\n[%s]\t" % (time.strftime("%d.%m.%Y %H:%M:%S")) 
        self.view.insert(edit, self.view.sel()[0].begin(), timestamp)    