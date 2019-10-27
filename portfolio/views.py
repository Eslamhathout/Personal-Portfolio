from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from .models import Job, Certificate

def index(request):
    #Recent Jobs
    job1 = Job.objects.get(id = 7)
    job2 = Job.objects.get(id = 5)
    job3 = Job.objects.get(id = 8)
    

    #Recent Certificates
    cert1 = Certificate.objects.get(id = 4)
    cert2 = Certificate.objects.get(id = 5)
    cert3 = Certificate.objects.get(id = 6)


    return render(request, 'hathout/index.html', {
        'Jobs': [job1, job2, job3],
        'Certificates': [cert1, cert2, cert3]
        })

def jobs(request):
    Jobs_obj = Job.objects.all()
    return render(request, 'hathout/jobs.html', {'Jobs': Jobs_obj})

# def job_detail(request, job_id):
#     Job_obj = get_object_or_404(Job, pk=job_id)
#     return render(request, 'hathout/job_detail.html', {'Job': Job_obj})

def certificates(request):
    Certificate_obj = Certificate.objects.all()
    return render(request, 'hathout/certificates.html', {'Certificates': Certificate_obj})

# def certificate_detail(request, cert_id):
#     Certificate_obj = get_object_or_404(Certificate, pk=cert_id)
#     return render(request, 'hathout/certificate_detail.html', {'Certificate': Certificate_obj})