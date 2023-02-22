### shortcut.bat

an alternative shortcut for portable apps. instead of pointing to a file at a specific path, it searches for an EXE with a specific name and launches it. Useful for portable apps on drives whose letter changes on different computers, or apps whose location within the drive may change for whatever reason.

### launch_zotero.py

Zotero is an amazing tool for anyone dealing with academic articles and other sources. One of its few flaws is that it does not allow the user to set a relative path to their library. A portable Zotero can then be annoying to use, as the drive letter of the library can change on different computers, breaking the library path which Zotero remembers. This python script makes it possible to launch Zotero from a portable drive without much hassle by looking for the library and updating its path in the user preferences of Zotero each time when the app launches.
