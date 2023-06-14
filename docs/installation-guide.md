<div align="center">
  <h1>Mood Sync Installation Guide</h1>
</div>

---

## 🚀 Getting Started

To set up Mood Sync locally, follow the steps below:

### 1. Install Git

Git is required to clone the project from the repository.

- Visit the [Git website](https://git-scm.com/) and follow the instructions to install Git on your machine.

### 2. Install Docker & Docker Compose

Docker and Docker Compose are used for containerization and managing the project's dependencies.

- Install Docker:
  - For Windows and macOS, visit the [Docker website](https://www.docker.com/) and download the Docker Desktop application.
  - For Linux, follow the instructions for your specific distribution to install Docker.

- Install Docker Compose:
  - Docker Compose usually comes bundled with Docker Desktop for Windows and macOS.
  - For Linux, you can follow the [official installation guide](https://docs.docker.com/compose/install/) to install Docker Compose separately.

### 3. Clone the Project

Open your preferred terminal or command prompt and run the following command:

```bash
git clone https://github.com/anuragbhatt1805/mood-sync-api.git
```

This will clone the Mood Sync project from the GitHub repository to your local machine.

### 4. Install a Code Editor

Choose a code editor for development. We recommend using Visual Studio Code (VS Code) due to its extensive features and compatibility.

- Download and install [Visual Studio Code](https://code.visualstudio.com/).

### 5. Move to Installation Directory

Navigate to the installation directory of the Mood Sync project using your preferred terminal or command prompt.

```bash
cd mood-sync-api
```

### 6. Run the Project

To start the Mood Sync project, run the following command:

```bash
docker-compose up
```

This command will build the necessary Docker containers and start the project.

Alternatively, you can use the following command if you need to run additional Django management commands:

```bash
docker-compose run app --rm sh -c 'python manage.py runserver'
```

This command will run the project using Django's built-in development server.

---

Congratulations! Mood Sync is now set up and running on your local machine. You can access the project by opening your web browser and visiting [http://localhost:8000/](http://127.0.0.1:8000/).

For more detailed instructions and information, please refer to the [Documentation](https://github.com/anuragbhatt1805/mood-sync-api/blob/main/README.md).

---

<div align="center">
  Made with ❤️ by Your Team
</div>