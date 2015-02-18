def main():
  fp = open('rosalind_cons.txt', 'r')
  dnamat = []
  matscore = []
  scoreinv = []
  strandcnt = 0
  tmpstrand = ''

  for line in fp:
      line = line.strip()
      if line[0] == '>':
          dnamat.append(tmpstrand)
          tmpstrand = ''
          pass
      else:
          tmpstrand += line
  fp.close()

  dnamat.append(tmpstrand)
  dnamat = dnamat[1::]
  dnalength = len(dnamat[0])
  strands = len(dnamat)
  A = [0]*dnalength
  C = [0]*dnalength
  T = [0]*dnalength
  G = [0]*dnalength

  for i in range(0, strands):
      for j in range(0, dnalength):
          if dnamat[i][j] == 'A':
              A[j] += 1
          elif dnamat[i][j] == 'C':
              C[j] += 1
          elif dnamat[i][j] == 'T':
              T[j] += 1
          elif dnamat[i][j] == 'G':
              G[j] += 1

  matscore.append(A)
  matscore.append(C)
  matscore.append(T)
  matscore.append(G)

  tmp = ''
  end = []
  for i in range(0, dnalength):
      for j in range(0, 4):
           score = str(matscore[j][i])
           if len(tmp) < 4:
               tmp += score
           elif len(tmp) == 4:
               scoreinv.append(tmp)
               tmp = ''
               tmp += score
  for i in range(0, 4):
      end.append(matscore[i][dnalength - 1])
  scoreinv.append(''.join(map(str, end)))

  conseq = ''
  for i in range(0, dnalength):
   if list(scoreinv[i]).index(max(scoreinv[i])) == 0:
       conseq += 'A'
   if list(scoreinv[i]).index(max(scoreinv[i])) == 1:
       conseq += 'C'
   if list(scoreinv[i]).index(max(scoreinv[i])) == 2:
       conseq += 'T'
   if list(scoreinv[i]).index(max(scoreinv[i])) == 3:
       conseq += 'G'

  print conseq
  print 'A:' , ' '.join(map(str, matscore[0]))
  print 'C:' , ' '.join(map(str, matscore[1]))
  print 'T:' , ' '.join(map(str, matscore[2]))
  print 'G:' , ' '.join(map(str, matscore[3]))
main()
