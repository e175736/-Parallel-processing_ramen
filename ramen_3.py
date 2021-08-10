from concurrent.futures import ThreadPoolExecutor
import time

def men():
  print('  麺を茹でます。')
  time.sleep(3)
  print('  麺が茹であがりました。')

def soup():
  print('  スープをつくります。')
  time.sleep(2)
  print('  スープができました。')
tpe = ThreadPoolExecutor(max_workers=3)

def ramen():
  start = time.time()
  print('ラーメンを10個作ります。')
  for _ in range(10):
      tpe.submit(men)
      tpe.submit(soup)
  tpe.shutdown()
  print('ラーメンが10個できました。')
  elapsed_time = time.time() - start
  print("elapsed_time:{0}".format(elapsed_time) + "[sec]")
ramen()