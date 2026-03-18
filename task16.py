narx = 100000


yosh = int(input("Yoshingizni kiriting: "))


chegirma_foiz = 0
chegirma_summa = 0
yakuniy_narx = 0


if 0 <= yosh <= 6:
  
    chegirma_foiz = 50
elif 7 <= yosh <= 17:
    
    chegirma_foiz = 20
elif yosh > 60:
   
    chegirma_foiz = 30
else:
   
    chegirma_foiz = 0

chegirma_summa = narx * chegirma_foiz / 100
yakuniy_narx = narx - chegirma_summa

print(f"Yakuniy narx: {yakuniy_narx} so'm ({chegirma_foiz}% chegirma qo'llanildi)")
