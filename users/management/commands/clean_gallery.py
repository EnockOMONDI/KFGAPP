from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
from users.models import Gallery
from django.db import connection

class Command(BaseCommand):
    help = 'Clean invalid gallery entries'

    def handle(self, *args, **kwargs):
        # Get all gallery entries
        with connection.cursor() as cursor:
            cursor.execute("""
                SELECT id, title, image 
                FROM users_gallery 
                WHERE image IS NULL 
                   OR image = '' 
                   OR image NOT LIKE 'https://%'
                   OR image NOT LIKE '%ucarecdn.com%'
            """)
            rows = cursor.fetchall()

        invalid_entries = []
        for row in rows:
            id, title, image = row
            invalid_entries.append({
                'id': id,
                'title': title or 'Untitled',
                'image': image
            })

        if not invalid_entries:
            self.stdout.write(self.style.SUCCESS("No invalid entries found!"))
            return

        self.stdout.write(f"Found {len(invalid_entries)} potentially invalid entries:")
        
        for entry in invalid_entries:
            self.stdout.write(
                f"ID: {entry['id']}\n"
                f"Title: {entry['title']}\n"
                f"Image: {entry['image']}\n"
                f"-------------------"
            )
        
        confirm = input("\nDo you want to delete these entries? (yes/no): ")
        if confirm.lower() == 'yes':
            with connection.cursor() as cursor:
                for entry in invalid_entries:
                    cursor.execute("DELETE FROM users_gallery WHERE id = %s", [entry['id']])
            self.stdout.write(self.style.SUCCESS(f"Deleted {len(invalid_entries)} invalid entries successfully"))
        else:
            self.stdout.write("No entries were deleted")