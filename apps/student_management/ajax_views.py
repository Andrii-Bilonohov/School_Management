import base64
import json
import os
from json import JSONDecodeError

from django.core.files.base import ContentFile
from django.http import JsonResponse

from .models import Student
from django.urls import reverse

def update_student_profile_picture(request):
    try:
        data = json.loads(request.body)

        student_id = data.get('student_id')
        image_data = data.get('image')

        if not student_id or not image_data:
            return JsonResponse(
                {"success": False, "message": "Invalid data."},
                status = 400
            )

        try:
            student = Student.objects.get(id=student_id)
        except Student.DoesNotExist:
            return JsonResponse(
                {"success": False, "message": "Student does not exist."},
                status = 404
            )

        extension = None

        if image_data.startswith('data:image/jpeg;base64,'):
            image_data = image_data.split('base64,')[1]
            extension = '.jpg'

        elif image_data.startswith('data:image/png;base64,'):
            image_data = image_data.split('base64,')[1]
            extension = '.png'
        else:
            return JsonResponse(
                {"success": False, "message": "Unsupported image format."},
                status = 400
            )

        try:
            image_data_decoded = base64.b64decode(image_data)
        except Exception:
            return JsonResponse(
                {"success": False, "message": "Invalid image data."},
                status = 400
            )

        file_name = f"{student_id}{extension}"

        if student.photo:
            old_file_path = student.photo.path
            if os.path.exists(old_file_path):
                try:
                    os.remove(old_file_path)
                except Exception as e:
                    print("Couldn't remove old file: ", e)

        profile_picture = ContentFile(image_data_decoded)
        student.photo.save(file_name, profile_picture, save=True)

        redirect_url = reverse("students:student_profile", args=[student.id])

        return JsonResponse(
            {"success": True, "message": "Profile picture updated successfully.", "redirect_url": redirect_url},

        )

    except JSONDecodeError:
        return JsonResponse(
            {"success": False, "message": "Invalid json data."},
        )

    except Exception as e:
        return JsonResponse(
            {"success": False, "message": "Something went wrong."},
        )