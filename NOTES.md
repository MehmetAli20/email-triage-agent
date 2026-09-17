# Karar Gunlugu

Her adimda uc satir: **ne yapildi - hangi sayi cikti - hangi karar verildi**.
Bu dosya, konusma bittiginde projenin hafizasi.

---

## 2026-09-17 - CP1 basladi

**Ne yapildi:** Iskelet olusturuldu. Olcum sozlesmesi `EVALUATION.md` olarak
donduruldu. Sema (`schemas.py`) yazildi.

**Karar - otonomi etiketlenemez.** Ilk tasarimda altin kumeye `autonomy_mode`
konuyordu. O etiket var olamaz: "bu mail otonom islenebilirdi" mailin ozelligi
degil, modelin dogru cevap uretip uretmediginin sonucu. Yerine `HUMAN /
not-HUMAN` ikili etiketi kondu - bu mailin ozelligi ve etiketlenebilir.

**Karar - etiket agent varliğindan bagimsiz.** Registry degisince gold
degismemeli, yoksa altin kume kararsiz hale gelir.

**Karar - R = 0.95, dokunulmaz dilim 60 mail, bilgi amacli mailler
"bilmek istiyorsam YES".**

**Sirada:** CP2 - korpus temizligi ve ilk 30 etiket.
