from datetime import datetime
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .models import (Task, Category, Tag)
from .serializers import (TaskSerializer, CategorySerializer, TagSerializer)

class TaskView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, task_id=None):
        if task_id:
            task = Task.objects.filter(id=task_id, user=request.user.id).first()
            
            if task:
                serializer = TaskSerializer(task)
                response = {
                    'code': 200,
                    'status': 'ok',
                    'body': {
                        'data': serializer.data
                    }
                }
                return Response(response, status=status.HTTP_200_OK)

            response = {
                'code': 1,
                'status': 'error',
                'body': {
                    'message': "Task not found"
                }
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)
            
        task_status = request.query_params.get('status')
        parent = request.query_params.get('parent')
        date_from = request.query_params.get('date_from')
        date_to = request.query_params.get('date_to')

        filters = {
            'user__id': request.user.id
        }

        if task_status:
            filters['status__exact'] = task_status

        if parent:
            filters['parent__id'] = parent

        if date_from:
            try:
                date_from = datetime.strptime(date_from, '%Y-%m-%d').date()
                filters['due_date__gte'] = date_from
            except ValueError:
                return Response({
                    'code': 5,
                    'status': 'error',
                    'body': {'message': 'Invalid date_from format. Use YYYY-MM-DD.'}
                }, status=status.HTTP_400_BAD_REQUEST)

        if date_to:
            try:
                date_to = datetime.strptime(date_to, '%Y-%m-%d').date()
                filters['due_date__lte'] = date_to
            except ValueError:
                return Response({
                    'code': 5,
                    'status': 'error',
                    'body': {'message': 'Invalid date_to format. Use YYYY-MM-DD.'}
                }, status=status.HTTP_400_BAD_REQUEST)
            
        tasks = Task.objects.filter(**filters)

        if not tasks:
            response = {
                'code': 2,
                'status': 'error',
                'body': {
                    'message': "Tasks not found with the specified parameters"
                }
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(tasks, request)

        serializer = TaskSerializer(result_page, many=True)

        response = {
            'code': 200,
            'status': 'ok',
            'body': {
                'data': serializer.data
            }
        }

        return paginator.get_paginated_response(response)

    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id

        serializer = TaskSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            response = {
                'code': 200,
                'status': 'ok',
                'body': {
                    'data': serializer.data
                }
            }
            return Response(response, status=status.HTTP_201_CREATED)
        
        response = {
            'code': 3,
            'status': 'error',
            'body': {
            'message': "An error ocurred while creating the new task",
                'errors': serializer.errors
            }
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, task_id):
        task = Task.objects.filter(id=task_id, user=request.user.id).first()
        if not task:
            response = {
                'code': 2,
                'status': 'error',
                'body': {
                    'message': "Task not found"
                }
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {
                'code': 200,
                'status': 'ok',
                'body': {
                    'data': serializer.data
                }
            }
            return Response(response, status=status.HTTP_200_OK)

        response = {
            'code': 4,
            'status': 'error',
            'body': {
                'message': 'An error ocurred while updating the task',
                'errors': serializer.errors
            }
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, task_id):
        task = Task.objects.filter(id=task_id, user=request.user.id).first()
        
        if not task:
            response = {
                'code': 1,
                'status': 'error',
                'body': {
                    'message': 'Task not found'
                }
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        task.delete()
            
        response = {
            'code': 200,
            'status': 'ok',
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)

class CategoryView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, category_id=None):
        if category_id:
            category = Category.objects.filter(id=category_id, user=request.user.id).first()
            
            if category:
                serializer = CategorySerializer(category)
                response = {
                    'code': 200,
                    'status': 'ok',
                    'body': {
                        'data': serializer.data
                    }
                }
                return Response(response, status=status.HTTP_200_OK)

            response = {
                'code': 6,
                'status': 'error',
                'body': {
                    'message': "Category not found"
                }
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)
            
        name = request.query_params.get('name')
        description = request.query_params.get('description')

        filters = {
            'user__id': request.user.id
        }

        if name:
            filters['name__icontains'] = name

        if description:
            filters['description__icontains'] = description

        categories = Category.objects.filter(**filters)

        if not categories:
            response = {
                'code': 7,
                'status': 'error',
                'body': {
                    'message': "Categories not found with the specified parameters"
                }
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(categories, request)

        serializer = CategorySerializer(result_page, many=True)

        response = {
            'code': 200,
            'status': 'ok',
            'body': {
                'data': serializer.data
            }
        }

        return paginator.get_paginated_response(response)

    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id

        serializer = CategorySerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            response = {
                'code': 200,
                'status': 'ok',
                'body': {
                    'data': serializer.data
                }
            }
            return Response(response, status=status.HTTP_201_CREATED)
        
        response = {
            'code': 8,
            'status': 'error',
            'body': {
            'message': "An error ocurred while creating the new category",
                'errors': serializer.errors
            }
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, category_id):
        category = Category.objects.filter(id=category_id, user=request.user.id).first()
        if not category:
            response = {
                'code': 5,
                'status': 'error',
                'body': {
                    'message': "Category not found"
                }
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        serializer = CategorySerializer(category, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {
                'code': 200,
                'status': 'ok',
                'body': {
                    'data': serializer.data
                }
            }
            return Response(response, status=status.HTTP_200_OK)

        response = {
            'code': 9,
            'status': 'error',
            'body': {
                'message': 'An error ocurred while updating the category',
                'errors': serializer.errors
            }
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, category_id):
        category = Category.objects.filter(id=category_id, user=request.user.id).first()
        
        if not category:
            response = {
                'code': 6,
                'status': 'error',
                'body': {
                    'message': 'Category not found'
                }
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        category.delete()
            
        response = {
            'code': 200,
            'status': 'ok',
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)

class TagView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, tag_id=None):
        if tag_id:
            tag = Tag.objects.filter(id=tag_id, user=request.user.id).first()
            
            if tag:
                serializer = TagSerializer(tag)
                response = {
                    'code': 200,
                    'status': 'ok',
                    'body': {
                        'data': serializer.data
                    }
                }
                return Response(response, status=status.HTTP_200_OK)

            response = {
                'code': 10,
                'status': 'error',
                'body': {
                    'message': "Tag not found"
                }
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)
            
        name = request.query_params.get('name')
        description = request.query_params.get('description')

        filters = {
            'user__id': request.user.id
        }

        if name:
            filters['name__icontains'] = name

        if description:
            filters['description__icontains'] = description

        tags = Tag.objects.filter(**filters)

        if not tags:
            response = {
                'code': 11,
                'status': 'error',
                'body': {
                    'message': "Tags not found with the specified parameters"
                }
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        paginator = PageNumberPagination()
        result_page = paginator.paginate_queryset(tags, request)

        serializer = TagSerializer(result_page, many=True)

        response = {
            'code': 200,
            'status': 'ok',
            'body': {
                'data': serializer.data
            }
        }

        return paginator.get_paginated_response(response)

    def post(self, request):
        data = request.data.copy()
        data['user'] = request.user.id

        serializer = TagSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            response = {
                'code': 200,
                'status': 'ok',
                'body': {
                    'data': serializer.data
                }
            }
            return Response(response, status=status.HTTP_201_CREATED)
        
        response = {
            'code': 12,
            'status': 'error',
            'body': {
            'message': "An error ocurred while creating the new tag",
                'errors': serializer.errors
            }
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, tag_id):
        tag = Tag.objects.filter(id=tag_id, user=request.user.id).first()
        if not tag:
            response = {
                'code': 12,
                'status': 'error',
                'body': {
                    'message': "Tag not found"
                }
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        serializer = TagSerializer(tag, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {
                'code': 200,
                'status': 'ok',
                'body': {
                    'data': serializer.data
                }
            }
            return Response(response, status=status.HTTP_200_OK)

        response = {
            'code': 13,
            'status': 'error',
            'body': {
                'message': 'An error ocurred while updating the tag',
                'errors': serializer.errors
            }
        }
        return Response(response, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, tag_id):
        tag = Tag.objects.filter(id=tag_id, user=request.user.id).first()
        
        if not tag:
            response = {
                'code': 10,
                'status': 'error',
                'body': {
                    'message': 'Tag not found'
                }
            }
            return Response(response, status=status.HTTP_404_NOT_FOUND)

        tag.delete()
            
        response = {
            'code': 200,
            'status': 'ok',
        }
        return Response(response, status=status.HTTP_204_NO_CONTENT)
