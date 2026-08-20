from fastapi import FastAPI, Path, Query

app = FastAPI(
    title="FastAPI Parameter Validation API",
    description="API demonstrating strict parameter validation.",
    version="1.0.0"
)


@app.get("/users/{user_id}")
async def get_user(
    user_id: int = Path(
        ...,
        ge=1,
        description="Unique user identifier. Must be a positive integer."
    ),
    tag: str | None = Query(
        default=None,
        min_length=1,
        max_length=30,
        description="Optional filtering tag."
    )
):
    return {
        "user_id": user_id,
        "tag": tag
    }