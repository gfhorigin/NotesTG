from .StartHandler import  router as start_router
from .CreateNoteHandler import  router as create_router
from .ViewNoteHandler import router as view_router

routers = [start_router, view_router, create_router]