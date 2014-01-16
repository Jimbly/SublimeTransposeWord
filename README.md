Jimbly's Transpose Word
====================

Transpose word plugin for Sublime Text 2/3

Features:
* Adds specific commands to transpose words or characters ("transpose_word" and "transpose_char")
* Smart transpose_word so that "foo| = bar" becomes "bar = foo|"

Why I need this:
* Sublime's default "transpose" command tries to be smart and choose when to transpose a word and a character, and often chooses wrong (specifically if you are twiddling a space and a character, it sometimes things you want to swap the words).

To use with the standard Visual Studio bindings, place these lines in your Key Bindings - User file:
```
  { "keys": ["ctrl+shift+t"], "command": "transpose_word" },
  { "keys": ["ctrl+t"], "command": "transpose_char" },
```
