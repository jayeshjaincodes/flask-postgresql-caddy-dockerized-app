# 🚀 Dockerized Flask + PostgreSQL + Caddy App

A containerized backend setup using:

* Flask (API backend)
* PostgreSQL (database)
* Caddy (reverse proxy)
* Adminer (DB UI)

---

# ⚙️ Setup Instructions

## 1. Clone the repository

```bash
git clone https://github.com/jayeshjaincodes/flask-postgresql-caddy-dockerized-app.git
cd flask-postgresql-caddy-dockerized-app

---

## 2. Configure Environment Variables

Create a `.env` file in the root:

```env
# Python & Image Versions
PYTHON_IMAGE_VERSION=3.10
POSTGRES_IMAGE_VERSION=14
CADDY_IMAGE_VERSION=2.5.1

# Database Config
POSTGRES_HOSTNAME=postgres
POSTGRES_DATABASE=db
POSTGRES_USERNAME=admin
POSTGRES_PASSWORD=password
```

---

# 🌐 Caddy Configuration

### Default (Local Development)

```caddy
localhost {
    reverse_proxy app:8000
}
```

---

### If using a real domain

Replace `localhost` with your domain:

```caddy
yourdomain.com {
    reverse_proxy app:8000
}
```

---

# 🐳 Run the Application

To run the project:

```bash
docker compose up --build
```

# 🐳 Stop the Application

To stop the project:

```bash
docker compose down
```

---

# 🌍 Access the Services

* App: [http://localhost](http://localhost)
* Direct Flask: [http://localhost:8000](http://localhost:8000)
* Adminer: [http://localhost:8080](http://localhost:8080)

