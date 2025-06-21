from fastapi import FastAPI, Request
from sse_starlette.sse import EventSourceResponse
import asyncio

app = FastAPI()

@app.get("/mcp/sse")
async def mcp_sse(request: Request):
    async def event_generator():
        yield {"event": "start", "data": "Processing..."}
        await asyncio.sleep(2)
        yield {"event": "progress", "data": "Calling LLM..."}
        await asyncio.sleep(2)
        yield {"event": "done", "data": "Here is your video URL: https://example.com/video.mp4"}

    return EventSourceResponse(event_generator())