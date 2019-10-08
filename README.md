# CampusInterview
Displays stats for campusinterview students, such as accepted requests per company.

This tool was made for CampusInterview 2019, it might not work in later years anymore.

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

Firmen, Akzeptierte Bewerbungen (Stand 08.10.2019)
  23 D ONE Solutions AG
  16 Stadler
  13 AWK Group AG
  12 ipt Innovation Process Technology
  10 Zühlke Engineering AG
  10 EY
  8 UNITY Schweiz AG
  8 Oliver Wyman AG
  8 VAT Group AG
  7 Digitec Galaxus
  6 Horváth & Partners Management Consultants
  6 HighCoordination Schweiz GmbH
  6 HBM Partners AG
  6 AXA Versicherungen AG
  5 Unitek Engineering AG
  5 Orbium AG
  5 Optima Nexus Consulting AG
  5 SIX
  4 AdNovum Informatik AG
  4 PRODYNA (Schweiz) AG
  4 Confinale AG
  4 Open Systems AG
  4 ELCA Informatik AG
  4 Palantir Technologies
  3 GFT Schweiz AG
  3 Siemens Schweiz AG
  3 Netlight Consulting AG
  3 abaQon AG
  3 On-Point Connect AG
  3 Sensirion AG
  3 Sunrise Communications AG
  3 Bertschi AG
  2 saracus consulting AG
  2 Noser Engineering AG
  2 Erni Schweiz AG
  2 Fachgruppe Georessourcen Schweiz
  2 BCT Technology GmbH
  2 VINCI Energies Schweiz AG
X 2 Simplificator AG
  2 Celonis
  1 PARALLEL Informatik AG
  1 Advertima AG
  1 Bard BD Interventional
  0 BSI Business Systems Integration AG
  0 Sitrox
  0 Libera AG
  0 Sonova AG
  0 Metagon AG
  0 Netcetera
  0 KPMG AG
  0 UBS
  0 Synpulse Management Consulting Schweiz AG
  0 CSL Behring AG
  0 duagon AG
  0 fundinfo AG
  0 WinGD (Winterthur Gas & Diesel Ltd.)
  0 APG|SGA, Allgemeine Plakatgesellschaft AG
  0 PriceHubble AG
  0 Accenture
  0 Komax AG
  0 Bank J. Safra Sarasin Ltd.
  0 ti&m AG
  0 Partners Group
  0 GetYourGuide AG
  0 Implenia Schweiz AG
  0 Cisco Systems Switzerland
  0 Swissgrid AG
  0 Apple
  0 Burckhardt Compression AG
  0 Leica Geosystems - part of Hexagon
  0 PostFinance AG
  0 Post CH AG
  0 Sika
  0 CAMELOT Management Consultants AG
  0 True Wealth
  0 Altersis Performance AG
You are accepted by 1 companies.
```