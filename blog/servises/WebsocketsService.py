import socketio
import uvicorn
from celery import Celery

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
    user_id = data["user_id"]
    data_user_id = data["data_user_id"]
    post_id = data["post_id"]
    username = data["username"]
    is_liked = data["is_liked"]
    await sio.emit(f'client{data_user_id}',
                   {'event': 'like',
                    'message': f'<a href="http://127.0.0.1:8000/blog/user-information/{username}">{username}</a> liked your post <a href="http://127.0.0.1:8000/blog/user-information/{username}">{post_id}</a>',
                    'post_id': post_id,
                    'username': username,
                    'is_liked': is_liked
                    })
    return {"data": data}


@app.post("/follow_on_user")
async def follow_on_user(data=Body()):
    author_id = data['author_id']
    follower = data['follower']
    is_followed = data['is_followed']
    follower_id = data['follower_id']
    await sio.emit(f'client{author_id}',
                   {'event': 'follow',
                    'message': f'<a href="http://127.0.0.1:8000/blog/user-information/{follower}">{follower}</a> followed you </a>',
                    'author_id': author_id,
                    'follower_id': follower_id,
                    'is_followed': is_followed
                    })
    return {"data": data}


if __name__ == '__main__':
    uvicorn.run(app_socket, port=3003, host='localhost')
