# 📘 Reflection: Day 27 – Python with MongoDB

## 🔍 Key Concepts

### 1. Why Use MongoDB?

- NoSQL database: stores flexible, JSON-like documents.
- Ideal for dynamic data structures and scalability.

### 2. Setting Up Atlas

- Create a free cluster on MongoDB Atlas.
- Configure IP access and database user.
- Get the connection URI for use in your Python app.

### 3. Integrating with Flask

- Use `pymongo` or `MongoClient` to connect Flask to MongoDB.
- URI enables remote database access.

### 4. CRUD Operations

- **Create**: Insert documents with `insert_one()` or `insert_many()`.
- **Read**: Query using `find()`, filters, and sorting.
- **Update**: Modify with `update_one()` or `update_many()`.
- **Delete**: Remove with `delete_one()`, `delete_many()` or drop collections.

### 5. Exercises Summary

- Connect to Atlas.
- Create and populate a collection.
- Run queries, updates, deletions, and drop a collection.

---

## 📌 Reflection

This lesson links Python to a real-world NoSQL database setup. MongoDB’s flexibility makes it well-suited for applications with evolving or user-generated data—such as a sustainability tracker app.

---

## 💡 Suggested Next Steps

- Add schema validation.
- Organize Flask routes with Blueprints.
- Build RESTful endpoints for full CRUD functionality.
