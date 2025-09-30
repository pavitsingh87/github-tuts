# Finance Support System

A multi-user finance support system with AI assistance and human support capabilities.

## Features

- **Customer Portal** (`/customer`): 
  - AI-powered finance assistance
  - Multi-user chat rooms
  - Human support escalation
  - Real-time messaging

- **Employee Portal** (`/employee`):
  - Support queue management
  - One-on-one customer assistance
  - Real-time dashboard
  - Session management

## URLs

- **Main Landing Page**: `http://localhost:8000/`
- **Customer Portal**: `http://localhost:8000/customer`
- **Employee Portal**: `http://localhost:8000/employee`

## Quick Start

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables in `.env`:
```
OPENAI_API_KEY=your_openai_api_key
SERPAPI_API_KEY=your_serpapi_key
```

3. Start the server:
```bash
uvicorn main:app --reload
```

4. Access the system:
   - Visit `http://localhost:8000/` to choose your portal
   - Customers: Click "Customer Portal" 
   - Employees: Click "Employee Portal"

## Usage

### For Customers:
1. Go to `/customer`
2. Enter your name and room ID
3. Start chatting with AI or type `/human` for human support

### For Employees:
1. Go to `/employee` 
2. Enter your employee ID
3. Access dashboard to manage support queue
4. Take customers from queue for one-on-one support