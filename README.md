# postbank-dwh-api
Postbank data warehouse API SoftUni Fest project

## Requirements
Python >= 3.9</br>
```pip install -r requirements.txt```</br>
Configure ```.env``` from ```env_example``` template</br>
```python manage.py runserver 127.0.0.1:8001```

## Introduction
This document aims to describe the features of this api.

## App overview
Postbank provides its clients (Traders) with POS terminals, with which they receive payments with debit or credit cards.
Aiming to popularise their business and stimulate card transactions, traders offer discounts to their clients when they
pay via card at a POS terminal. The main the purpose of this app is to act as a data warehouse, which stores employees, traders
and terminals.

## Features
POS Discount data warehouse app, built with DRF.
It has 2 users - traders and bank employees
There is a POS Terminal model

Traders can have POS terminals.
