# **FastAPI Question Answering API 🚀**

This FastAPI-based API provides answers to user queries using OpenAI's language model. It retrieves relevant documents from a database and generates responses based on their content.  

---

## **📌 Features**
- Retrieve stored documents from a database
- Identify the most relevant document for a given question
- Generate answers using OpenAI's language model

---

## **🛠️ Installation & Setup**

### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/piyushsangale13/rag_embedding.git
cd rag_embedding
```

### **2️⃣ Create a Virtual Environment (Optional but Recommended)**
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

Ensure you have **FastAPI, SQLAlchemy, Uvicorn, OpenAI, and LangChain** installed.

---

## **📝 Configuration**
### **Set Up Environment Variables**
Create a `.env` file and add the following:
```env
OPENAI_API_KEY=your_openai_api_key
DATABASE_URL=your_database_url
```
Replace with your actual API key and database URL.

---

## **🚀 Running the API**
### **Start the FastAPI Server**
```sh
uvicorn app.main:app --reload
```
- The API will be available at: **`http://127.0.0.1:8000`**
- Visit **`http://127.0.0.1:8000/docs`** for interactive API documentation.

---

## **📡 API Endpoints**
### **1️⃣ Get an Answer**
**Endpoint:**  
```http
POST /qa/
```
**Request Body:**
```json
{
  "question": "What is AI?"
}
```
**Response:**
```json
{
  "answer": "AI stands for Artificial Intelligence...",
  "document": "Introduction to AI"
}
```

---

## **📂 Project Structure**
```
/app
  ├── routes/
  │   ├── qa.py          # API route for Q&A
  ├── services/
  │   ├── retrieve_best_document.py  # Finds the most relevant document
  ├── database.py        # Database connection setup
  ├── schemas.py         # Pydantic models for request/response validation
  ├── crud.py            # Database queries
  ├── main.py            # FastAPI app entry point
.env                     # Environment variables (not included in repo)
requirements.txt         # List of dependencies
README.md                # Project documentation
```

---

## **💡 Future Improvements**
- ✅ Support for multiple document retrieval methods
- ✅ Integration with vector databases for better matching
- ✅ User authentication & access control

---