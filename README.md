# Email Triage Agent

Kurumsal gelen kutusu icin risk-farkindali yonlendirme agent'i. Asil isi cevap
yazmak degil, **bu mailin kontrolunu kimin almasi gerektigine karar vermek**.

```
DISCARD    kullaniciya gosterme (arsivle, SILME)
DELEGATE   baska bir agent'a yonlendir (registry'den kontrol)
DRAFT      taslak uret, GONDERME
HUMAN      mutlaka kullaniciya getir
```

`SEND` karari yok. v1'de agent'a gonderme yetkisi verilmiyor.

## Arastirma sorusu

> Bir LLM yonlendirme agent'i, **kacirilan insan-gerekli mail oranini
> belirtilen bir tavanin altinda tutarken**, insan e-posta yukunu ne kadar
> azaltabilir?

Kisit once, optimizasyon sonra. Olcum sozlesmesi: [EVALUATION.md](EVALUATION.md)

## Uc katman

| Katman | Soru | Rolu |
|---|---|---|
| **HUMAN?** | Bu mail bana gelmeli mi? | Projenin bilimsel katkisi |
| **WHO?** | Gelmeyecekse kim ilgilenecek? | Mimari katki |
| **HOW?** | Ne yapilacak? | Genisletilebilirlik |

## Mimari siniri

`analyzer.py` tek non-deterministik modul. `policy.py`, `router.py` ve
`eval/metrics.py` saf ve deterministik - icinde `import anthropic` gorursen
sinir kaymis demektir.

`RoutingDecision` **saklanmaz**, her seferinde yeniden hesaplanir. Esigi
supurmek bu yuzden bedava.

## Kurulum

```bash
uv sync --extra dev
cp .env.example .env
uv run pytest
uv run ruff check
```

## Durum

CP1 - iskelet ve sozlesme. Ilerleme: [NOTES.md](NOTES.md)
