# Instrucțiuni pentru Claude în Chrome — setările FlexyPlay din Shopify Admin

Copiază tot textul din chenarul de mai jos în Claude în Chrome. Completează înainte cele două câmpuri marcate cu ⚠️.

```
Ești în browserul meu și ești logat în Shopify Admin la magazinul FlexyPlay (ze1kwj-if, domeniu flexyplay.ro). Te rog să faci setările de mai jos, în ordine. Reguli:
- Lucrează într-un tab nou.
- Înainte de fiecare „Save” la pașii 4, 5 și 6 (livrare, plăți, politici), arată-mi ce ai completat și așteaptă să-ți confirm.
- Nu scoate parola site-ului. Nu șterge nimic. Nu instala aplicații cu plată.
- Dacă un pas îmi cere date personale, documente sau un cod primit pe telefon/email, oprește-te și spune-mi.
- La final, dă-mi un rezumat: ce ai făcut, ce a rămas și de ce.

DATE
- Nume magazin: FlexyPlay
- Firmă: CLEVNY RO S.R.L., CUI 45226920, J23/7166/2021, neplătitoare de TVA
- Adresă firmă: Str. Predeal nr. 19, camera 6, oraș Voluntari, jud. Ilfov, România
- Email clienți: flexyplaytoys@gmail.com
- Telefon: +40 765 725 463
- ⚠️ Curier: ____________
- ⚠️ Cost livrare sub 150 lei: ____ lei

1) SETTINGS → GENERAL (Store details)
- Store name: FlexyPlay (cu P mare).
- Store contact email și Sender email: flexyplaytoys@gmail.com (dacă cere confirmarea adresei, spune-mi ca s-o confirm din Gmail).
- Store phone: +40 765 725 463.
- Billing information / Legal business name: CLEVNY RO S.R.L., cu adresa de mai sus.
- Verifică: moneda RON, fusul orar (GMT+02:00) Bucharest, unități kg.

2) SETTINGS → LANGUAGES
- Verifică că româna e limba principală (Default) a magazinului. Dacă nu e, spune-mi înainte să schimbi.

3) ONLINE STORE → PREFERENCES
- Homepage title: FlexyPlay — Jucării flexi articulate, printate 3D în România
- Homepage meta description: Jucării flexi articulate și playseturi în miniatură, printate 3D cu drag în România. Ambalate cadou, livrare în 3–6 zile.
- Social sharing image: alege din Files imaginea „flexyplay-share.jpg”.
- NU atinge „Password protection”.

4) SETTINGS → SHIPPING AND DELIVERY
- În profilul general de livrare, zona de livrare: doar România (dacă există alte țări/zone, spune-mi înainte să le scoți).
- Tarife pentru România:
  a) „Livrare standard prin curier (2–4 zile lucrătoare)” – preț: costul de la DATE – condiție: pe baza valorii comenzii, de la 0 la 149,99 lei.
  b) „Livrare gratuită (2–4 zile lucrătoare)” – preț 0 – condiție: valoarea comenzii minim 150 lei.
- Șterge orice alt tarif din zona România doar după ce îmi arăți lista.

5) SETTINGS → PAYMENTS
- Shopify Payments: completează business details cu datele firmei de la DATE (tip: companie/SRL, CUI, adresă). Pentru IBAN și verificarea identității reprezentantului legal oprește-te și spune-mi – le completez eu.
- După activare: activează Apple Pay, Google Pay și Shop Pay (dacă sunt disponibile).
- Manual payment methods → adaugă „Cash on Delivery (COD)”, cu numele afișat: „Plată ramburs – plătești la curier”.
- Spune-mi dacă e pornit „Test mode” și ce status are contul Shopify Payments.

6) SETTINGS → POLICIES
- Deschide documentul: https://github.com/eremiasebastian/flexyplay/blob/claude/flexyplay-shopify-setup-lqpj3n/docs/politici-flexyplay.md
- Înlocuiește [CURIER] și [COST LIVRARE] cu valorile din DATE.
- Lipește fiecare politică în câmpul ei: 1 → Return and refund policy, 2 → Shipping policy, 3 → Terms of service, 4 → Privacy policy, 5 → Contact information. Fără titlul mare și fără tabelul cu instrucțiuni de la începutul documentului. Păstrează îngroșările și listele.

7) SETTINGS → CHECKOUT
- Contact: clientul se identifică prin email.
- Full name: cere nume și prenume. Company name: optional. Address line 2: optional.
- Shipping address phone number: Required (curierul are nevoie de telefon).
- Marketing: lasă bifa de abonare la email nebifată implicit.
- Dacă există „Customize” (checkout editor): pune logo-ul FlexyPlay (din Files: flexyplay-logo-trim.png), culoarea principală a butoanelor #FF6B5E, fundal #FFF6EC, text #432B21. Salvează doar după ce îmi arăți preview-ul.

8) SETTINGS → CUSTOMER PRIVACY
- Activează bannerul de cookie-uri (Cookie banner) pentru vizitatorii din UE/România, cu opțiunile Accept / Refuz / Preferințe.
- Spune-mi ce opțiuni au rămas nesetate.

9) VERIFICARE FINALĂ (nu schimba nimic aici)
- Deschide flexyplay.ro (folosește parola dacă e cerută), pune un produs în coș și mergi până la pagina de plată, fără să plătești. Spune-mi: ce metode de plată apar, ce costuri de livrare apar sub și peste 150 lei, dacă apar linkurile către politici jos în checkout și dacă textele sunt în română.
```

## Ce rămâne după ce termină extensia

- **Comanda de test:** cu Test mode din Shopify Payments (card `4242 4242 4242 4242`) sau o comandă ramburs pe care o anulezi după.
- **Facturare:** un cont la SmartBill sau Oblio pe CLEVNY RO S.R.L., apoi aplicația lor din Shopify App Store.
- **Reclame:** aplicațiile „Facebook & Instagram” și „Google & YouTube” din Shopify (pixel și Google tag), plus verificarea domeniului flexyplay.ro în Meta Business. Ai nevoie de conturile de Business Manager și Google Ads.
- **Lansarea:** Online Store → Preferences → scoți Password protection.
- **Tokenul de acces:** când nu mai lucrăm pe site, revocă tokenul aplicației folosite de mine (Settings → Apps and sales channels → Develop apps).
