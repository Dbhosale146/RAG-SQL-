import os
from dotenv import load_dotenv
load_dotenv()

EURI_API_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VySWQiOiIzZDk1ZjRjNC03ZDc1LTRlMjItODY1Mi0wNGViMjkxMjU1Y2UiLCJlbWFpbCI6ImRueWFuZXNod2FyYmhvc2FsZTExMUBnbWFpbC5jb20iLCJpYXQiOjE3Mzg0ODk0NjQsImV4cCI6MTc3MDAyNTQ2NH0.frcheb8DJU_9AOCaTHdLDJ9Ud9OWrk1Gjp-NpV3dSp8"
EURI_API_URL  = "https://api.euron.one/api/v1/euri/alpha/chat/completions"
MODEL_NAME  = "gpt-4.1-nano"
DATABASE_URI = "postgresql://neondb_owner:npg_GPhIBZdv3XL5@ep-rough-cake-a8ic91hs-pooler.eastus2.azure.neon.tech/neondb?sslmode=require"
