### modules: a file contains functions, classes, and variables etc.

import messages as msg # import the module messages as msg (alias)

msg.hello()
msg.bye()

from messages import hello, bye # import the function hello and bye from the module messages, might be confusing, conflicts might occur
hello()
bye()

help("modules") # list all modules
# help("modules os") # list all modules that contain os
# or https://docs.python.org/3/py-modindex.html