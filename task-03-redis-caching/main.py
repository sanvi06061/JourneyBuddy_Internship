from fastapi import FastAPI, HTTPException
import redis.asyncio as redis
import json


app = FastAPI(
    title="Redis Cache-Aside API",
    description="FastAPI API demonstrating Redis caching with TTL.",
    version="1.0.0"
)


# Simulated persistent database
DATABASE = {
    1: {
        "id": 1,
        "name": "Sanvi",
        "email": "sanvi@example.com"
    },
    2: {
        "id": 2,
        "name": "Rahul",
        "email": "rahul@example.com"
    },
    3: {
        "id": 3,
        "name": "Priya",
        "email": "priya@example.com"
    }
}


# Connect to Redis running locally
redis_client = redis.Redis(
    host="localhost",
    port=6379,
    decode_responses=True
)


# Cache duration: 60 seconds
CACHE_TTL = 60


@app.get("/")
async def root():
    return {
        "message": "Redis Cache-Aside API is running"
    }


@app.get("/users/{user_id}")
async def get_user(user_id: int):

    # Redis key
    cache_key = f"user:profile:{user_id}"

    # 1. Check Redis cache
    cached_user = await redis_client.get(cache_key)

    if cached_user:
        return {
            "source": "cache",
            "data": json.loads(cached_user)
        }

    # 2. Cache miss -> read from persistent storage
    user = DATABASE.get(user_id)

    if user is None:
        raise HTTPException(
            status_code=404,
            detail="User not found"
        )

    # 3. Store the database result in Redis
    await redis_client.set(
        cache_key,
        json.dumps(user),
        ex=CACHE_TTL
    )

    # 4. Return the user
    return {
        "source": "database",
        "data": user
    }


@app.delete("/users/{user_id}/cache")
async def clear_user_cache(user_id: int):

    cache_key = f"user:profile:{user_id}"

    deleted = await redis_client.delete(cache_key)

    return {
        "cache_key": cache_key,
        "deleted": deleted > 0
    }