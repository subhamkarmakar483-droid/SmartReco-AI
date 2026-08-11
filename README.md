# SmartReco AI

SmartReco AI is an agentic behavioral recommendation system that observes user interactions with products and generates personalized recommendations using AI.

## 🚀 Features

- User registration and login
- JWT-based authentication
- Secure password hashing with bcrypt
- Product management
- User behavior tracking
- Behavior-based product recommendations
- Category-based recommendation engine
- AI-generated personalized recommendation messages
- Mesh API integration for AI generation
- PostgreSQL database
- FastAPI REST API
- Swagger API documentation

## 🧠 How SmartReco Works

The recommendation pipeline works as follows:

User
  ↓
Login
  ↓
User interacts with a product
  ↓
Behavior is recorded
  ↓
System identifies the user's latest interaction
  ↓
Product category is analyzed
  ↓
Relevant products are retrieved
  ↓
Mesh API generates a personalized message
  ↓
Recommendation is returned to the user

## 🏗️ Project Structure

```text
app/
│
├── agent/
│   └── recommender.py
│
├── auth/
│   └── routes.py
│
├── core/
│   ├── config.py
│   └── security.py
│
├── db/
│   ├── base.py
│   └── database.py
│
├── dependencies/
│   └── auth.py
│
├── models/
│   ├── behavior.py
│   ├── product.py
│   └── user.py
│
├── routes/
│   ├── behavior.py
│   ├── product.py
│   └── recommendation.py
│
├── schemas/
│   ├── behavior.py
│   ├── product.py
│   └── user.py
│
├── services/
│   └── mesh.py
│
└── main.py
Submission check trigger - SmartReco AI
