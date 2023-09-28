import socketio
import uvicorn

from fastapi import FastAPI, Body
app = FastAPI()

sio = socketio.AsyncServer(async_mode='asgi', cors_allowed_origins=[])
app_socket = socketio.ASGIApp(sio, app)


@sio.event
async def connect(sid, environ):
    # await sio.emit('client', {'data': 'foobar', 'message': 'Adam liked your post!'})
    print('server connected to client with session ID =  ', sid)

@sio.event
def disconnect(sid):
    print('disconnect=>SERVER ', 'SID: ', sid)


# @app.get("/")
# async def like_root():
#     print("fsafasf")
#     await sio.emit('client', {'data': 'foobar', 'message': 'Adam liked your post!'})
#     return {"Hello": "World"}

@app.post("/like_post")
async def like_post(data=Body()):
    print(data)
    user_id = data["data_user_id"]
    post_id = data["post_id"]
    username = data["username"]
    await sio.emit(f'client{user_id}', {'message': f'<a href="http://127.0.0.1:8000/blog/user-information/{username}">{username}</a> liked your post <a href="http://127.0.0.1:8000/blog/user-information/{username}">{post_id}</a>'})
    return {"Hello": "World"}

if __name__ == '__main__':
    uvicorn.run(app_socket, port=3003, host='localhost')