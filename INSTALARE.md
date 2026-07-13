# FlexyPlay — instalare temă Shopify

Acest folder conține implementarea reală (Liquid, nu prototip) a designului FlexyPlay
exportat din Claude Design: **homepage-ul** și **pagina de produs Pug Bakery Playset**,
gata de instalat într-o temă Shopify Online Store 2.0 (Dawn sau derivat).

Citește această pagină întâi — descrie exact ce face fiecare fișier, ce e static și ce
e dinamic (citit din Admin), și pașii de instalare în ordine.

## De ce există 2 pagini, nu doar homepage

Cardurile de produs de pe homepage trebuie să ducă undeva. Fără o pagină de produs în
același stil, ar duce la pagina standard Dawn (funcțională, dar vizual ruptă de restul
site-ului). Am făcut-o pentru ca site-ul să fie coerent de la primul click.

## Fișiere din acest folder → unde se duc în temă

| Fișier aici | Destinație în temă |
|---|---|
| `sections--flexyplay-homepage.liquid` | `sections/flexyplay-homepage.liquid` |
| `sections--flexyplay-product.liquid` | `sections/flexyplay-product.liquid` |
| `snippets--flexyplay-styles.liquid` | `snippets/flexyplay-styles.liquid` |
| `templates--index.json` | `templates/index.json` (**fă backup la cel existent înainte**) |
| `templates--product.flexyplay.json` | `templates/product.flexyplay.json` |

Cele două fișiere `sections--*` includ `{% render 'flexyplay-styles' %}` la început —
de-asta `snippets--flexyplay-styles.liquid` trebuie copiat și el, altfel secțiunile nu
au stiluri (fonturi, culori, animații, chip-uri, accordion FAQ).

## Design — paletă, fonturi, ton (neschimbate față de prototip)

- Fundal cremă `#FFF6EC`, text ciocolată `#432B21`, coral `#FF6B5E`, teal `#2EC4B6`,
  galben cald `#FFD166`.
- Titluri: **Baloo 2** (500–800). Text: **Nunito** (400–800, + italic 600).
  Încărcate din Google Fonts direct în snippet — pentru performanță maximă, ideal ar fi
  mutate în `<head>`-ul din `layout/theme.liquid`, dar funcționează și așa.
- Butoane 3D (umbră groasă dedesubt, se "apasă" la click), carduri cu hover ridicat,
  reveal-on-scroll (`IntersectionObserver`), marquee derulant infinit, accordion FAQ.
- Ton text: română, cald, direct — toate textele implicite sunt editabile din temă
  (Personalizare temă → secțiune → setări), nu sunt hardcodate ireversibil.

## Ce e static vs. ce e dinamic (important de înțeles înainte să adaugi produse)

### Homepage (`flexyplay-homepage.liquid`)

- **Grid-ul de produse citește o colecție reală** (setarea `collection` din secțiune).
  Nimic hardcodat — orice produs pui în colecție apare automat în grid, până la limita
  `max_products` (implicit 6).
- **Filtrele-chip** (Toate / Playseturi complete / Figurine flexi / Keychains) se leagă
  de **tag-urile produsului**: pune tag-ul `playseturi`, `figurine` sau `keychains` pe
  fiecare produs. Un produs fără niciunul din aceste tag-uri apare doar la "Toate".
- **Badge-urile** (Bestseller / Nou / Preț prietenos) vin tot din tag-uri: `bestseller`,
  `nou`, `pret-prietenos`. Dacă produsul are `compare_at_price` mai mare decât prețul
  curent și niciunul din tag-urile de mai sus, primește automat badge-ul "Reducere".
- **Gradientul de fundal al cardului** e ales automat, ciclic, din cele 6 gradiente ale
  designului original (nu ține de produs — e doar decor sub poză).
- **Poza cardului**: dacă produsul are `featured_image`, se afișează poza reală; dacă nu,
  apare un emoji placeholder (tot ciclic din setul original 🐶🥐 🦡🗑️ 🐞🌸 🦊🏜️ 🦫 🐒).
  Când urci poze în Admin, cardurile trec automat de la emoji la poză — nu trebuie
  schimbat nimic în cod.

### Pagina de produs (`flexyplay-product.liquid`)

- **Cardurile de variantă** din secțiunea "Alege varianta ta" se generează automat din
  variantele reale ale produsului (`product.variants`) — câte una pe variantă, oricâte
  ar fi. Nu mai există limita de "exact 3 variante" din prototip.
- **Varianta evidențiată** ("CEL MAI POPULAR", cardul coral) e cea al cărei titlu se
  potrivește cu setarea `featured_variant_title` (implicit "Setul Complet"). Dacă
  redenumești varianta din Admin, actualizează și setarea din temă.
- **Subtitlurile și bulinele de beneficii** de sub fiecare card sunt text editabil din
  setările secțiunii, aplicat **pe poziție** (variantă 1 / 2 / 3), nu pe nume — dacă
  reordonezi variantele, verifică dacă textele mai au sens.
- **Adaugă în coș / Comandă acum funcționează real**: fiecare card e un `<form
  action="/cart/add">` cu id-ul variantei corecte. Variantele fără stoc afișează automat
  "Stoc epuizat" și butonul e dezactivat. Nu depinde de tema Dawn — merge cu orice temă
  Shopify standard (POST simplu, fără JS obligatoriu pentru add-to-cart).
- **Titlul mare, prețul, poza, descrierea** vin din produsul real (`product.title`,
  `product.price_min`, `product.compare_at_price`, `product.featured_image`,
  `product.description`) — cu excepția "headline"-ului de marketing (ex. "Mopsul care
  se îndoaie, brutăria care se deschide"), care e text editabil separat, pentru că e
  un slogan, nu titlul de produs literal.

## Pași de instalare (Shopify CLI, temă de development — nu live)

1. Din rădăcina temei clonate local:
   ```
   cp sections--flexyplay-homepage.liquid sections/flexyplay-homepage.liquid
   cp sections--flexyplay-product.liquid sections/flexyplay-product.liquid
   cp snippets--flexyplay-styles.liquid snippets/flexyplay-styles.liquid
   cp templates/index.json templates/index.json.backup   # backup înainte de suprascriere
   cp templates--index.json templates/index.json
   cp templates--product.flexyplay.json templates/product.flexyplay.json
   ```
2. Creează colecția manuală **"Homepage"** (handle-ul rezultat trebuie să fie
   `homepage` — așa e referențiată în `templates/index.json`, setarea `collection`).
   Dacă handle-ul iese altul, editează manual setarea colecției din
   `templates/index.json` sau din Personalizare temă.
3. Creează produsul **Pug Bakery Playset**:
   - Opțiune "Variantă" cu 3 valori: **Doar Mopsul**, **Setul Complet**, **Doar Brutăria**
     (numele contează — `featured_variant_title` din `templates--product.flexyplay.json`
     caută exact "Setul Complet").
   - Tag: `playseturi` (ca să apară la filtrul corect pe homepage) + opțional
     `bestseller` pentru badge.
   - Status: Active.
   - Adaugă produsul în colecția "Homepage".
4. Asignează produsului șablonul de pagină **"product.flexyplay"** (Admin → Produs →
   secțiunea "Șablon temă", dropdown) — altfel folosește tot pagina Dawn standard.
5. Pornește preview-ul temei de development și verifică:
   - Homepage: grid-ul arată produsul, filtrul "Playseturi complete" îl afișează, badge-ul
     apare dacă ai pus tag-ul, click pe card duce la pagina de produs FlexyPlay (nu Dawn).
   - Pagina de produs: cele 3 carduri de variantă apar, "Setul Complet" e cel evidențiat
     coral, "Adaugă în coș" chiar adaugă în coș (verifică `/cart` după click).

## De configurat separat, în Admin (nu ține de cod)

- **Format monedă**: Settings → General → Store currency formatting. Ca prețurile să
  arate "129 lei" (ca-n design), setează formatul HTML/email la `{{amount_no_decimals}}
  lei` (sau echivalent, în funcție de cum vrei zecimalele).
- **Prețuri reale** pe cele 3 variante (sunt 0 până le pui tu).
- **Poze produs** — cardurile și pagina de produs trec automat de la emoji/placeholder
  la poze reale imediat ce le urci.
- **Logo** — opțional, setarea "Logo" din fiecare secțiune; dacă rămâne goală, se
  afișează wordmark-ul text cu gradient (identic cu prototipul).
- **Video demo** pe pagina de produs — setarea "Video demo"; dacă rămâne goală, apare
  placeholder-ul text "[ video vertical ]" ca-n prototip.

## Ce nu am făcut (intenționat, în afara scopului acestui pas)

- Nu am activat payment providers, nu am publicat nimic live, nu am șters produse sau
  colecții existente.
- Grid-ul homepage arată doar produsele puse manual în colecția "Homepage" — nu există
  produse placeholder inventate; cu un singur produs real creat, grid-ul arată un singur
  card, ceea ce e corect și așteptat.
- Restul produselor menționate în conversația de design (Dumpster Badger, Flower Ladybug
  etc.) nu sunt create aici — grid-ul e deja pregătit să le afișeze automat de îndată ce
  le adaugi în colecție, cu tag-urile potrivite (`playseturi` / `figurine` / `keychains`,
  plus opțional `bestseller` / `nou` / `pret-prietenos`).
