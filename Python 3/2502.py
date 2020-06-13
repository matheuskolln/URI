while True:
  try:
    c, n = map(int,input().split())
    c1 = input().lower()
    c2 = input().lower()
    c1_aux =c1.upper()
    c2_aux =c2.upper()
    output = ''
   
    for i in range(n):
        txt = input()
        txt = list(txt)
       
        for j in range(len(txt)):
            for k in range(c):
                if txt[j] == c1[k]:
                    txt[j] = c2[k]
               
                elif txt[j] == c2[k]:
                    txt[j] = c1[k]

                elif txt[j] == c1_aux[k]:
                    txt[j] = c2_aux[k]
               
                elif txt[j] == c2_aux[k]:
                    txt[j] = c1_aux[k]
           
            output += txt[j]
        print(output)
        output = ''
    print()
  except:
    break