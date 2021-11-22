from dbtpro.toolmatt import first_step, computing


def test_try_me_too_short():
    assert first_step('xxx') == 'Try again'
    assert first_step(' ') == 'Try again'
    assert first_step('!!! ') == 'Try again'

def test_try_me_lower():
    assert first_step('password') == 'Try again'

def test_try_me_valid():
    assert first_step('PASSWORD') == 'Password ok'
    assert first_step('MY_PASSWORD') == 'Password ok'

def test_compute_res():
    assert computing(1,2,3) == -1
    assert computing(12,2,3) == 21
    assert computing(50,2,3) == 97
