



good = r"""

 ,--.     ,--.
(  O )   (  O )
 `--'  \  `--'
        \   _
  >-.   /   /| 
     `-.__.'
"""



bad = r"""


      _..._
    ,'     `.
  ,'         `.
,'    _   ,-.  `.
|    (_)  `-'   |
|        >      |
|     ,----.    |
|    /,-""-.\   |
`.  |/      "  ,'
  `.         ,'
    `._____,'
"""
escaped = True

if escaped:
    outcome = "Legend: I escaped yes."
    print(good)
else:
    outcome = "Doom: im stuck here"
    print(bad)


print(outcome)