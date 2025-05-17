# retool-lite

Build internal tools just like in retools

## Backend

Create a virtual environment and start it:

```sh
python -m venv .env # windows
/.env/Scripts/activate
```

Install the requirements:

```sh
pip install -r requirements.txt
```

Start the API:

```sh
fastapi dev main.py
```

## Frontend

Create vite project

```sh
npm create vite@latest
```

Follow the instructions to start a vite project using React and Javascript.

Then install the libraries:

```sh
npm install
```

Run the frontend:

```sh
npm run dev
```

## Requirements

1. Create resources/tables like customer, subscriptions etc. User can create any resource and the application should create a database table for that resource with the specified columns.
2. Every resource should have some CRUD APIs available after they are created.
3. All API endpoints should work as expected when any of them is called. API could be of GET, POST, PUT and DELETE types.
4. There should be a form component for sumbitting new values inside the resources. User should be able to build that form according to the type of values needed to create a resource entry.
5. For every resource there should be a seperate page where user can go and use the APIs of that resource.
