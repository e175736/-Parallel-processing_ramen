import time

def men():
  print('  麺を茹でます。')
  time.sleep(3)
  print('  麺が茹であがりました。')

def soup():
  print('  スープをつくります。')
  time.sleep(2)
  print('  スープができました。')

def ramen():
  start = time.time()
  print('ラーメンを作ります。')
  men()
  soup()
  print('盛り付けます。')
  print('ラーメンができました。')
  elapsed_time = time.time() - start
  print("elapsed_time:{0}".format(elapsed_time) + "[sec]")
  
ramen()
  