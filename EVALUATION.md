# Olcum Sozlesmesi

**Durum: DONDURULDU.** Asagidaki "Donar" tablosundaki hicbir sey, sonuclara
bakildiktan sonra degistirilemez. Degisirse tum etiketler ve tum sayilar
gecersizdir.

Birim: **bir e-posta**. Pozitif sinif: **HUMAN**.

## 1. Etiket tanimi

`human_required = YES` - sunlardan **herhangi biri** dogruysa:

- Sadece senin verebilecegin bir karar ya da yetki gerekiyor
- Bir taahhut veya son tarih yaratiyor, ya da ona atif yapiyor
- Cevapsiz kalmasinin bir bedeli var (para, hukuk, iliski, kacan firsat)
- Aksiyon gerekmese bile **bilmek isteyecegin** bir bilgi tasiyor

`human_required = NO` - sunlarin **hepsi** dogruysa:

- Senden aksiyon gerekmiyor
- Senden karar gerekmiyor
- Tamamen kaybolsa hicbir sey kaybetmezsin

### Iki baglayici kural

1. **Etiket, agent varliğindan bagimsizdir.** Registry gercegi degistirmez.
   Sonucu: gold `HUMAN` olan bir maili `DELEGATE` etmek **her zaman** hatadir.
2. Etiketleyemiyorsan **`UNCERTAIN`** yaz. Birincil metrikte `YES` sayilir;
   rapor dahil ve haric **iki turlu** verilir.

### Sinir vakalari - etiketleme rehberi

| Vaka | Etiket | Gerekce |
|---|---|---|
| API kirici degisiklik bulteni | `YES` | Bilmen gerek; kacirmanin bedeli var |
| Soguk recruiter maili | `YES` | Bugun yuksek degerli - etiket zamana bagli |
| Opsiyonel toplanti daveti | `YES` | RSVP senin verebilecegin karar |
| CC'li thread, sana soru yok | **iceriğe bagli** | Senin alanınsa YES, saf CC gurultusuyse NO |
| CI hata bildirimi (senin repon) | `YES` | Bilmek istersin. Sistem DELEGATE dese de gold YES kalir |
| Fatura bilgi kopyasi, onaylanmis | `NO` | Aksiyon/karar yok. Sert politika yine de yakalar - bilincli |

## 2. Metrikler

```
TP = gold HUMAN,     tahmin HUMAN
FN = gold HUMAN,     tahmin not-HUMAN     <- pahali olan
FP = gold not-HUMAN, tahmin HUMAN
TN = gold not-HUMAN, tahmin not-HUMAN

HUMAN recall      = TP / (TP + FN)        <- MANSET, her zaman CI ile
kacirilan oran    = FN / (TP + FN) = 1 - recall
FP orani          = FP / (FP + TN)        <- populasyona yeniden agirliklandirilir
beklenen maliyet  = c_FN * FN + c_FP * FP
AUC                                        <- yardimci metrik
```

**Yuksek-onem recall'u ayrica raporlanir.** Recall hicbir zaman nokta tahmini
olarak yazilmaz - guven araligi (Wilson) zorunludur.

## 3. Isletme noktasi

- **Birincil kural:** `recall >= 0.95` kisiti altinda FP minimum.
- **Ikincil (capraz kontrol):** `argmin(c_FN*FN + c_FP*FP)`, su oranlar icin
  ayri ayri: **20:1, 50:1, 100:1, 200:1**.

Tek bir maliyet orani **sabitlenmez**. `tau*` oranin fonksiyonu olarak
cizilir; sabitse saglamlik sonucu, oynuyorsa duyarlilik bulgusudur.

## 4. Haric tutulanlar

Sert politika ile bloklanan vakalar esik egrisine **girmez**. Ayrica ve kendi
precision'iyla raporlanir. Gerekce: bunlar "model dogru esigi mi secti"
sorusunu test etmiyor, "politika yakaliyor mu" sorusunu test ediyor.

## 5. Veri

```
Altin kume      ~250, KASITLI DENGESIZ: ~150 HUMAN adayi + ~100 not-HUMAN
                (temsili ornekleme yanlis tasarim - recall tahmini icin
                 yeterli POZITIF gerekiyor, gercek dagilim degil)
Prevalans       ~100 mail, RASTGELE ve stratifiye edilmemis -> pi tahmini
                (FP oranini "gunde kac gereksiz mail"e cevirmek icin sart)
Dokunulmaz      60 mail, CP8'e kadar ACILMAZ. Manset sayilar orada raporlanir.
Surum           gold_version. Duzeltme serbest, surum artar, eval bastan kosar.
```

## 6. Donar / degisebilir

| Donar (CP1'den sonra degismez) | Degisebilir |
|---|---|
| Etiket tanimi | Model |
| Iki baglayici kural | Prompt |
| Metrik formulleri | Esik (tau) |
| Pozitif sinif | Ozellik seti |
| Haric tutma kurali | Kalibratör |
| Isletme noktasi kurali, R = 0.95 | Gold icerigi *(surum artirarak)* |
| Dokunulmaz dilim | |

## 7. Kapsam siniri

Tek gelen kutusu, tek etiketleyici, belirli bir zaman dilimi. Sonuclar bu
kisiye ve bu doneme ozeldir.

**Ogrenilen katman kisisel, sert politika evrensel.** Soguk recruiter maili
ornegi bunun kaniti: bugun `YES`, alti ay sonra muhtemelen `NO`.
