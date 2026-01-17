import asyncio
import json
import os
from pymongo import AsyncMongoClient

tappa_esistente = {
    "name": "Tappa 1 Assoluti",
    "played": True,
    "partite": {
        "Ottavi di Finale": [
            {
                "id": 5,
                "teamA": "ANDREATTA TIZIANO - BENZI DAVIDE",
                "teamB": "PIZZILEO FILIPPO - INGROSSO PAOLO",
                "playersA": [
                    "ANDREATTA TIZIANO",
                    "BENZI DAVIDE"
                ],
                "playersB": [
                    "PIZZILEO FILIPPO",
                    "INGROSSO PAOLO"
                ],
                "score_sets": [
                    0,
                    2
                ],
                "current_set": 2,
                "points": [
                    0,
                    0
                ],
                "sets_history": [
                    [
                        17,
                        21
                    ],
                    [
                        11,
                        21
                    ]
                ],
                "events": [
                    {
                        "match_time": 150,
                        "type": "Punto e Cambio Palla",
                        "player": "INGROSSO PAOLO",
                        "description": "Punto INGROSSO PAOLO (B)",
                        "score": "0-1"
                    },
                    {
                        "match_time": 350,
                        "type": "Punto e Cambio Palla",
                        "player": "BENZI DAVIDE",
                        "description": "Punto BENZI DAVIDE (A)",
                        "score": "1-2"
                    },
                    {
                        "match_time": 450,
                        "type": "Punto e Cambio Palla",
                        "player": "PIZZILEO FILIPPO",
                        "description": "Punto PIZZILEO FILIPPO (B)",
                        "score": "1-3"
                    },
                    {
                        "match_time": 800,
                        "type": "Punto e Cambio Palla",
                        "player": "ANDREATTA TIZIANO",
                        "description": "Punto ANDREATTA TIZIANO (A)",
                        "score": "2-4"
                    },
                    {
                        "match_time": 950,
                        "type": "Punto e Cambio Palla",
                        "player": "INGROSSO PAOLO",
                        "description": "Punto INGROSSO PAOLO (B)",
                        "score": "2-5"
                    },
                    {
                        "match_time": 950,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 1050,
                        "type": "Punto e Cambio Palla",
                        "player": "BENZI DAVIDE",
                        "description": "Punto BENZI DAVIDE (A)",
                        "score": "3-5"
                    },
                    {
                        "match_time": 1250,
                        "type": "Punto e Cambio Palla",
                        "player": "PIZZILEO FILIPPO",
                        "description": "Punto PIZZILEO FILIPPO (B)",
                        "score": "3-6"
                    },
                    {
                        "match_time": 1550,
                        "type": "Punto e Cambio Palla",
                        "player": "ANDREATTA TIZIANO",
                        "description": "Punto ANDREATTA TIZIANO (A)",
                        "score": "4-7"
                    },
                    {
                        "match_time": 1700,
                        "type": "Punto e Cambio Palla",
                        "player": "INGROSSO PAOLO",
                        "description": "Punto INGROSSO PAOLO (B)",
                        "score": "4-8"
                    },
                    {
                        "match_time": 1750,
                        "type": "Punto e Cambio Palla",
                        "player": "BENZI DAVIDE",
                        "description": "Punto BENZI DAVIDE (A)",
                        "score": "5-8"
                    },
                    {
                        "match_time": 1950,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 2400,
                        "type": "Punto e Cambio Palla",
                        "player": "PIZZILEO FILIPPO",
                        "description": "Punto PIZZILEO FILIPPO (B)",
                        "score": "8-9"
                    },
                    {
                        "match_time": 2950,
                        "type": "Punto e Cambio Palla",
                        "player": "ANDREATTA TIZIANO",
                        "description": "Punto ANDREATTA TIZIANO (A)",
                        "score": "9-12"
                    },
                    {
                        "match_time": 2950,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 2950,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 3200,
                        "type": "Punto e Cambio Palla",
                        "player": "INGROSSO PAOLO",
                        "description": "Punto INGROSSO PAOLO (B)",
                        "score": "10-13"
                    },
                    {
                        "match_time": 3500,
                        "type": "Punto e Cambio Palla",
                        "player": "BENZI DAVIDE",
                        "description": "Punto BENZI DAVIDE (A)",
                        "score": "11-14"
                    },
                    {
                        "match_time": 3650,
                        "type": "Punto e Cambio Palla",
                        "player": "PIZZILEO FILIPPO",
                        "description": "Punto PIZZILEO FILIPPO (B)",
                        "score": "11-15"
                    },
                    {
                        "match_time": 3850,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 4100,
                        "type": "Punto e Cambio Palla",
                        "player": "ANDREATTA TIZIANO",
                        "description": "Punto ANDREATTA TIZIANO (A)",
                        "score": "12-18"
                    },
                    {
                        "match_time": 4400,
                        "type": "Punto e Cambio Palla",
                        "player": "INGROSSO PAOLO",
                        "description": "Punto INGROSSO PAOLO (B)",
                        "score": "13-19"
                    },
                    {
                        "match_time": 4500,
                        "type": "Punto e Cambio Palla",
                        "player": "BENZI DAVIDE",
                        "description": "Punto BENZI DAVIDE (A)",
                        "score": "14-19"
                    },
                    {
                        "match_time": 4900,
                        "type": "Punto e Cambio Palla",
                        "player": "PIZZILEO FILIPPO",
                        "description": "Punto PIZZILEO FILIPPO (B)",
                        "score": "15-20"
                    },
                    {
                        "match_time": 4900,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 5050,
                        "type": "Punto e Cambio Palla",
                        "player": "ANDREATTA TIZIANO",
                        "description": "Punto ANDREATTA TIZIANO (A)",
                        "score": "16-20"
                    },
                    {
                        "match_time": 5200,
                        "type": "Punto e Cambio Palla",
                        "player": "INGROSSO PAOLO",
                        "description": "Punto INGROSSO PAOLO (B)",
                        "score": "17-21"
                    },
                    {
                        "match_time": 5200,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team B"
                    },
                    {
                        "match_time": 5450,
                        "type": "Punto e Cambio Palla",
                        "player": "BENZI DAVIDE",
                        "description": "Punto BENZI DAVIDE (A)",
                        "score": "1-1"
                    },
                    {
                        "match_time": 5600,
                        "type": "Punto e Cambio Palla",
                        "player": "PIZZILEO FILIPPO",
                        "description": "Punto PIZZILEO FILIPPO (B)",
                        "score": "1-2"
                    },
                    {
                        "match_time": 5750,
                        "type": "Punto e Cambio Palla",
                        "player": "ANDREATTA TIZIANO",
                        "description": "Punto ANDREATTA TIZIANO (A)",
                        "score": "2-2"
                    },
                    {
                        "match_time": 6000,
                        "type": "Punto e Cambio Palla",
                        "player": "INGROSSO PAOLO",
                        "description": "Punto INGROSSO PAOLO (B)",
                        "score": "3-3"
                    },
                    {
                        "match_time": 6150,
                        "type": "Punto e Cambio Palla",
                        "player": "BENZI DAVIDE",
                        "description": "Punto BENZI DAVIDE (A)",
                        "score": "4-3"
                    },
                    {
                        "match_time": 6150,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 6450,
                        "type": "Punto e Cambio Palla",
                        "player": "PIZZILEO FILIPPO",
                        "description": "Punto PIZZILEO FILIPPO (B)",
                        "score": "5-4"
                    },
                    {
                        "match_time": 6550,
                        "type": "Punto e Cambio Palla",
                        "player": "ANDREATTA TIZIANO",
                        "description": "Punto ANDREATTA TIZIANO (A)",
                        "score": "6-4"
                    },
                    {
                        "match_time": 6750,
                        "type": "Punto e Cambio Palla",
                        "player": "INGROSSO PAOLO",
                        "description": "Punto INGROSSO PAOLO (B)",
                        "score": "6-5"
                    },
                    {
                        "match_time": 6900,
                        "type": "Punto e Cambio Palla",
                        "player": "BENZI DAVIDE",
                        "description": "Punto BENZI DAVIDE (A)",
                        "score": "7-5"
                    },
                    {
                        "match_time": 7000,
                        "type": "Punto e Cambio Palla",
                        "player": "PIZZILEO FILIPPO",
                        "description": "Punto PIZZILEO FILIPPO (B)",
                        "score": "7-6"
                    },
                    {
                        "match_time": 7200,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 7500,
                        "type": "Punto e Cambio Palla",
                        "player": "ANDREATTA TIZIANO",
                        "description": "Punto ANDREATTA TIZIANO (A)",
                        "score": "8-8"
                    },
                    {
                        "match_time": 7650,
                        "type": "Punto e Cambio Palla",
                        "player": "INGROSSO PAOLO",
                        "description": "Punto INGROSSO PAOLO (B)",
                        "score": "8-9"
                    },
                    {
                        "match_time": 8150,
                        "type": "Punto e Cambio Palla",
                        "player": "BENZI DAVIDE",
                        "description": "Punto BENZI DAVIDE (A)",
                        "score": "9-12"
                    },
                    {
                        "match_time": 8150,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 8150,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 8450,
                        "type": "Punto e Cambio Palla",
                        "player": "PIZZILEO FILIPPO",
                        "description": "Punto PIZZILEO FILIPPO (B)",
                        "score": "10-13"
                    },
                    {
                        "match_time": 8500,
                        "type": "Punto e Cambio Palla",
                        "player": "ANDREATTA TIZIANO",
                        "description": "Punto ANDREATTA TIZIANO (A)",
                        "score": "11-13"
                    },
                    {
                        "match_time": 8600,
                        "type": "Punto e Cambio Palla",
                        "player": "INGROSSO PAOLO",
                        "description": "Punto INGROSSO PAOLO (B)",
                        "score": "11-14"
                    },
                    {
                        "match_time": 9100,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 9750,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team B"
                    },
                    {
                        "match_time": 9750,
                        "type": "Fine Match",
                        "player": "Arbitro",
                        "description": "Partita Terminata"
                    }
                ],
                "match_time": 9750,
                "status": "finished",
                "server_team": 1,
                "server_index": [
                    0,
                    1
                ],
                "final_type": None
            },
            {
                "id": 7,
                "teamA": "COTTAFAVA SAMUELE - DAL CORSO GIANLUCA",
                "teamB": "VISCOVICH MARCO - ROSSI ENRICO",
                "playersA": [
                    "COTTAFAVA SAMUELE",
                    "DAL CORSO GIANLUCA"
                ],
                "playersB": [
                    "VISCOVICH MARCO",
                    "ROSSI ENRICO"
                ],
                "score_sets": [
                    0,
                    2
                ],
                "current_set": 2,
                "points": [
                    0,
                    0
                ],
                "sets_history": [
                    [
                        15,
                        21
                    ],
                    [
                        15,
                        21
                    ]
                ],
                "events": [
                    {
                        "match_time": 150,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (B)",
                        "score": "0-1"
                    },
                    {
                        "match_time": 250,
                        "type": "Punto e Cambio Palla",
                        "player": "DAL CORSO GIANLUCA",
                        "description": "Punto DAL CORSO GIANLUCA (A)",
                        "score": "1-1"
                    },
                    {
                        "match_time": 700,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (B)",
                        "score": "3-2"
                    },
                    {
                        "match_time": 1000,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 1200,
                        "type": "Punto e Cambio Palla",
                        "player": "COTTAFAVA SAMUELE",
                        "description": "Punto COTTAFAVA SAMUELE (A)",
                        "score": "4-4"
                    },
                    {
                        "match_time": 1350,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (B)",
                        "score": "4-5"
                    },
                    {
                        "match_time": 1800,
                        "type": "Punto e Cambio Palla",
                        "player": "DAL CORSO GIANLUCA",
                        "description": "Punto DAL CORSO GIANLUCA (A)",
                        "score": "5-7"
                    },
                    {
                        "match_time": 1900,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (B)",
                        "score": "5-8"
                    },
                    {
                        "match_time": 2050,
                        "type": "Punto e Cambio Palla",
                        "player": "COTTAFAVA SAMUELE",
                        "description": "Punto COTTAFAVA SAMUELE (A)",
                        "score": "6-8"
                    },
                    {
                        "match_time": 2050,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 2100,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (B)",
                        "score": "6-9"
                    },
                    {
                        "match_time": 2300,
                        "type": "Punto e Cambio Palla",
                        "player": "DAL CORSO GIANLUCA",
                        "description": "Punto DAL CORSO GIANLUCA (A)",
                        "score": "7-9"
                    },
                    {
                        "match_time": 2550,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (B)",
                        "score": "8-10"
                    },
                    {
                        "match_time": 2750,
                        "type": "Punto e Cambio Palla",
                        "player": "COTTAFAVA SAMUELE",
                        "description": "Punto COTTAFAVA SAMUELE (A)",
                        "score": "9-11"
                    },
                    {
                        "match_time": 2850,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (B)",
                        "score": "9-12"
                    },
                    {
                        "match_time": 2850,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 2850,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 3250,
                        "type": "Punto e Cambio Palla",
                        "player": "DAL CORSO GIANLUCA",
                        "description": "Punto DAL CORSO GIANLUCA (A)",
                        "score": "10-14"
                    },
                    {
                        "match_time": 3500,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (B)",
                        "score": "11-15"
                    },
                    {
                        "match_time": 3650,
                        "type": "Punto e Cambio Palla",
                        "player": "COTTAFAVA SAMUELE",
                        "description": "Punto COTTAFAVA SAMUELE (A)",
                        "score": "12-15"
                    },
                    {
                        "match_time": 3800,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (B)",
                        "score": "12-16"
                    },
                    {
                        "match_time": 3800,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 4000,
                        "type": "Punto e Cambio Palla",
                        "player": "DAL CORSO GIANLUCA",
                        "description": "Punto DAL CORSO GIANLUCA (A)",
                        "score": "13-16"
                    },
                    {
                        "match_time": 4100,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (B)",
                        "score": "13-17"
                    },
                    {
                        "match_time": 4500,
                        "type": "Punto e Cambio Palla",
                        "player": "COTTAFAVA SAMUELE",
                        "description": "Punto COTTAFAVA SAMUELE (A)",
                        "score": "14-19"
                    },
                    {
                        "match_time": 4800,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (B)",
                        "score": "15-20"
                    },
                    {
                        "match_time": 4800,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 4900,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team B"
                    },
                    {
                        "match_time": 5450,
                        "type": "Punto e Cambio Palla",
                        "player": "DAL CORSO GIANLUCA",
                        "description": "Punto DAL CORSO GIANLUCA (A)",
                        "score": "1-3"
                    },
                    {
                        "match_time": 5550,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (B)",
                        "score": "1-4"
                    },
                    {
                        "match_time": 5700,
                        "type": "Punto e Cambio Palla",
                        "player": "COTTAFAVA SAMUELE",
                        "description": "Punto COTTAFAVA SAMUELE (A)",
                        "score": "2-4"
                    },
                    {
                        "match_time": 5850,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 6150,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (B)",
                        "score": "4-5"
                    },
                    {
                        "match_time": 6250,
                        "type": "Punto e Cambio Palla",
                        "player": "DAL CORSO GIANLUCA",
                        "description": "Punto DAL CORSO GIANLUCA (A)",
                        "score": "5-5"
                    },
                    {
                        "match_time": 6550,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (B)",
                        "score": "6-6"
                    },
                    {
                        "match_time": 6900,
                        "type": "Punto e Cambio Palla",
                        "player": "COTTAFAVA SAMUELE",
                        "description": "Punto COTTAFAVA SAMUELE (A)",
                        "score": "7-7"
                    },
                    {
                        "match_time": 6900,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 6950,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (B)",
                        "score": "7-8"
                    },
                    {
                        "match_time": 7500,
                        "type": "Punto e Cambio Palla",
                        "player": "DAL CORSO GIANLUCA",
                        "description": "Punto DAL CORSO GIANLUCA (A)",
                        "score": "8-11"
                    },
                    {
                        "match_time": 7850,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 7850,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 8150,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (B)",
                        "score": "11-12"
                    },
                    {
                        "match_time": 8900,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 9100,
                        "type": "Punto e Cambio Palla",
                        "player": "COTTAFAVA SAMUELE",
                        "description": "Punto COTTAFAVA SAMUELE (A)",
                        "score": "12-18"
                    },
                    {
                        "match_time": 9400,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (B)",
                        "score": "13-19"
                    },
                    {
                        "match_time": 9550,
                        "type": "Punto e Cambio Palla",
                        "player": "DAL CORSO GIANLUCA",
                        "description": "Punto DAL CORSO GIANLUCA (A)",
                        "score": "14-19"
                    },
                    {
                        "match_time": 9750,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (B)",
                        "score": "14-20"
                    },
                    {
                        "match_time": 9900,
                        "type": "Punto e Cambio Palla",
                        "player": "COTTAFAVA SAMUELE",
                        "description": "Punto COTTAFAVA SAMUELE (A)",
                        "score": "15-20"
                    },
                    {
                        "match_time": 9900,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 10000,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (B)",
                        "score": "15-21"
                    },
                    {
                        "match_time": 10000,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team B"
                    },
                    {
                        "match_time": 10000,
                        "type": "Fine Match",
                        "player": "Arbitro",
                        "description": "Partita Terminata"
                    }
                ],
                "match_time": 10000,
                "status": "finished",
                "server_team": 1,
                "server_index": [
                    0,
                    1
                ],
                "final_type": None
            },
            {
                "id": 3,
                "teamA": "PODESTA' SIMONE - MARTINO MATTEO",
                "teamB": "AREZZO DI TRIFILETTI FRANCO - BIGARELLI LUCA",
                "playersA": [
                    "PODESTA' SIMONE",
                    "MARTINO MATTEO"
                ],
                "playersB": [
                    "AREZZO DI TRIFILETTI FRANCO",
                    "BIGARELLI LUCA"
                ],
                "score_sets": [
                    0,
                    2
                ],
                "current_set": 2,
                "points": [
                    0,
                    0
                ],
                "sets_history": [
                    [
                        19,
                        21
                    ],
                    [
                        19,
                        21
                    ]
                ],
                "events": [
                    {
                        "match_time": 650,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (B)",
                        "score": "3-1"
                    },
                    {
                        "match_time": 950,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 1100,
                        "type": "Punto e Cambio Palla",
                        "player": "MARTINO MATTEO",
                        "description": "Punto MARTINO MATTEO (A)",
                        "score": "4-4"
                    },
                    {
                        "match_time": 1250,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (B)",
                        "score": "4-5"
                    },
                    {
                        "match_time": 1550,
                        "type": "Punto e Cambio Palla",
                        "player": "PODESTA' SIMONE",
                        "description": "Punto PODESTA' SIMONE (A)",
                        "score": "5-7"
                    },
                    {
                        "match_time": 1850,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 2000,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (B)",
                        "score": "7-8"
                    },
                    {
                        "match_time": 2100,
                        "type": "Punto e Cambio Palla",
                        "player": "MARTINO MATTEO",
                        "description": "Punto MARTINO MATTEO (A)",
                        "score": "8-8"
                    },
                    {
                        "match_time": 2950,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (B)",
                        "score": "12-9"
                    },
                    {
                        "match_time": 2950,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 2950,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 3150,
                        "type": "Punto e Cambio Palla",
                        "player": "PODESTA' SIMONE",
                        "description": "Punto PODESTA' SIMONE (A)",
                        "score": "13-10"
                    },
                    {
                        "match_time": 3400,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (B)",
                        "score": "14-11"
                    },
                    {
                        "match_time": 3800,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 4050,
                        "type": "Punto e Cambio Palla",
                        "player": "MARTINO MATTEO",
                        "description": "Punto MARTINO MATTEO (A)",
                        "score": "15-15"
                    },
                    {
                        "match_time": 4350,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (B)",
                        "score": "16-16"
                    },
                    {
                        "match_time": 4450,
                        "type": "Punto e Cambio Palla",
                        "player": "PODESTA' SIMONE",
                        "description": "Punto PODESTA' SIMONE (A)",
                        "score": "17-16"
                    },
                    {
                        "match_time": 4550,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (B)",
                        "score": "17-17"
                    },
                    {
                        "match_time": 4650,
                        "type": "Punto e Cambio Palla",
                        "player": "MARTINO MATTEO",
                        "description": "Punto MARTINO MATTEO (A)",
                        "score": "18-17"
                    },
                    {
                        "match_time": 4650,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 4750,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (B)",
                        "score": "18-18"
                    },
                    {
                        "match_time": 4950,
                        "type": "Punto e Cambio Palla",
                        "player": "PODESTA' SIMONE",
                        "description": "Punto PODESTA' SIMONE (A)",
                        "score": "19-18"
                    },
                    {
                        "match_time": 5100,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (B)",
                        "score": "19-19"
                    },
                    {
                        "match_time": 5350,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team B"
                    },
                    {
                        "match_time": 5500,
                        "type": "Punto e Cambio Palla",
                        "player": "MARTINO MATTEO",
                        "description": "Punto MARTINO MATTEO (A)",
                        "score": "1-0"
                    },
                    {
                        "match_time": 5650,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (B)",
                        "score": "1-1"
                    },
                    {
                        "match_time": 5850,
                        "type": "Punto e Cambio Palla",
                        "player": "PODESTA' SIMONE",
                        "description": "Punto PODESTA' SIMONE (A)",
                        "score": "2-1"
                    },
                    {
                        "match_time": 6100,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (B)",
                        "score": "3-2"
                    },
                    {
                        "match_time": 6250,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 6650,
                        "type": "Punto e Cambio Palla",
                        "player": "MARTINO MATTEO",
                        "description": "Punto MARTINO MATTEO (A)",
                        "score": "4-6"
                    },
                    {
                        "match_time": 7000,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (B)",
                        "score": "6-7"
                    },
                    {
                        "match_time": 7150,
                        "type": "Punto e Cambio Palla",
                        "player": "PODESTA' SIMONE",
                        "description": "Punto PODESTA' SIMONE (A)",
                        "score": "7-7"
                    },
                    {
                        "match_time": 7150,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 7250,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (B)",
                        "score": "7-8"
                    },
                    {
                        "match_time": 7450,
                        "type": "Punto e Cambio Palla",
                        "player": "MARTINO MATTEO",
                        "description": "Punto MARTINO MATTEO (A)",
                        "score": "8-8"
                    },
                    {
                        "match_time": 7650,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (B)",
                        "score": "8-9"
                    },
                    {
                        "match_time": 7800,
                        "type": "Punto e Cambio Palla",
                        "player": "PODESTA' SIMONE",
                        "description": "Punto PODESTA' SIMONE (A)",
                        "score": "9-9"
                    },
                    {
                        "match_time": 8000,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (B)",
                        "score": "9-10"
                    },
                    {
                        "match_time": 8300,
                        "type": "Punto e Cambio Palla",
                        "player": "MARTINO MATTEO",
                        "description": "Punto MARTINO MATTEO (A)",
                        "score": "10-11"
                    },
                    {
                        "match_time": 8300,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 8300,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 8450,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (B)",
                        "score": "10-12"
                    },
                    {
                        "match_time": 8600,
                        "type": "Punto e Cambio Palla",
                        "player": "PODESTA' SIMONE",
                        "description": "Punto PODESTA' SIMONE (A)",
                        "score": "11-12"
                    },
                    {
                        "match_time": 8700,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (B)",
                        "score": "11-13"
                    },
                    {
                        "match_time": 8850,
                        "type": "Punto e Cambio Palla",
                        "player": "MARTINO MATTEO",
                        "description": "Punto MARTINO MATTEO (A)",
                        "score": "12-13"
                    },
                    {
                        "match_time": 8950,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (B)",
                        "score": "12-14"
                    },
                    {
                        "match_time": 9300,
                        "type": "Punto e Cambio Palla",
                        "player": "PODESTA' SIMONE",
                        "description": "Punto PODESTA' SIMONE (A)",
                        "score": "13-15"
                    },
                    {
                        "match_time": 9300,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 9650,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (B)",
                        "score": "15-16"
                    },
                    {
                        "match_time": 10050,
                        "type": "Punto e Cambio Palla",
                        "player": "MARTINO MATTEO",
                        "description": "Punto MARTINO MATTEO (A)",
                        "score": "16-18"
                    },
                    {
                        "match_time": 10100,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 10500,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (B)",
                        "score": "19-19"
                    },
                    {
                        "match_time": 10750,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team B"
                    },
                    {
                        "match_time": 10750,
                        "type": "Fine Match",
                        "player": "Arbitro",
                        "description": "Partita Terminata"
                    }
                ],
                "match_time": 10750,
                "status": "finished",
                "server_team": 1,
                "server_index": [
                    1,
                    0
                ],
                "final_type": None
            },
            {
                "id": 4,
                "teamA": "MARCHETTO TOBIA - DAL MOLIN DAVIDE",
                "teamB": "GEROMIN FEDERICO - CAMOZZI MATTEO",
                "playersA": [
                    "MARCHETTO TOBIA",
                    "DAL MOLIN DAVIDE"
                ],
                "playersB": [
                    "GEROMIN FEDERICO",
                    "CAMOZZI MATTEO"
                ],
                "score_sets": [
                    2,
                    1
                ],
                "current_set": 3,
                "points": [
                    0,
                    0
                ],
                "sets_history": [
                    [
                        15,
                        21
                    ],
                    [
                        21,
                        11
                    ],
                    [
                        15,
                        13
                    ]
                ],
                "events": [
                    {
                        "match_time": 150,
                        "type": "Punto e Cambio Palla",
                        "player": "CAMOZZI MATTEO",
                        "description": "Punto CAMOZZI MATTEO (B)",
                        "score": "0-1"
                    },
                    {
                        "match_time": 250,
                        "type": "Punto e Cambio Palla",
                        "player": "DAL MOLIN DAVIDE",
                        "description": "Punto DAL MOLIN DAVIDE (A)",
                        "score": "1-1"
                    },
                    {
                        "match_time": 400,
                        "type": "Punto e Cambio Palla",
                        "player": "GEROMIN FEDERICO",
                        "description": "Punto GEROMIN FEDERICO (B)",
                        "score": "1-2"
                    },
                    {
                        "match_time": 650,
                        "type": "Punto e Cambio Palla",
                        "player": "MARCHETTO TOBIA",
                        "description": "Punto MARCHETTO TOBIA (A)",
                        "score": "2-3"
                    },
                    {
                        "match_time": 800,
                        "type": "Punto e Cambio Palla",
                        "player": "CAMOZZI MATTEO",
                        "description": "Punto CAMOZZI MATTEO (B)",
                        "score": "2-4"
                    },
                    {
                        "match_time": 950,
                        "type": "Punto e Cambio Palla",
                        "player": "DAL MOLIN DAVIDE",
                        "description": "Punto DAL MOLIN DAVIDE (A)",
                        "score": "3-4"
                    },
                    {
                        "match_time": 950,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 1400,
                        "type": "Punto e Cambio Palla",
                        "player": "GEROMIN FEDERICO",
                        "description": "Punto GEROMIN FEDERICO (B)",
                        "score": "5-5"
                    },
                    {
                        "match_time": 1600,
                        "type": "Punto e Cambio Palla",
                        "player": "MARCHETTO TOBIA",
                        "description": "Punto MARCHETTO TOBIA (A)",
                        "score": "6-6"
                    },
                    {
                        "match_time": 1700,
                        "type": "Punto e Cambio Palla",
                        "player": "CAMOZZI MATTEO",
                        "description": "Punto CAMOZZI MATTEO (B)",
                        "score": "6-7"
                    },
                    {
                        "match_time": 1800,
                        "type": "Punto e Cambio Palla",
                        "player": "DAL MOLIN DAVIDE",
                        "description": "Punto DAL MOLIN DAVIDE (A)",
                        "score": "7-7"
                    },
                    {
                        "match_time": 1800,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 1950,
                        "type": "Punto e Cambio Palla",
                        "player": "GEROMIN FEDERICO",
                        "description": "Punto GEROMIN FEDERICO (B)",
                        "score": "7-8"
                    },
                    {
                        "match_time": 2100,
                        "type": "Punto e Cambio Palla",
                        "player": "MARCHETTO TOBIA",
                        "description": "Punto MARCHETTO TOBIA (A)",
                        "score": "8-8"
                    },
                    {
                        "match_time": 2150,
                        "type": "Punto e Cambio Palla",
                        "player": "CAMOZZI MATTEO",
                        "description": "Punto CAMOZZI MATTEO (B)",
                        "score": "8-9"
                    },
                    {
                        "match_time": 2250,
                        "type": "Punto e Cambio Palla",
                        "player": "DAL MOLIN DAVIDE",
                        "description": "Punto DAL MOLIN DAVIDE (A)",
                        "score": "9-9"
                    },
                    {
                        "match_time": 2350,
                        "type": "Punto e Cambio Palla",
                        "player": "GEROMIN FEDERICO",
                        "description": "Punto GEROMIN FEDERICO (B)",
                        "score": "9-10"
                    },
                    {
                        "match_time": 2500,
                        "type": "Punto e Cambio Palla",
                        "player": "MARCHETTO TOBIA",
                        "description": "Punto MARCHETTO TOBIA (A)",
                        "score": "10-10"
                    },
                    {
                        "match_time": 2550,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 2550,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 2650,
                        "type": "Punto e Cambio Palla",
                        "player": "CAMOZZI MATTEO",
                        "description": "Punto CAMOZZI MATTEO (B)",
                        "score": "11-11"
                    },
                    {
                        "match_time": 3650,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 3900,
                        "type": "Punto e Cambio Palla",
                        "player": "DAL MOLIN DAVIDE",
                        "description": "Punto DAL MOLIN DAVIDE (A)",
                        "score": "12-18"
                    },
                    {
                        "match_time": 4000,
                        "type": "Punto e Cambio Palla",
                        "player": "GEROMIN FEDERICO",
                        "description": "Punto GEROMIN FEDERICO (B)",
                        "score": "12-19"
                    },
                    {
                        "match_time": 4150,
                        "type": "Punto e Cambio Palla",
                        "player": "MARCHETTO TOBIA",
                        "description": "Punto MARCHETTO TOBIA (A)",
                        "score": "13-19"
                    },
                    {
                        "match_time": 4550,
                        "type": "Punto e Cambio Palla",
                        "player": "CAMOZZI MATTEO",
                        "description": "Punto CAMOZZI MATTEO (B)",
                        "score": "15-20"
                    },
                    {
                        "match_time": 4550,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 4750,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team B"
                    },
                    {
                        "match_time": 4950,
                        "type": "Punto e Cambio Palla",
                        "player": "DAL MOLIN DAVIDE",
                        "description": "Punto DAL MOLIN DAVIDE (A)",
                        "score": "1-0"
                    },
                    {
                        "match_time": 5100,
                        "type": "Punto e Cambio Palla",
                        "player": "GEROMIN FEDERICO",
                        "description": "Punto GEROMIN FEDERICO (B)",
                        "score": "1-1"
                    },
                    {
                        "match_time": 5250,
                        "type": "Punto e Cambio Palla",
                        "player": "MARCHETTO TOBIA",
                        "description": "Punto MARCHETTO TOBIA (A)",
                        "score": "2-1"
                    },
                    {
                        "match_time": 5650,
                        "type": "Punto e Cambio Palla",
                        "player": "CAMOZZI MATTEO",
                        "description": "Punto CAMOZZI MATTEO (B)",
                        "score": "4-2"
                    },
                    {
                        "match_time": 5750,
                        "type": "Punto e Cambio Palla",
                        "player": "DAL MOLIN DAVIDE",
                        "description": "Punto DAL MOLIN DAVIDE (A)",
                        "score": "5-2"
                    },
                    {
                        "match_time": 5750,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 5900,
                        "type": "Punto e Cambio Palla",
                        "player": "GEROMIN FEDERICO",
                        "description": "Punto GEROMIN FEDERICO (B)",
                        "score": "5-3"
                    },
                    {
                        "match_time": 6000,
                        "type": "Punto e Cambio Palla",
                        "player": "MARCHETTO TOBIA",
                        "description": "Punto MARCHETTO TOBIA (A)",
                        "score": "6-3"
                    },
                    {
                        "match_time": 6750,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 7400,
                        "type": "Punto e Cambio Palla",
                        "player": "CAMOZZI MATTEO",
                        "description": "Punto CAMOZZI MATTEO (B)",
                        "score": "14-4"
                    },
                    {
                        "match_time": 7500,
                        "type": "Punto e Cambio Palla",
                        "player": "DAL MOLIN DAVIDE",
                        "description": "Punto DAL MOLIN DAVIDE (A)",
                        "score": "15-4"
                    },
                    {
                        "match_time": 7650,
                        "type": "Punto e Cambio Palla",
                        "player": "GEROMIN FEDERICO",
                        "description": "Punto GEROMIN FEDERICO (B)",
                        "score": "15-5"
                    },
                    {
                        "match_time": 7750,
                        "type": "Punto e Cambio Palla",
                        "player": "MARCHETTO TOBIA",
                        "description": "Punto MARCHETTO TOBIA (A)",
                        "score": "16-5"
                    },
                    {
                        "match_time": 7750,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 7750,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 8050,
                        "type": "Punto e Cambio Palla",
                        "player": "CAMOZZI MATTEO",
                        "description": "Punto CAMOZZI MATTEO (B)",
                        "score": "17-6"
                    },
                    {
                        "match_time": 8200,
                        "type": "Punto e Cambio Palla",
                        "player": "DAL MOLIN DAVIDE",
                        "description": "Punto DAL MOLIN DAVIDE (A)",
                        "score": "18-6"
                    },
                    {
                        "match_time": 8400,
                        "type": "Punto e Cambio Palla",
                        "player": "GEROMIN FEDERICO",
                        "description": "Punto GEROMIN FEDERICO (B)",
                        "score": "19-7"
                    },
                    {
                        "match_time": 8650,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 9100,
                        "type": "Punto e Cambio Palla",
                        "player": "MARCHETTO TOBIA",
                        "description": "Punto MARCHETTO TOBIA (A)",
                        "score": "20-11"
                    },
                    {
                        "match_time": 9150,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team A"
                    },
                    {
                        "match_time": 9350,
                        "type": "Punto e Cambio Palla",
                        "player": "CAMOZZI MATTEO",
                        "description": "Punto CAMOZZI MATTEO (B)",
                        "score": "0-1"
                    },
                    {
                        "match_time": 9950,
                        "type": "Punto e Cambio Palla",
                        "player": "DAL MOLIN DAVIDE",
                        "description": "Punto DAL MOLIN DAVIDE (A)",
                        "score": "1-4"
                    },
                    {
                        "match_time": 10200,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 10550,
                        "type": "Punto e Cambio Palla",
                        "player": "GEROMIN FEDERICO",
                        "description": "Punto GEROMIN FEDERICO (B)",
                        "score": "5-5"
                    },
                    {
                        "match_time": 10750,
                        "type": "Punto e Cambio Palla",
                        "player": "MARCHETTO TOBIA",
                        "description": "Punto MARCHETTO TOBIA (A)",
                        "score": "6-5"
                    },
                    {
                        "match_time": 10900,
                        "type": "Punto e Cambio Palla",
                        "player": "CAMOZZI MATTEO",
                        "description": "Punto CAMOZZI MATTEO (B)",
                        "score": "7-6"
                    },
                    {
                        "match_time": 11050,
                        "type": "Punto e Cambio Palla",
                        "player": "DAL MOLIN DAVIDE",
                        "description": "Punto DAL MOLIN DAVIDE (A)",
                        "score": "8-6"
                    },
                    {
                        "match_time": 11050,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 11300,
                        "type": "Punto e Cambio Palla",
                        "player": "GEROMIN FEDERICO",
                        "description": "Punto GEROMIN FEDERICO (B)",
                        "score": "9-7"
                    },
                    {
                        "match_time": 11600,
                        "type": "Punto e Cambio Palla",
                        "player": "MARCHETTO TOBIA",
                        "description": "Punto MARCHETTO TOBIA (A)",
                        "score": "10-8"
                    },
                    {
                        "match_time": 12000,
                        "type": "Punto e Cambio Palla",
                        "player": "CAMOZZI MATTEO",
                        "description": "Punto CAMOZZI MATTEO (B)",
                        "score": "12-9"
                    },
                    {
                        "match_time": 12000,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 12000,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 12100,
                        "type": "Punto e Cambio Palla",
                        "player": "DAL MOLIN DAVIDE",
                        "description": "Punto DAL MOLIN DAVIDE (A)",
                        "score": "13-9"
                    },
                    {
                        "match_time": 12200,
                        "type": "Punto e Cambio Palla",
                        "player": "GEROMIN FEDERICO",
                        "description": "Punto GEROMIN FEDERICO (B)",
                        "score": "13-10"
                    },
                    {
                        "match_time": 12650,
                        "type": "Punto e Cambio Palla",
                        "player": "MARCHETTO TOBIA",
                        "description": "Punto MARCHETTO TOBIA (A)",
                        "score": "14-12"
                    },
                    {
                        "match_time": 12750,
                        "type": "Punto e Cambio Palla",
                        "player": "CAMOZZI MATTEO",
                        "description": "Punto CAMOZZI MATTEO (B)",
                        "score": "14-13"
                    },
                    {
                        "match_time": 12850,
                        "type": "Punto e Cambio Palla",
                        "player": "DAL MOLIN DAVIDE",
                        "description": "Punto DAL MOLIN DAVIDE (A)",
                        "score": "15-13"
                    },
                    {
                        "match_time": 12850,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 12850,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team A"
                    },
                    {
                        "match_time": 12850,
                        "type": "Fine Match",
                        "player": "Arbitro",
                        "description": "Partita Terminata"
                    }
                ],
                "match_time": 12850,
                "status": "finished",
                "server_team": 0,
                "server_index": [
                    1,
                    1
                ],
                "final_type": None
            },
            {
                "id": 1,
                "teamA": "ALFIERI MANUEL - RANGHIERI ALEX",
                "teamB": "PRETI ALESSANDRO - MUSSA FABRIZIO",
                "playersA": [
                    "ALFIERI MANUEL",
                    "RANGHIERI ALEX"
                ],
                "playersB": [
                    "PRETI ALESSANDRO",
                    "MUSSA FABRIZIO"
                ],
                "score_sets": [
                    2,
                    1
                ],
                "current_set": 3,
                "points": [
                    0,
                    0
                ],
                "sets_history": [
                    [
                        13,
                        21
                    ],
                    [
                        21,
                        18
                    ],
                    [
                        15,
                        12
                    ]
                ],
                "events": [
                    {
                        "match_time": 300,
                        "type": "Punto e Cambio Palla",
                        "player": "MUSSA FABRIZIO",
                        "description": "Punto MUSSA FABRIZIO (B)",
                        "score": "1-1"
                    },
                    {
                        "match_time": 450,
                        "type": "Punto e Cambio Palla",
                        "player": "RANGHIERI ALEX",
                        "description": "Punto RANGHIERI ALEX (A)",
                        "score": "2-1"
                    },
                    {
                        "match_time": 550,
                        "type": "Punto e Cambio Palla",
                        "player": "PRETI ALESSANDRO",
                        "description": "Punto PRETI ALESSANDRO (B)",
                        "score": "2-2"
                    },
                    {
                        "match_time": 900,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 1200,
                        "type": "Punto e Cambio Palla",
                        "player": "ALFIERI MANUEL",
                        "description": "Punto ALFIERI MANUEL (A)",
                        "score": "3-6"
                    },
                    {
                        "match_time": 1250,
                        "type": "Punto e Cambio Palla",
                        "player": "MUSSA FABRIZIO",
                        "description": "Punto MUSSA FABRIZIO (B)",
                        "score": "3-7"
                    },
                    {
                        "match_time": 1600,
                        "type": "Punto e Cambio Palla",
                        "player": "RANGHIERI ALEX",
                        "description": "Punto RANGHIERI ALEX (A)",
                        "score": "4-8"
                    },
                    {
                        "match_time": 1950,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 2000,
                        "type": "Punto e Cambio Palla",
                        "player": "PRETI ALESSANDRO",
                        "description": "Punto PRETI ALESSANDRO (B)",
                        "score": "6-9"
                    },
                    {
                        "match_time": 2200,
                        "type": "Punto e Cambio Palla",
                        "player": "ALFIERI MANUEL",
                        "description": "Punto ALFIERI MANUEL (A)",
                        "score": "7-9"
                    },
                    {
                        "match_time": 2350,
                        "type": "Punto e Cambio Palla",
                        "player": "MUSSA FABRIZIO",
                        "description": "Punto MUSSA FABRIZIO (B)",
                        "score": "7-10"
                    },
                    {
                        "match_time": 2600,
                        "type": "Punto e Cambio Palla",
                        "player": "RANGHIERI ALEX",
                        "description": "Punto RANGHIERI ALEX (A)",
                        "score": "8-11"
                    },
                    {
                        "match_time": 2700,
                        "type": "Punto e Cambio Palla",
                        "player": "PRETI ALESSANDRO",
                        "description": "Punto PRETI ALESSANDRO (B)",
                        "score": "8-12"
                    },
                    {
                        "match_time": 2900,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 2900,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 3000,
                        "type": "Punto e Cambio Palla",
                        "player": "ALFIERI MANUEL",
                        "description": "Punto ALFIERI MANUEL (A)",
                        "score": "9-13"
                    },
                    {
                        "match_time": 3100,
                        "type": "Punto e Cambio Palla",
                        "player": "MUSSA FABRIZIO",
                        "description": "Punto MUSSA FABRIZIO (B)",
                        "score": "9-14"
                    },
                    {
                        "match_time": 3500,
                        "type": "Punto e Cambio Palla",
                        "player": "RANGHIERI ALEX",
                        "description": "Punto RANGHIERI ALEX (A)",
                        "score": "10-17"
                    },
                    {
                        "match_time": 3600,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 3800,
                        "type": "Punto e Cambio Palla",
                        "player": "PRETI ALESSANDRO",
                        "description": "Punto PRETI ALESSANDRO (B)",
                        "score": "12-18"
                    },
                    {
                        "match_time": 4250,
                        "type": "Punto e Cambio Palla",
                        "player": "ALFIERI MANUEL",
                        "description": "Punto ALFIERI MANUEL (A)",
                        "score": "13-20"
                    },
                    {
                        "match_time": 4400,
                        "type": "Punto e Cambio Palla",
                        "player": "MUSSA FABRIZIO",
                        "description": "Punto MUSSA FABRIZIO (B)",
                        "score": "13-21"
                    },
                    {
                        "match_time": 4400,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team B"
                    },
                    {
                        "match_time": 4650,
                        "type": "Punto e Cambio Palla",
                        "player": "RANGHIERI ALEX",
                        "description": "Punto RANGHIERI ALEX (A)",
                        "score": "1-1"
                    },
                    {
                        "match_time": 5400,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 5650,
                        "type": "Punto e Cambio Palla",
                        "player": "PRETI ALESSANDRO",
                        "description": "Punto PRETI ALESSANDRO (B)",
                        "score": "8-2"
                    },
                    {
                        "match_time": 5900,
                        "type": "Punto e Cambio Palla",
                        "player": "ALFIERI MANUEL",
                        "description": "Punto ALFIERI MANUEL (A)",
                        "score": "9-3"
                    },
                    {
                        "match_time": 6100,
                        "type": "Punto e Cambio Palla",
                        "player": "MUSSA FABRIZIO",
                        "description": "Punto MUSSA FABRIZIO (B)",
                        "score": "10-4"
                    },
                    {
                        "match_time": 6100,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 6200,
                        "type": "Punto e Cambio Palla",
                        "player": "RANGHIERI ALEX",
                        "description": "Punto RANGHIERI ALEX (A)",
                        "score": "11-4"
                    },
                    {
                        "match_time": 6850,
                        "type": "Punto e Cambio Palla",
                        "player": "PRETI ALESSANDRO",
                        "description": "Punto PRETI ALESSANDRO (B)",
                        "score": "15-5"
                    },
                    {
                        "match_time": 7050,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 7050,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 7250,
                        "type": "Punto e Cambio Palla",
                        "player": "ALFIERI MANUEL",
                        "description": "Punto ALFIERI MANUEL (A)",
                        "score": "16-7"
                    },
                    {
                        "match_time": 7550,
                        "type": "Punto e Cambio Palla",
                        "player": "MUSSA FABRIZIO",
                        "description": "Punto MUSSA FABRIZIO (B)",
                        "score": "17-8"
                    },
                    {
                        "match_time": 7850,
                        "type": "Punto e Cambio Palla",
                        "player": "RANGHIERI ALEX",
                        "description": "Punto RANGHIERI ALEX (A)",
                        "score": "18-9"
                    },
                    {
                        "match_time": 8000,
                        "type": "Punto e Cambio Palla",
                        "player": "PRETI ALESSANDRO",
                        "description": "Punto PRETI ALESSANDRO (B)",
                        "score": "18-10"
                    },
                    {
                        "match_time": 8000,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 8800,
                        "type": "Punto e Cambio Palla",
                        "player": "ALFIERI MANUEL",
                        "description": "Punto ALFIERI MANUEL (A)",
                        "score": "19-15"
                    },
                    {
                        "match_time": 8950,
                        "type": "Punto e Cambio Palla",
                        "player": "MUSSA FABRIZIO",
                        "description": "Punto MUSSA FABRIZIO (B)",
                        "score": "19-16"
                    },
                    {
                        "match_time": 8950,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 9200,
                        "type": "Punto e Cambio Palla",
                        "player": "RANGHIERI ALEX",
                        "description": "Punto RANGHIERI ALEX (A)",
                        "score": "20-17"
                    },
                    {
                        "match_time": 9300,
                        "type": "Punto e Cambio Palla",
                        "player": "PRETI ALESSANDRO",
                        "description": "Punto PRETI ALESSANDRO (B)",
                        "score": "20-18"
                    },
                    {
                        "match_time": 9400,
                        "type": "Punto e Cambio Palla",
                        "player": "ALFIERI MANUEL",
                        "description": "Punto ALFIERI MANUEL (A)",
                        "score": "21-18"
                    },
                    {
                        "match_time": 9400,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team A"
                    },
                    {
                        "match_time": 9950,
                        "type": "Punto e Cambio Palla",
                        "player": "MUSSA FABRIZIO",
                        "description": "Punto MUSSA FABRIZIO (B)",
                        "score": "3-1"
                    },
                    {
                        "match_time": 10100,
                        "type": "Punto e Cambio Palla",
                        "player": "RANGHIERI ALEX",
                        "description": "Punto RANGHIERI ALEX (A)",
                        "score": "4-1"
                    },
                    {
                        "match_time": 10200,
                        "type": "Punto e Cambio Palla",
                        "player": "PRETI ALESSANDRO",
                        "description": "Punto PRETI ALESSANDRO (B)",
                        "score": "4-2"
                    },
                    {
                        "match_time": 10300,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 10750,
                        "type": "Punto e Cambio Palla",
                        "player": "ALFIERI MANUEL",
                        "description": "Punto ALFIERI MANUEL (A)",
                        "score": "5-5"
                    },
                    {
                        "match_time": 10900,
                        "type": "Punto e Cambio Palla",
                        "player": "MUSSA FABRIZIO",
                        "description": "Punto MUSSA FABRIZIO (B)",
                        "score": "5-6"
                    },
                    {
                        "match_time": 11100,
                        "type": "Punto e Cambio Palla",
                        "player": "RANGHIERI ALEX",
                        "description": "Punto RANGHIERI ALEX (A)",
                        "score": "6-7"
                    },
                    {
                        "match_time": 11300,
                        "type": "Punto e Cambio Palla",
                        "player": "PRETI ALESSANDRO",
                        "description": "Punto PRETI ALESSANDRO (B)",
                        "score": "6-8"
                    },
                    {
                        "match_time": 11300,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 11850,
                        "type": "Punto e Cambio Palla",
                        "player": "ALFIERI MANUEL",
                        "description": "Punto ALFIERI MANUEL (A)",
                        "score": "7-11"
                    },
                    {
                        "match_time": 12200,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 12200,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 12550,
                        "type": "Punto e Cambio Palla",
                        "player": "MUSSA FABRIZIO",
                        "description": "Punto MUSSA FABRIZIO (B)",
                        "score": "11-12"
                    },
                    {
                        "match_time": 12700,
                        "type": "Punto e Cambio Palla",
                        "player": "RANGHIERI ALEX",
                        "description": "Punto RANGHIERI ALEX (A)",
                        "score": "12-12"
                    },
                    {
                        "match_time": 13050,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team A"
                    },
                    {
                        "match_time": 13050,
                        "type": "Fine Match",
                        "player": "Arbitro",
                        "description": "Partita Terminata"
                    }
                ],
                "match_time": 13050,
                "status": "finished",
                "server_team": 0,
                "server_index": [
                    1,
                    1
                ],
                "final_type": None
            },
            {
                "id": 2,
                "teamA": "SPADONI GIACOMO - LUISETTO MICHELE",
                "teamB": "LUPO DANIELE - BORRACCINO DAVIDE",
                "playersA": [
                    "SPADONI GIACOMO",
                    "LUISETTO MICHELE"
                ],
                "playersB": [
                    "LUPO DANIELE",
                    "BORRACCINO DAVIDE"
                ],
                "score_sets": [
                    2,
                    1
                ],
                "current_set": 3,
                "points": [
                    0,
                    0
                ],
                "sets_history": [
                    [
                        16,
                        21
                    ],
                    [
                        21,
                        19
                    ],
                    [
                        15,
                        11
                    ]
                ],
                "events": [
                    {
                        "match_time": 400,
                        "type": "Punto e Cambio Palla",
                        "player": "BORRACCINO DAVIDE",
                        "description": "Punto BORRACCINO DAVIDE (B)",
                        "score": "2-1"
                    },
                    {
                        "match_time": 550,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (A)",
                        "score": "3-1"
                    },
                    {
                        "match_time": 650,
                        "type": "Punto e Cambio Palla",
                        "player": "LUPO DANIELE",
                        "description": "Punto LUPO DANIELE (B)",
                        "score": "3-2"
                    },
                    {
                        "match_time": 900,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 1800,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (A)",
                        "score": "4-9"
                    },
                    {
                        "match_time": 1950,
                        "type": "Punto e Cambio Palla",
                        "player": "BORRACCINO DAVIDE",
                        "description": "Punto BORRACCINO DAVIDE (B)",
                        "score": "4-10"
                    },
                    {
                        "match_time": 1950,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 2250,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (A)",
                        "score": "5-11"
                    },
                    {
                        "match_time": 2550,
                        "type": "Punto e Cambio Palla",
                        "player": "LUPO DANIELE",
                        "description": "Punto LUPO DANIELE (B)",
                        "score": "6-12"
                    },
                    {
                        "match_time": 2850,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (A)",
                        "score": "7-13"
                    },
                    {
                        "match_time": 3050,
                        "type": "Punto e Cambio Palla",
                        "player": "BORRACCINO DAVIDE",
                        "description": "Punto BORRACCINO DAVIDE (B)",
                        "score": "7-14"
                    },
                    {
                        "match_time": 3050,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 3050,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 3150,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (A)",
                        "score": "8-14"
                    },
                    {
                        "match_time": 3450,
                        "type": "Punto e Cambio Palla",
                        "player": "LUPO DANIELE",
                        "description": "Punto LUPO DANIELE (B)",
                        "score": "9-15"
                    },
                    {
                        "match_time": 3650,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (A)",
                        "score": "10-15"
                    },
                    {
                        "match_time": 4050,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 4350,
                        "type": "Punto e Cambio Palla",
                        "player": "BORRACCINO DAVIDE",
                        "description": "Punto BORRACCINO DAVIDE (B)",
                        "score": "14-16"
                    },
                    {
                        "match_time": 5100,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (A)",
                        "score": "15-20"
                    },
                    {
                        "match_time": 5100,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 5400,
                        "type": "Punto e Cambio Palla",
                        "player": "LUPO DANIELE",
                        "description": "Punto LUPO DANIELE (B)",
                        "score": "16-21"
                    },
                    {
                        "match_time": 5400,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team B"
                    },
                    {
                        "match_time": 5550,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (A)",
                        "score": "1-0"
                    },
                    {
                        "match_time": 5950,
                        "type": "Punto e Cambio Palla",
                        "player": "BORRACCINO DAVIDE",
                        "description": "Punto BORRACCINO DAVIDE (B)",
                        "score": "4-1"
                    },
                    {
                        "match_time": 6300,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 6800,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (A)",
                        "score": "5-5"
                    },
                    {
                        "match_time": 6900,
                        "type": "Punto e Cambio Palla",
                        "player": "LUPO DANIELE",
                        "description": "Punto LUPO DANIELE (B)",
                        "score": "5-6"
                    },
                    {
                        "match_time": 7150,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (A)",
                        "score": "6-7"
                    },
                    {
                        "match_time": 7250,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 7350,
                        "type": "Punto e Cambio Palla",
                        "player": "BORRACCINO DAVIDE",
                        "description": "Punto BORRACCINO DAVIDE (B)",
                        "score": "7-8"
                    },
                    {
                        "match_time": 7500,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (A)",
                        "score": "8-8"
                    },
                    {
                        "match_time": 7750,
                        "type": "Punto e Cambio Palla",
                        "player": "LUPO DANIELE",
                        "description": "Punto LUPO DANIELE (B)",
                        "score": "9-9"
                    },
                    {
                        "match_time": 7850,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (A)",
                        "score": "10-9"
                    },
                    {
                        "match_time": 8100,
                        "type": "Punto e Cambio Palla",
                        "player": "BORRACCINO DAVIDE",
                        "description": "Punto BORRACCINO DAVIDE (B)",
                        "score": "11-10"
                    },
                    {
                        "match_time": 8100,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 8100,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 8200,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (A)",
                        "score": "12-10"
                    },
                    {
                        "match_time": 8750,
                        "type": "Punto e Cambio Palla",
                        "player": "LUPO DANIELE",
                        "description": "Punto LUPO DANIELE (B)",
                        "score": "15-11"
                    },
                    {
                        "match_time": 9000,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 9200,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (A)",
                        "score": "16-14"
                    },
                    {
                        "match_time": 9500,
                        "type": "Punto e Cambio Palla",
                        "player": "BORRACCINO DAVIDE",
                        "description": "Punto BORRACCINO DAVIDE (B)",
                        "score": "18-15"
                    },
                    {
                        "match_time": 9700,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (A)",
                        "score": "19-15"
                    },
                    {
                        "match_time": 9850,
                        "type": "Punto e Cambio Palla",
                        "player": "LUPO DANIELE",
                        "description": "Punto LUPO DANIELE (B)",
                        "score": "19-16"
                    },
                    {
                        "match_time": 9850,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 10350,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (A)",
                        "score": "20-19"
                    },
                    {
                        "match_time": 10500,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team A"
                    },
                    {
                        "match_time": 10700,
                        "type": "Punto e Cambio Palla",
                        "player": "BORRACCINO DAVIDE",
                        "description": "Punto BORRACCINO DAVIDE (B)",
                        "score": "1-1"
                    },
                    {
                        "match_time": 10800,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (A)",
                        "score": "2-1"
                    },
                    {
                        "match_time": 11350,
                        "type": "Punto e Cambio Palla",
                        "player": "LUPO DANIELE",
                        "description": "Punto LUPO DANIELE (B)",
                        "score": "5-2"
                    },
                    {
                        "match_time": 11350,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 11600,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (A)",
                        "score": "6-3"
                    },
                    {
                        "match_time": 11900,
                        "type": "Punto e Cambio Palla",
                        "player": "BORRACCINO DAVIDE",
                        "description": "Punto BORRACCINO DAVIDE (B)",
                        "score": "7-4"
                    },
                    {
                        "match_time": 12300,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 12400,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (A)",
                        "score": "8-7"
                    },
                    {
                        "match_time": 12750,
                        "type": "Punto e Cambio Palla",
                        "player": "LUPO DANIELE",
                        "description": "Punto LUPO DANIELE (B)",
                        "score": "9-8"
                    },
                    {
                        "match_time": 12900,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (A)",
                        "score": "10-8"
                    },
                    {
                        "match_time": 13200,
                        "type": "Punto e Cambio Palla",
                        "player": "BORRACCINO DAVIDE",
                        "description": "Punto BORRACCINO DAVIDE (B)",
                        "score": "12-9"
                    },
                    {
                        "match_time": 13200,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 13200,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 13400,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (A)",
                        "score": "13-9"
                    },
                    {
                        "match_time": 13500,
                        "type": "Punto e Cambio Palla",
                        "player": "LUPO DANIELE",
                        "description": "Punto LUPO DANIELE (B)",
                        "score": "13-10"
                    },
                    {
                        "match_time": 13600,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (A)",
                        "score": "14-10"
                    },
                    {
                        "match_time": 13650,
                        "type": "Punto e Cambio Palla",
                        "player": "BORRACCINO DAVIDE",
                        "description": "Punto BORRACCINO DAVIDE (B)",
                        "score": "14-11"
                    },
                    {
                        "match_time": 13800,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (A)",
                        "score": "15-11"
                    },
                    {
                        "match_time": 13800,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team A"
                    },
                    {
                        "match_time": 13800,
                        "type": "Fine Match",
                        "player": "Arbitro",
                        "description": "Partita Terminata"
                    }
                ],
                "match_time": 13800,
                "status": "finished",
                "server_team": 0,
                "server_index": [
                    1,
                    1
                ],
                "final_type": None
            },
            {
                "id": 6,
                "teamA": "SACRIPANTI MAURO - TITTA GIACOMO",
                "teamB": "KRUMINS DAVIS - CAMINATI MARCO",
                "playersA": [
                    "SACRIPANTI MAURO",
                    "TITTA GIACOMO"
                ],
                "playersB": [
                    "KRUMINS DAVIS",
                    "CAMINATI MARCO"
                ],
                "score_sets": [
                    2,
                    1
                ],
                "current_set": 3,
                "points": [
                    0,
                    0
                ],
                "sets_history": [
                    [
                        21,
                        13
                    ],
                    [
                        13,
                        21
                    ],
                    [
                        20,
                        18
                    ]
                ],
                "events": [
                    {
                        "match_time": 150,
                        "type": "Punto e Cambio Palla",
                        "player": "CAMINATI MARCO",
                        "description": "Punto CAMINATI MARCO (B)",
                        "score": "0-1"
                    },
                    {
                        "match_time": 300,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (A)",
                        "score": "1-1"
                    },
                    {
                        "match_time": 450,
                        "type": "Punto e Cambio Palla",
                        "player": "KRUMINS DAVIS",
                        "description": "Punto KRUMINS DAVIS (B)",
                        "score": "1-2"
                    },
                    {
                        "match_time": 600,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (A)",
                        "score": "2-2"
                    },
                    {
                        "match_time": 1000,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 1700,
                        "type": "Punto e Cambio Palla",
                        "player": "CAMINATI MARCO",
                        "description": "Punto CAMINATI MARCO (B)",
                        "score": "9-3"
                    },
                    {
                        "match_time": 1800,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (A)",
                        "score": "10-3"
                    },
                    {
                        "match_time": 1900,
                        "type": "Punto e Cambio Palla",
                        "player": "KRUMINS DAVIS",
                        "description": "Punto KRUMINS DAVIS (B)",
                        "score": "10-4"
                    },
                    {
                        "match_time": 1900,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 2350,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (A)",
                        "score": "11-6"
                    },
                    {
                        "match_time": 2600,
                        "type": "Punto e Cambio Palla",
                        "player": "CAMINATI MARCO",
                        "description": "Punto CAMINATI MARCO (B)",
                        "score": "12-7"
                    },
                    {
                        "match_time": 2700,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (A)",
                        "score": "13-7"
                    },
                    {
                        "match_time": 2800,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 2800,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 3150,
                        "type": "Punto e Cambio Palla",
                        "player": "KRUMINS DAVIS",
                        "description": "Punto KRUMINS DAVIS (B)",
                        "score": "15-8"
                    },
                    {
                        "match_time": 3600,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (A)",
                        "score": "16-10"
                    },
                    {
                        "match_time": 3850,
                        "type": "Punto e Cambio Palla",
                        "player": "CAMINATI MARCO",
                        "description": "Punto CAMINATI MARCO (B)",
                        "score": "17-11"
                    },
                    {
                        "match_time": 3850,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 4200,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (A)",
                        "score": "18-13"
                    },
                    {
                        "match_time": 4550,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team A"
                    },
                    {
                        "match_time": 4650,
                        "type": "Punto e Cambio Palla",
                        "player": "KRUMINS DAVIS",
                        "description": "Punto KRUMINS DAVIS (B)",
                        "score": "0-1"
                    },
                    {
                        "match_time": 5450,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 5550,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (A)",
                        "score": "1-7"
                    },
                    {
                        "match_time": 5700,
                        "type": "Punto e Cambio Palla",
                        "player": "CAMINATI MARCO",
                        "description": "Punto CAMINATI MARCO (B)",
                        "score": "1-8"
                    },
                    {
                        "match_time": 5950,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (A)",
                        "score": "2-9"
                    },
                    {
                        "match_time": 6100,
                        "type": "Punto e Cambio Palla",
                        "player": "KRUMINS DAVIS",
                        "description": "Punto KRUMINS DAVIS (B)",
                        "score": "2-10"
                    },
                    {
                        "match_time": 6150,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (A)",
                        "score": "3-10"
                    },
                    {
                        "match_time": 6350,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 6600,
                        "type": "Punto e Cambio Palla",
                        "player": "CAMINATI MARCO",
                        "description": "Punto CAMINATI MARCO (B)",
                        "score": "5-11"
                    },
                    {
                        "match_time": 7050,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (A)",
                        "score": "6-13"
                    },
                    {
                        "match_time": 7250,
                        "type": "Punto e Cambio Palla",
                        "player": "KRUMINS DAVIS",
                        "description": "Punto KRUMINS DAVIS (B)",
                        "score": "6-14"
                    },
                    {
                        "match_time": 7350,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (A)",
                        "score": "7-14"
                    },
                    {
                        "match_time": 7350,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 7350,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 7700,
                        "type": "Punto e Cambio Palla",
                        "player": "CAMINATI MARCO",
                        "description": "Punto CAMINATI MARCO (B)",
                        "score": "9-15"
                    },
                    {
                        "match_time": 7850,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (A)",
                        "score": "10-15"
                    },
                    {
                        "match_time": 8000,
                        "type": "Punto e Cambio Palla",
                        "player": "KRUMINS DAVIS",
                        "description": "Punto KRUMINS DAVIS (B)",
                        "score": "10-16"
                    },
                    {
                        "match_time": 8250,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 8350,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (A)",
                        "score": "11-18"
                    },
                    {
                        "match_time": 8450,
                        "type": "Punto e Cambio Palla",
                        "player": "CAMINATI MARCO",
                        "description": "Punto CAMINATI MARCO (B)",
                        "score": "11-19"
                    },
                    {
                        "match_time": 8800,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (A)",
                        "score": "12-20"
                    },
                    {
                        "match_time": 9100,
                        "type": "Punto e Cambio Palla",
                        "player": "KRUMINS DAVIS",
                        "description": "Punto KRUMINS DAVIS (B)",
                        "score": "13-21"
                    },
                    {
                        "match_time": 9100,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team B"
                    },
                    {
                        "match_time": 9200,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (A)",
                        "score": "1-0"
                    },
                    {
                        "match_time": 9450,
                        "type": "Punto e Cambio Palla",
                        "player": "CAMINATI MARCO",
                        "description": "Punto CAMINATI MARCO (B)",
                        "score": "2-1"
                    },
                    {
                        "match_time": 9600,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (A)",
                        "score": "3-1"
                    },
                    {
                        "match_time": 10000,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 10100,
                        "type": "Punto e Cambio Palla",
                        "player": "KRUMINS DAVIS",
                        "description": "Punto KRUMINS DAVIS (B)",
                        "score": "6-2"
                    },
                    {
                        "match_time": 10250,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (A)",
                        "score": "7-2"
                    },
                    {
                        "match_time": 10700,
                        "type": "Punto e Cambio Palla",
                        "player": "CAMINATI MARCO",
                        "description": "Punto CAMINATI MARCO (B)",
                        "score": "10-3"
                    },
                    {
                        "match_time": 10900,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 11950,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (A)",
                        "score": "11-10"
                    },
                    {
                        "match_time": 11950,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 11950,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 12150,
                        "type": "Punto e Cambio Palla",
                        "player": "KRUMINS DAVIS",
                        "description": "Punto KRUMINS DAVIS (B)",
                        "score": "11-11"
                    },
                    {
                        "match_time": 12500,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (A)",
                        "score": "12-13"
                    },
                    {
                        "match_time": 12650,
                        "type": "Punto e Cambio Palla",
                        "player": "CAMINATI MARCO",
                        "description": "Punto CAMINATI MARCO (B)",
                        "score": "12-14"
                    },
                    {
                        "match_time": 12700,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (A)",
                        "score": "13-14"
                    },
                    {
                        "match_time": 12850,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 13050,
                        "type": "Punto e Cambio Palla",
                        "player": "KRUMINS DAVIS",
                        "description": "Punto KRUMINS DAVIS (B)",
                        "score": "14-15"
                    },
                    {
                        "match_time": 13200,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (A)",
                        "score": "15-15"
                    },
                    {
                        "match_time": 13400,
                        "type": "Punto e Cambio Palla",
                        "player": "CAMINATI MARCO",
                        "description": "Punto CAMINATI MARCO (B)",
                        "score": "15-16"
                    },
                    {
                        "match_time": 13600,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (A)",
                        "score": "16-16"
                    },
                    {
                        "match_time": 13850,
                        "type": "Punto e Cambio Palla",
                        "player": "KRUMINS DAVIS",
                        "description": "Punto KRUMINS DAVIS (B)",
                        "score": "17-17"
                    },
                    {
                        "match_time": 14000,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (A)",
                        "score": "18-17"
                    },
                    {
                        "match_time": 14000,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 14100,
                        "type": "Punto e Cambio Palla",
                        "player": "CAMINATI MARCO",
                        "description": "Punto CAMINATI MARCO (B)",
                        "score": "18-18"
                    },
                    {
                        "match_time": 14200,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (A)",
                        "score": "19-18"
                    },
                    {
                        "match_time": 14350,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team A"
                    },
                    {
                        "match_time": 14350,
                        "type": "Fine Match",
                        "player": "Arbitro",
                        "description": "Partita Terminata"
                    }
                ],
                "match_time": 14350,
                "status": "finished",
                "server_team": 0,
                "server_index": [
                    1,
                    1
                ],
                "final_type": None
            },
            {
                "id": 8,
                "teamA": "BONIFAZI CARLO - ACERBI RAOUL",
                "teamB": "CECCOLI EDGARDO - CARUCCI ALESSANDRO",
                "playersA": [
                    "BONIFAZI CARLO",
                    "ACERBI RAOUL"
                ],
                "playersB": [
                    "CECCOLI EDGARDO",
                    "CARUCCI ALESSANDRO"
                ],
                "score_sets": [
                    2,
                    1
                ],
                "current_set": 3,
                "points": [
                    0,
                    0
                ],
                "sets_history": [
                    [
                        21,
                        18
                    ],
                    [
                        19,
                        21
                    ],
                    [
                        15,
                        12
                    ]
                ],
                "events": [
                    {
                        "match_time": 250,
                        "type": "Punto e Cambio Palla",
                        "player": "CARUCCI ALESSANDRO",
                        "description": "Punto CARUCCI ALESSANDRO (B)",
                        "score": "1-1"
                    },
                    {
                        "match_time": 550,
                        "type": "Punto e Cambio Palla",
                        "player": "ACERBI RAOUL",
                        "description": "Punto ACERBI RAOUL (A)",
                        "score": "2-2"
                    },
                    {
                        "match_time": 650,
                        "type": "Punto e Cambio Palla",
                        "player": "CECCOLI EDGARDO",
                        "description": "Punto CECCOLI EDGARDO (B)",
                        "score": "2-3"
                    },
                    {
                        "match_time": 800,
                        "type": "Punto e Cambio Palla",
                        "player": "BONIFAZI CARLO",
                        "description": "Punto BONIFAZI CARLO (A)",
                        "score": "3-3"
                    },
                    {
                        "match_time": 900,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 1100,
                        "type": "Punto e Cambio Palla",
                        "player": "CARUCCI ALESSANDRO",
                        "description": "Punto CARUCCI ALESSANDRO (B)",
                        "score": "4-4"
                    },
                    {
                        "match_time": 1250,
                        "type": "Punto e Cambio Palla",
                        "player": "ACERBI RAOUL",
                        "description": "Punto ACERBI RAOUL (A)",
                        "score": "5-4"
                    },
                    {
                        "match_time": 1450,
                        "type": "Punto e Cambio Palla",
                        "player": "CECCOLI EDGARDO",
                        "description": "Punto CECCOLI EDGARDO (B)",
                        "score": "5-5"
                    },
                    {
                        "match_time": 1650,
                        "type": "Punto e Cambio Palla",
                        "player": "BONIFAZI CARLO",
                        "description": "Punto BONIFAZI CARLO (A)",
                        "score": "6-5"
                    },
                    {
                        "match_time": 1850,
                        "type": "Punto e Cambio Palla",
                        "player": "CARUCCI ALESSANDRO",
                        "description": "Punto CARUCCI ALESSANDRO (B)",
                        "score": "6-6"
                    },
                    {
                        "match_time": 2100,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 2200,
                        "type": "Punto e Cambio Palla",
                        "player": "ACERBI RAOUL",
                        "description": "Punto ACERBI RAOUL (A)",
                        "score": "7-8"
                    },
                    {
                        "match_time": 2800,
                        "type": "Punto e Cambio Palla",
                        "player": "CECCOLI EDGARDO",
                        "description": "Punto CECCOLI EDGARDO (B)",
                        "score": "10-9"
                    },
                    {
                        "match_time": 3100,
                        "type": "Punto e Cambio Palla",
                        "player": "BONIFAZI CARLO",
                        "description": "Punto BONIFAZI CARLO (A)",
                        "score": "11-10"
                    },
                    {
                        "match_time": 3100,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 3100,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 3300,
                        "type": "Punto e Cambio Palla",
                        "player": "CARUCCI ALESSANDRO",
                        "description": "Punto CARUCCI ALESSANDRO (B)",
                        "score": "11-11"
                    },
                    {
                        "match_time": 3550,
                        "type": "Punto e Cambio Palla",
                        "player": "ACERBI RAOUL",
                        "description": "Punto ACERBI RAOUL (A)",
                        "score": "12-12"
                    },
                    {
                        "match_time": 3750,
                        "type": "Punto e Cambio Palla",
                        "player": "CECCOLI EDGARDO",
                        "description": "Punto CECCOLI EDGARDO (B)",
                        "score": "12-13"
                    },
                    {
                        "match_time": 3800,
                        "type": "Punto e Cambio Palla",
                        "player": "BONIFAZI CARLO",
                        "description": "Punto BONIFAZI CARLO (A)",
                        "score": "13-13"
                    },
                    {
                        "match_time": 4000,
                        "type": "Punto e Cambio Palla",
                        "player": "CARUCCI ALESSANDRO",
                        "description": "Punto CARUCCI ALESSANDRO (B)",
                        "score": "13-14"
                    },
                    {
                        "match_time": 4150,
                        "type": "Punto e Cambio Palla",
                        "player": "ACERBI RAOUL",
                        "description": "Punto ACERBI RAOUL (A)",
                        "score": "14-14"
                    },
                    {
                        "match_time": 4150,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 4950,
                        "type": "Punto e Cambio Palla",
                        "player": "CECCOLI EDGARDO",
                        "description": "Punto CECCOLI EDGARDO (B)",
                        "score": "18-15"
                    },
                    {
                        "match_time": 5100,
                        "type": "Punto e Cambio Palla",
                        "player": "BONIFAZI CARLO",
                        "description": "Punto BONIFAZI CARLO (A)",
                        "score": "19-15"
                    },
                    {
                        "match_time": 5250,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 5400,
                        "type": "Punto e Cambio Palla",
                        "player": "CARUCCI ALESSANDRO",
                        "description": "Punto CARUCCI ALESSANDRO (B)",
                        "score": "20-16"
                    },
                    {
                        "match_time": 5900,
                        "type": "Punto e Cambio Palla",
                        "player": "ACERBI RAOUL",
                        "description": "Punto ACERBI RAOUL (A)",
                        "score": "21-18"
                    },
                    {
                        "match_time": 5900,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team A"
                    },
                    {
                        "match_time": 6700,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 6900,
                        "type": "Punto e Cambio Palla",
                        "player": "CECCOLI EDGARDO",
                        "description": "Punto CECCOLI EDGARDO (B)",
                        "score": "8-1"
                    },
                    {
                        "match_time": 7000,
                        "type": "Punto e Cambio Palla",
                        "player": "BONIFAZI CARLO",
                        "description": "Punto BONIFAZI CARLO (A)",
                        "score": "9-1"
                    },
                    {
                        "match_time": 7450,
                        "type": "Punto e Cambio Palla",
                        "player": "CARUCCI ALESSANDRO",
                        "description": "Punto CARUCCI ALESSANDRO (B)",
                        "score": "11-2"
                    },
                    {
                        "match_time": 7600,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 7850,
                        "type": "Punto e Cambio Palla",
                        "player": "ACERBI RAOUL",
                        "description": "Punto ACERBI RAOUL (A)",
                        "score": "12-4"
                    },
                    {
                        "match_time": 8000,
                        "type": "Punto e Cambio Palla",
                        "player": "CECCOLI EDGARDO",
                        "description": "Punto CECCOLI EDGARDO (B)",
                        "score": "12-5"
                    },
                    {
                        "match_time": 8200,
                        "type": "Punto e Cambio Palla",
                        "player": "BONIFAZI CARLO",
                        "description": "Punto BONIFAZI CARLO (A)",
                        "score": "13-6"
                    },
                    {
                        "match_time": 8400,
                        "type": "Punto e Cambio Palla",
                        "player": "CARUCCI ALESSANDRO",
                        "description": "Punto CARUCCI ALESSANDRO (B)",
                        "score": "13-7"
                    },
                    {
                        "match_time": 8600,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 8600,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 8900,
                        "type": "Punto e Cambio Palla",
                        "player": "ACERBI RAOUL",
                        "description": "Punto ACERBI RAOUL (A)",
                        "score": "14-9"
                    },
                    {
                        "match_time": 9200,
                        "type": "Punto e Cambio Palla",
                        "player": "CECCOLI EDGARDO",
                        "description": "Punto CECCOLI EDGARDO (B)",
                        "score": "15-10"
                    },
                    {
                        "match_time": 9500,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 10000,
                        "type": "Punto e Cambio Palla",
                        "player": "BONIFAZI CARLO",
                        "description": "Punto BONIFAZI CARLO (A)",
                        "score": "16-15"
                    },
                    {
                        "match_time": 10150,
                        "type": "Punto e Cambio Palla",
                        "player": "CARUCCI ALESSANDRO",
                        "description": "Punto CARUCCI ALESSANDRO (B)",
                        "score": "16-16"
                    },
                    {
                        "match_time": 10200,
                        "type": "Punto e Cambio Palla",
                        "player": "ACERBI RAOUL",
                        "description": "Punto ACERBI RAOUL (A)",
                        "score": "17-16"
                    },
                    {
                        "match_time": 10400,
                        "type": "Punto e Cambio Palla",
                        "player": "CECCOLI EDGARDO",
                        "description": "Punto CECCOLI EDGARDO (B)",
                        "score": "17-17"
                    },
                    {
                        "match_time": 10550,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 10700,
                        "type": "Punto e Cambio Palla",
                        "player": "BONIFAZI CARLO",
                        "description": "Punto BONIFAZI CARLO (A)",
                        "score": "18-18"
                    },
                    {
                        "match_time": 10900,
                        "type": "Punto e Cambio Palla",
                        "player": "CARUCCI ALESSANDRO",
                        "description": "Punto CARUCCI ALESSANDRO (B)",
                        "score": "18-19"
                    },
                    {
                        "match_time": 11100,
                        "type": "Punto e Cambio Palla",
                        "player": "ACERBI RAOUL",
                        "description": "Punto ACERBI RAOUL (A)",
                        "score": "19-19"
                    },
                    {
                        "match_time": 11300,
                        "type": "Punto e Cambio Palla",
                        "player": "CECCOLI EDGARDO",
                        "description": "Punto CECCOLI EDGARDO (B)",
                        "score": "19-20"
                    },
                    {
                        "match_time": 11400,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team B"
                    },
                    {
                        "match_time": 11500,
                        "type": "Punto e Cambio Palla",
                        "player": "BONIFAZI CARLO",
                        "description": "Punto BONIFAZI CARLO (A)",
                        "score": "1-0"
                    },
                    {
                        "match_time": 12100,
                        "type": "Punto e Cambio Palla",
                        "player": "CARUCCI ALESSANDRO",
                        "description": "Punto CARUCCI ALESSANDRO (B)",
                        "score": "4-1"
                    },
                    {
                        "match_time": 12350,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 12600,
                        "type": "Punto e Cambio Palla",
                        "player": "ACERBI RAOUL",
                        "description": "Punto ACERBI RAOUL (A)",
                        "score": "5-4"
                    },
                    {
                        "match_time": 13000,
                        "type": "Punto e Cambio Palla",
                        "player": "CECCOLI EDGARDO",
                        "description": "Punto CECCOLI EDGARDO (B)",
                        "score": "7-5"
                    },
                    {
                        "match_time": 13150,
                        "type": "Punto e Cambio Palla",
                        "player": "BONIFAZI CARLO",
                        "description": "Punto BONIFAZI CARLO (A)",
                        "score": "8-5"
                    },
                    {
                        "match_time": 13350,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 13800,
                        "type": "Punto e Cambio Palla",
                        "player": "CARUCCI ALESSANDRO",
                        "description": "Punto CARUCCI ALESSANDRO (B)",
                        "score": "12-6"
                    },
                    {
                        "match_time": 14250,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 14250,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 14650,
                        "type": "Punto e Cambio Palla",
                        "player": "ACERBI RAOUL",
                        "description": "Punto ACERBI RAOUL (A)",
                        "score": "13-11"
                    },
                    {
                        "match_time": 14850,
                        "type": "Punto e Cambio Palla",
                        "player": "CECCOLI EDGARDO",
                        "description": "Punto CECCOLI EDGARDO (B)",
                        "score": "14-12"
                    },
                    {
                        "match_time": 15000,
                        "type": "Punto e Cambio Palla",
                        "player": "BONIFAZI CARLO",
                        "description": "Punto BONIFAZI CARLO (A)",
                        "score": "15-12"
                    },
                    {
                        "match_time": 15000,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team A"
                    },
                    {
                        "match_time": 15000,
                        "type": "Fine Match",
                        "player": "Arbitro",
                        "description": "Partita Terminata"
                    }
                ],
                "match_time": 15000,
                "status": "finished",
                "server_team": 0,
                "server_index": [
                    0,
                    0
                ],
                "final_type": None
            }
        ],
        "Quarti di Finale": [
            {
                "id": 4,
                "teamA": "VISCOVICH MARCO - ROSSI ENRICO",
                "teamB": "BONIFAZI CARLO - ACERBI RAOUL",
                "playersA": [
                    "VISCOVICH MARCO",
                    "ROSSI ENRICO"
                ],
                "playersB": [
                    "BONIFAZI CARLO",
                    "ACERBI RAOUL"
                ],
                "score_sets": [
                    2,
                    0
                ],
                "current_set": 2,
                "points": [
                    0,
                    0
                ],
                "sets_history": [
                    [
                        21,
                        11
                    ],
                    [
                        21,
                        19
                    ]
                ],
                "events": [
                    {
                        "match_time": 100,
                        "type": "Punto e Cambio Palla",
                        "player": "ACERBI RAOUL",
                        "description": "Punto ACERBI RAOUL (B)",
                        "score": "0-1"
                    },
                    {
                        "match_time": 200,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (A)",
                        "score": "1-1"
                    },
                    {
                        "match_time": 450,
                        "type": "Punto e Cambio Palla",
                        "player": "BONIFAZI CARLO",
                        "description": "Punto BONIFAZI CARLO (B)",
                        "score": "2-2"
                    },
                    {
                        "match_time": 550,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (A)",
                        "score": "3-2"
                    },
                    {
                        "match_time": 700,
                        "type": "Punto e Cambio Palla",
                        "player": "ACERBI RAOUL",
                        "description": "Punto ACERBI RAOUL (B)",
                        "score": "3-3"
                    },
                    {
                        "match_time": 850,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (A)",
                        "score": "4-3"
                    },
                    {
                        "match_time": 850,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 1350,
                        "type": "Punto e Cambio Palla",
                        "player": "BONIFAZI CARLO",
                        "description": "Punto BONIFAZI CARLO (B)",
                        "score": "7-4"
                    },
                    {
                        "match_time": 1500,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (A)",
                        "score": "8-4"
                    },
                    {
                        "match_time": 1850,
                        "type": "Punto e Cambio Palla",
                        "player": "ACERBI RAOUL",
                        "description": "Punto ACERBI RAOUL (B)",
                        "score": "9-5"
                    },
                    {
                        "match_time": 1850,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 1950,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (A)",
                        "score": "10-5"
                    },
                    {
                        "match_time": 2400,
                        "type": "Punto e Cambio Palla",
                        "player": "BONIFAZI CARLO",
                        "description": "Punto BONIFAZI CARLO (B)",
                        "score": "13-6"
                    },
                    {
                        "match_time": 2600,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (A)",
                        "score": "14-7"
                    },
                    {
                        "match_time": 2600,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 2600,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 2850,
                        "type": "Punto e Cambio Palla",
                        "player": "ACERBI RAOUL",
                        "description": "Punto ACERBI RAOUL (B)",
                        "score": "15-8"
                    },
                    {
                        "match_time": 3100,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (A)",
                        "score": "16-9"
                    },
                    {
                        "match_time": 3250,
                        "type": "Punto e Cambio Palla",
                        "player": "BONIFAZI CARLO",
                        "description": "Punto BONIFAZI CARLO (B)",
                        "score": "16-10"
                    },
                    {
                        "match_time": 3350,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (A)",
                        "score": "17-10"
                    },
                    {
                        "match_time": 3550,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 3800,
                        "type": "Punto e Cambio Palla",
                        "player": "ACERBI RAOUL",
                        "description": "Punto ACERBI RAOUL (B)",
                        "score": "19-11"
                    },
                    {
                        "match_time": 3900,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (A)",
                        "score": "20-11"
                    },
                    {
                        "match_time": 3950,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team A"
                    },
                    {
                        "match_time": 4200,
                        "type": "Punto e Cambio Palla",
                        "player": "BONIFAZI CARLO",
                        "description": "Punto BONIFAZI CARLO (B)",
                        "score": "1-1"
                    },
                    {
                        "match_time": 4650,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (A)",
                        "score": "2-3"
                    },
                    {
                        "match_time": 4900,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 5100,
                        "type": "Punto e Cambio Palla",
                        "player": "ACERBI RAOUL",
                        "description": "Punto ACERBI RAOUL (B)",
                        "score": "4-4"
                    },
                    {
                        "match_time": 5200,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (A)",
                        "score": "5-4"
                    },
                    {
                        "match_time": 5400,
                        "type": "Punto e Cambio Palla",
                        "player": "BONIFAZI CARLO",
                        "description": "Punto BONIFAZI CARLO (B)",
                        "score": "5-5"
                    },
                    {
                        "match_time": 5900,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (A)",
                        "score": "6-7"
                    },
                    {
                        "match_time": 6000,
                        "type": "Punto e Cambio Palla",
                        "player": "ACERBI RAOUL",
                        "description": "Punto ACERBI RAOUL (B)",
                        "score": "6-8"
                    },
                    {
                        "match_time": 6000,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 6200,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (A)",
                        "score": "7-8"
                    },
                    {
                        "match_time": 6350,
                        "type": "Punto e Cambio Palla",
                        "player": "BONIFAZI CARLO",
                        "description": "Punto BONIFAZI CARLO (B)",
                        "score": "7-9"
                    },
                    {
                        "match_time": 6700,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (A)",
                        "score": "8-11"
                    },
                    {
                        "match_time": 7050,
                        "type": "Punto e Cambio Palla",
                        "player": "ACERBI RAOUL",
                        "description": "Punto ACERBI RAOUL (B)",
                        "score": "9-12"
                    },
                    {
                        "match_time": 7050,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 7050,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 7200,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (A)",
                        "score": "10-12"
                    },
                    {
                        "match_time": 7350,
                        "type": "Punto e Cambio Palla",
                        "player": "BONIFAZI CARLO",
                        "description": "Punto BONIFAZI CARLO (B)",
                        "score": "10-13"
                    },
                    {
                        "match_time": 7450,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (A)",
                        "score": "11-13"
                    },
                    {
                        "match_time": 7750,
                        "type": "Punto e Cambio Palla",
                        "player": "ACERBI RAOUL",
                        "description": "Punto ACERBI RAOUL (B)",
                        "score": "13-14"
                    },
                    {
                        "match_time": 7950,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 8000,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (A)",
                        "score": "14-15"
                    },
                    {
                        "match_time": 8450,
                        "type": "Punto e Cambio Palla",
                        "player": "BONIFAZI CARLO",
                        "description": "Punto BONIFAZI CARLO (B)",
                        "score": "16-16"
                    },
                    {
                        "match_time": 8650,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (A)",
                        "score": "17-16"
                    },
                    {
                        "match_time": 9000,
                        "type": "Punto e Cambio Palla",
                        "player": "ACERBI RAOUL",
                        "description": "Punto ACERBI RAOUL (B)",
                        "score": "18-17"
                    },
                    {
                        "match_time": 9000,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 9100,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (A)",
                        "score": "19-17"
                    },
                    {
                        "match_time": 9250,
                        "type": "Punto e Cambio Palla",
                        "player": "BONIFAZI CARLO",
                        "description": "Punto BONIFAZI CARLO (B)",
                        "score": "19-18"
                    },
                    {
                        "match_time": 9300,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (A)",
                        "score": "20-18"
                    },
                    {
                        "match_time": 9400,
                        "type": "Punto e Cambio Palla",
                        "player": "ACERBI RAOUL",
                        "description": "Punto ACERBI RAOUL (B)",
                        "score": "20-19"
                    },
                    {
                        "match_time": 9500,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (A)",
                        "score": "21-19"
                    },
                    {
                        "match_time": 9500,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team A"
                    },
                    {
                        "match_time": 9500,
                        "type": "Fine Match",
                        "player": "Arbitro",
                        "description": "Partita Terminata"
                    }
                ],
                "match_time": 9500,
                "status": "finished",
                "server_team": 0,
                "server_index": [
                    1,
                    1
                ],
                "final_type": None
            },
            {
                "id": 3,
                "teamA": "PIZZILEO FILIPPO - INGROSSO PAOLO",
                "teamB": "SACRIPANTI MAURO - TITTA GIACOMO",
                "playersA": [
                    "PIZZILEO FILIPPO",
                    "INGROSSO PAOLO"
                ],
                "playersB": [
                    "SACRIPANTI MAURO",
                    "TITTA GIACOMO"
                ],
                "score_sets": [
                    0,
                    2
                ],
                "current_set": 2,
                "points": [
                    0,
                    0
                ],
                "sets_history": [
                    [
                        11,
                        21
                    ],
                    [
                        20,
                        22
                    ]
                ],
                "events": [
                    {
                        "match_time": 50,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (B)",
                        "score": "0-1"
                    },
                    {
                        "match_time": 350,
                        "type": "Punto e Cambio Palla",
                        "player": "INGROSSO PAOLO",
                        "description": "Punto INGROSSO PAOLO (A)",
                        "score": "1-2"
                    },
                    {
                        "match_time": 600,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (B)",
                        "score": "2-3"
                    },
                    {
                        "match_time": 750,
                        "type": "Punto e Cambio Palla",
                        "player": "PIZZILEO FILIPPO",
                        "description": "Punto PIZZILEO FILIPPO (A)",
                        "score": "3-3"
                    },
                    {
                        "match_time": 850,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (B)",
                        "score": "3-4"
                    },
                    {
                        "match_time": 850,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 1850,
                        "type": "Punto e Cambio Palla",
                        "player": "INGROSSO PAOLO",
                        "description": "Punto INGROSSO PAOLO (A)",
                        "score": "4-10"
                    },
                    {
                        "match_time": 1850,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 2300,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (B)",
                        "score": "6-11"
                    },
                    {
                        "match_time": 2400,
                        "type": "Punto e Cambio Palla",
                        "player": "PIZZILEO FILIPPO",
                        "description": "Punto PIZZILEO FILIPPO (A)",
                        "score": "7-11"
                    },
                    {
                        "match_time": 2500,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (B)",
                        "score": "7-12"
                    },
                    {
                        "match_time": 2850,
                        "type": "Punto e Cambio Palla",
                        "player": "INGROSSO PAOLO",
                        "description": "Punto INGROSSO PAOLO (A)",
                        "score": "8-13"
                    },
                    {
                        "match_time": 2850,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 2850,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 3000,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (B)",
                        "score": "8-14"
                    },
                    {
                        "match_time": 3350,
                        "type": "Punto e Cambio Palla",
                        "player": "PIZZILEO FILIPPO",
                        "description": "Punto PIZZILEO FILIPPO (A)",
                        "score": "9-15"
                    },
                    {
                        "match_time": 3650,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (B)",
                        "score": "10-16"
                    },
                    {
                        "match_time": 3850,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 4300,
                        "type": "Punto e Cambio Palla",
                        "player": "INGROSSO PAOLO",
                        "description": "Punto INGROSSO PAOLO (A)",
                        "score": "11-20"
                    },
                    {
                        "match_time": 4400,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (B)",
                        "score": "11-21"
                    },
                    {
                        "match_time": 4400,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team B"
                    },
                    {
                        "match_time": 4700,
                        "type": "Punto e Cambio Palla",
                        "player": "PIZZILEO FILIPPO",
                        "description": "Punto PIZZILEO FILIPPO (A)",
                        "score": "1-1"
                    },
                    {
                        "match_time": 4850,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (B)",
                        "score": "1-2"
                    },
                    {
                        "match_time": 4950,
                        "type": "Punto e Cambio Palla",
                        "player": "INGROSSO PAOLO",
                        "description": "Punto INGROSSO PAOLO (A)",
                        "score": "2-2"
                    },
                    {
                        "match_time": 5350,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (B)",
                        "score": "4-3"
                    },
                    {
                        "match_time": 5350,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 5500,
                        "type": "Punto e Cambio Palla",
                        "player": "PIZZILEO FILIPPO",
                        "description": "Punto PIZZILEO FILIPPO (A)",
                        "score": "5-3"
                    },
                    {
                        "match_time": 5600,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (B)",
                        "score": "5-4"
                    },
                    {
                        "match_time": 6000,
                        "type": "Punto e Cambio Palla",
                        "player": "INGROSSO PAOLO",
                        "description": "Punto INGROSSO PAOLO (A)",
                        "score": "6-6"
                    },
                    {
                        "match_time": 6150,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (B)",
                        "score": "6-7"
                    },
                    {
                        "match_time": 6250,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 6450,
                        "type": "Punto e Cambio Palla",
                        "player": "PIZZILEO FILIPPO",
                        "description": "Punto PIZZILEO FILIPPO (A)",
                        "score": "7-9"
                    },
                    {
                        "match_time": 6700,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (B)",
                        "score": "8-10"
                    },
                    {
                        "match_time": 7000,
                        "type": "Punto e Cambio Palla",
                        "player": "INGROSSO PAOLO",
                        "description": "Punto INGROSSO PAOLO (A)",
                        "score": "9-11"
                    },
                    {
                        "match_time": 7150,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 7150,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 7500,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (B)",
                        "score": "11-12"
                    },
                    {
                        "match_time": 7600,
                        "type": "Punto e Cambio Palla",
                        "player": "PIZZILEO FILIPPO",
                        "description": "Punto PIZZILEO FILIPPO (A)",
                        "score": "12-12"
                    },
                    {
                        "match_time": 7850,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (B)",
                        "score": "13-13"
                    },
                    {
                        "match_time": 8000,
                        "type": "Punto e Cambio Palla",
                        "player": "INGROSSO PAOLO",
                        "description": "Punto INGROSSO PAOLO (A)",
                        "score": "14-13"
                    },
                    {
                        "match_time": 8200,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 8350,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (B)",
                        "score": "15-14"
                    },
                    {
                        "match_time": 8450,
                        "type": "Punto e Cambio Palla",
                        "player": "PIZZILEO FILIPPO",
                        "description": "Punto PIZZILEO FILIPPO (A)",
                        "score": "16-14"
                    },
                    {
                        "match_time": 8550,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (B)",
                        "score": "16-15"
                    },
                    {
                        "match_time": 8900,
                        "type": "Punto e Cambio Palla",
                        "player": "INGROSSO PAOLO",
                        "description": "Punto INGROSSO PAOLO (A)",
                        "score": "17-16"
                    },
                    {
                        "match_time": 9050,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (B)",
                        "score": "17-17"
                    },
                    {
                        "match_time": 9200,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 9250,
                        "type": "Punto e Cambio Palla",
                        "player": "PIZZILEO FILIPPO",
                        "description": "Punto PIZZILEO FILIPPO (A)",
                        "score": "18-18"
                    },
                    {
                        "match_time": 9500,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (B)",
                        "score": "19-19"
                    },
                    {
                        "match_time": 9750,
                        "type": "Punto e Cambio Palla",
                        "player": "INGROSSO PAOLO",
                        "description": "Punto INGROSSO PAOLO (A)",
                        "score": "20-20"
                    },
                    {
                        "match_time": 9850,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (B)",
                        "score": "20-21"
                    },
                    {
                        "match_time": 10000,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 10000,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team B"
                    },
                    {
                        "match_time": 10000,
                        "type": "Fine Match",
                        "player": "Arbitro",
                        "description": "Partita Terminata"
                    }
                ],
                "match_time": 10000,
                "status": "finished",
                "server_team": 1,
                "server_index": [
                    1,
                    0
                ],
                "final_type": None
            },
            {
                "id": 1,
                "teamA": "ALFIERI MANUEL - RANGHIERI ALEX",
                "teamB": "SPADONI GIACOMO - LUISETTO MICHELE",
                "playersA": [
                    "ALFIERI MANUEL",
                    "RANGHIERI ALEX"
                ],
                "playersB": [
                    "SPADONI GIACOMO",
                    "LUISETTO MICHELE"
                ],
                "score_sets": [
                    0,
                    2
                ],
                "current_set": 2,
                "points": [
                    0,
                    0
                ],
                "sets_history": [
                    [
                        16,
                        21
                    ],
                    [
                        20,
                        22
                    ]
                ],
                "events": [
                    {
                        "match_time": 100,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (B)",
                        "score": "0-1"
                    },
                    {
                        "match_time": 450,
                        "type": "Punto e Cambio Palla",
                        "player": "RANGHIERI ALEX",
                        "description": "Punto RANGHIERI ALEX (A)",
                        "score": "1-3"
                    },
                    {
                        "match_time": 600,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (B)",
                        "score": "1-4"
                    },
                    {
                        "match_time": 700,
                        "type": "Punto e Cambio Palla",
                        "player": "ALFIERI MANUEL",
                        "description": "Punto ALFIERI MANUEL (A)",
                        "score": "2-4"
                    },
                    {
                        "match_time": 800,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (B)",
                        "score": "2-5"
                    },
                    {
                        "match_time": 800,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 1000,
                        "type": "Punto e Cambio Palla",
                        "player": "RANGHIERI ALEX",
                        "description": "Punto RANGHIERI ALEX (A)",
                        "score": "3-5"
                    },
                    {
                        "match_time": 1550,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (B)",
                        "score": "6-6"
                    },
                    {
                        "match_time": 1850,
                        "type": "Punto e Cambio Palla",
                        "player": "ALFIERI MANUEL",
                        "description": "Punto ALFIERI MANUEL (A)",
                        "score": "7-7"
                    },
                    {
                        "match_time": 1850,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 1950,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (B)",
                        "score": "7-8"
                    },
                    {
                        "match_time": 2400,
                        "type": "Punto e Cambio Palla",
                        "player": "RANGHIERI ALEX",
                        "description": "Punto RANGHIERI ALEX (A)",
                        "score": "8-10"
                    },
                    {
                        "match_time": 2700,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (B)",
                        "score": "9-11"
                    },
                    {
                        "match_time": 2750,
                        "type": "Punto e Cambio Palla",
                        "player": "ALFIERI MANUEL",
                        "description": "Punto ALFIERI MANUEL (A)",
                        "score": "10-11"
                    },
                    {
                        "match_time": 2750,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 2750,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 3200,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (B)",
                        "score": "12-12"
                    },
                    {
                        "match_time": 3300,
                        "type": "Punto e Cambio Palla",
                        "player": "RANGHIERI ALEX",
                        "description": "Punto RANGHIERI ALEX (A)",
                        "score": "13-12"
                    },
                    {
                        "match_time": 3450,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (B)",
                        "score": "13-13"
                    },
                    {
                        "match_time": 3700,
                        "type": "Punto e Cambio Palla",
                        "player": "ALFIERI MANUEL",
                        "description": "Punto ALFIERI MANUEL (A)",
                        "score": "14-14"
                    },
                    {
                        "match_time": 3700,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 4000,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (B)",
                        "score": "15-15"
                    },
                    {
                        "match_time": 4500,
                        "type": "Punto e Cambio Palla",
                        "player": "RANGHIERI ALEX",
                        "description": "Punto RANGHIERI ALEX (A)",
                        "score": "16-19"
                    },
                    {
                        "match_time": 4500,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 4700,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (B)",
                        "score": "16-20"
                    },
                    {
                        "match_time": 4850,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team B"
                    },
                    {
                        "match_time": 4950,
                        "type": "Punto e Cambio Palla",
                        "player": "ALFIERI MANUEL",
                        "description": "Punto ALFIERI MANUEL (A)",
                        "score": "1-0"
                    },
                    {
                        "match_time": 5500,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (B)",
                        "score": "3-1"
                    },
                    {
                        "match_time": 5850,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 6100,
                        "type": "Punto e Cambio Palla",
                        "player": "RANGHIERI ALEX",
                        "description": "Punto RANGHIERI ALEX (A)",
                        "score": "4-5"
                    },
                    {
                        "match_time": 6150,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (B)",
                        "score": "4-6"
                    },
                    {
                        "match_time": 6300,
                        "type": "Punto e Cambio Palla",
                        "player": "ALFIERI MANUEL",
                        "description": "Punto ALFIERI MANUEL (A)",
                        "score": "5-6"
                    },
                    {
                        "match_time": 6550,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (B)",
                        "score": "6-7"
                    },
                    {
                        "match_time": 6700,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 6850,
                        "type": "Punto e Cambio Palla",
                        "player": "RANGHIERI ALEX",
                        "description": "Punto RANGHIERI ALEX (A)",
                        "score": "7-8"
                    },
                    {
                        "match_time": 7000,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (B)",
                        "score": "7-9"
                    },
                    {
                        "match_time": 7150,
                        "type": "Punto e Cambio Palla",
                        "player": "ALFIERI MANUEL",
                        "description": "Punto ALFIERI MANUEL (A)",
                        "score": "8-9"
                    },
                    {
                        "match_time": 7450,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (B)",
                        "score": "9-10"
                    },
                    {
                        "match_time": 7600,
                        "type": "Punto e Cambio Palla",
                        "player": "RANGHIERI ALEX",
                        "description": "Punto RANGHIERI ALEX (A)",
                        "score": "10-10"
                    },
                    {
                        "match_time": 7750,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (B)",
                        "score": "10-11"
                    },
                    {
                        "match_time": 7750,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 7750,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 7900,
                        "type": "Punto e Cambio Palla",
                        "player": "ALFIERI MANUEL",
                        "description": "Punto ALFIERI MANUEL (A)",
                        "score": "11-11"
                    },
                    {
                        "match_time": 8050,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (B)",
                        "score": "11-12"
                    },
                    {
                        "match_time": 8200,
                        "type": "Punto e Cambio Palla",
                        "player": "RANGHIERI ALEX",
                        "description": "Punto RANGHIERI ALEX (A)",
                        "score": "12-12"
                    },
                    {
                        "match_time": 8400,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (B)",
                        "score": "13-13"
                    },
                    {
                        "match_time": 8600,
                        "type": "Punto e Cambio Palla",
                        "player": "ALFIERI MANUEL",
                        "description": "Punto ALFIERI MANUEL (A)",
                        "score": "14-14"
                    },
                    {
                        "match_time": 8600,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 8700,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (B)",
                        "score": "14-15"
                    },
                    {
                        "match_time": 8950,
                        "type": "Punto e Cambio Palla",
                        "player": "RANGHIERI ALEX",
                        "description": "Punto RANGHIERI ALEX (A)",
                        "score": "15-16"
                    },
                    {
                        "match_time": 9350,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (B)",
                        "score": "17-17"
                    },
                    {
                        "match_time": 9500,
                        "type": "Punto e Cambio Palla",
                        "player": "ALFIERI MANUEL",
                        "description": "Punto ALFIERI MANUEL (A)",
                        "score": "18-17"
                    },
                    {
                        "match_time": 9500,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 9650,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (B)",
                        "score": "18-18"
                    },
                    {
                        "match_time": 9950,
                        "type": "Punto e Cambio Palla",
                        "player": "RANGHIERI ALEX",
                        "description": "Punto RANGHIERI ALEX (A)",
                        "score": "19-19"
                    },
                    {
                        "match_time": 10050,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (B)",
                        "score": "19-20"
                    },
                    {
                        "match_time": 10150,
                        "type": "Punto e Cambio Palla",
                        "player": "ALFIERI MANUEL",
                        "description": "Punto ALFIERI MANUEL (A)",
                        "score": "20-20"
                    },
                    {
                        "match_time": 10250,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (B)",
                        "score": "20-21"
                    },
                    {
                        "match_time": 10400,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 10400,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team B"
                    },
                    {
                        "match_time": 10400,
                        "type": "Fine Match",
                        "player": "Arbitro",
                        "description": "Partita Terminata"
                    }
                ],
                "match_time": 10400,
                "status": "finished",
                "server_team": 1,
                "server_index": [
                    0,
                    1
                ],
                "final_type": None
            },
            {
                "id": 2,
                "teamA": "AREZZO DI TRIFILETTI FRANCO - BIGARELLI LUCA",
                "teamB": "MARCHETTO TOBIA - DAL MOLIN DAVIDE",
                "playersA": [
                    "AREZZO DI TRIFILETTI FRANCO",
                    "BIGARELLI LUCA"
                ],
                "playersB": [
                    "MARCHETTO TOBIA",
                    "DAL MOLIN DAVIDE"
                ],
                "score_sets": [
                    2,
                    0
                ],
                "current_set": 2,
                "points": [
                    0,
                    0
                ],
                "sets_history": [
                    [
                        21,
                        19
                    ],
                    [
                        22,
                        20
                    ]
                ],
                "events": [
                    {
                        "match_time": 200,
                        "type": "Punto e Cambio Palla",
                        "player": "DAL MOLIN DAVIDE",
                        "description": "Punto DAL MOLIN DAVIDE (B)",
                        "score": "1-1"
                    },
                    {
                        "match_time": 450,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (A)",
                        "score": "2-2"
                    },
                    {
                        "match_time": 650,
                        "type": "Punto e Cambio Palla",
                        "player": "MARCHETTO TOBIA",
                        "description": "Punto MARCHETTO TOBIA (B)",
                        "score": "3-3"
                    },
                    {
                        "match_time": 800,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 950,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (A)",
                        "score": "4-4"
                    },
                    {
                        "match_time": 1050,
                        "type": "Punto e Cambio Palla",
                        "player": "DAL MOLIN DAVIDE",
                        "description": "Punto DAL MOLIN DAVIDE (B)",
                        "score": "4-5"
                    },
                    {
                        "match_time": 1200,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (A)",
                        "score": "5-5"
                    },
                    {
                        "match_time": 1300,
                        "type": "Punto e Cambio Palla",
                        "player": "MARCHETTO TOBIA",
                        "description": "Punto MARCHETTO TOBIA (B)",
                        "score": "5-6"
                    },
                    {
                        "match_time": 1500,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (A)",
                        "score": "6-6"
                    },
                    {
                        "match_time": 1700,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 1900,
                        "type": "Punto e Cambio Palla",
                        "player": "DAL MOLIN DAVIDE",
                        "description": "Punto DAL MOLIN DAVIDE (B)",
                        "score": "8-7"
                    },
                    {
                        "match_time": 2100,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (A)",
                        "score": "9-7"
                    },
                    {
                        "match_time": 2250,
                        "type": "Punto e Cambio Palla",
                        "player": "MARCHETTO TOBIA",
                        "description": "Punto MARCHETTO TOBIA (B)",
                        "score": "10-8"
                    },
                    {
                        "match_time": 2400,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (A)",
                        "score": "11-8"
                    },
                    {
                        "match_time": 2550,
                        "type": "Punto e Cambio Palla",
                        "player": "DAL MOLIN DAVIDE",
                        "description": "Punto DAL MOLIN DAVIDE (B)",
                        "score": "11-9"
                    },
                    {
                        "match_time": 2700,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 2700,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 2800,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (A)",
                        "score": "12-10"
                    },
                    {
                        "match_time": 3100,
                        "type": "Punto e Cambio Palla",
                        "player": "MARCHETTO TOBIA",
                        "description": "Punto MARCHETTO TOBIA (B)",
                        "score": "13-11"
                    },
                    {
                        "match_time": 3250,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (A)",
                        "score": "14-11"
                    },
                    {
                        "match_time": 3300,
                        "type": "Punto e Cambio Palla",
                        "player": "DAL MOLIN DAVIDE",
                        "description": "Punto DAL MOLIN DAVIDE (B)",
                        "score": "14-12"
                    },
                    {
                        "match_time": 3500,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (A)",
                        "score": "15-12"
                    },
                    {
                        "match_time": 3650,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 3750,
                        "type": "Punto e Cambio Palla",
                        "player": "MARCHETTO TOBIA",
                        "description": "Punto MARCHETTO TOBIA (B)",
                        "score": "16-13"
                    },
                    {
                        "match_time": 4400,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (A)",
                        "score": "17-17"
                    },
                    {
                        "match_time": 4450,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 4650,
                        "type": "Punto e Cambio Palla",
                        "player": "DAL MOLIN DAVIDE",
                        "description": "Punto DAL MOLIN DAVIDE (B)",
                        "score": "18-18"
                    },
                    {
                        "match_time": 4950,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (A)",
                        "score": "19-19"
                    },
                    {
                        "match_time": 5150,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team A"
                    },
                    {
                        "match_time": 5550,
                        "type": "Punto e Cambio Palla",
                        "player": "MARCHETTO TOBIA",
                        "description": "Punto MARCHETTO TOBIA (B)",
                        "score": "2-1"
                    },
                    {
                        "match_time": 5750,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (A)",
                        "score": "3-2"
                    },
                    {
                        "match_time": 5950,
                        "type": "Punto e Cambio Palla",
                        "player": "DAL MOLIN DAVIDE",
                        "description": "Punto DAL MOLIN DAVIDE (B)",
                        "score": "3-3"
                    },
                    {
                        "match_time": 6100,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (A)",
                        "score": "4-3"
                    },
                    {
                        "match_time": 6100,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 6700,
                        "type": "Punto e Cambio Palla",
                        "player": "MARCHETTO TOBIA",
                        "description": "Punto MARCHETTO TOBIA (B)",
                        "score": "7-4"
                    },
                    {
                        "match_time": 6850,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (A)",
                        "score": "8-4"
                    },
                    {
                        "match_time": 7050,
                        "type": "Punto e Cambio Palla",
                        "player": "DAL MOLIN DAVIDE",
                        "description": "Punto DAL MOLIN DAVIDE (B)",
                        "score": "8-5"
                    },
                    {
                        "match_time": 7200,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 7300,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (A)",
                        "score": "9-6"
                    },
                    {
                        "match_time": 7350,
                        "type": "Punto e Cambio Palla",
                        "player": "MARCHETTO TOBIA",
                        "description": "Punto MARCHETTO TOBIA (B)",
                        "score": "9-7"
                    },
                    {
                        "match_time": 7500,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (A)",
                        "score": "10-7"
                    },
                    {
                        "match_time": 7600,
                        "type": "Punto e Cambio Palla",
                        "player": "DAL MOLIN DAVIDE",
                        "description": "Punto DAL MOLIN DAVIDE (B)",
                        "score": "10-8"
                    },
                    {
                        "match_time": 7900,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (A)",
                        "score": "11-9"
                    },
                    {
                        "match_time": 8000,
                        "type": "Punto e Cambio Palla",
                        "player": "MARCHETTO TOBIA",
                        "description": "Punto MARCHETTO TOBIA (B)",
                        "score": "11-10"
                    },
                    {
                        "match_time": 8000,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 8000,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 8100,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (A)",
                        "score": "12-10"
                    },
                    {
                        "match_time": 8450,
                        "type": "Punto e Cambio Palla",
                        "player": "DAL MOLIN DAVIDE",
                        "description": "Punto DAL MOLIN DAVIDE (B)",
                        "score": "13-11"
                    },
                    {
                        "match_time": 8950,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (A)",
                        "score": "14-13"
                    },
                    {
                        "match_time": 9100,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 9250,
                        "type": "Punto e Cambio Palla",
                        "player": "MARCHETTO TOBIA",
                        "description": "Punto MARCHETTO TOBIA (B)",
                        "score": "15-14"
                    },
                    {
                        "match_time": 9650,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (A)",
                        "score": "16-16"
                    },
                    {
                        "match_time": 10050,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 10200,
                        "type": "Punto e Cambio Palla",
                        "player": "DAL MOLIN DAVIDE",
                        "description": "Punto DAL MOLIN DAVIDE (B)",
                        "score": "19-17"
                    },
                    {
                        "match_time": 10600,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (A)",
                        "score": "20-18"
                    },
                    {
                        "match_time": 10650,
                        "type": "Punto e Cambio Palla",
                        "player": "MARCHETTO TOBIA",
                        "description": "Punto MARCHETTO TOBIA (B)",
                        "score": "20-19"
                    },
                    {
                        "match_time": 10950,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (A)",
                        "score": "21-20"
                    },
                    {
                        "match_time": 11150,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 11150,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team A"
                    },
                    {
                        "match_time": 11150,
                        "type": "Fine Match",
                        "player": "Arbitro",
                        "description": "Partita Terminata"
                    }
                ],
                "match_time": 11150,
                "status": "finished",
                "server_team": 0,
                "server_index": [
                    0,
                    0
                ],
                "final_type": None
            }
        ],
        "Semifinali": [
            {
                "id": 1,
                "teamA": "SPADONI GIACOMO - LUISETTO MICHELE",
                "teamB": "AREZZO DI TRIFILETTI FRANCO - BIGARELLI LUCA",
                "playersA": [
                    "SPADONI GIACOMO",
                    "LUISETTO MICHELE"
                ],
                "playersB": [
                    "AREZZO DI TRIFILETTI FRANCO",
                    "BIGARELLI LUCA"
                ],
                "score_sets": [
                    0,
                    2
                ],
                "current_set": 2,
                "points": [
                    0,
                    0
                ],
                "sets_history": [
                    [
                        16,
                        21
                    ],
                    [
                        13,
                        21
                    ]
                ],
                "events": [
                    {
                        "match_time": 250,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (B)",
                        "score": "1-1"
                    },
                    {
                        "match_time": 550,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (A)",
                        "score": "2-2"
                    },
                    {
                        "match_time": 850,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (B)",
                        "score": "3-3"
                    },
                    {
                        "match_time": 1000,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 1300,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (A)",
                        "score": "4-5"
                    },
                    {
                        "match_time": 1400,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (B)",
                        "score": "4-6"
                    },
                    {
                        "match_time": 1550,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (A)",
                        "score": "5-6"
                    },
                    {
                        "match_time": 1700,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (B)",
                        "score": "5-7"
                    },
                    {
                        "match_time": 2050,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 2300,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (A)",
                        "score": "6-10"
                    },
                    {
                        "match_time": 2400,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (B)",
                        "score": "6-11"
                    },
                    {
                        "match_time": 2650,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (A)",
                        "score": "7-12"
                    },
                    {
                        "match_time": 2950,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (B)",
                        "score": "8-13"
                    },
                    {
                        "match_time": 2950,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 2950,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 3200,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (A)",
                        "score": "9-14"
                    },
                    {
                        "match_time": 3300,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (B)",
                        "score": "9-15"
                    },
                    {
                        "match_time": 3400,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (A)",
                        "score": "10-15"
                    },
                    {
                        "match_time": 3750,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (B)",
                        "score": "12-16"
                    },
                    {
                        "match_time": 3750,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 3850,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (A)",
                        "score": "13-16"
                    },
                    {
                        "match_time": 4000,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (B)",
                        "score": "13-17"
                    },
                    {
                        "match_time": 4150,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (A)",
                        "score": "14-17"
                    },
                    {
                        "match_time": 4300,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (B)",
                        "score": "15-18"
                    },
                    {
                        "match_time": 4550,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (A)",
                        "score": "16-19"
                    },
                    {
                        "match_time": 4550,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 4650,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (B)",
                        "score": "16-20"
                    },
                    {
                        "match_time": 4800,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team B"
                    },
                    {
                        "match_time": 5050,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (A)",
                        "score": "1-1"
                    },
                    {
                        "match_time": 5150,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (B)",
                        "score": "1-2"
                    },
                    {
                        "match_time": 5600,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 5750,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (A)",
                        "score": "2-6"
                    },
                    {
                        "match_time": 5950,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (B)",
                        "score": "2-7"
                    },
                    {
                        "match_time": 6250,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (A)",
                        "score": "3-8"
                    },
                    {
                        "match_time": 6350,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (B)",
                        "score": "3-9"
                    },
                    {
                        "match_time": 6450,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (A)",
                        "score": "4-9"
                    },
                    {
                        "match_time": 6600,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 6750,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (B)",
                        "score": "5-10"
                    },
                    {
                        "match_time": 6850,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (A)",
                        "score": "6-10"
                    },
                    {
                        "match_time": 7000,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (B)",
                        "score": "6-11"
                    },
                    {
                        "match_time": 7500,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (A)",
                        "score": "7-13"
                    },
                    {
                        "match_time": 7550,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 7550,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 7950,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (B)",
                        "score": "10-14"
                    },
                    {
                        "match_time": 8500,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (A)",
                        "score": "11-17"
                    },
                    {
                        "match_time": 8500,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 8850,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (B)",
                        "score": "12-18"
                    },
                    {
                        "match_time": 9150,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (A)",
                        "score": "13-19"
                    },
                    {
                        "match_time": 9250,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (B)",
                        "score": "13-20"
                    },
                    {
                        "match_time": 9450,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team B"
                    },
                    {
                        "match_time": 9450,
                        "type": "Fine Match",
                        "player": "Arbitro",
                        "description": "Partita Terminata"
                    }
                ],
                "match_time": 9450,
                "status": "finished",
                "server_team": 1,
                "server_index": [
                    0,
                    1
                ],
                "final_type": None
            },
            {
                "id": 2,
                "teamA": "SACRIPANTI MAURO - TITTA GIACOMO",
                "teamB": "VISCOVICH MARCO - ROSSI ENRICO",
                "playersA": [
                    "SACRIPANTI MAURO",
                    "TITTA GIACOMO"
                ],
                "playersB": [
                    "VISCOVICH MARCO",
                    "ROSSI ENRICO"
                ],
                "score_sets": [
                    2,
                    1
                ],
                "current_set": 3,
                "points": [
                    0,
                    0
                ],
                "sets_history": [
                    [
                        10,
                        21
                    ],
                    [
                        22,
                        20
                    ],
                    [
                        17,
                        15
                    ]
                ],
                "events": [
                    {
                        "match_time": 200,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (B)",
                        "score": "0-1"
                    },
                    {
                        "match_time": 500,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (A)",
                        "score": "1-2"
                    },
                    {
                        "match_time": 600,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (B)",
                        "score": "1-3"
                    },
                    {
                        "match_time": 800,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (A)",
                        "score": "2-3"
                    },
                    {
                        "match_time": 1050,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (B)",
                        "score": "3-4"
                    },
                    {
                        "match_time": 1050,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 1400,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (A)",
                        "score": "4-6"
                    },
                    {
                        "match_time": 1650,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (B)",
                        "score": "5-7"
                    },
                    {
                        "match_time": 1950,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (A)",
                        "score": "6-8"
                    },
                    {
                        "match_time": 1950,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 2100,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (B)",
                        "score": "6-9"
                    },
                    {
                        "match_time": 2850,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 2850,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 3100,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (A)",
                        "score": "7-16"
                    },
                    {
                        "match_time": 3300,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (B)",
                        "score": "8-17"
                    },
                    {
                        "match_time": 3700,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 3850,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (A)",
                        "score": "9-20"
                    },
                    {
                        "match_time": 4100,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (B)",
                        "score": "10-21"
                    },
                    {
                        "match_time": 4100,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team B"
                    },
                    {
                        "match_time": 4650,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (A)",
                        "score": "1-4"
                    },
                    {
                        "match_time": 4800,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (B)",
                        "score": "1-5"
                    },
                    {
                        "match_time": 4900,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 5100,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (A)",
                        "score": "2-7"
                    },
                    {
                        "match_time": 5250,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (B)",
                        "score": "2-8"
                    },
                    {
                        "match_time": 5300,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (A)",
                        "score": "3-8"
                    },
                    {
                        "match_time": 5400,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (B)",
                        "score": "3-9"
                    },
                    {
                        "match_time": 5500,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (A)",
                        "score": "4-9"
                    },
                    {
                        "match_time": 5650,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (B)",
                        "score": "4-10"
                    },
                    {
                        "match_time": 5650,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 5800,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (A)",
                        "score": "5-10"
                    },
                    {
                        "match_time": 6350,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (B)",
                        "score": "7-11"
                    },
                    {
                        "match_time": 6450,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (A)",
                        "score": "8-11"
                    },
                    {
                        "match_time": 6750,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (B)",
                        "score": "9-12"
                    },
                    {
                        "match_time": 6750,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 6750,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 6950,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (A)",
                        "score": "10-13"
                    },
                    {
                        "match_time": 7250,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (B)",
                        "score": "12-14"
                    },
                    {
                        "match_time": 7400,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (A)",
                        "score": "13-14"
                    },
                    {
                        "match_time": 7450,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 7600,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (B)",
                        "score": "14-15"
                    },
                    {
                        "match_time": 7800,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (A)",
                        "score": "15-15"
                    },
                    {
                        "match_time": 7850,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (B)",
                        "score": "15-16"
                    },
                    {
                        "match_time": 8500,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (A)",
                        "score": "16-19"
                    },
                    {
                        "match_time": 8500,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 9000,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (B)",
                        "score": "19-20"
                    },
                    {
                        "match_time": 9100,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (A)",
                        "score": "20-20"
                    },
                    {
                        "match_time": 9450,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 9450,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team A"
                    },
                    {
                        "match_time": 9600,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (B)",
                        "score": "0-1"
                    },
                    {
                        "match_time": 9950,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (A)",
                        "score": "1-2"
                    },
                    {
                        "match_time": 10100,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (B)",
                        "score": "1-3"
                    },
                    {
                        "match_time": 10300,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (A)",
                        "score": "2-4"
                    },
                    {
                        "match_time": 10400,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 10750,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (B)",
                        "score": "4-5"
                    },
                    {
                        "match_time": 10850,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (A)",
                        "score": "5-5"
                    },
                    {
                        "match_time": 11000,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (B)",
                        "score": "5-6"
                    },
                    {
                        "match_time": 11350,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (A)",
                        "score": "6-7"
                    },
                    {
                        "match_time": 11550,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 11800,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (B)",
                        "score": "9-8"
                    },
                    {
                        "match_time": 12400,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (A)",
                        "score": "10-11"
                    },
                    {
                        "match_time": 12400,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 12400,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 12750,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (B)",
                        "score": "12-12"
                    },
                    {
                        "match_time": 12850,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (A)",
                        "score": "13-12"
                    },
                    {
                        "match_time": 13000,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (B)",
                        "score": "13-13"
                    },
                    {
                        "match_time": 13150,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (A)",
                        "score": "14-13"
                    },
                    {
                        "match_time": 13300,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (B)",
                        "score": "14-14"
                    },
                    {
                        "match_time": 13300,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 13600,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (A)",
                        "score": "15-15"
                    },
                    {
                        "match_time": 13950,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team A"
                    },
                    {
                        "match_time": 13950,
                        "type": "Fine Match",
                        "player": "Arbitro",
                        "description": "Partita Terminata"
                    }
                ],
                "match_time": 13950,
                "status": "finished",
                "server_team": 0,
                "server_index": [
                    1,
                    1
                ],
                "final_type": None
            }
        ],
        "Finali": [
            {
                "id": 1,
                "teamA": "SPADONI GIACOMO - LUISETTO MICHELE",
                "teamB": "VISCOVICH MARCO - ROSSI ENRICO",
                "playersA": [
                    "SPADONI GIACOMO",
                    "LUISETTO MICHELE"
                ],
                "playersB": [
                    "VISCOVICH MARCO",
                    "ROSSI ENRICO"
                ],
                "score_sets": [
                    0,
                    2
                ],
                "current_set": 2,
                "points": [
                    0,
                    0
                ],
                "sets_history": [
                    [
                        12,
                        21
                    ],
                    [
                        19,
                        21
                    ]
                ],
                "events": [
                    {
                        "match_time": 200,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (B)",
                        "score": "1-1"
                    },
                    {
                        "match_time": 950,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 1350,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (A)",
                        "score": "2-8"
                    },
                    {
                        "match_time": 1500,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (B)",
                        "score": "2-9"
                    },
                    {
                        "match_time": 1600,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (A)",
                        "score": "3-9"
                    },
                    {
                        "match_time": 1750,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (B)",
                        "score": "3-10"
                    },
                    {
                        "match_time": 1850,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (A)",
                        "score": "4-10"
                    },
                    {
                        "match_time": 1850,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 1950,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (B)",
                        "score": "4-11"
                    },
                    {
                        "match_time": 2200,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (A)",
                        "score": "5-12"
                    },
                    {
                        "match_time": 2450,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (B)",
                        "score": "6-13"
                    },
                    {
                        "match_time": 2800,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 2800,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 3000,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (A)",
                        "score": "7-16"
                    },
                    {
                        "match_time": 3550,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (B)",
                        "score": "10-17"
                    },
                    {
                        "match_time": 3700,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 3950,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (A)",
                        "score": "11-19"
                    },
                    {
                        "match_time": 4200,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (B)",
                        "score": "12-20"
                    },
                    {
                        "match_time": 4300,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team B"
                    },
                    {
                        "match_time": 4450,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (A)",
                        "score": "1-0"
                    },
                    {
                        "match_time": 4550,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (B)",
                        "score": "1-1"
                    },
                    {
                        "match_time": 4700,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (A)",
                        "score": "2-1"
                    },
                    {
                        "match_time": 4900,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (B)",
                        "score": "2-2"
                    },
                    {
                        "match_time": 5250,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 5450,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (A)",
                        "score": "3-5"
                    },
                    {
                        "match_time": 5600,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (B)",
                        "score": "3-6"
                    },
                    {
                        "match_time": 5900,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (A)",
                        "score": "4-7"
                    },
                    {
                        "match_time": 6000,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (B)",
                        "score": "4-8"
                    },
                    {
                        "match_time": 6300,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (A)",
                        "score": "5-9"
                    },
                    {
                        "match_time": 6300,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 6750,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (B)",
                        "score": "7-10"
                    },
                    {
                        "match_time": 6950,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (A)",
                        "score": "8-11"
                    },
                    {
                        "match_time": 7050,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (B)",
                        "score": "8-12"
                    },
                    {
                        "match_time": 7200,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (A)",
                        "score": "9-12"
                    },
                    {
                        "match_time": 7200,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 7200,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 8100,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 8250,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (B)",
                        "score": "16-13"
                    },
                    {
                        "match_time": 9000,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (A)",
                        "score": "17-18"
                    },
                    {
                        "match_time": 9000,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 9150,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (B)",
                        "score": "17-19"
                    },
                    {
                        "match_time": 9250,
                        "type": "Punto e Cambio Palla",
                        "player": "LUISETTO MICHELE",
                        "description": "Punto LUISETTO MICHELE (A)",
                        "score": "18-19"
                    },
                    {
                        "match_time": 9400,
                        "type": "Punto e Cambio Palla",
                        "player": "VISCOVICH MARCO",
                        "description": "Punto VISCOVICH MARCO (B)",
                        "score": "18-20"
                    },
                    {
                        "match_time": 9550,
                        "type": "Punto e Cambio Palla",
                        "player": "SPADONI GIACOMO",
                        "description": "Punto SPADONI GIACOMO (A)",
                        "score": "19-20"
                    },
                    {
                        "match_time": 9700,
                        "type": "Punto e Cambio Palla",
                        "player": "ROSSI ENRICO",
                        "description": "Punto ROSSI ENRICO (B)",
                        "score": "19-21"
                    },
                    {
                        "match_time": 9700,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team B"
                    },
                    {
                        "match_time": 9700,
                        "type": "Fine Match",
                        "player": "Arbitro",
                        "description": "Partita Terminata"
                    }
                ],
                "match_time": 9700,
                "status": "finished",
                "server_team": 1,
                "server_index": [
                    0,
                    1
                ],
                "final_type": "3-4"
            },
            {
                "id": 2,
                "teamA": "AREZZO DI TRIFILETTI FRANCO - BIGARELLI LUCA",
                "teamB": "SACRIPANTI MAURO - TITTA GIACOMO",
                "playersA": [
                    "AREZZO DI TRIFILETTI FRANCO",
                    "BIGARELLI LUCA"
                ],
                "playersB": [
                    "SACRIPANTI MAURO",
                    "TITTA GIACOMO"
                ],
                "score_sets": [
                    2,
                    1
                ],
                "current_set": 3,
                "points": [
                    0,
                    0
                ],
                "sets_history": [
                    [
                        17,
                        21
                    ],
                    [
                        22,
                        20
                    ],
                    [
                        15,
                        12
                    ]
                ],
                "events": [
                    {
                        "match_time": 150,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (B)",
                        "score": "0-1"
                    },
                    {
                        "match_time": 850,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (A)",
                        "score": "1-5"
                    },
                    {
                        "match_time": 1000,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 1200,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (B)",
                        "score": "3-6"
                    },
                    {
                        "match_time": 1950,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (A)",
                        "score": "4-10"
                    },
                    {
                        "match_time": 1950,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 2700,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (B)",
                        "score": "8-11"
                    },
                    {
                        "match_time": 2800,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (A)",
                        "score": "9-11"
                    },
                    {
                        "match_time": 2900,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (B)",
                        "score": "9-12"
                    },
                    {
                        "match_time": 2900,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 2900,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 3300,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (A)",
                        "score": "10-14"
                    },
                    {
                        "match_time": 3900,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 4050,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (B)",
                        "score": "14-15"
                    },
                    {
                        "match_time": 4150,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (A)",
                        "score": "15-15"
                    },
                    {
                        "match_time": 4300,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (B)",
                        "score": "15-16"
                    },
                    {
                        "match_time": 4350,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (A)",
                        "score": "16-16"
                    },
                    {
                        "match_time": 4500,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (B)",
                        "score": "16-17"
                    },
                    {
                        "match_time": 4800,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 5000,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (A)",
                        "score": "17-19"
                    },
                    {
                        "match_time": 5150,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (B)",
                        "score": "17-20"
                    },
                    {
                        "match_time": 5300,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team B"
                    },
                    {
                        "match_time": 5600,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (A)",
                        "score": "1-1"
                    },
                    {
                        "match_time": 5700,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (B)",
                        "score": "1-2"
                    },
                    {
                        "match_time": 6000,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (A)",
                        "score": "2-3"
                    },
                    {
                        "match_time": 6200,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (B)",
                        "score": "2-4"
                    },
                    {
                        "match_time": 6350,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (A)",
                        "score": "3-4"
                    },
                    {
                        "match_time": 6350,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 7050,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (B)",
                        "score": "8-5"
                    },
                    {
                        "match_time": 7200,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 7350,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (A)",
                        "score": "9-6"
                    },
                    {
                        "match_time": 7500,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (B)",
                        "score": "9-7"
                    },
                    {
                        "match_time": 7650,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (A)",
                        "score": "10-7"
                    },
                    {
                        "match_time": 8000,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (B)",
                        "score": "11-8"
                    },
                    {
                        "match_time": 8250,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 8250,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 8350,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (A)",
                        "score": "12-10"
                    },
                    {
                        "match_time": 8500,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (B)",
                        "score": "12-11"
                    },
                    {
                        "match_time": 8700,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (A)",
                        "score": "13-11"
                    },
                    {
                        "match_time": 8850,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (B)",
                        "score": "13-12"
                    },
                    {
                        "match_time": 8950,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (A)",
                        "score": "14-12"
                    },
                    {
                        "match_time": 9100,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (B)",
                        "score": "14-13"
                    },
                    {
                        "match_time": 9250,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 9550,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (A)",
                        "score": "15-15"
                    },
                    {
                        "match_time": 9750,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (B)",
                        "score": "15-16"
                    },
                    {
                        "match_time": 9850,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (A)",
                        "score": "16-16"
                    },
                    {
                        "match_time": 10000,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (B)",
                        "score": "16-17"
                    },
                    {
                        "match_time": 10250,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (A)",
                        "score": "17-18"
                    },
                    {
                        "match_time": 10250,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 10300,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (B)",
                        "score": "17-19"
                    },
                    {
                        "match_time": 10450,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (A)",
                        "score": "18-19"
                    },
                    {
                        "match_time": 10600,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (B)",
                        "score": "18-20"
                    },
                    {
                        "match_time": 10750,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (A)",
                        "score": "19-20"
                    },
                    {
                        "match_time": 11150,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 11150,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team A"
                    },
                    {
                        "match_time": 11650,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (B)",
                        "score": "2-1"
                    },
                    {
                        "match_time": 11950,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (A)",
                        "score": "3-2"
                    },
                    {
                        "match_time": 12200,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 12550,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (B)",
                        "score": "7-3"
                    },
                    {
                        "match_time": 12700,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (A)",
                        "score": "8-3"
                    },
                    {
                        "match_time": 12900,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (B)",
                        "score": "8-4"
                    },
                    {
                        "match_time": 13200,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (A)",
                        "score": "9-5"
                    },
                    {
                        "match_time": 13200,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 13700,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (B)",
                        "score": "11-6"
                    },
                    {
                        "match_time": 14250,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (A)",
                        "score": "12-9"
                    },
                    {
                        "match_time": 14250,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Cambio Campo"
                    },
                    {
                        "match_time": 14250,
                        "type": "Info",
                        "player": "Sistema",
                        "description": "Time-out Tecnico"
                    },
                    {
                        "match_time": 14550,
                        "type": "Punto e Cambio Palla",
                        "player": "TITTA GIACOMO",
                        "description": "Punto TITTA GIACOMO (B)",
                        "score": "13-10"
                    },
                    {
                        "match_time": 14650,
                        "type": "Punto e Cambio Palla",
                        "player": "BIGARELLI LUCA",
                        "description": "Punto BIGARELLI LUCA (A)",
                        "score": "14-10"
                    },
                    {
                        "match_time": 14750,
                        "type": "Punto e Cambio Palla",
                        "player": "SACRIPANTI MAURO",
                        "description": "Punto SACRIPANTI MAURO (B)",
                        "score": "14-11"
                    },
                    {
                        "match_time": 15000,
                        "type": "Punto e Cambio Palla",
                        "player": "AREZZO DI TRIFILETTI FRANCO",
                        "description": "Punto AREZZO DI TRIFILETTI FRANCO (A)",
                        "score": "15-12"
                    },
                    {
                        "match_time": 15000,
                        "type": "Fine Set",
                        "player": "Arbitro",
                        "description": "Set vinto da Team A"
                    },
                    {
                        "match_time": 15000,
                        "type": "Fine Match",
                        "player": "Arbitro",
                        "description": "Partita Terminata"
                    }
                ],
                "match_time": 15000,
                "status": "finished",
                "server_team": 0,
                "server_index": [
                    0,
                    0
                ],
                "final_type": "1-2"
            }
        ]
    }
}

async def init_database():
    # In Docker usiamo 'db', in locale 'localhost'
    mongo_url = os.environ.get("MONGO_URL", "mongodb://db:27017")
    client = AsyncMongoClient(mongo_url)
    db = client["beachvolley"]

    await db.teams.delete_many({})
    await db.tournaments.delete_many({})

    teams = [
        "ALFIERI MANUEL - RANGHIERI ALEX", "ANDREATTA TIZIANO - BENZI DAVIDE",
        "COTTAFAVA SAMUELE - DAL CORSO GIANLUCA", "PODESTA' SIMONE - MARTINO MATTEO",
        "MARCHETTO TOBIA - DAL MOLIN DAVIDE", "BONIFAZI CARLO - ACERBI RAOUL",
        "SACRIPANTI MAURO - TITTA GIACOMO", "SPADONI GIACOMO - LUISETTO MICHELE",
        "LUPO DANIELE - BORRACCINO DAVIDE", "KRUMINS DAVIS - CAMINATI MARCO",
        "CECCOLI EDGARDO - CARUCCI ALESSANDRO", "GEROMIN FEDERICO - CAMOZZI MATTEO",
        "AREZZO DI TRIFILETTI FRANCO - BIGARELLI LUCA", "VISCOVICH MARCO - ROSSI ENRICO",
        "PIZZILEO FILIPPO - INGROSSO PAOLO", "PRETI ALESSANDRO - MUSSA FABRIZIO"
    ]
    punti = [400, 504, 300, 200, 300, 600, 700, 500, 900, 1200, 600, 700, 600, 200, 500, 400]

    team_data = [{"name": teams[i], "points": punti[i]} for i in range(len(teams))]
    await db.teams.insert_many(team_data)

    tappa2 = {
        "name": "Tappa 2 Assoluti",
        "played": False,
        "partite": {"Ottavi di Finale": [], "Quarti di Finale": [], "Semifinali": [], "Finali": []}
    }

    await db.tournaments.insert_many([tappa_esistente, tappa2])

    print("✅ Database inizializzato correttamente con Tappa 1 e Tappa 2.")
    client.close()


if __name__ == "__main__":
    asyncio.run(init_database())