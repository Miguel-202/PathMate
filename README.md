# PathMate: Your AI-Powered Roadmap for Career Success
<p align="center">
  <img src="logo.png" alt="PathMate Logo">
</p>
*Submitted for ShellHacks 2023*

## Overview
PathMate is designed to bridge the gap between aspiring professionals—or anyone looking to achieve a specific set of goals—and the realization of those goals. "Where your dreams find a date in your calendar," PathMate employs AI-powered roadmaps to provide a comprehensive development solution. This app covers everything from legal paperwork to skills enhancement opportunities, making it ideal for students, young professionals, and anyone looking to streamline their career path.

What sets PathMate apart is its intelligent calendar integration. The app not only crafts a tailored roadmap but also schedules events—smaller, actionable steps toward your goal—right into your calendar. With adjustable time durations and frequency recommendations, PathMate ensures that you stay on track to achieve any type of goal you set.

## Features
- **AI-Powered Roadmaps**: Custom roadmaps generated using advanced Natural Language algorithms.
![AI-Powered Roadmaps](screenshot1.png)
- **Task Interactivity**: Each task on the roadmap is clickable for more details, deletion, or marking as done.
- **Holistic Solutions**: From visa paperwork to coding skills, we have got you covered.
- **User-Friendly UI**: Easy to navigate and use, helping you to focus on what truly matters.

## Technology Stack
- **AI and Machine Learning**
- **Python for backend logic**
- **Django for web framework**
- **JavaScript for frontend interactions**
- **SQL for databases**
- **MindDBS for prompt engineering**
- **Github for Version control**
- **Github Global Campus for learning and Github Copilot**
- **Github sites for site deployment**
- **GoDaddy for Domain registry**
- **Auth0 for user authorization account login**

## Installation & Setup

1. **Clone the GitHub repository:**
    ```bash
    git clone https://github.com/Miguel-202/PathMate
    ```

2. **Navigate to the project directory:**
    ```bash
    cd PathMate
    ```

3. **Create a virtual environment:**
    ```bash
    python3 -m venv venv
    ```

4. **Activate the virtual environment:**
    ```bash
    source venv/bin/activate
    ```

5. **Install the required packages:**
    ```bash
    pip install -r requirements.txt
    ```

6. **Make initial database migrations:**
    ```bash
    python manage.py makemigrations
    ```

7. **Apply the database migrations:**
    ```bash
    python manage.py migrate
    ```

8. **Create an admin user:**
    ```bash
    python manage.py createsuperuser
    ```

9. **Run the server:**
    ```bash
    python manage.py runserver
    ```




## How to Use
1. **Sign Up**: Create a new account or sign in.
2. **Input Goals**: Enter your career goals or objectives.
3. **Input Current Situation**: Enter your current skills, situation.
4. **Generate Roadmap**: Click on "Generate" and your AI-powered roadmap will be displayed.
5. **Task Interactions**: Click on tasks for more details, mark them as done, or delete them.

## Acknowledgements
The team would like to thank ShellHacks 2023 for the opportunity to participate in this hackathon. Special thanks to our mentors and advisors.

## Contact
For more information or to report issues, please contact us at [info@pathmateai.co](mailto:info@pathmateai.co).
