# import library
import openbci_node2py as onp

# create stream object
stream = onp.Stream(port=3004, verbose=True)

# start stream
stream.start()
