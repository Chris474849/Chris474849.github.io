from fastapi import Request
from fastapi.responses import JSONResponse
from app.core.rate_limit import rate_limit
from app.core.security import decode_token

async def global_middleware(request: Request, call_next):
    ip = request.client.host
    if not rate_limit(ip, 60, 60):
        return JSONResponse({"error": "Rate limit exceeded"})
    auth = request.headers.get("Authorization")
    if auth:
        parts = auth.split(" ")
        if len(parts) == 2 and parts[0] == "Bearer":
            try:
                payload = decode_token(parts[1])
                request.state.user_id = int(payload["sub"])
            except:
                request.state.user_id = None
        else:
            request.state.user_id = None
    else:
        request.state.user_id = None
    response = await call_next(request)
    return response
