from math_series.series import fibonacci, lucas, sum_series

def test_char ():
    assert fibonacci("")== "you have to give me int nomber  its better to be biger than 0"

def test_zeroF ():
    assert fibonacci(0)== 0

def test_oneF ():
    assert fibonacci(1)== 1

def test_towF ():
    assert fibonacci(2)== 1

def test_threeF ():
    assert fibonacci(3)== 2
   
def test_fourF ():
    assert fibonacci(4)== 3

def test_fiveF ():
    assert fibonacci(5)== 5

def test_sixF ():
    assert fibonacci(6)== 8

def test_sevenF ():
    assert fibonacci(7)== 13

def test_eightF ():
    assert fibonacci(8)== 21

##############
    
def test_charL ():
    assert lucas ("")== "you have to give me int nomber  its better to be biger than 0"

def test_zeroL ():
    assert lucas(0)== 2

def test_oneL ():
    assert lucas(1)== 1

def test_towL ():
    assert lucas(2)== 3

def test_threeL ():
    assert lucas(3)== 4
   
def test_fourL ():
    assert lucas(4)== 7

def test_fiveL ():
    assert lucas(5)== 11

def test_sixL ():
    assert lucas(6)== 18

def test_sevenL ():
    assert lucas(7)== 29

def test_eightL ():
    assert lucas(8)== 47


################

def test_fibo():
      assert sum_series(9) == 34

def test_lucas():
    assert sum_series(9,2,1) == 76

def test_lucas():
    assert sum_series(10,2,1) == 123

