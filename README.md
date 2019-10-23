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
Saves all available student data about yourself to student.json

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

## save_accepted_request_companies
Saves all company data for accepted requests to companies_accepted.json. There is much more interesting data about these companies in this file than in the standard companies.json file.

Example:
```
./main.py save_accepted_request_companies
```
Output:
```
Please enter your mail address: pascscha@student.ethz.ch
Please enter your password:

Saved data to companies_accepted.json.
```

## display_interview_stats
Shows usefull stats for your upcoming interview, including some otherwise unaccessible information, such as accepted / rejected count, the names and position of the recruiters and wether the company has booked the economy or business package.

```
Please enter your mail address: pascscha@student.ethz.ch
Please enter your password:

Sitrox (www.sitrox.com)
Package: Economy
Accepted: 3, Rejected: 16
Recruiters:
 Marius Roth - HR
 Thomas Singer - HR
Interview Goal:
1. Gegenseitiges Kennenlernen
2. Diskussion eines Projekts des kandidierenden Person
3. Weiteres Vorgehen

Bertschi AG (www.bertschi.com)
Package: Economy
Accepted: 8, Rejected: 23
Recruiters:
 Markus Berner - Leiter Bertschi Digital Logistics
 Joël Bader - Software Development Teamleader
Interview Goal:
Generelle sowie technische Fragen.

Simplificator AG (www.simplificator.com)
Package: Business
Accepted: 9, Rejected: 14
Recruiters:
 Eppler Lukas - Gründer und Geschäftsführer
 Blatter Sandra - HR Verantwortliche
Interview Goal:
Wir suchen junge, aufgestellte und teamfähige Entwickler (Fullstack), die gerne in einem kleineren Team arbeiten und nicht nur eine "Nummer" sein wollen.

PriceHubble AG (www.pricehubble.com)
Package: Economy
Accepted: 8, Rejected: 26
Recruiters:
 Batiste Bieler - Lead Frontend Engineer
 Mario Ubeda Garcia - CTO
Interview Goal:
Technical rounds interviews
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

Firmen, Akzeptierte Bewerbungen (Stand 23.10.2019)
  39 AWK Group AG
  26 D ONE Solutions AG
  18 Cisco Systems Switzerland
  16 ipt Innovation Process Technology
  16 PRODYNA (Schweiz) AG
  16 Zühlke Engineering AG
  16 Synpulse Management Consulting Schweiz AG
  16 Bank J. Safra Sarasin Ltd.
  16 Partners Group
  16 Netlight Consulting AG
  16 Stadler
  16 Leica Geosystems - part of Hexagon
  15 Orbium AG
  15 EY
  9 saracus consulting AG
  9 Siemens Schweiz AG
  9 KPMG AG
  9 Unitek Engineering AG
  9 Advertima AG
  9 Accenture
  9 Erni Schweiz AG
  9 abaQon AG
  9 Post CH AG
  9 True Wealth
  9 Apple
  9 Bard BD Interventional
X 9 Simplificator AG
  9 CAMELOT Management Consultants AG
  8 Sonova AG
  8 AdNovum Informatik AG
  8 UNITY Schweiz AG
  8 Confinale AG
  8 ELCA Informatik AG
  8 CSL Behring AG
  8 Horváth & Partners Management Consultants
  8 Swissgrid AG
  8 HighCoordination Schweiz GmbH
  8 Digitec Galaxus
  8 ti&m AG
  8 GetYourGuide AG
  8 Implenia Schweiz AG
  8 Palantir Technologies
  8 BCT Technology GmbH
  8 VAT Group AG
  8 On-Point Connect AG
  8 Optima Nexus Consulting AG
X 8 Bertschi AG
  8 SIX
  8 AXA Versicherungen AG
  8 GFT Schweiz AG
  8 WinGD (Winterthur Gas & Diesel Ltd.)
  8 Sensirion AG
X 8 PriceHubble AG
  8 VINCI Energies Schweiz AG
  7 Oliver Wyman AG
  7 PostFinance AG
  7 Sika
  7 Altersis Performance AG
  7 Celonis
  7 Noser Engineering AG
  6 BSI Business Systems Integration AG
  6 PARALLEL Informatik AG
  6 Metagon AG
  6 Netcetera
  6 UBS
  6 Open Systems AG
  6 duagon AG
  6 fundinfo AG
  6 HBM Partners AG
  6 Fachgruppe Georessourcen Schweiz
  5 Sunrise Communications AG
  4 Libera AG
  4 Komax AG
X 3 Sitrox
You are accepted by 4 companies.

You are accepted by 1 companies.
```