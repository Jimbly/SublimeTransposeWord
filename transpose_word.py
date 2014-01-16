import sublime, sublime_plugin, re


class TransposeWordCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        # TODO: Use the Sublime language definitions to determine which characters
        # delineate value tokens better (although Javascript is missing $, so that
        # might just make things worse for me)
        r = re.compile('^[\\w\\$]+$')
        view = self.view
        end_sels = [];
        for s in view.sel():
            # do transpose
            word1 = view.word(s)
            if not r.match(view.substr(word1)):
                word1 = view.word(word1.begin() - 1)
            word2 = view.word(word1.end() + 1)
            if not r.match(view.substr(word2)):
                word2 = view.word(word2.end() + 1)
            word1_text = view.substr(word1)
            word2_text = view.substr(word2)
            view.replace(edit, word2, word1_text)
            view.replace(edit, word1, word2_text)
            end_sels.append(sublime.Region(word2.end(), word2.end()))

        view.sel().clear()
        for s in end_sels:
            view.sel().add(s)

class TransposeCharCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        end_sels = [];
        for s in view.sel():
            # do transpose
            if not s.begin() == s.end():
                # Selection is more than one character, no character transpose
                continue
            right = view.substr(s.begin())
            view.erase(edit, sublime.Region(s.begin(), s.begin() + 1));
            view.insert(edit, s.begin()-1, right);
