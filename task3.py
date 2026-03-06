





good = r"""


                 z
                z
                 Z
       .--.  Z Z
      / _(c\   .-.     __
     | / /  '-;   \'-'`  `\______
     \_\/'/ __/ )  /  )   |      \--,
     | \`""`__-/ .'--/   /--------\  \
      \\`  ///-\/   /   /---;-.    '-'
jgs                (________\  \
                             '-'
"""
bad = r"""

             __)),
            //_ _)
            ( "\"
             \_-/
         ,---/  '---.
        /     - -    \
       /  \_. _|__,/  \
      /  )\        )\_ \
     / _/  (   '  ) /  /
    / |     (_____) | /
   /,'      /     \/ /,
 _/(_      (   ._, )-'
`--,/      |____|__|
           |    )  |
           |   /   |
           |  / \  |
          / `|  | _)
          |  |  |  |
          |  /  \  |
          | |    \ |
          | \    | \_
   gnv   /__(    '-._`,
"""
guard_awake = True

if not guard_awake:
    outcome = "Shadow:the guard is sleeping"
    print(good)
else:
    outcome = "Doom: a guard is appearing right ahead of me."
    print(bad)

print(outcome)