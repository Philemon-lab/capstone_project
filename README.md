# 🚍 Bus Ticketing System

A Django REST API for a bus ticketing system that allows multiple bus agencies to register and passengers to book tickets.

## ✨ Features

- **User Authentication**: Role-based authentication (Passenger, Agency Staff, Admin)
- **Bus Management**: Agencies can register and manage their buses and routes
- **Trip Scheduling**: Create and manage trips with dynamic pricing
- **Ticket Booking**: Passengers can search, view, and book tickets
- **Payment Processing**: Simulated payment system
- **Booking History**: Users can view their past and upcoming trips

## 🛠️ Technology Stack

- **Backend**: Django, Django REST Framework
- **Database**: SQLite (development), PostgreSQL (production-ready)
- **Authentication**: Session-based authentication
- **API Documentation**: Django REST Framework's browsable API

## 📦 Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/bus-ticketing-system.git
   cd bus-ticketing-system