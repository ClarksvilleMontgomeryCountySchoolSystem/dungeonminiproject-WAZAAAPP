


good = r"""

             
           /.-. '----------.
           \'-' .--"--""-"-'
            '--'
"""

bad = """


     ______
  ,-' ;  ! `-.
 / :  !  :  . \
|_ ;   __:  ;  |
)| .  :)(.  !  |
|"    (##)  _  |
|  :  ;`'  (_) (
|  :  :  .     |
)_ !  ,  ;  ;  |
|| .  .  :  :  |
|" .  |  :  .  |
|mt-2_;----.___|
"""

has_key = True

if has_key:
    outcome = "Click: the door opened."
    print(good)
else:
    outcome = "Doom: the door it locked with no key."
    print(bad)


print(outcome)