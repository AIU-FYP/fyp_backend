from django.conf import settings
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def send_email(to_email, subject, content):
    message = Mail(
        from_email=settings.DEFAULT_FROM_EMAIL,
        to_emails=to_email,
        subject=subject,
        html_content=content
    )

    try:
        sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
        response = sg.send(message)
        return response
    except Exception as e:
        print(str(e))
        return None


def send_change_room_request_created(request, student_email, staff_email):
    student_subject = "Room Change Request Submitted"
    student_content = """
    <h2>Room Change Request Acknowledgement</h2>
    <p>Thank you for your request. We will review it within the next two weeks before proceeding to the approval stage.</p>
    """

    staff_subject = "New Room Change Request"
    staff_content = f"""
    <h2>New Room Change Request Submitted</h2>
    <p>Student Details:</p>
    <ul>
        <li>Student ID: {request.student_id}</li>
        <li>Name: {request.student}</li>
        <li>Room Number: {request.room_number}</li>
        <li>Reason: {request.reason}</li>
    </ul>
    """

    send_email(student_email, student_subject, student_content)
    send_email(staff_email, staff_subject, staff_content)


def send_change_room_request_update(request, student_email):
    subject = "Room Change Request Update"

    if request.status == 'accepted':
        content = """
        <h2>Room Change Request Accepted</h2>
        <p>Kindly be informed that your request has been accepted. You will be contacted for further steps in the process.</p>
        """
    else:
        content = """
        <h2>Room Change Request Rejected</h2>
        <p>Kindly be informed that your request has been rejected as it does not meet the criteria for room changes as outlined in the Student Handbook. Please be reminded that room changes will only be considered under special circumstances and after a thorough investigation by Student Affairs.</p>
        """

    send_email(student_email, subject, content)


def send_maintenance_request_created(request, student_email, staff_email, ppk_email):
    student_subject = "Maintenance Request Submitted"
    student_content = """
    <h2>Maintenance Report Acknowledgement</h2>
    <p>Thank you for your maintenance report. We will process your request and update you once the work has been completed.</p>
    """

    staff_subject = "New Maintenance Request"
    staff_content = f"""
    <h2>New Maintenance Request Submitted</h2>
    <p>Details:</p>
    <ul>
        <li>Student ID: {request.student_id}</li>
        <li>Room Number: {request.room_number}</li>
        <li>Issue: {request.issue}</li>
    </ul>
    """

    send_email(student_email, student_subject, student_content)
    send_email(staff_email, staff_subject, staff_content)
    send_email(ppk_email, staff_subject, staff_content)


def send_maintenance_request_update(request, student_email, staff_email):
    subject = "Maintenance Request Update"
    content = """
    <h2>Completed Maintenance Report</h2>
    <p>Kindly be informed that the maintenance work for your room, associated with work order no: TBA, has been completed. We will now proceed with closing the report. Should you require further assistance, please let us know.</p>
    """

    send_email(student_email, subject, content)
    send_email(staff_email, subject, content)


def send_student_welcome_email(student):
    subject = "Welcome to Student Housing"
    content = f"""
    <h2>Welcome {student.name}!</h2>
    <p>Your student housing account has been created successfully.</p>
    <p>Details:</p>
    <ul>
        <li>Student ID: {student.student_id}</li>
        <li>Email: {student.email}</li>
    </ul>
    """

    send_email(student.email, subject, content)
