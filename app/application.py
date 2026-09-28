from fastapi import FastAPI, HTTPException
from app.schemas import PostCreate
from app.db import Post,create_db_and_tables, get_async_session
from sqlalchemy.ext.asyncio import AsyncSession
from contextlib import asynccontextmanager


@asynccontextmanager
async def lifespan(app: FastAPI):
    await create_db_and_tables()
    yield
app = FastAPI(lifespan=lifespan)

text_posts = {1: {"title": "New Post", "content": "cool text post"}}

@app.get("/posts")
def get_all_posts(limit: int | None = None):
    if limit:
        return list(text_posts.values())[:limit]
    return text_posts

@app.get("/posts/{post_id}")
def get_post(post_id: int) -> dict[str, str] | None:
    if id not in text_posts:
        raise HTTPException(status_code=404, detail="Post not found")

    return text_posts.get(post_id)

@app.post("/posts")
def create_post(post: PostCreate) -> dict[str, str]:
    new_post = {"title": post.title, "content": post.content}
    text_posts[max(text_posts.keys()) + 1] = new_post
    return new_post