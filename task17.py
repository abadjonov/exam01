matn = int(input("Baho kirting: "))

if matn > 90 and matn < 100:
 print("A (A'lo)")
elif matn > 80 and matn < 89:
 print("B (Yaxshi)")
elif matn > 70 and matn < 79:
 print("C (Qoniqarli)")
elif matn > 60 and matn < 69:
 print("D (Qoniqarsiz)")
elif matn > 0 and matn < 59:
 print("F (Yomon)")
else:
    print("Aks xolatda: 'Ball 0-100 oralig'ida bolishi kerak!")