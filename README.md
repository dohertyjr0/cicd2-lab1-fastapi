# CICD-2 FastAPI Product Service Lab

The FastAPI application on port `8000` exposes the required
`GET /api/products/{product_id}` endpoint. It forwards product lookups to the
Product Service on port `8001`.

## Run both services in Codespaces

Open two terminals at the repository root.

**Terminal 1 — Product Service (port 8001):**

```bash
uvicorn product_service.main:app --host 0.0.0.0 --port 8001 --reload
```

**Terminal 2 — API (port 8000):**

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

`PRODUCT_SERVICE_URL` is the base URL the API uses to reach the Product
Service. It defaults to `http://127.0.0.1:8001`; set it before starting the
API if the service is hosted elsewhere:

```bash
PRODUCT_SERVICE_URL=http://127.0.0.1:8001 uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

For example, with both services running, request a product with:

```bash
curl http://localhost:8000/api/products/1
```

The Product Service returns `404` for unknown product IDs. The API returns
`503` if it cannot connect to the Product Service.

## Tests

Install dependencies and run the test suite:

```bash
pip install -r requirements.txt
python -m pytest
```

GitHub Actions also runs the suite with coverage on pushes and pull requests.
