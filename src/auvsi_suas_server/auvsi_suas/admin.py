from django.contrib import admin
from auvsi_suas.models import AerialPosition
from auvsi_suas.models import GpsPosition
from auvsi_suas.models import MovingObstacle
from auvsi_suas.models import Obstacle
from auvsi_suas.models import ObstacleAccessLog
from auvsi_suas.models import ServerInfo
from auvsi_suas.models import ServerInfoAccessLog
from auvsi_suas.models import StationaryObstacle
from auvsi_suas.models import UasTelemetry 
from auvsi_suas.models import Waypoint

# Register models for admin page
admin.site.register(AerialPosition)
admin.site.register(GpsPosition)
admin.site.register(MovingObstacle)
admin.site.register(Obstacle)
admin.site.register(ObstacleAccessLog)
admin.site.register(ServerInfo)
admin.site.register(ServerInfoAccessLog)
admin.site.register(StationaryObstacle)
admin.site.register(UasTelemetry)
admin.site.register(Waypoint)
