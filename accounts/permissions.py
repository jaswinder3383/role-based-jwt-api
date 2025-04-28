from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsAdmin(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_autheticated and request.user.role == 'admin'
    
class IsModerator(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_autheticated and request.user.role == 'moderator'
    
class IsUser(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_autheticated and request.user.role == 'user' 
    
    
    
    
class RolePermission(BasePermission):
    def has_permission(self, request, view):
        if request.user.role == "admin":
            return True
        elif request.user.role == "moderator":
           
            return request.method in ["GET", "PUT", "PATCH"]
        
        elif request.user.role == "user":
            print("User Role:", request.user.role)
            print("Request Method:", request.method)
            return request.method in SAFE_METHODS
        return False