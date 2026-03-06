

good = r"""                              / |                         
                                     \ ^ | / \ / \
                               (\ / \ / ^ / \ /) / ^ )
                                 \  \ / ^ / \ ^ /
                                      ) ^ ^  \     (
                                     (^ ^ ^ \ )
                                \___ \ /___ _ /_____ _/
                                  [________________]
                                   |              |
                                   |     / /\\     |
                                   |    < <( )>>    |
                                   |     \ \//     |
                                    \___________ _/
                                        |    |
                                        |    |
                                        |    |
                                        |    |
                                        |    |
                                        |    |
                                        |    |
"""

bad = r"""
                  \___ \ / ___
                     _ / _____
                       _ /
                [________________]
                        | |
                    | / / \\ |
                  | < < ( ) >> |
                  |      \ \ // |
                 \____________ /
                       | |
                       | |
                       | |
                       | |
                       | |
                       | |
                       | |
"""

torch_lit = True

if torch_lit:
    outcome = "Flicker: the torch works lighting up the cold air around it."
    print(good)
else:
    outcome = "Doom: the torch didn't work."
    print(bad)

print(outcome)