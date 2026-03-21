# Pickns (handicapped.io)
A lightweight, structured web application for browsing U.S. thoroughbred race data by date, track, and race.

## Overview
Handicapped.io provides a fast, minimal interface for viewing race schedules and race‑level details across U.S. racetracks. The application exposes a predictable URL structure and clean HTML pages suitable for both human users and downstream integrations.

The site supports three core views:

1. **Today’s active racetracks**
2. **Race cards for a specific track on a specific date**
3. **Detailed information for an individual race**

All pages follow a consistent pattern, making the service easy to navigate and simple to extend.

---

## Features

### 1. Today’s Races (Homepage)
**URL:**  

/

Displays all racetracks running **today**, each linking to its race card.  
Examples include:

- Fairmount Park (IL)  
- Finger Lakes (NY)  
- Horseshoe Indianapolis (IN)  
- Mahoning Valley (OH)  
- Mountaineer (WV)  
- Parx Racing (PA)  
- Will Rogers Downs (OK)

Each track links to a standardized race‑day URL:


/races/YYYY-MM-DD/TRACK/

---

### 2. Track Race Card
**Example:**  

/races/2025-10-28/FP/

This page displays:

- Track name, state, and country  
- All races scheduled for the selected date  
- Quick links to each race (Race 1, Race 2, etc.)  
- A sortable table containing:

| Field | Description |
|-------|-------------|
| Race # | Race number (e.g., 8) |
| Post Time | Scheduled post time |
| Purse | Total purse amount |
| Type | Race classification (e.g., Allowance Optional Claiming) |
| Distance | Distance in furlongs |
| Surface | Dirt, turf, synthetic |
| Breed | Typically TB |

The table supports column sorting for easier navigation.

---

### 3. Individual Race Page
**Example:**  

/races/2025-10-28/FP/8/

Displays race‑specific details, including:

- Race number and post time  
- Race conditions and classification  
- Entry‑level information (varies by data availability)  
- Breadcrumb navigation back to the track’s race card  

This page follows the same structural pattern for all tracks and dates.

---

## URL Structure

The application uses a clean, REST‑like URL format:

### Today’s Races

/

### Track Race Card

/races/<YYYY-MM-DD>/<TRACK>/

### Individual Race

/races/<YYYY-MM-DD>/<TRACK>/<RACE_NUMBER>/

This predictable structure makes the service easy to integrate with scripts, scrapers, or analytics tools.

---

## Technology

| Component | Description |
|----------|-------------|
| Framework | Python Django web framework |
| Frontend | Static HTML templates |
| Data | Parsed race‑day information |
| Extras | Cookie‑consent banner, mobile‑friendly layout |

---

## Roadmap

Potential future enhancements:

- JSON API endpoints (e.g., `/api/races/today`)  
- Odds, results, scratches, and changes  
- User accounts and saved race lists  
- Track‑level statistics  

---
