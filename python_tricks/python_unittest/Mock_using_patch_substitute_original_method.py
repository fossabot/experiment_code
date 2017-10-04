from unittest.mock import patch
import os
# test success under python3.6
def fake_remove(path, *a, **k):
    print("remove done")

@patch('os.remove', fake_remove)
def test():
    try:
        os.remove('%$!?&*') # fake os.remove
    except OSError as e:
        print(e)
    else:
        print('test success')
test()
