# CampusInterview
Displays stats for campusinterview students, such as accepted requests per company.

This tool was made for CampusInterview 2019, it might not work in later years anymore.

Strangely, the script seems to have trouble verifying the sites SSL Certificate (which never happens on other sites). If this is a problem for you and you know what you're doing you can pass the extra argument `verify_ssl=False` to the `StudentProfile` class in `main.py`. Just be aware that this could leak your password and lead to MITM attacks.

# Available Functions

## display_id
Displays your Campusinterview ID.

Example:
```
./main.py display_id
```
Output:
```
Please enter your mail address: pascscha@student.ethz.ch
Please enter your password:
Your ID is: 5d93 [Censored]
```

## save_company_data
Saves all available company data to companies.json

Example:
```
./main.py save_company_data
```
Output:
```
Please enter your mail address: pascscha@student.ethz.ch
Please enter your password:

Saved data to companies.json.
```

## save_student_data
Saves all available student data about yourself to companies.json

Example:
```
./main.py save_student_data
```
Output:
```
Please enter your mail address: pascscha@student.ethz.ch
Please enter your password:

Saved data to student.json.
```

## company_acceptance_count
Sorts all companies by acceptance count and shows which of them accepted you.

Example:
```
./main.py company_acceptance_count
```
Output:
```
Please enter your mail address: pascscha@student.ethz.ch
Please enter your password:

Firmen, Akzeptierte Bewerbungen (Stand 14.10.2019)
  31 AWK Group AG
  27 D ONE Solutions AG
  16 ipt Innovation Process Technology
  16 Stadler
  15 EY
  14 Netlight Consulting AG
  12 Zühlke Engineering AG
  9 PRODYNA (Schweiz) AG
  9 Unitek Engineering AG
  9 Bank J. Safra Sarasin Ltd.
  9 Apple
  8 AdNovum Informatik AG
  8 UNITY Schweiz AG
  8 Siemens Schweiz AG
  8 Orbium AG
  8 Oliver Wyman AG
  8 Horváth & Partners Management Consultants
  8 Advertima AG
  8 HighCoordination Schweiz GmbH
  8 Digitec Galaxus
  8 ti&m AG
  8 VAT Group AG
  8 On-Point Connect AG
  8 Bertschi AG
  8 SIX
  8 AXA Versicherungen AG
  8 GFT Schweiz AG
  8 Sensirion AG
  7 Sonova AG
  7 Optima Nexus Consulting AG
  7 True Wealth
  6 KPMG AG
  6 Accenture
  6 HBM Partners AG
  6 Celonis
  6 Bard BD Interventional
  6 WinGD (Winterthur Gas & Diesel Ltd.)
  5 Metagon AG
  5 Netcetera
  5 saracus consulting AG
  5 Confinale AG
  5 Open Systems AG
  5 Palantir Technologies
  5 BCT Technology GmbH
  5 CAMELOT Management Consultants AG
  4 BSI Business Systems Integration AG
  4 ELCA Informatik AG
  4 Partners Group
  4 Erni Schweiz AG
  4 abaQon AG
  4 PostFinance AG
  4 Sunrise Communications AG
  4 Sika
  3 PARALLEL Informatik AG
  3 Implenia Schweiz AG
X 3 Simplificator AG
  2 duagon AG
  2 fundinfo AG
  2 Noser Engineering AG
  2 Fachgruppe Georessourcen Schweiz
  2 VINCI Energies Schweiz AG
  2 PriceHubble AG
  1 Libera AG
  1 Altersis Performance AG
  0 Sitrox
  0 UBS
  0 Synpulse Management Consulting Schweiz AG
  0 CSL Behring AG
  0 APG|SGA, Allgemeine Plakatgesellschaft AG
  0 uniqFEED AG
  0 Swissgrid AG
  0 Komax AG
  0 GetYourGuide AG
  0 Cisco Systems Switzerland
  0 Burckhardt Compression AG
  0 Leica Geosystems - part of Hexagon
  0 Post CH AG
You are accepted by 1 companies.
```