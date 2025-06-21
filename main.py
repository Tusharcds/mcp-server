# main.py

from fastapi import FastAPI, Request
from sse_starlette.sse import EventSourceResponse
from tools import get_tools
import asyncio

app = FastAPI()


@app.get("/tools")
async def tools_endpoint():
    return {"tools": get_tools()}


@app.get("/mcp/sse")
async def mcp_sse(request: Request):
    async def event_generator():
        # Send initial start event
        yield {
            "event": "start",
            "data": "Processing..."
        }

        await asyncio.sleep(1)

        # Simulate tool execution step
        yield {
            "event": "progress",
            "data": "Running 'create-short-video'..."
        }

        await asyncio.sleep(2)

        # Send done event with output (e.g. a video URL)
        yield {
            "event": "done",
            "data": "Video ready at: https://example.com/video.mp4"
        }

    return EventSourceResponse(event_generator())
