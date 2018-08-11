from B import BB

def TestA():
  #region
  aa = ['A','B','C','D']
  bb = ['A','B']
  cc = set(aa)<=set(bb)
  dd = set(aa)>=set(bb)
  ee = set(bb)<=set(aa)
  ff = set(bb)>=set(aa)

  x = bb in aa
  y = 'A' in aa
  z = 'E' in aa
  #endregion
  '''
  #b = BB().TestB(a,6)
  #i = BB().TestB2(0)
  a = '9999'
  a = '888'
  '''
if __name__ == "__main__":
  TestA()