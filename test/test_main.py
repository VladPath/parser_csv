import os
import pytest

def test_1():
    # test for using terminal data 1
    assert os.system('python3 main.py data1.csv --report payout') == 0

def test_2():
    # test for using terminal data 2
    assert os.system('python3 main.py data2.csv --report payout') == 0

def test_3():
    # test for using terminal data 3
    assert os.system('python3 main.py data3.csv --report payout') == 0

def test_4():
    # test for using terminal all three data
    assert os.system('python3 main.py data1.csv data2.csv data3.csv --report payout') == 0

def test_5():
    # test for using terminal
    assert os.system('python3 main.py data1.csv data2.csv data3.png --report payout')

def test_6():
    # test for wrong report
    assert os.system('python3 main.py data1.csv data2.csv data3.csv --reportd payout')

def test_6():
    # test for wrong report
    assert os.system('python3 main.py data1.csv data2.csv data3.csv --report payouts')


