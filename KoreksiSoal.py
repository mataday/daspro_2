def Koreksi_Soal(soal:int,benar:int,salah:int)->int:
    return (benar * 4) + (salah*-1)
print(Koreksi_Soal(25,0,0))