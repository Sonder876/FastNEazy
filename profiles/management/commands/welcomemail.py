from django.core.management.base import BaseCommand

from django.core.mail import EmailMessage

from django.conf import settings
from django.contrib.auth.models import User


from django.template.loader import get_template

from profiles.models import Profile


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        # recievers = []
        for user in User.objects.all():
            # recievers.append(user.email) if i want to send email one time

            profile = Profile.objects.get(user=user)

            name = str(user.first_name) + " " + str(user.last_name)
            ctx = {"name": name, "code": profile.affiliate_code}

            subject = " Welcome To SizExpress! "
            # html_message = render_to_string("email.html", {Context})
            # plain_message = strip_tags(html_message)
            email_from = settings.EMAIL_HOST_USER

            # mail.send_mail(
            #     subject,
            #     plain_message,
            #     email_from,
            #     [User.email],
            #     html_message=html_message,
            # )
            usermail = str(user.email)
            print(usermail)
            print(name)
            print(profile.affiliate_code)
            message = get_template("Welcome_email.html").render(ctx)
            msg = EmailMessage(
                subject,
                message,
                "SizExpress - The Shipping Company <email_from>",
                [usermail],
            )
            msg.content_subtype = "html"
            msg.send()
