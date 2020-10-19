from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser

from .models import InputFiles, GeneratedReport
from .tasks import upload_reports, generate_data
from celery.result import AsyncResult
from reportTestProject.celery import app


class ReportCreate(APIView):
    parser_classes = [FormParser, MultiPartParser]

    def put(self, request):
        result = {'success': True, 'msg': 'Success!'}
        input_files = InputFiles.objects.create(cfn_inventory=request.data.get('cfn_inventory'),
                                                inventory_listing=request.data.get('inventory_listing'),
                                                reserved_inventory=request.data.get('reserved_inventory'))

        up_res = upload_reports.apply_async([input_files.id])
        res = generate_data.apply_async([input_files.id])

        print(res.get())
        result.update(res.get())
        result['report_files_id'] = input_files.id
        result['task_id'] = res.task_id

        return Response(result, status=200)



